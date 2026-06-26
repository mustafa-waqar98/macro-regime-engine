from src.phase_2.fred_data import fetch_cpi, fetch_pmi, smooth, cpi_to_yoy
from src.phase_2.backtest import build_weights_table
from src.phase_2.price_data import fetch_prices
from src.phase_2.backtest import to_monthly_returns, cumulative
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['SPY', 'DBC', 'TIP', 'BIL', 'LQD', 'GLD', 'TLT']

def build_current_inputs(cpi_raw, pmi_raw):
    cpi_yoy = cpi_to_yoy(cpi_raw)
    pmi_smoothed = smooth(pmi_raw)

    inputs = pd.DataFrame({
        'cpi': cpi_yoy,
        'pmi': pmi_smoothed,
        }).dropna()

    return inputs

if __name__ == '__main__':
    cpi_raw = fetch_cpi()
    pmi_raw = fetch_pmi()

    inputs = build_current_inputs(cpi_raw, pmi_raw)

    weights = build_weights_table(inputs, tickers)
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
    plt.savefig('results/strategy_vs_benchmark.png')