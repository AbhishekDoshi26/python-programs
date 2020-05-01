import numpy as np
import matplotlib.pyplot as plt

result = [9.13, 9.60, 9.24, 9.12, 9.20]
sem = [1, 2, 3, 4, 5]

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.set_xlim([1, 8])
axes.set_ylim([5, 10])
axes.plot(sem, result)
plt.grid()
plt.ylabel('CPI')
plt.xlabel('Semester')
plt.title('Result of Abhishek Doshi (170050107024)')
plt.show()
