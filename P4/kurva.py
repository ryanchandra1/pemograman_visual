print("\033c")

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4, 4, 10000)
plt.figure(figsize=(3, 30))

plt.plot(x, -((0.01 - x**2)**0.5), '-k')  # Negate the function values
plt.plot(x, ((0.01 - x**2)**0.5), '-k')  # Negate the function values

y = x - x - 0
y1 = -(x**3 - 2*x**2 - x + 2)  # Negate the function values

plt.plot(x, y, '-k')
plt.plot(x, y1, '-p', label='y1')

plt.legend(loc='upper left')
plt.grid()
plt.show()
