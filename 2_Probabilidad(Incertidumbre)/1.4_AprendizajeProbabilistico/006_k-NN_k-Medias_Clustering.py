import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Datos 2D
X = np.array([[1,2],[1,4],[1,0],[6,5],[7,7],[8,6],[5,5],[6,6]])
y = np.array([0,0,0,1,1,1,1,1])  # etiquetas para K-NN

# K-means
k = 2
centroides = X[:k].copy()

for _ in range(10):
    etiquetas = np.argmin(np.linalg.norm(X[:, None] - centroides[None, :], axis=2), axis=1)
    for i in range(k):
        centroides[i] = X[etiquetas==i].mean(axis=0)

print("Centroides K-means:", centroides)
print("Etiquetas K-means:", etiquetas)

# K-NN
x_new = np.array([5,5])
k_nn = 3
dist = np.linalg.norm(X - x_new, axis=1)
idx = np.argsort(dist)[:k_nn]
clase_pred = Counter(y[idx]).most_common(1)[0][0]
print("Clase predicha K-NN:", clase_pred)

#  Visualización de clustering y K-NN
plt.scatter(X[:,0], X[:,1], c=etiquetas, s=100, cmap='viridis', label='Datos')
plt.scatter(centroides[:,0], centroides[:,1], c='red', marker='X', s=200, label='Centroides K-means')
plt.scatter(x_new[0], x_new[1], c='black', marker='*', s=200, label='Punto K-NN')
plt.title("K-means y K-NN")
plt.legend()
plt.show()
