import matplotlib.pyplot as plt
import pandas as pd

# index_col=‘date’, aapl[‘2007’:’2008’] ifadesini
# kullanmamızı vr indexi verisetindeki date değişkeni olarak 
# almamızı sağladı.
# parse_dates=True, her bir ayı x eksenine bir kez yazdırır.
df=pd.read_csv('stocks.csv', index_col='date',
               parse_dates=True)

# aapl hissesinin 2001-2011 arasındaki değerlerini
# mavi renk kullanarak ilk grafikte gösterdik.
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(df.aapl, color='blue')

# aapl hisselerinin 2007 ile 2008 arasındaki değerleri
# için ['2007':'2008'] ifadesini kullanarak view değişkenini oluşturduk.
view = df.aapl['2007':'2008']

# 2007 - 2008 aapl hisselerini 2. grafikte siyah renkle gösterdik.
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()
