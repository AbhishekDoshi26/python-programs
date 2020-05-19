import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

bond.rename(columns={'Year': 'Release Date',
                     'Box Office': 'Revenue'}, inplace=True)
print(bond)

bond.rename(index={'Dr. No': 'Doctor No',
                   'GoldenEye': 'Golden Eye'}, inplace=True)
print(bond)

bond.columns = ['Release Year', 'Actor',
                'Director', 'Revenue', 'Budget', 'Actor Salary']
print(bond)
