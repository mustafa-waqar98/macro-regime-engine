from src.phase_1.classify_regime import classify_regime
from src.phase_3.momentum import momentum
from src.phase_3.momentum_tilt import lookup, momentum_to_state, apply_tilt, TILT_TABLE
import pandas as pd

CATEGORY_TO_TICKER = {
    'Equities': 'SPY',
    'Credit': 'LQD',
    'Commodities': 'DBC',
    'Gold': 'GLD',
    'TIPS': 'TIP',
    'Long Bonds': 'TLT',
    'USD': 'BIL',
}

def to_monthly_returns(prices):
    monthly_prices = prices.resample('ME').last()
    returns = monthly_prices.pct_change()

    return returns.dropna()

def cumulative(returns):
    return (1 + returns).cumprod()

def weights_from_classification(classification, tickers):
    overweight = classification['overweight']
    overweight_tickers = [CATEGORY_TO_TICKER[c] for c in overweight]
    equal_share = 1 / len(overweight)

    weights = {}

    for i in tickers:
        if i in overweight_tickers:
            weights[i] = equal_share
        else:
            weights[i] = 0

    return weights

def build_weights_table(inputs, tickers, states, buffer=0.20, magnitude=0.10, table=TILT_TABLE):
    rows = {}
    for date, row in inputs.iterrows():
        classification = classify_regime(row['pmi'], row['cpi'])
        base = weights_from_classification(classification, tickers)
        state = states[date]
        stance = lookup(classification['regime'], state, table)
        tilted_row = apply_tilt(pd.Series(base), stance, buffer, magnitude)
        rows[date] = tilted_row

    return pd.DataFrame(rows).T
    