import pandas as pd
y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
y.sort_values(ascending=False, inplace=True)
# Now the value of y is the series in descending order

y.sort_index(inplace=True)
# Now the data is again back to the old one.
print(y)
