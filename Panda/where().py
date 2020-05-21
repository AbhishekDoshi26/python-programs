import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

print(bond.where(bond['Actor'] == 'Sean Connery'))
