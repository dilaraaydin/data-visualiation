import matplotlib.pyplot as plt
import pandas as pd

# index_col=‘date’, aapl[‘2007’:’2008’] ifadesini
# kullanmamızı vr indexi verisetindeki date değişkeni olarak 
# almamızı sağladı.
# parse_dates=True, her bir ayı x eksenine bir kez yazdırır.
df=pd.read_csv('stocks.csv', index_col='date',
               parse_dates=True)

# aapl hisselerinin 2007 Kasım ayı ile 2008 Nisan ayı arasındaki değerleri
# için ['2007-11':'2008-04'] ifadesini kullanarak view_1 değişkenini oluşturduk.
view_1 = df.aapl['2007-11':'2008-04']

# ilk grafikte view_1 değişkeninin değerlerini kırmızı ile çizdik.
plt.subplot(2,1,1)
plt.plot(view_1, color='red')
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.xticks(rotation=45)

# aapl hisselerinin 2008 Ocak ay değerlerini görüntülemek için view_2
# değişkenini oluşturduk.
view_2 = df.aapl['2008-01']

# 2. grafikte view_2 değişkeninin değerlerini yeşil renkte gösterdik.
plt.subplot(2,1,2)
plt.plot(view_2, color='green')
plt.title('AAPL: Jan. 2008')
plt.xticks(rotation=45)

# tight_layout ile grafik değerlerinin görüntü olarak çakışmasını önledik.
plt.tight_layout()
plt.show()
