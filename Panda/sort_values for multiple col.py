import pandas as pd

nba = pd.read_csv('Datasets//nba.csv')

# Sort according to team and inside team, name will also be sorted
nba.sort_values(["Team", "Name"], inplace=True)

# Sort according to team and inside team, name will also be sorted descending
nba.sort_values(["Team", "Name"], ascending=[True, False], inplace=True)
print(nba.head())
