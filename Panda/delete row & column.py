import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

bond.drop('A View to a Kill', inplace=True)

bond.drop(['Dr. No', 'Casino Royale'])

bond.drop(columns={'Box Office'})

bond.drop(['Box Office', 'Budget'], axis=1)

actor = bond.pop('Actor')

del bond['Director']
print(bond)
