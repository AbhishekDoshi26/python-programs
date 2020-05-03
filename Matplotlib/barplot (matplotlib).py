import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 24, 36, 40, 5]
label = ['One', 'Two', 'Three', 'Four', 'Five']

plt.bar(x, y, tick_label=label, width=0.8, color=['green', 'blue', 'black'])
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar Graph')
plt.show()
