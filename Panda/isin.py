import pandas as pd

employees = pd.read_csv('Datasets\employees.csv', parse_dates=[
                        "Start Date", "Last Login Time"])
employees['Senior Management'] = employees['Senior Management'].astype(bool)
employees['Gender'] = employees['Gender'].astype("category")

# Displays employees from Legal or Sales or Product team
print(employees[employees['Team'].isin(['Legal', 'Sales', 'Product'])])
