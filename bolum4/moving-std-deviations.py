import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv('stocks.csv', index_col='date',
               parse_dates=True)

# Pandas kütüphanesinin series() metodunda aapl 
# değişkenini kullanarak aapl değişkenini s serisine 
# aktardık 
s = pd.Series(df.aapl)

# s serisinin ilk 30, 75, 125 ve 250 verisini 
# rolling() metoduyla alarak std() metoduyla bunların 
# standart sapmasını hesapladık ve tek bir grafikte 
# farklı renklerle görüntüledik.
std_30 = s.rolling(30).std()
plt.plot(std_30, color='red', label='30d')

std_75 = s.rolling(75).std()
plt.plot(std_75, color='cyan', label='75d')

std_125 = s.rolling(125).std()
plt.plot(std_125, color='green', label='125d')

std_250 = s.rolling(250).std()
plt.plot(std_250, color='magenta', label='250d')

# Sol üste çizgilerin renkleri için bir gösterge ekledik.
plt.legend(loc='upper left')

plt.title('Moving standard deviations')

plt.show()
