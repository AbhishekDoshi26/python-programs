import matplotlib.pyplot as plt
import numpy as np
import random

x = random.sample(range(0, 10), 10)

y = random.sample(range(0, 10), 10)

# label is the one that gives detail about marker
plt.scatter(x, y, label='Data', color='green', marker='*', s=50)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()  # legend is the box that displays marker and label
plt.show()
