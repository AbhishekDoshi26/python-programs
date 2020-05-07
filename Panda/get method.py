import pandas as pd

y = pd.read_csv('data.csv', squeeze=True, index_col='X-Axis')
y.sort_index(inplace=True)

# Displays data of One and Three
test = y.get(["One", "Three"])
print(test)

# Displays the default value if there's no data.
test = y.get('Zero', default='Data Not Available!!')
print(test)
