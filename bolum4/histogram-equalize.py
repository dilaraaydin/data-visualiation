import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('nature.jpg')
image = img.sum(2)

# flatten() ile resmi 1 boyutta düzleştirdik
pixels = image.flatten()

# plt.hist() ile orijinal resmin CDF’sini hesapladık
cdf, bins, patches = plt.hist(pixels, bins=256, 
                range=(0,256), normed=True, 
                cumulative=True)
# Yeni piksel değerlerini interp() komutu ile enterpolasyon 
# yapan new_pixels’i oluşturduk. 
new_pixels = np.interp(pixels, bins[:-1], cdf*256)

# Resmin yeni pixellerle oluşmuş halini görüntüledik.
new_image = new_pixels.reshape(image.shape)
plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

# İlk histogram ile kırmızı renkte PDF değerlerini,
# 2. histogramda ise mavi renkte CDF değerlerini 
# new_pixels kullanarak görüntüledik. 
plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, 
               range=(0,256), normed=False, 
               color='red', alpha=0.4)
plt.grid('off')
plt.twinx()
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (equalized image)')
cdf = plt.hist(new_pixels, bins=64, 
               range=(0,256), cumulative=True, 
               normed=True, color='blue', alpha=0.4)
plt.show()
