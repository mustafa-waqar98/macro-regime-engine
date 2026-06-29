from src.phase_1.classify_regime import classify_regime
from src.phase_2.fred_data import fetch_cpi, fetch_pmi, smooth, cpi_to_yoy, latest_valid_reading, latest_valid_date
from src.phase_2.price_data import fetch_prices
from src.phase_2.backtest import to_monthly_returns, cumulative
import matplotlib.pyplot as plt
import pandas as pd
import os
from fredapi import Fred

def date_format(date):
    formatted_date = date.strftime('%B %Y')

    return formatted_date

def format_report(cpi_value, cpi_date, pmi_value_raw, pmi_value_smoothed, pmi_date, classification):
    regime = classification['regime']
    overweight = ', '.join(classification['overweight'])
    underweight = ', '.join(classification['underweight'])
    
    pmi = f"PMI (3M avg) as of {date_format(pmi_date)}: {round(pmi_value_smoothed, 2)} (raw: {round(pmi_value_raw, 2)})"
    cpi = f"CPI as of {date_format(cpi_date)}: {round(cpi_value, 2)}%"

    formatted_output = f"Current Regime: {regime}\n{pmi}\n{cpi}\nOverweight: {overweight}\nUnderweight: {underweight}"

    return formatted_output

if __name__ == '__main__':
    api_key = os.environ['FRED_API_KEY']
    fred = Fred(api_key=api_key)

    # CPI
    cpi_raw = fetch_cpi(fred)
    cpi_yoy = cpi_to_yoy(cpi_raw)
    cpi_value = latest_valid_reading(cpi_yoy)
    cpi_date = latest_valid_date(cpi_yoy)

    # PMI
    pmi_series = fetch_pmi(fred)
    smoothed_pmi = smooth(pmi_series)
    pmi_value_raw = latest_valid_reading(pmi_series)
    pmi_value_smoothed = latest_valid_reading(smoothed_pmi)
    pmi_date = latest_valid_date(smoothed_pmi)

    # Classify
    classification = classify_regime(pmi_value_smoothed, cpi_value)

    # Print
    report = format_report(cpi_value, cpi_date, pmi_value_raw, pmi_value_smoothed, pmi_date, classification)
    print(report)

    # Backtest — 60/40 benchmark
    prices = fetch_prices(['SPY','AGG','DBC','TIP','BIL'], '2010-01-01', None)
    monthly = to_monthly_returns(prices)
    benchmark = 0.6 * monthly['SPY'] + 0.4 * monthly['AGG']
    benchmark = benchmark['2014-01':]
    growth = cumulative(benchmark)
    print(f"\n60/40 benchmark, 2014–now: {round(growth.iloc[-1], 2)}x")
    growth.plot()
    plt.savefig('benchmark.png')
