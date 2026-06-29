import pandas as pd

TILT_TABLE = {
    ('Goldilocks', 'accel'): 'lean-in',
    ('Goldilocks', 'decel'): 'de-risk',
    ('Goldilocks', 'flat'): 'hold',
    ('Inflationary Boom', 'accel'): 'lean-in',
    ('Inflationary Boom', 'decel'): 'de-risk',
    ('Inflationary Boom', 'flat'): 'hold',
    ('Stagflation', 'accel'): 'de-risk',
    ('Stagflation', 'decel'): 'lean-in',
    ('Stagflation', 'flat'): 'hold',
    ('Risk-Off', 'accel'): 'de-risk',
    ('Risk-Off', 'decel'): 'lean-in',
    ('Risk-Off', 'flat'): 'hold',
}

def lookup(regime, state):
    if state == 'none':
        return 'hold'
    return TILT_TABLE[(regime, state)]

def momentum_to_state(momentum, deadband=1.0):
    if pd.isna(momentum):
        return 'none'
    elif momentum > deadband:
        return 'accel'
    elif momentum < -deadband:
        return 'decel'
    else:
        return 'flat'
    

for val in [2.5, -2.5, 0.3, -0.8, float('nan')]:
    print(val, '->', momentum_to_state(val))
    print(lookup('Goldilocks', 'accel'))
    print(lookup('Risk-Off', 'accel'))
    print(lookup('Stagflation', 'decel'))
    print(lookup('Goldilocks', 'none'))

