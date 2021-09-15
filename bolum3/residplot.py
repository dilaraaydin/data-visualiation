import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pandas'ın read_csv komutuyla auto-mpg.csv verisetini ekledik.
auto = pd.read_csv('auto-mpg.csv')

# beygir gücünün gidilen mil sayısıyla arasındaki
# regresyonun kalıntı grafiğini oluşturmak için
# residplot() kullandık ve x eksenine horsepower, 
# y eksenine de mpg kolonunu verdik. 
# color ile bu verilerin yeşil renkte görünmesini sağladık.
sns.residplot(x='horsepower', y='mpg', data=auto, 
              color='green')

plt.show()

