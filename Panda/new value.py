import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

# Changes the name of Actor of Dr. No
bond.loc['Dr. No', 'Actor'] = 'Sir Sean Connery'
print(bond.loc['Dr. No'])

# Changes multiple values
bond.loc['Dr. No', ['Actor', 'Budget']] = ['Sean Connery', '10']
print(bond.loc['Dr. No'])
