import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv')

data = bond.loc[[0, 1, 25]]
print(data)
