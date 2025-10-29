import numpy as np

# Estados (por ejemplo, fonemas)
estados = ["A", "B"]

# Matriz de transición
P = np.array([[0.8, 0.2],
              [0.3, 0.7]])

# Matriz de observación (probabilidad de feature dado fonema)
O = np.array([[0.6, 0.4],
              [0.3, 0.7]])

# Estado inicial
pi = np.array([0.5, 0.5])

# Secuencia de observaciones (0 o 1 como feature simplificado)
obs = [0, 1, 0, 0, 1]

# Viterbi: encontrar secuencia más probable de estados
T = len(obs)
N = len(estados)
v = np.zeros((T, N))
ptr = np.zeros((T, N), dtype=int)

v[0] = pi * O[:, obs[0]]

for t in range(1, T):
    for j in range(N):
        v[t, j] = np.max(v[t-1] * P[:, j]) * O[j, obs[t]]
        ptr[t, j] = np.argmax(v[t-1] * P[:, j])

# Reconstruir secuencia de estados
estado_max = np.zeros(T, dtype=int)
estado_max[-1] = np.argmax(v[-1])
for t in reversed(range(1, T)):
    estado_max[t-1] = ptr[t, estado_max[t]]

# Mostrar secuencia de fonemas reconocidos
reconocido = [estados[i] for i in estado_max]
print("Secuencia reconocida:", reconocido)