import matplotlib.pyplot as plt
import pandas as pd

dfCar=pd.read_csv('auto-mpg.csv')

# Altıgenler ile 2 boyutlu bir histogram grafiği oluşturmak 
# için hexbin() kullandık. x ekseni beygir gücünü, y ekseni
# gidilen mil'i verir. gridsize ile eksenlerin alacağı altıgen
# sayısı, extent ile eksen değer aralıkları verildi.
plt.hexbin(dfCar.horsepower, dfCar.mpg, gridsize=(15,12), 
           extent=(40,235,8,48))

plt.colorbar()
plt.xlabel('Beygir Gücü')
plt.ylabel('1 Galon başına gidilen mil')
plt.title('hexbin()')
plt.show()
