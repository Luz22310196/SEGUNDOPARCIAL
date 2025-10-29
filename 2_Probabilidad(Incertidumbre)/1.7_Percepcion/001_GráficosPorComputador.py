import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Datos 2D
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# Datos 3D
X = np.linspace(-5, 5, 50)
Y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Crear figura
fig = plt.figure(figsize=(12,5))

# Graficar 2D
ax1 = fig.add_subplot(121)
ax1.plot(x, y, label="Seno")
ax1.set_title("Gráfico 2D")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True)

# Graficar 3D
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, Z, cmap='viridis')
ax2.set_title("Gráfico 3D")

plt.tight_layout()
plt.show()