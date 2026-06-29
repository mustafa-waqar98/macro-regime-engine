from src.phase_3.momentum import momentum
import pytest
import pandas as pd

def test_momentum():
    series = pd.Series([
        7.5333333, 3.7933333, 8.6366667, 13.193333, 21.296667, 
        19.856667, 22.61, 16.133333, 14.623333, 4.25
        ])
    values = momentum(series)

    assert values.iloc[5] == pytest.approx(11.461111, abs=1e-4)
    assert values.iloc[9] == pytest.approx(-9.585556, abs = 1e-4)