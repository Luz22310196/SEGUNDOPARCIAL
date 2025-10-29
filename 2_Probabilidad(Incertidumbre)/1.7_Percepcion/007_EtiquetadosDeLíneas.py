import cv2
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
img = cv2.imread('texto.jpg', cv2.IMREAD_GRAYSCALE)

# Binarizar imagen
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# Encontrar componentes conectados (líneas)
num_labels, labels_im = cv2.connectedComponents(binary)

# Crear imagen coloreada para visualización
label_hue = np.uint8(179*labels_im/np.max(labels_im))
blank_ch = 255*np.ones_like(label_hue)
labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2RGB)
labeled_img[label_hue==0] = 0

# Mostrar resultados
plt.imshow(labeled_img)
plt.title(f"Líneas etiquetadas: {num_labels-1}")
plt.axis('off')
plt.show()