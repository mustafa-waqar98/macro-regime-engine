import pandas as pd

def momentum(series, window=3, delta=3):
    smooth = series.rolling(window).mean()
    result = smooth.diff(delta)

    return result

if __name__ == '__main__':
    path = pd.read_csv('data/vintage_inputs.csv', index_col='date', parse_dates=True)
    series = path['pmi']
    values = momentum(series)
    print(values.iloc[5])
    print(values.iloc[9])
    print(values.loc['2019-10':'2020-12'])
    print(values.loc['2021-06':'2022-12'])
