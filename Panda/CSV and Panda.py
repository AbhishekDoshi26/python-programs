import pandas as pd
x = pd.read_csv('data.csv', squeeze=True, usecols=['X-Axis'])
# squeeze converts csv file into panda series.
# usecols defines which column yoou want to access

print(x.head())  # Extracts  values from start
print(x.head(7))  # Extracts 7 values from start

print(x.tail())  # Extracts 5 values from end

print(x.values)  # Displays only values

# Checks if there are any repeated values or not. Returns True if all are unique
print(x.is_unique)

# To get the dimension of series
print(x.ndim)

# To print number of rows and columns
print(x.shape)

print(x.size)

# Prints column name
print(x.name)
