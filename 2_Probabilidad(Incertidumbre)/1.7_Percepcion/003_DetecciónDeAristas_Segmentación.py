import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('ejemplo.jpg', cv2.IMREAD_GRAYSCALE)

# Detección de aristas con Canny
edges = cv2.Canny(img, 100, 200)

# Segmentación simple con umbral
_, segmented = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Mostrar resultados
plt.figure(figsize=(12,5))
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Imagen original")
plt.axis('off')

plt.subplot(1,3,2)
plt.imshow(edges, cmap='gray')
plt.title("Detección de aristas")
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(segmented, cmap='gray')
plt.title("Segmentación")
plt.axis('off')

plt.show()