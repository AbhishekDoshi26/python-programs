import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv')
bond.set_index("Film", inplace=True)  # Does the same work of index_col
print(bond)
bond.reset_index()
print(bond)
