import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('auto-mpg.csv')

# Burada beygir gücünün (horsepower) silindir
# sayısına (cyl) göre dağılım grafiğini
# violinplot() kullanarak oluşturduk.
plt.subplot(2,1,1)
sns.violinplot(x='cyl', y='horsepower', 
               data=auto)

plt.subplot(2,1,2)
sns.violinplot(x='cyl', y='horsepower', 
               data=auto, color='lightgray', 
               inner=None)

sns.stripplot(x='cyl', y='horsepower', 
              data=auto, jitter=True, 
              size=1.5)

plt.show()
