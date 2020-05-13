import pandas as pd

employees = pd.read_csv('Datasets\employees.csv', parse_dates=[
                        "Start Date", "Last Login Time"])
employees['Senior Management'] = employees['Senior Management'].astype(bool)
employees['Gender'] = employees['Gender'].astype("category")

# Prints all data that contains Team value as NaN or NULL
print(employees[employees['Team'].isnull()])

# Prints all data that doesn't contain null values
print(employees[employees['Team'].notnull()])
