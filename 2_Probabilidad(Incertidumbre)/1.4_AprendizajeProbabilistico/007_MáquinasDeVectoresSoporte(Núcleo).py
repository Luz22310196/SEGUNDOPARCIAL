import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Datos 2D
X = np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])
y = np.array([0,0,0,1,1,1])

# SVM con núcleo RBF
clf = svm.SVC(kernel='rbf', C=1.0, gamma='scale')
clf.fit(X, y)

# Predicción de un punto nuevo
x_new = np.array([[5,5]])
print("Clase predicha:", clf.predict(x_new))

# Crear malla para visualización
xx, yy = np.meshgrid(np.linspace(0,9,200), np.linspace(0,9,200))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)

plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')  # región de decisión
plt.scatter(X[:,0], X[:,1], c=y, s=100, cmap='coolwarm')  # datos
plt.scatter(x_new[0,0], x_new[0,1], c='black', marker='*', s=200, label='Nuevo punto')  # nuevo punto
plt.title("SVM con núcleo RBF")
plt.legend()
plt.show()