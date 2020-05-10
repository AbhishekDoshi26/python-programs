import pandas as pd

nba = pd.read_csv('Datasets\\nba.csv')

# Replace all NULL values
nba.fillna(value=0, inplace=True)
# Replace all NULL Values in Salary
nba['Salary'].fillna(value=0, inplace=True)
# Replace all NULL Values in College
nba['College'].fillna(value="No College", inplace=True)
print(nba.head())
