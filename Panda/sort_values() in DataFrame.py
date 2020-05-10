import pandas as pd

nba = pd.read_csv('Datasets//nba.csv')
# NAN or NULL values will be at starting
# na_position='last' will bring them at last.
nba.sort_values("Salary", ascending=False, inplace=True, na_position="first")
print(nba.head())
