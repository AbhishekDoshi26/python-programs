import pandas as pd
y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
print(y.sort_values())  # Ascending
print(y.sort_values(ascending=False))  # Descending
