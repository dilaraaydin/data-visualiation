# Veriseti işlemleri için pandas kütüphanesi,
# grafiksel işlemler için de matplotlib kütüphanesi
# import edildi
import matplotlib.pyplot as plt
import pandas as pd

# iris.csv verisetini dfiris adında ekledik.
dfiris =pd.read_csv('iris.csv')

# dfiris verisetindeki sepal ve petal length ve width değerlerine
# ulaştık ve grafikte yeşil ve mavi renkli olarak gösterdik.
plt.scatter(dfiris.sepal_length, dfiris.sepal_width, 
    marker='o', color='green', label='Çanak Yaprağı')
plt.scatter(dfiris.petal_length, dfiris.petal_width,
    marker='o', color='blue', label='Taç Yaprağı')

# çanak ve taç yapraklarının renginin göstergesini grafikte sağ üstte gösterdiğimizi belirttik.
plt.legend(loc='upper rigth')
plt.title('Iris Verisi')

# x eksenine Uzunluk, y eksenine Genişlik adını verdik.
plt.xlabel('Uzunluk')
plt.ylabel('Genişlik')

plt.show()