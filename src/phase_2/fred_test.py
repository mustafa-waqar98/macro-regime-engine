import os
from fredapi import Fred

api_key = os.environ['FRED_API_KEY']
fred = Fred(api_key=api_key)

print(fred.get_series('CPIAUCSL'))
