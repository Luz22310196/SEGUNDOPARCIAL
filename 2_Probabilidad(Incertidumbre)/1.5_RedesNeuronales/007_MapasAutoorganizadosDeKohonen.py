import numpy as np
from minisom import MiniSom
import matplotlib.pyplot as plt

# Datos aleatorios 3D
np.random.seed(0)
data = np.random.rand(100, 3)

# Crear SOM 5x5
som = MiniSom(5, 5, 3, sigma=1.0, learning_rate=0.5)
som.random_weights_init(data)
som.train_random(data, 500)

# Visualizar mapa de distancias (U-Matrix)
plt.figure(figsize=(6,6))
plt.pcolor(som.distance_map().T, cmap='coolwarm') 
plt.colorbar()
plt.title("Mapa Autoorganizado de Kohonen (U-Matrix)")
plt.show()