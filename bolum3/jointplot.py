import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('auto-mpg.csv')

# Dağılımları grafiğin üst ve sağ kenarında
# göstermek için jointplot() kullandık.
# kind parametresi ile grafik veri dağılımının
# altıgen şekillerle oluşmasını sağladık.
sns.jointplot(x='horsepower',y='mpg', 
              data=auto, kind='hex')

plt.show()
