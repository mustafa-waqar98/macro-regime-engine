import os
from fredapi import Fred
import pandas as pd
import numpy as np

def fetch_cpi():
    api_key = os.environ['FRED_API_KEY']
    fred = Fred(api_key=api_key)

    cpi_level = fred.get_series('CPIAUCSL')

    return cpi_level

def fetch_pmi():
    api_key = os.environ['FRED_API_KEY']
    fred = Fred(api_key=api_key)

    pmi_series = fred.get_series('GACDISA066MSFRBNY')

    return pmi_series

def cpi_to_yoy(cpi_level):
    transform = (cpi_level / cpi_level.shift(12) - 1) * 100
    
    return transform

def latest_valid_reading(series):
    reading = series.dropna().iloc[-1]

    return reading

def latest_valid_date(series):
    date = series.dropna().index[-1]

    return date

# Tests
my_series = pd.Series([100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 200])
result = cpi_to_yoy(my_series)
print(result)
assert result.head().isna().all(), f"Head is not NaN"
assert result.iloc[-1] == 100, f"Tail is not 100"

my_series1 = pd.Series([np.nan, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan, np.nan])
result = latest_valid_reading(my_series1)
print(result)

my_series2 = pd.Series([np.nan, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.nan, np.nan])
result = latest_valid_date(my_series1)
print(result)