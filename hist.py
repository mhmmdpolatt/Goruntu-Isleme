import cv2
import matplotlib.pyplot as plt

resim = cv2.imread("image.jpg")

B = resim[:,:,0]
G = resim[:,:,1]
R = resim[:,:,2]

resim = 0.2989 * R + 0.5870 * G + 0.1140 * B



histogram = {}


for satir in resim:
    for piksel in satir:
        piksel = int(piksel)
        if piksel in histogram:
            
            histogram[piksel] += 1
        else:
            histogram[piksel] = 1


for renk_degeri, frekans in histogram.items():
    print(f"{renk_degeri}: {frekans}")


renk_degerleri = list(histogram.keys())
frekanslar = list(histogram.values())

plt.bar(renk_degerleri, frekanslar, color='blue')
plt.xlabel('Renk Değeri')
plt.ylabel('Frekans')
plt.title('Histogram Görselleştirmesi')
plt.show()