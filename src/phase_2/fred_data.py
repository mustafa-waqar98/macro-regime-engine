import os
from fredapi import Fred
import pandas as pd

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

my_series = pd.Series([100, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 200])
result = cpi_to_yoy(my_series)
print(result)
assert result.head().isna().all(), f"Head is not NaN"
assert result.iloc[-1] == 100, f"Tail is not 100"

print(cpi_to_yoy(fetch_cpi()).tail())
