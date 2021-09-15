import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)
X,Y = np.meshgrid(u, v)
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

# contour(), konturları çizgiler olarak görüntüler.
plt.subplot(2,2,1)
plt.contour(Z)
plt.title('contour')

plt.subplot(2,2,2)
plt.contour(X, Y, Z, 20)
plt.title('contour')

# contourf() konturlar arasında doldurulmuş alanları görüntüler.
plt.subplot(2,2,3)
plt.contourf(Z)
plt.title('contourf')

plt.subplot(2,2,4)
plt.contourf(X, Y, Z, 20)
plt.title('contourf')

plt.tight_layout()
plt.show()
