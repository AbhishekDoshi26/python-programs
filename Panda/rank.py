import pandas as pd

nba = pd.read_csv('Datasets\\nba.csv')
nba.dropna(how='all', inplace=True)
nba['Salary'].fillna(0, inplace=True)
nba['SalaryRank'] = nba['Salary'].rank(ascending=False).astype(int)
nba.sort_values(by="Salary", ascending=False, inplace=True)
print(nba)
