import matplotlib.pyplot as plt

image = plt.imread('flower.jpg')
intensity = image.sum(2)
plt.imshow(intensity, cmap='gray')

# Pixel yoğunluklarını bulduk.
pmin, pmax = intensity.min(), intensity.max()
print("En küçük ve en büyük piksel yoğunlukları %d ve %d 'dir." % (pmin, pmax))

# Görüntüden minimum ve maksimum değerleri çıkardık: pmin, pmax.
rescaled_image = 256*(intensity - pmin) / (pmax - pmin)
print("Yeniden ölçeklenen en küçük ve en büyük piksel yoğunlukları %.1f ve %.1f 'dir." % 
      (rescaled_image.min(), rescaled_image.max()))

plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)
plt.show()
