import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('stocks.csv', index_col='date',
               parse_dates=True)

# aapl genel hisse değişimi(her grafikte olan siyah renkli çizgi) ve
# mean_30 için [::30] ile aapl'nin 30 günlük değişim ortalamalarını
# aynı grafikte gösterdik.
mean_30=df.aapl[::30]
plt.subplot(3,2,1)
plt.plot(mean_30, color='green')
plt.plot(df.aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')

# siyah çizgi ile gösterilen aapl genel hisse değişimi ve
# mean_75 ile aapl'nin 75 günlük değişim ortalamalarını
# aynı grafikte gösterdik.
mean_75=df.aapl[::75]
plt.subplot(3,2,2)
plt.plot(mean_75, color='red')
plt.plot(df.aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

# siyah çizgi ile gösterilen aapl genel hisse değişimi ve
# mean_125 ile aapl'nin 125 günlük değişim ortalamalarını
# aynı grafikte gösterdik.
mean_125=df.aapl[::125]
plt.subplot(3, 2, 3)
plt.plot(mean_125, color='magenta')
plt.plot(df.aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

# siyah çizgi ile gösterilen aapl genel hisse değişimi ve
# mean_250 ile aapl'nin 250 günlük değişim ortalamalarını
# aynı grafikte gösterdik.
mean_250=df.aapl[::250]
plt.subplot(3,2,4)
plt.plot(mean_250,color='cyan')
plt.plot(df.aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

plt.tight_layout()
plt.show()