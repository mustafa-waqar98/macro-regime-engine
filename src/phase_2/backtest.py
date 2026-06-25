def to_monthly_returns(prices):
    monthly_prices = prices.resample('ME').last()
    returns = monthly_prices.pct_change()

    return returns.dropna()

def cumulative(returns):
    return (1 + returns).cumprod()