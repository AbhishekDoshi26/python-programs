import pandas as pd
rate = [10, 20, 3.95, 7.85, 4.65, 1.26, 3.84, 2.79]
index = [10, 20, 30, 40, 50, 60, 70, 80]
r = pd.Series(rate)
print('Sum of all values: ', r.sum())
print('Product of all values: ', r.product())
print('Average of all values: ', r.mean())
print(pd.Series(rate, index, name='List'))
