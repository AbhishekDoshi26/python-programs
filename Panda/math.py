import pandas as pd

y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
print(y.count())  # Counts number of rows
print(len(y))  # Counts number of rows
print(y.sum())  # Adds all data
print(y.mean())  # Calculates Average
print(y.std())  # Calculates Standard Deviation
print(y.min())  # Prints minimum value
print(y.max())  # Prints maximum value
print(y.median())  # Prints Median
