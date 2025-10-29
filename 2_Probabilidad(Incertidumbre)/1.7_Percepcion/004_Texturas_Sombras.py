import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import greycomatrix, greycoprops

# Cargar imagen en escala de grises
img = cv2.imread('ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Detección de aristas
edges = cv2.Canny(img, 100, 200)

# Segmentación simple por umbral
_, segmented = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Extraer texturas usando matriz de co-ocurrencia
glcm = greycomatrix(img, distances=[1], angles=[0], levels=256, symmetric=True, normed=True)
contrast = greycoprops(glcm, 'contrast')[0,0]

# Simulación de sombra (simple): suavizado para efecto de profundidad
shadow = cv2.GaussianBlur(img, (15,15), 0)

# Mostrar resultados
plt.figure(figsize=(15,5))
plt.subplot(1,4,1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1,4,2)
plt.imshow(edges, cmap='gray')
plt.title("Aristas")
plt.axis('off')

plt.subplot(1,4,3)
plt.imshow(segmented, cmap='gray')
plt.title("Segmentación")
plt.axis('off')

plt.subplot(1,4,4)
plt.imshow(shadow, cmap='gray')
plt.title(f"Sombras y Texturas\nContrast={contrast:.2f}")
plt.axis('off')

plt.show()