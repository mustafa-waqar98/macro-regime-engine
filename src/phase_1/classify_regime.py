REGIME_BY_CONDITIONS = {('Expansion', 'Low Inflation'): 'Goldilocks',
                         ('Expansion', 'High Inflation'): 'Inflationary Boom',
                         ('Contraction', 'High Inflation'): 'Stagflation',
                         ('Contraction', 'Low Inflation'): 'Risk-Off',
                         
                         }

ALLOCATIONS_BY_REGIME = {'Goldilocks': 
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

def pmi_classification(pmi, pmi_benchmark = 0.0):
    try:
        clean_pmi = float(pmi)
    except ValueError:
        raise ValueError('Please input a numerical value')

    if clean_pmi < -100 or clean_pmi > 100:
        raise ValueError('Error: Please provide a PMI value between -100 and 100')

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
    
def classify_regime(pmi, cpi, pmi_benchmark = 0.0, cpi_benchmark = 2.5):
    pmi_status = pmi_classification(pmi, pmi_benchmark)
    cpi_status = cpi_classification(cpi, cpi_benchmark)

    regime = REGIME_BY_CONDITIONS[(pmi_status, cpi_status)]
    
    allocation = ALLOCATIONS_BY_REGIME[regime]
    overweight = list(allocation['overweight'])
    underweight = list(allocation['underweight'])

    return {
        'regime': regime,
        'overweight': overweight,
        'underweight': underweight,
    }

# Safety Check
for conditions, regime in REGIME_BY_CONDITIONS.items():
    assert regime in ALLOCATIONS_BY_REGIME, f" The conditions cell {conditions} maps to regime {regime}, but {regime} has no entry in ALLOCATIONS_BY_REGIME"

print("")


if __name__ == '__main__':
    # Test Cases
    test_cases = [
        {'pmi': 15.0, 'cpi': 2.1, 'expected_regime': 'Goldilocks', 'expected_overweight': ['Equities', 'Credit'],'expected_underweight': ['Commodities', 'Gold']}, 
        {'pmi': 20.0, 'cpi': 5.4, 'expected_regime': 'Inflationary Boom', 'expected_overweight': ['Commodities', 'TIPS'],'expected_underweight': ['Bonds', 'USD']},
        {'pmi': -10.0, 'cpi': 9.1, 'expected_regime': 'Stagflation', 'expected_overweight': ['Gold', 'Commodities'],'expected_underweight': ['Equities', 'Duration']},
        {'pmi': -18.0, 'cpi': 1.2, 'expected_regime': 'Risk-Off', 'expected_overweight': ['Long Bonds', 'Gold', 'USD'],'expected_underweight': ['Equities', 'Credit']},
    ]

    for test in test_cases:
        result = classify_regime(test['pmi'], test['cpi'])
        assert result['regime'] == test['expected_regime'], f" Case {test['pmi']} Expected  {test['expected_regime']} but got {result['regime']}"
        assert result['overweight'] == test['expected_overweight'], f" Case {test['pmi']} Expected  {test['expected_overweight']} but got {result['overweight']}"
        assert result['underweight'] == test['expected_underweight'], f" Case {test['pmi']} Expected  {test['expected_underweight']} but got {result['underweight']}"
        print(f" PMI: {test['pmi']} | CPI: {test['cpi']}% | Regime: {result['regime']}")
        print(f" Overweight: {result['overweight']}")
        print(f" Underweight: {result['underweight']}")
        
        print()