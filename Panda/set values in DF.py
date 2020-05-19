import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

bond.loc[bond['Actor'] == 'Sean Connery']['Actor'] = 'Sir Sean Connery'

print(data)
