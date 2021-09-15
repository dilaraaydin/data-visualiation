import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

auto = pd.read_csv('auto-mpg.csv')

plt.subplot(2,1,1)
sns.stripplot(x='cyl', y='horsepower', 
              data=auto)
# İlk grafikten farklı olarak, veri noktalarının
# görünümünü iyileştirmek için size ve jitter
# parametrelerini kullandık.
plt.subplot(2,1,2)
sns.stripplot(x='cyl', y='horsepower', 
             data=auto, size=3, jitter=True)

plt.show()
