# Veriseti işlemleri için pandas kütüphanesi,
# grafiksel işlemler için de matplotlib kütüphanesi
# import edildi
import matplotlib.pyplot as plt
import pandas as pd

# iris.csv verisetini dfiris adında ekledik.
dfiris =pd.read_csv('iris.csv')

plt.style.use('ggplot')
# plt.style.use('fivethirtyeight') gibi diğer stiller de kullanılabilir.

# dfiris verisetindeki sepal ve petal length ve width değerlerine
# ulaştık ve grafikte yeşil ve mavi renkli olarak gösterdik.
plt.scatter(dfiris.sepal_length, dfiris.sepal_width, 
    marker='o', color='green', label='Çanak Yaprağı')
plt.scatter(dfiris.petal_length, dfiris.petal_width,
    marker='o', color='blue', label='Taç Yaprağı')
# çanak ve taç yapraklarının renginin göstergesini grafikte sağ üstte gösterdiğimizi belirttik.
plt.legend(loc='upper rigth')
plt.title('Iris Verisi')
plt.xlabel('Uzunluk')
plt.ylabel('Genişlik')

# grafikte gösterilen verilerin açıklamalarını ok ile işaretleyerek gösterdik.
# burada xy ile verinin konumunu, xytext ile de verilerin açıklamasının konumunu verdik.
plt.annotate('Setosa', xy=(4.9,3.1), 
    xytext=(2.8,2.9), arrowprops={'color':'red'})
plt.annotate('Virginica', xy=(7.2,3.2), 
    xytext=(2.9,2.2), arrowprops={'color':'purple'})
plt.annotate('Versicolor', xy=(6.3,2.3), 
    xytext=(6.5,1.1), arrowprops={'color':'yellow'})

plt.show()