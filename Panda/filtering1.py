import pandas as pd

employees = pd.read_csv('Datasets\employees.csv')

# Displays the info such as column data type.
print(employees.info())
# Now, the task is to change the data type of all the columns to correct datatype
# Change Start Date to date-time data format
employees['Start Date'] = pd.to_datetime(employees['Start Date'])
# Change Login Time into date-time data format
employees['Last Login Time'] = pd.to_datetime(employees['Last Login Time'])
# Change Senior Management into Boolean data format
employees['Senior Management'] = employees['Senior Management'].astype(bool)
# Change Gender into Category data format
employees['Gender'] = employees['Gender'].astype("category")
