import pandas as pd
y = pd.read_csv('data.csv', squeeze=True, usecols=['Y-Axis'])
# Extract data using index
test = y[5]

# Extracting multiple values
test = y[[5, 7, 8]]

# Extracting series
test = y[5:10]

# Extracting last 6 values
test = y[-6:]
