def classify_regime(pmi, cpi):
    if pmi > 50 and cpi < 2.5:
        regime = "Goldilocks"
        overweight = ["Equities", "Credit"]
        underweight = ["Commodities", "Gold"]
    elif pmi > 50 and cpi >= 2.5:
        regime = "Inflationary Boom"
        overweight = ["Commodities", "TIPS"]
        underweight = ["Bonds", "USD"]
    elif pmi <= 50 and cpi >= 2.5:
        regime = "Stagflation"
        overweight = ["Gold", "Commodities"]
        underweight = ["Equities", "Duration"]
    else:
        regime = "Risk-Off"
        overweight = ["Long Bonds", "Gold", "USD"]
        underweight = ["Equities", "Credit"]

    return {
        "regime": regime,
        "overweight": overweight,
        "underweight": underweight
    }
    

# Test Cases
test_cases = [
    {"pmi": 55.0, "cpi": 2.1},
    {"pmi": 58.0, "cpi": 5.4},
    {"pmi": 47.0, "cpi": 9.1},
    {"pmi": 44.0, "cpi": 1.2},
]

for test in test_cases:
    result = classify_regime(test["pmi"], test["cpi"])
    print(f"PMI: {test['pmi']} | CPI: {test['cpi']}% | Regime: {result['regime']}")
    print(f" Overweight: {result['overweight']}")
    print(f" Underweight: {result['underweight']}")
    print()
