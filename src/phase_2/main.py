from src.phase_1.classify_regime import classify_regime
from src.phase_2.fred_data import fetch_cpi, fetch_pmi, smooth, cpi_to_yoy, latest_valid_reading, latest_valid_date


if __name__ == '__main__':

    # CPI
    cpi_raw = fetch_cpi()
    cpi_yoy = cpi_to_yoy(cpi_raw)
    cpi_value = latest_valid_reading(cpi_yoy)
    cpi_date = latest_valid_date(cpi_yoy)

    # PMI
    pmi_series = fetch_pmi()
    smoothed_pmi = smooth(pmi_series)
    pmi_value = latest_valid_reading(smoothed_pmi)
    pmi_date = latest_valid_date(pmi_series)

    # Classify
    regime = classify_regime(pmi_value, cpi_value)

    print(f" PMI date: {pmi_date} | CPI date: {cpi_date}")
    print(f" PMI value: {round(pmi_value, 2)} | CPI value: {round(cpi_value, 2)}")
    print(regime)