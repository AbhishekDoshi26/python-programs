import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0.0, 2.0, 0.01)
voltage = np.arange(0, 20, 0.1)
current = []
for (a, b) in zip(voltage, time):
    current.append(a//b)
plt.plot(time, current)
plt.grid()
plt.xlabel('Time')
plt.ylabel('Current (mV)')
plt.title('Cosine Wave Plot (cos(x))')
plt.show()
