import pandas as pd

employees = pd.read_csv('Datasets\employees.csv', parse_dates=[
                        "Start Date", "Last Login Time"])
employees['Senior Management'] = employees['Senior Management'].astype(bool)
employees['Gender'] = employees['Gender'].astype("category")

employees.sort_values('First Name', inplace=True)

# Prints all duplicates
print(employees[employees['First Name'].duplicated(keep=False)])

# Prints all the unique values
print(employees[~employees['First Name'].duplicated(keep=False)])
