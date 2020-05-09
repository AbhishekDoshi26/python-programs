import pandas as pd

nba = pd.read_csv('Datasets\\nba.csv')

nba['Sports'] = 'BasketBall'  # Adds a col 'Sports' with value Basketball
# However, it doesn't affect data in csv file

nba.insert(2, 'Sports', 'Basketball')  # nba.insert(index,column_name,value)
print(nba.head())
