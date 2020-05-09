import pandas as pd

nba = pd.read_csv('Datasets\\nba.csv')

# Removes all the rows that contain any NaN or NULL Value for a column
print(nba.dropna())

# Removes the rows that contains all NULL values.
nba.dropna(how="all", inplace=True)
print(nba)

# Removes null values from a specific column
print(nba.dropna(subset=['Salary']))
