REGIMES_BY_CONDITIONS = {('Expansion', 'Low Inflation'): 'Goldilocks',
                         ('Expansion', 'High Inflation'): 'Inflationary Boom',
                         ('Contraction', 'High Inflation'): 'Stagflation',
                         ('Contraction', 'Low Inflation'): 'Risk-Off',
                         
                         }

REGIME_ALLOCATIONS = {'Goldilocks': 
                        {'overweight': ['Equities', 'Credit'], 
                         'underweight': ['Commodities', 'Gold']},
                    'Inflationary Boom': 
                        {'overweight': ['Commodities', 'TIPS'],
                         'underweight': ['Bonds', 'USD']},
                    'Stagflation': 
                        {'overweight': ['Gold', 'Commodities'],
                         'underweight': ['Equities', 'Duration']},
                    'Risk-Off': 
                        {'overweight': ['Long Bonds', 'Gold', 'USD'],
                         'underweight': ['Equities', 'Credit']},

                        }

def pmi_classification(pmi, pmi_benchmark = 50.0):
    try:
        clean_pmi = float(pmi)
    except ValueError:
        raise ValueError('Please input a numerical value')

    if clean_pmi < 0 or clean_pmi > 100:
        raise ValueError('Error: Please provide a PMI value between 0 and 100')

    if clean_pmi > pmi_benchmark:
        return 'Expansion'
    else:
        return 'Contraction'
    
def cpi_classification(cpi, cpi_benchmark = 2.5):
    try:
        clean_cpi = float(cpi)
    except ValueError:
        raise ValueError('Please input a numerical value')
    
    if clean_cpi < cpi_benchmark:
        return 'Low Inflation'
    else:
        return 'High Inflation'
    
def classify_regime(pmi, cpi, pmi_benchmark = 50.0, cpi_benchmark = 2.5):
    pmi_status = pmi_classification(pmi, pmi_benchmark)
    cpi_status = cpi_classification(cpi, cpi_benchmark)

    regime = REGIMES_BY_CONDITIONS[(pmi_status, cpi_status)]
    
    allocation = REGIME_ALLOCATIONS[regime]
    overweight = allocation['overweight']
    underweight = allocation['underweight']

    return {
        'regime': regime,
        'overweight': overweight,
        'underweight': underweight,
    }

# Test Cases
test_cases = [
    {'pmi': 55.0, 'cpi': 2.1, 'expected_regime': 'Goldilocks'},
    {'pmi': 58.0, 'cpi': 5.4, 'expected_regime': 'Inflationary Boom'},
    {'pmi': 47.0, 'cpi': 9.1, 'expected_regime': 'Stagflation'},
    {'pmi': 44.0, 'cpi': 1.2, 'expected_regime': 'Risk-Off'},
]

for test in test_cases:
    result = classify_regime(test['pmi'], test['cpi'])
    assert result['regime'] == test['expected_regime'], f" Case {test['pmi']} Expected  {test['expected_regime']} but got {result['regime']}"
    print(f" PMI: {test['pmi']} | CPI: {test['cpi']}% | Regime: {result['regime']}")
    print(f" Overweight: {result['overweight']}")
    print(f" Underweight: {result['underweight']}")
    
    print()