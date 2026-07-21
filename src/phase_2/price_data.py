import yfinance as yf

'''
SPY - SPDR S&P 500 ETF Trust
AGG - iShares Core US Aggregate Bond ETF
DBC - Invesco DB Commodity Index Tracking Fund
TIP - iShares TIPS Bond ETF
BIL - SPDR Bloomberg 1-3 Month T-Bill ETF
'''

def fetch_prices(tickers, start, end):
    prices = yf.download(tickers, start, end, auto_adjust=True)['Close']

    return prices

