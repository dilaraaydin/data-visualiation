import matplotlib.pyplot as plt

image = plt.imread('img1.jpg')

# Histogram oluşturacağımız renkleri iki boyutlu dizi haline getirdik.
red, green, blue = image[:,:,0], image[:,:,1], image[:,:,2]

# Her bir rengin 2 boyutlu dizilerini, flatten() ile 1 
# boyutlu diziler haline getirdik.
red_pixels = red.flatten()
green_pixels = green.flatten()
blue_pixels = blue.flatten()

# hist2d() ile kırmızı ve yeşil piksellerin 2 boyutlu histogramını oluşturduk.
# bins(32,32) ile 32 ye 32 şeklinde bölmeler oluşmasını sağladık.
plt.subplot(2,2,1)
plt.grid('off') 
plt.xticks(rotation=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels,green_pixels,bins=(32,32))

# Yeşil ve mavi piksellerin 2 boyutlu histogramını oluşturduk.
plt.subplot(2,2,2)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels,blue_pixels, bins=(32,32))

# Mavi ve kırmızı piksellerin 2 boyutlu histogramını oluşturduk.
plt.subplot(2,2,3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.hist2d(blue_pixels,red_pixels,bins=(32,32))

plt.tight_layout()
plt.show()
