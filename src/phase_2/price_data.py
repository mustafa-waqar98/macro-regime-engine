import yfinance as yf

def fetch_prices(tickers, start, end):
    prices = yf.download(tickers, start, end, auto_adjust=True)['Close']

    return prices

tickers = ['SPY', 'AGG', 'DBC', 'TIP', 'BIL', 'LQD', 'GLD']
'''
SPY - SPDR S&P 500 ETF Trust
AGG - iShares Core US Aggregate Bond ETF
DBC - Invesco DB Commodity Index Tracking Fund
TIP - iShares TIPS Bond ETF
BIL - SPDR Bloomberg 1-3 Month T-Bill ETF
'''
start_date = '2010-01-01'
end_date = None
prices = fetch_prices(tickers, start_date, end_date)