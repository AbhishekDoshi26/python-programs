import numpy as np
import matplotlib.pyplot as plt

time = np.arange(0.0, 2.0, 0.01)
s = 1 + np.cos(2*np.pi*time)
plt.plot(time, s, 'g')
plt.xlabel('Time')
plt.ylabel('Voltage (mV)')
plt.title('Cosine Wave Plot (cos(x))')
plt.show()
