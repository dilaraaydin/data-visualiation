import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Rastgele olarak 4x3 grafik oluşturduk ve
# bu bölmelere rastgele renkler vermiş olduk.
covariance = np.random.rand(3, 4)

# Konsolda yazdırdık.
print(covariance)

# Rastgele oluşturduğumuz grafikte heatmap()
# ile bir renk haritası oluşturduk.
sns.heatmap(covariance)

plt.show()
