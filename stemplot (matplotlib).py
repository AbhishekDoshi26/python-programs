import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10)
y = np.exp(np.sin(x))

plt.stem(x, y, use_line_collection=True)
plt.show()
