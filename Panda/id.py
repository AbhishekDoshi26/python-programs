import pandas as pd

y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
print(y.idxmax())  # Displays index of maximum value
print(y.idxmin())  # Displays index of minimum value
