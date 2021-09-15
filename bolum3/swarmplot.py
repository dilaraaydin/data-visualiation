import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('auto-mpg.csv')

# Varsayılan olarak gelen orient özelliği dikey
# olduğunda ilk grafik dikey oluştu.
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='horsepower', 
              data=auto)

# orient özelliğini horizental(yatay)(h) verdiğimizde
# 2. grafiğin yatay oluştuğunu görürüz.
plt.subplot(2,1,2)
sns.swarmplot(x='horsepower', y='cyl', 
              data=auto, orient='h', 
              hue='origin')
plt.show()
