import matplotlib.pyplot as plt

age = [2, 50, 10, 70, 8, 21, 22, 30, 40, 64, 78, 20,
       36, 78, 0, 85, 20, 36, 90, 8, 75, 21, 56, 32, 14]
range = (0, 100)  # Range of data
bins = 10  # Range for Y-axis as histogram works only on x-axis.

plt.hist(age, bins, range, color='green', histtype='bar', rwidth=0.7)
# histtype is type of histogram and rwidth is width between the bars
plt.xlabel('Ages')
plt.title('Histogram')
plt.ylabel('Bins')
plt.show()
