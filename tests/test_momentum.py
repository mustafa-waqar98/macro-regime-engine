from src.phase_3.momentum import momentum
from src.phase_3.momentum_tilt import lookup, momentum_to_state, apply_tilt
import pytest
import pandas as pd
from pandas.testing import assert_series_equal

def test_momentum():
    series = pd.Series([
        7.5333333, 3.7933333, 8.6366667, 13.193333, 21.296667, 
        19.856667, 22.61, 16.133333, 14.623333, 4.25
        ])
    values = momentum(series)

    assert values.iloc[5] == pytest.approx(11.461111, abs=1e-4)
    assert values.iloc[9] == pytest.approx(-9.585556, abs = 1e-4)

def test_momentum_to_state():
    assert momentum_to_state(2.5) == 'accel'
    assert momentum_to_state(-2.5) == 'decel'
    assert momentum_to_state(0.5) == 'flat'
    assert momentum_to_state(float('nan')) == 'none'

def test_lookup():
    assert lookup('Risk-Off', 'accel') == 'de-risk'
    assert lookup('Stagflation', 'decel') == 'lean-in'
    assert lookup('Goldilocks', 'flat') == 'hold'
    assert lookup('Stagflation', 'flat') == 'hold'
    assert lookup('Goldilocks', 'none') == 'hold'

def test_apply_tilt():
    row = pd.Series({'TLT': 0.34, 'GLD': 0.33, 'BIL': 0.33})
    result = apply_tilt(row, 'de-risk', 0.20, 0.10)
    expected = pd.Series({'TLT': 0.238, 'GLD': 0.231, 'BIL': 0.531})
    assert_series_equal(result, expected)