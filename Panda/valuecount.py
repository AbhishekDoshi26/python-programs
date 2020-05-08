import pandas as pd

y = pd.read_csv('data.csv', squeeze=True, index_col='Y-Axis')
print(y.value_counts(ascending=True))
