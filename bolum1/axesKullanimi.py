# Veriseti işlemleri için pandas kütüphanesi,
# Grafik çizimleri için de matplotlib kütüphanesi import edildi
import matplotlib.pyplot as plt
import pandas as pd

# data_by_year.csv dosyası projeye eklendi
df=pd.read_csv('data_by_year.csv')

# İlk grafik için axes() komutu ile x,y 
# koordinatları ve grafiğin genişlik ve yüksekliğini belirttik.
plt.axes([0.05, 0.05, 0.425, 0.9])

# Yıllara göre şarkıların akustiklik oranı için kırmızı renk (r) kullandık.
plt.plot(df.year, df.acousticness, 'r')

# Grafiğin x koordinatında year değişkeni kullanacağımız için etiketinde Year kullandık
plt.xlabel("Year")

# Akustikliğinin grafiği olduğu için grafiğe bu başlığı verdik.
plt.title("Acousticness")

# 2. Grafik için konumlar, genişlik ve yükseklik belirlenir.
plt.axes([0.525,0.5,0.425,0.9])

# Yıllara göre şarkıların dans edilebilirlik oranı için mavi renk (b) kullandık.
plt.plot(df.year, df.danceability, 'b')

plt.xlabel("Year")

# Dans edilebilirliğin grafiği olduğu için grafiğe bu başlığı verdik.
plt.title("Danceability")

# show() komutuyla grafiği çağırdık.
# Spyder kullandığımız için "Plots" bölümünde grafikleri görebiliriz.
plt.show()