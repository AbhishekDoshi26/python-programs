# Filtering using AND OR operators.
# Operations on multiple columns
import pandas as pd

employees = pd.read_csv('Datasets\employees.csv', parse_dates=[
                        "Start Date", "Last Login Time"])
employees['Senior Management'] = employees['Senior Management'].astype(bool)
employees['Gender'] = employees['Gender'].astype("category")

data1 = employees['Gender'] == 'Male'
data2 = employees['Team'] == 'Marketing'
data3 = employees['Bonus %'] < 1.5
print(employees[data1 & data2 & data3])
