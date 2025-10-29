import numpy as np

# Datos 2D
X = np.array([[1,2],[1,4],[1,0],
              [10,2],[10,4],[10,0]])

k = 2  # número de clusters

# Inicializar centroides (primeros k puntos)
centroides = X[:k].copy()

for iter in range(10):
    # Asignación: distancia al centroide más cercano
    etiquetas = np.argmin(np.linalg.norm(X[:, None] - centroides[None, :], axis=2), axis=1)
    
    # Actualización: media de los puntos asignados
    for i in range(k):
        centroides[i] = X[etiquetas==i].mean(axis=0)

print("Centroides finales:", centroides)
print("Etiquetas:", etiquetas)