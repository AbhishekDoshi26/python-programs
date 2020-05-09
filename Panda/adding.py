import pandas as pd
rev = pd.read_csv('D:\python-programs\Datasets\\revenue.csv', index_col="Date")

print(rev.sum())  # Adds data column-wise

print(rev.sum(axis=0))  # 0 is used for Column wise adding
print(rev.sum(axis=1))  # 1 is used for Row wise adding
