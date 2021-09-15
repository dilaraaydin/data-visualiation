import numpy as np
import matplotlib.pyplot as plt

u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

X,Y = np.meshgrid(u, v)

Z = np.sin(3*np.sqrt(X**2 + Y**2))

# ilk grafik için;
plt.subplot(2,2,1)
# contourf() içerisinde cmap ile yazılan değer grafiğin 
# içereceği renk skalasıdır. 
plt.contourf(X,Y,Z,20, cmap='twilight')
# colorbar(), grafiğin yanında renk skalasını gösterir.
plt.colorbar()
plt.title('Twilight')
# 2. grafik için;
plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')
# 3. grafik için;
plt.subplot(2,2,3)
plt.contourf(X,Y,Z,20,cmap='autumn')
plt.colorbar()
plt.title('Autumn')
# 4. grafik için;
plt.subplot(2,2,4)
plt.contourf(X,Y,Z,20,cmap='winter')
plt.colorbar()
plt.title('Winter')

plt.tight_layout()
plt.show()