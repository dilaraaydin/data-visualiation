import matplotlib.pyplot as plt

img = plt.imread('nature.jpg')
image = img.sum(2)

plt.subplot(2,1,1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')

# flatten() ile resmi 1 boyutta düzleştirdik
pixels = image.flatten()

# Önce olasılık dağılımlı kırmızı alanı çizdik.
plt.subplot(2,1,2)
pdf = plt.hist(pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)

# ızgara görünümü için.
plt.grid('off')

# twinx(), x ekseni aynı, y ekseni farklı olan
# iki grafiğin üst üste bindirilmesine izin verir.
plt.twinx()

# sonra kümülatif(birikimli) dağılımlı alanı mavi ile çizdik.
cdf = plt.hist(pixels, bins=64, range=(0,256),
               normed=True, cumulative=True,
               color='blue', alpha=0.4)

# x ekseni değerleri için.
plt.xlim((0,256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()
