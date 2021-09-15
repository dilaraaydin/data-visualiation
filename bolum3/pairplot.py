import matplotlib.pyplot as plt
import seaborn as sns

# seaborn da hazır bulunan 'tips' veri
# setini ekledik.
tips = sns.load_dataset('tips')

# Konsolda ilk 5 veriyi yazdırdık
print(tips.head())

# hue ile cinsiyet(sex) verisinin diğer verilerle
# oluşturduğu grafikleri görüntüledik.
# kind ile regresyon grafiği olmasını sağladık.
sns.pairplot(data=tips, 
            hue='sex', kind='reg')

plt.show()
