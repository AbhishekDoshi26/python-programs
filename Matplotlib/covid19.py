import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

x = []
y1 = []

y = pd.read_csv('D:\python-programs\Datasets\covid_19_india.csv',
                squeeze=True, usecols=["State/UnionTerritory", "Confirmed"], index_col='State/UnionTerritory')
with open('D:\python-programs\Datasets\covid_19_india.csv', 'r')as datafile:
    plots = csv.reader(datafile)
    for col in plots:
        x.append(col[3])
        y1.append(col[8])

plt.axes([0.3, 0.3, .5, .5])
plt.bar(x, y1)
plt.xlabel('States')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=90)
plt.title('COVID-19 Cases in India')
plt.show()
