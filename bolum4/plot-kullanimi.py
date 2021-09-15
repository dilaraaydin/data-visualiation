import matplotlib.pyplot as plt
import pandas as pd

# 4 tane farklı hisse değişkenlerini içeren stocks.csv
# dosyasını Pandas ile dahil ettik.
df1 = pd.read_csv('stocks.csv')

# Her bir hisse değişkenini tek 1 grafikte çizdik.
plt.plot(df1.aapl, color='blue', label='AAPL')

plt.plot(df1.ibm, color='green', label='IBM')

plt.plot(df1.csco, color='red', label='CSCO')

plt.plot(df1.msft, color='magenta', label='MSFT')

# 4 hissenin grafikte hangisi olduğunu
# belirtmek için sol üste bir gösterge ekledik.
plt.legend(loc='upper left')

# rotation değeri ile x eksenindeki değerlerin
# eğimli görünmesini sağladık.
plt.xticks(rotation=60)

plt.show()