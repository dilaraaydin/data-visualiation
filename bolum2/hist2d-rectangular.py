import matplotlib.pyplot as plt
import pandas as pd

# pandas ile auto-mpg.csv veri setini ekledik.
dfCar=pd.read_csv('auto-mpg.csv')

# arabaların beygir gücü ve gittiği mil sayısını eksen
# olarak verdik ve bins ile bölme sayısını, range ile de
# eksenlerin değer aralıklarını verdik.
plt.hist2d(dfCar.horsepower, dfCar.mpg,bins=(20,20),
           range=((40,235), (8, 48)))

# Grafiğin yanına bir colorbar ekledik.
plt.colorbar()
plt.xlabel('Beygir Gücü')
plt.ylabel('1 Galon Başına Gidilen Mil')
plt.title('hist2d()')
plt.show()
