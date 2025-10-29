import numpy as np
import matplotlib.pyplot as plt

# Datos linealmente separables
X = np.array([[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]])
y = np.array([0,0,0,1,1,1])

# Graficar datos
plt.scatter(X[y==0][:,0], X[y==0][:,1], color='blue', label='Clase 0')
plt.scatter(X[y==1][:,0], X[y==1][:,1], color='red', label='Clase 1')

# Línea de separación aproximada
x_vals = np.linspace(0,9,100)
y_vals = 0.8 * x_vals - 0.5  # línea que separa clases
plt.plot(x_vals, y_vals, 'k--', label='Separador lineal')

plt.title("Ejemplo de Separabilidad Lineal")
plt.xlabel("X1")
plt.ylabel("X2")
plt.legend()
plt.grid(True)
plt.show()
