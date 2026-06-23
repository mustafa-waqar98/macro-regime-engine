from src.phase_2.main import format_report
import pandas as pd

cpi_value = 4.0
cpi_date = pd.Timestamp('2026-05-01')
pmi_value_raw = 5.7
pmi_value_smoothed = 12.1
pmi_date = pd.Timestamp('2026-06-01')
classification = {'regime': 'Inflationary Boom', 'overweight': ['Commodities', 'TIPS'], 'underweight': ['Bonds', 'USD']}

test = format_report(cpi_value, cpi_date, pmi_value_raw, pmi_value_smoothed, pmi_date, classification)
expected = "Current Regime: Inflationary Boom\nPMI (3M avg) as of June 2026: 12.1 (raw: 5.7)\nCPI as of May 2026: 4.0%\nOverweight: Commodities, TIPS\nUnderweight: Bonds, USD"
assert test == expected, f"\nGOT:\n{test}\nEXPECTED:\n{expected}"
print('format_report: passed')