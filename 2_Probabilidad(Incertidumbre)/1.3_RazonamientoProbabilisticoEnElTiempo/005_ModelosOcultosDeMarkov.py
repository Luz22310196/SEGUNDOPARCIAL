import numpy as np

# Matriz de transición de estados ocultos
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Matriz de observación (probabilidad de ver 0 o 1 dado estado)
O = np.array([[0.9, 0.1],
              [0.2, 0.8]])

# Estado inicial
pi = np.array([0.6, 0.4])

# Secuencia de observaciones
obs = [0, 0, 1, 0, 1]

T = len(obs)
N = P.shape[0]

# FORWARD (filtrado)
alpha = np.zeros((T, N))
alpha[0] = pi * O[:, obs[0]]
for t in range(1, T):
    alpha[t] = (alpha[t-1] @ P) * O[:, obs[t]]

# BACKWARD (suavizado)
beta = np.zeros((T, N))
beta[-1] = 1
for t in reversed(range(T-1)):
    beta[t] = P @ (O[:, obs[t+1]] * beta[t+1])

# SUAVIZADO (estado oculto estimado)
gamma = (alpha * beta)
gamma = gamma / gamma.sum(axis=1, keepdims=True)

# PREDICCIÓN: siguiente estado
prediccion = alpha[-1] @ P

print("Filtrado (alpha):", alpha)
print("Suavizado (gamma):", gamma)
print("Predicción del siguiente estado:", prediccion)