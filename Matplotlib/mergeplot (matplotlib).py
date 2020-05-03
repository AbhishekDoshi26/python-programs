import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos')

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Sin and Cos Functions')
plt.legend()
plt.show()
