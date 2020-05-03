import matplotlib.pyplot as plt

activities = ['TOC', 'AJ', '.Net', 'WT', 'SE']
slices = [3, 7, 8, 6, 5]
plt.pie(slices, labels=activities, startangle=90,
        explode=(0.2, 0, 0, 0, 0), autopct='%1.2f%%')
# explode gives the slice out of the chart.
# autopct gives % automatically and %1.2%% means that 2 values after decimal
plt.legend()
plt.show()
