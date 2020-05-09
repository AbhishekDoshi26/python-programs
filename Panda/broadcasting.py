import pandas as pd

nba = pd.read_csv('Datasets//nba.csv')

# Addition
print(nba['Salary'].add(50000))
print(nba['Salary']+50000)

# Subtraction
print(nba['Salary'].sub(50000))
print(nba['Salary']-50000)

# Multiplication
print(nba['Salary'].mul(2))
print(nba['Salary']*2)

# Replace with another column
nba["Weight in KG"] = nba["Weight"]*0.453592
print(nba.head())
