import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# pandas'ın read_csv komutuyla auto-mpg.csv
 # verisetini ekledik.
auto = pd.read_csv('auto-mpg.csv')

plt.scatter(auto['weight'], auto['mpg'], 
            label='data', color='red', 
            marker='o')

# sns.regplot() kullanarak gidilen mil ve 
# ağırlık arasında ikinci 
# dereceden regresyon çizdirdik.
# Dağılım çizim noktalarının yeniden
# çizilmesini önlemek için scatter=None dedik.
sns.regplot(x='weight', y='mpg', 
        data=auto, scatter=None, 
        color='blue', label='First Order')

sns.regplot(x='weight', y='mpg', 
            data=auto, scatter=None, 
            order=2, color='green', 
            label='Second Order')

# Sağ üste bir gösterge ekledik.
plt.legend(loc='upper right')
plt.show()