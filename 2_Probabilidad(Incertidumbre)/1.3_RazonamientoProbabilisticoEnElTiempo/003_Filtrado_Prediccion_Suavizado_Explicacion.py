import numpy as np

# Matriz de transición de estados
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Matriz de observación (probabilidad de observar dado estado)
O = np.array([[0.9, 0.1],
              [0.2, 0.8]])

# Estado inicial
estado = np.array([1, 0])

# Secuencia de observaciones (0 o 1)
observaciones = [0, 0, 1, 0, 1]

# Listas para guardar resultados
filtrado = []
prediccion = []
suavizado = []

# FILTRADO: estimar estado actual dado observaciones hasta ahora
for obs in observaciones:
    # Probabilidad del estado dado la observación
    estado = estado * O[:, obs]
    estado = estado / np.sum(estado)  # Normalizar
    filtrado.append(estado.copy())
    # PREDICCION: siguiente estado usando matriz de transición
    predic = np.dot(estado, P)
    prediccion.append(predic.copy())

# SUAVIZADO: estimar estados pasados usando toda la secuencia
T = len(observaciones)
suav = filtrado.copy()
for t in reversed(range(T-1)):
    suav[t] = filtrado[t] * np.dot(P, suav[t+1])
    suav[t] = suav[t] / np.sum(suav[t])  # Normalizar
    suavizado.append(suav[t].copy())

print("Filtrado:", filtrado)
print("Predicción:", prediccion)
print("Suavizado:", list(reversed(suavizado)))