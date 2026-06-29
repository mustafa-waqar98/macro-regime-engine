from src.phase_2.fred_data import collapse_to_snapshot
import pandas as pd

def test_collapse_keeps_latest_revision():
    test_data = pd.DataFrame({
        'realtime_start': ['2019-12-17', '2019-12-20', '2020-01-01'],
        'date': ['2020-01-01', '2020-01-01', '2020-02-01'],
        'value': [100, 101, 98],
    })

    result = collapse_to_snapshot(test_data)
    value = result[result['date'] == '2020-01-01']['value'].iloc[0]
    assert value == 101