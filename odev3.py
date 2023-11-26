import cv2
import numpy as np

def count_rice(image):
    rice_count = 0

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) 

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 100:
            rice_count += 1

    return rice_count

def apply_threshold(image, threshold):
    # Görüntüyü gri tonlamaya çevir
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Eşikleme ile daha net bir görüntü elde et
    _, thresholded_image = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    return thresholded_image

file_path = 'image.jpeg'
threshold_value = 200

image = cv2.imread(file_path)

# Eşiklenmiş görüntüyü alma
thresholded_image = apply_threshold(image, threshold_value)

# Pirinç sayısını alma
total_rice_count = count_rice(thresholded_image)

# Sonuç görüntüsü oluşturma
result_image = image.copy()
cv2.putText(result_image, f'Rice Count: {total_rice_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Eşiklenmiş görüntüyü ve sonucu gösterme
cv2.imshow('Thresholded Image', thresholded_image)
cv2.imshow('Result Image', result_image)

# Görüntüyü kaydetme
cv2.imwrite("yedek.jpg", result_image)

# Konsolda sonucu yazdırma
print(f'Total Rice Count: {total_rice_count}')

# Bekleme tuşuna basılmasını bekleme
cv2.waitKey(0)

# Tüm pencereleri kapatma
cv2.destroyAllWindows()
