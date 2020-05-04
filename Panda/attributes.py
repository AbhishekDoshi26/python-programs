import pandas as pd
men = ['Smart', 'Intelligent', 'Caring', 'Loving']
s = pd.Series(men)
print(s.values)  # Displays values as array
print(s.index)  # Displays start and end index
print(s.dtype)  # Displays data type
