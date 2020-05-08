import pandas as pd

google = pd.read_csv(
    'D:\python-programs\Datasets\google_stock_price.csv', squeeze=True)


def classify_performance(number):
    if number < 300:
        return "OK"
    elif 650 > number >= 300:
        return "Satisfactory"
    else:
        return "Incredible"


print(google.apply(classify_performance))

# Using Anonymous Function
print(google.apply(lambda stock_price: stock_price+1))
