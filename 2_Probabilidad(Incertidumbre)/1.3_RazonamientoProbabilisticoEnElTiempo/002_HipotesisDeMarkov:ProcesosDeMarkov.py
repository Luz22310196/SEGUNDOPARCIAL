import numpy as np

# Matriz de transición
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Estado inicial
estado = np.array([1, 0])

# Número de pasos
pasos = 10

for i in range(pasos):
    print(f"Paso {i}: {estado}")  # Mostrar estado
    estado = np.dot(estado, P)    # Calcular siguiente estado
