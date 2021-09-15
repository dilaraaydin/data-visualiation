# Veriseti işlemleri için pandas kütüphanesi,
# grafiksel işlemler için de matplotlib kütüphanesi
# import edildi
import matplotlib.pyplot as plt
import pandas as pd

# data_by_year.csv dosyası projeye eklendi
df=pd.read_csv('data_by_year.csv')

# 2x1 alt planlı 1. grafiği oluşturur.
plt.subplot(2,1,1)
plt.plot(df.year, df.acousticness, 'r')
plt.xlabel('Year')
plt.title('Acousticness')

# 2x1 alt planlı 2. grafiği oluşturur.
plt.subplot(2,1,2)
plt.plot(df.year, df.danceability, 'b')
plt.xlabel('Year')
plt.title('Danceability')

plt.tight_layout()
plt.show()