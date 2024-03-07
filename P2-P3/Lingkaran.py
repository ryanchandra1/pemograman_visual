import numpy as np
import matplotlib.pyplot as plt

print("\033c")

x = np.linspace(-8,8,10000)
plt.figure(figsize=(8,6.5))


y = x -x -0
y1 = (4-x**2)**0.5
y2 = -(4-x**2)**0.5

y3 =5 + (4-(x-5)**2)**0.5
y4 =5 - (4-(x-5)**2)**0.5

y5 =-5 + (4-(x-5)**2)**0.5
y6 =-5 - (4-(x-5)**2)**0.5

y7 =5 + (4-(x-5)**2)**0.5
y8 =5 - (4-(x-5)**2)**0.5

y9 =-5 - (4-(x-5)**2)**0.5
y10 =-5 - (4-(x-5)**2)**0.5

plt.plot(x, y , '-k')
plt.plot(x, y1 , '-r', label= 'y1, y2')
plt.plot(x, y2 , '-r')
plt.plot(x, y3 , '-g', label= 'y1, y2')
plt.plot(x, y , '-k')
plt.plot(x, y , '-r', label= 'y1, y2')
plt.plot(x, y , '-k')
plt.plot(x, y , '-r', label= 'y1, y2')
plt.plot(x, y , '-k')
plt.plot(x, y , '-r', label= 'y1, y2')