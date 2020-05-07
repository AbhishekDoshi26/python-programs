import pandas as pd
y = pd.read_csv('data.csv', squeeze=True, index_col='X-Axis')
test = y["One"]
print(test)
