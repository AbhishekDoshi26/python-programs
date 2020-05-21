import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)


def add_millions(number):
    return str(number)+' Millions'


bond['Box Office'] = bond['Box Office'].apply(add_millions)
print(bond)
