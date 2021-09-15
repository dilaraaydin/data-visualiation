import matplotlib.pyplot as plt

img = plt.imread('nature.jpg')
image = img.sum(2)

plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

# flatten() ile resmi 1 boyutta düzleştirdik
pixels = image.flatten()

plt.subplot(2,1,2)
plt.xlim((0,255))
plt.title('Normalized histogram')

# mutlak yerine olasılık dağılımı almak için normed=True yazılır.
# bins=64 ile frekansa göre sayısal veriler gruplara bölünür.
# range ile bölmelerin alt ve üst aralığı girilir.
plt.hist(pixels, bins=64, range=(0,256), 
         normed=True, color='red', alpha=0.4)

plt.show()
