import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv')
print(bond.iloc[0:20:2])

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index()
print(bond.iloc[0])
print(bond.loc['Dr. No'])
