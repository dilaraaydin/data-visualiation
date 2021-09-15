# Veriseti işlemleri için pandas kütüphanesi,
# grafiksel işlemler için de matplotlib kütüphanesi
# import edildi
import matplotlib.pyplot as plt
import pandas as pd

# data_by_year.csv dosyası projeye eklendi
df=pd.read_csv('data_by_year.csv')

plt.plot(df.year, df.danceability)
plt.xlabel('Year')
plt.ylabel('Danceability')
plt.title('Dans edilebilir şarkı sayısının 100 yıl içindeki değişimi')

# xlim ve ylim ile ayrı ayrı verdiğimiz değer aralıklarını 
# 4 parametre alan axis() içerisinde aynı anda verebiliyoruz.
# Aynı sonucu alırız.
plt.axis((1920,2020,0.4,0.7))

plt.show()