from src.phase_2.fred_data import snapshot_to_series
import pandas as pd

def test_snapshot_to_series():
    series = pd.DataFrame({
            'date': ['2020-03-01', '2020-01-01', '2020-02-01'],
            'value': ['100', '101', '98'],
        })

    result = snapshot_to_series(series)

    assert result.dtype == float
    assert result.index.is_monotonic_increasing
    assert result.iloc[0] == 101.00
