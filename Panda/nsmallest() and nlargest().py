import pandas as pd

bond = pd.read_csv('Datasets\jamesbond.csv', index_col='Film')
bond.sort_index(inplace=True)

bond.nsmallest(n=3, columns='Box Office')

bond.nlargest(n=3, columns='Box Office')

print(bond['Box Office'].nlargest(10))
