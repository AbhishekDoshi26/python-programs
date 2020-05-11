import pandas as pd

employees = pd.read_csv('Datasets\employees.csv', parse_dates=[
                        "Start Date", "Last Login Time"])
employees['Senior Management'] = employees['Senior Management'].astype(bool)
employees['Gender'] = employees['Gender'].astype("category")

# Extract data that has Gender = Male
print(employees[employees['Gender'] == 'Male'])

# It can also be done as:
data = employees['Gender'] == 'Male'
print(employees[data])
