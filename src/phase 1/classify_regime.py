def pmi_classification(pmi, pmi_benchmark = 50.0):
    if pmi > pmi_benchmark:
        return 'Expansion'
    else:
        return 'Contraction'
    
def cpi_classification(cpi, cpi_benchmark = 2.5):
    if cpi < cpi_benchmark:
        return 'Low Inflation'
    else:
        return 'High Inflation'
    
def classify_regime(pmi, cpi, pmi_benchmark = 50.0, cpi_benchmark = 2.5):
    pmi_status = pmi_classification(pmi, pmi_benchmark)
    cpi_status = cpi_classification(cpi, cpi_benchmark)

    if pmi_status == 'Expansion' and cpi_status == 'Low Inflation':
        regime = 'Goldilocks'
        overweight = ['Equities', 'Credit']
        underweight = ['Commodities', 'Gold']
    elif pmi_status == 'Expansion' and cpi_status == 'High Inflation':
        regime = 'Inflationary Boom'
        overweight = ['Commodities', 'TIPS']
        underweight = ['Bonds', 'USD']
    elif pmi_status == 'Contraction' and cpi_status == 'High Inflation':
        regime = 'Stagflation'
        overweight = ['Gold', 'Commodities']
        underweight = ['Equities', 'Duration']
    else:
        regime = 'Risk-Off'
        overweight = ['Long Bonds', 'Gold', 'USD']
        underweight = ['Equities', 'Credit']

    return {
        'regime': regime,
        'overweight': overweight,
        'underweight': underweight
    }

# Test Cases
test_cases = [
    {'pmi': 55.0, 'cpi': 2.1},
    {'pmi': 58.0, 'cpi': 5.4},
    {'pmi': 47.0, 'cpi': 9.1},
    {'pmi': 44.0, 'cpi': 1.2},
]

for test in test_cases:
    result = classify_regime(test['pmi'], test['cpi'])
    print(f'PMI: {test['pmi']} | CPI: {test['cpi']}% | Regime: {result['regime']}')
    print(f' Overweight: {result['overweight']}')
    print(f' Underweight: {result['underweight']}')
    print()


classify_regime(55, 2.1)
