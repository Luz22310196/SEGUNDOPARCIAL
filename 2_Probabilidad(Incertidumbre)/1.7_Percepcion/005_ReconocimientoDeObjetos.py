import cv2
import matplotlib.pyplot as plt

# Cargar imagen
img = cv2.imread('personas.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cargar clasificador Haar para rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detectar objetos (rostros)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Dibujar bounding boxes
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar resultados
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title(f"Objetos detectados: {len(faces)}")
plt.axis('off')
plt.show()