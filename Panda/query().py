import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)
bond.columns = [column_name.replace(' ', '_') for column_name in bond.columns]

print(bond.query(expr='Budget > 10.0'))
