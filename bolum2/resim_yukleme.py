import matplotlib.pyplot as plt

# plt.imread() ile dosyadaki jpg uzantılı resmimizi yükledik.
img = plt.imread('flower.jpg')
print(img.shape)
# Renkli görüntüyü plt.imshow() ile çizdirdik. 3 boyutlu bir
# dizi olarak (RGB).
plt.imshow(img)

# axis('off') ile kenarlardaki eksen görünümünü kaldırdık.
plt.axis('off')
plt.show()
