import matplotlib.pyplot as plt

image = plt.imread('img1.jpg')

plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image)

# Histogram oluşturacağımız renkleri iki boyutlu dizi haline getirdik.
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]

# Her bir rengin 2 boyutlu dizilerini, flatten() ile 1 
# boyutlu diziler haline getirdik.
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()

# Ortak eksenler üzerinde üst üste 3 rengin histogramını çizdik.
plt.subplot(2,1,2)
plt.title('Histograms from color image')
plt.xlim((0,256))
# Her renk için bins ile 64 bölme kullandık
# alpha ile renkleri yarı saydam hale getirdik
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)

plt.show()
