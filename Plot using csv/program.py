import matplotlib.pyplot as plt
import csv

x = []
y1 = []
y2 = []

with open('D:\python-programs\Plot using csv\data.txt', 'r')as datafile:
    plots = csv.reader(datafile)
    for col in plots:
        x.append(col[0])
        y1.append(col[1])

with open('D:\python-programs\Plot using csv\data.csv', 'r')as datafile:
    plots = csv.reader(datafile)
    for col in plots:
        y2.append(col[1])


plt.plot(x, y1, label='Text File Data')
plt.plot(x, y2, label='CSV File Data')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Plot using txt and csv file')
plt.legend()
plt.show()
