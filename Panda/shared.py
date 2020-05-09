import pandas as pd

nba = pd.read_csv('Datasets//nba.csv')
print(nba.head(11))

# Extract Data Column wise
# Name is the column name. Drawback is that the column name must not have space
print(nba.Name.head())

print(nba["Name"].head())  # Using List. Can have space.

columns = ["Name", "Team"]
print(nba[columns].head())  # Accessing multiple columns
