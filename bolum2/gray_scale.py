import matplotlib.pyplot as plt

img = plt.imread('flower.jpg')
print(img.shape)
intensity = img.sum(2)
print(intensity.shape)
# Renklerdeki toplam yoğunluğu hesaplayıp,
# sonucu plt.imshow() ’da gri renk haritasıyla görüntüledik.
plt.imshow(intensity, cmap='gray')

plt.colorbar()
plt.axis('off')
plt.show()
