import pandas as pd

def momentum(series, window=3, delta=3):
    smooth = series.rolling(window).mean()
    result = smooth.diff(delta)

    return result

if __name__ == '__main__':
    path = pd.read_csv('data/vintage_inputs.csv')
    series = path['pmi']
    values = momentum(series)
    print(values.head())
    print(values.tail())
    print(values.iloc[5])
    print(values.iloc[9])
    

