# seaborn kütüphanesini import ederek
# istatistiksel veri görselleştimesi yaptık, 
# seaborn, pandas'ın dataframe'i ile 
# iyi çalıştığından pandas'ı da ekledik. 
# Aynı zaman da seaborn ile matplotlib'i birlikte
# kullanacğız.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn kütüphanesinde bulunan hazır veri seti olan tips
# verisetinin load_dataset ile ekledik.
tips = sns.load_dataset('tips')

# lmplot ile grafiğin x ve y eksenlerini belirttik.
sns.lmplot(x='total_bill', 
           y='tip', 
           data=tips,
           # hue='sex',
           # palette='Set1',
           # col='sex',
           row='sex'
           )

plt.show()