import matplotlib.pyplot as plt
import pandas as pd

# index_col=‘date’, aapl[‘2007’:’2008’] ifadesini
# kullanmamızı vr indexi verisetindeki date değişkeni olarak 
# almamızı sağladı.
# parse_dates=True, her bir ayı x eksenine bir kez yazdırır.
df=pd.read_csv('stocks.csv', index_col='date',
               parse_dates=True)

# aapl hisselerinin 2007 Kasım ayı ile 2008 Nisan ayı arasındaki değerleri
# için ['2007-11':'2008-04'] ifadesini kullanarak view değişkenini oluşturduk.
view = df.aapl['2007-11':'2008-04']

plt.plot(df.aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

# axes() ile kırmızı çizgili grafiğin, mavi çizgili grafik içindeki 
# konumunu belirttik.
plt.axes([0.25,0.5,0.35,0.35])

plt.plot(view,color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')

plt.tight_layout()
plt.show()
