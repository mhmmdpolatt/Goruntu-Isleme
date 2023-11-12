import cv2
import matplotlib.pyplot as plt

# Örnek olarak bir gri tonlu resmi temsil eden bir matris
resim = cv2.imread("image.jpg", 0)

# Histogramı saklamak için boş bir sözlük oluştur
histogram = {}

# Her pikselin histogramını hesapla
for satir in resim:
    for piksel in satir:
        if piksel in histogram:
            histogram[piksel] += 1
        else:
            histogram[piksel] = 1

# Histogramı ekrana yazdır
for renk_degeri, frekans in histogram.items():
    print(f"{renk_degeri}: {frekans}")

# Histogram verilerini ayrıştır
renk_degerleri = list(histogram.keys())
frekanslar = list(histogram.values())

# Histogramı görselleştir
plt.bar(renk_degerleri, frekanslar, color='blue')
plt.xlabel('Renk Değeri')
plt.ylabel('Frekans')
plt.title('Histogram Görselleştirmesi')
plt.show()