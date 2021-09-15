# Z değişkenini oluştururken matematiksel 
# ifadeler kullanacağımız için Numpy kütüphanesini import ettik.
# Grafiksel işlemler için de matplotlib kütüphanesini import ettik.
import numpy as np
import matplotlib.pyplot as plt

# meshgrid() 2 parametre alacağından, u ve v adında 
# 1 Boyutlu 2 adet dizi oluşturduk.
u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# meshgrid kullanarak 2 Boyutlu bir dizi oluşturduk.
X,Y = np.meshgrid(u, v)

# X ve Y 'ye göre Z'yi hesapladık.
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

plt.pcolor(Z)
plt.show()
