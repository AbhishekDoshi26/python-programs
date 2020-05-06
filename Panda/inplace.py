import pandas as pd
y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
y.sort_values(inplace=True, ascending=False)
# inplace replaces the original list with the sorted list.
# It is like: y=y.sort(ascending=False)
print(y)
