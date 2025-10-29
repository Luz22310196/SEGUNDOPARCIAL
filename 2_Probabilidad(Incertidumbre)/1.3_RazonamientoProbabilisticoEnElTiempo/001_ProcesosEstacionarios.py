import numpy as np

# Matriz de transición de Markov
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Distribución inicial
pi = np.array([1.0, 0.0])  # empezamos en estado 0

# Iteramos para acercarnos a la distribución estacionaria
for _ in range(50):
    pi = pi @ P  # actualización de distribución

print("Distribución estacionaria:", np.round(pi,4))