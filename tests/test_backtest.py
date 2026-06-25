from src.phase_2.backtest import to_monthly_returns, cumulative
import pandas as pd

def test_to_monthly_returns():
    test_df = pd.DataFrame(
        {'price': [100.0, 110.0, 120.0, 121.0]},
        index=pd.to_datetime(['2026-01-30', '2026-01-31', '2026-02-27', '2026-02-28'])
    )
    result = to_monthly_returns(test_df)
    assert abs(result['price'].iloc[0] - 0.10) < 1e-9
    assert len(result) == 1

def test_cumulative():
    result = cumulative(pd.Series([0.1, 0.1]))
    assert abs(result.iloc[0] - 1.10) < 1e-9
    assert abs(result.iloc[1] - 1.21) < 1e-9 