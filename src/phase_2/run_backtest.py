from src.phase_2.fred_data import fetch_cpi, fetch_pmi, smooth, cpi_to_yoy, fetch_vintage_snapshot, snapshot_to_series, latest_valid_reading
from src.phase_2.backtest import build_weights_table
from src.phase_2.price_data import fetch_prices
from src.phase_2.backtest import to_monthly_returns, cumulative
from src.phase_3.momentum import momentum
from src.phase_3.momentum_tilt import momentum_to_state, apply_tilt, lookup

import pandas as pd
import matplotlib.pyplot as plt
import os
from fredapi import Fred
import time

api_key = os.environ['FRED_API_KEY']
fred = Fred(api_key=api_key)

tickers = ['SPY', 'DBC', 'TIP', 'BIL', 'LQD', 'GLD', 'TLT']

def build_current_inputs(cpi_raw, pmi_raw):
    cpi_yoy = cpi_to_yoy(cpi_raw)
    pmi_smoothed = smooth(pmi_raw)

    inputs = pd.DataFrame({
        'cpi': cpi_yoy,
        'pmi': pmi_smoothed,
        }).dropna()

    return inputs

def build_vintage_inputs(fred):
    cache_path = 'data/vintage_inputs.csv'

    if os.path.exists(cache_path):
        return pd.read_csv(cache_path, index_col='date', parse_dates=True)

    as_of_dates = pd.date_range('2014-03-31', pd.Timestamp.today(), freq='ME')
    rows = []

    for as_of_date in as_of_dates:
        time.sleep(1)
        print(as_of_date)
        cpi_snap = fetch_vintage_snapshot(fred, 'CPIAUCSL', as_of_date)
        cpi_series = snapshot_to_series(cpi_snap)
        cpi = latest_valid_reading(cpi_to_yoy(cpi_series))

        pmi_snap = fetch_vintage_snapshot(fred, 'GACDISA066MSFRBNY', as_of_date)
        pmi_series = snapshot_to_series(pmi_snap)
        pmi = latest_valid_reading(smooth(pmi_series))

        rows.append({
            'date': as_of_date,
            'cpi': cpi,
            'pmi': pmi
        })

    os.makedirs('data', exist_ok=True)
    inputs = pd.DataFrame(rows).set_index('date').dropna()
    inputs.to_csv(cache_path)

    return inputs

if __name__ == '__main__':
    inputs = build_vintage_inputs(fred)
    mom = momentum(inputs['pmi'])
    states = mom.apply(momentum_to_state)
    weights = build_weights_table(inputs, tickers, states)
    weights = weights.shift(1)

    prices = fetch_prices(tickers, '2010-01-01', None)
    monthly = to_monthly_returns(prices)
    print(set(weights.columns) == set(monthly.columns))

    weights.index = weights.index + pd.offsets.MonthEnd(0)
    portfolio = (weights * monthly).sum(axis=1)
    portfolio = portfolio['2014':'2026-05']
    strategy_growth = cumulative(portfolio)
    bench_prices = fetch_prices(['SPY', 'AGG'], '2010-01-01', None)
    bench_monthly = to_monthly_returns(bench_prices)
    benchmark = 0.6 * bench_monthly['SPY'] + 0.4 * bench_monthly['AGG']
    benchmark = benchmark['2014':'2026-05']
    benchmark_growth = cumulative(benchmark)
    strategy_growth.plot(label='Strategy')
    benchmark_growth.plot(label='60/40 Benchmark')
    plt.legend()
    print(f"\nStrategy, 2014-2026-05: {round(strategy_growth.iloc[-1], 2)}x")
    print(f"\n60/40 Benchmark, 2014-2026-05: {round(benchmark_growth.iloc[-1], 2)}x")
    plt.savefig('results/strategy_vs_benchmark_vintage.png')