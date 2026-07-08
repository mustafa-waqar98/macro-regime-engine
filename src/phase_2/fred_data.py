import os
from fredapi import Fred
import pandas as pd
import numpy as np

def fetch_cpi(fred):
    cpi_level = fred.get_series('CPIAUCSL')

    return cpi_level

def fetch_pmi(fred):
    pmi_series = fred.get_series('GACDISA066MSFRBNY')

    return pmi_series

def smooth(series, window=3):
    rolling_mean = series.rolling(window).mean()

    return rolling_mean

def cpi_to_yoy(cpi_level):
    transform = (cpi_level / cpi_level.shift(12) - 1) * 100
    
    return transform

def latest_valid_reading(series):
    reading = series.dropna().iloc[-1]

    return reading

def latest_valid_date(series):
    date = series.dropna().index[-1]

    return date

# Vintage Fetcher

def collapse_to_snapshot(releases):
    snapshot = releases.sort_values('realtime_start').drop_duplicates(subset='date', keep='last')
    return snapshot

def snapshot_to_series(snap):
    series = pd.Series(
        pd.to_numeric(snap['value'], errors='coerce').astype(float).values,
        index=pd.to_datetime(snap['date']).values
    ).sort_index()
    return series

def fetch_vintage_snapshot(fred, series, as_of_date):
    releases = fred.get_series_as_of_date(series, as_of_date)
    return collapse_to_snapshot(releases)

# Tests
if __name__ == '__main__':
    api_key = os.environ['FRED_API_KEY']
    fred = Fred(api_key=api_key)

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

    print(smooth(pd.Series([3, 6, 9, 12])))
    
    x = fetch_vintage_snapshot(fred, 'CPIAUCSL', '2015-12-01')
    print(x)

    mask = pd.to_datetime(x['date']) == '2015-01-01'
    jan_2015 = x[mask]
    print(jan_2015)