import numpy as np

# Estados ocultos
estados = ["Lluvioso", "Soleado"]

# Observaciones
obs = [0, 1, 0, 0, 1]  # 0=Lluvia, 1=Sol

# Matriz de transición
A = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Matriz de emisión
B = np.array([[0.9, 0.1],
              [0.2, 0.8]])

# Estado inicial
pi = np.array([0.6, 0.4])

T = len(obs)
N = len(estados)

# FORWARD: filtrado
alpha = np.zeros((T, N))
alpha[0] = pi * B[:, obs[0]]
for t in range(1, T):
    alpha[t] = (alpha[t-1] @ A) * B[:, obs[t]]

# BACKWARD: suavizado
beta = np.zeros((T, N))
beta[-1] = 1
for t in reversed(range(T-1)):
    beta[t] = A @ (B[:, obs[t+1]] * beta[t+1])

# GAMMA: probabilidad suavizada
gamma = (alpha * beta)
gamma /= gamma.sum(axis=1, keepdims=True)

# VITERBI: secuencia más probable
delta = np.zeros((T, N))
ptr = np.zeros((T, N), dtype=int)
delta[0] = pi * B[:, obs[0]]

for t in range(1, T):
    for j in range(N):
        delta[t, j] = np.max(delta[t-1] * A[:, j]) * B[j, obs[t]]
        ptr[t, j] = np.argmax(delta[t-1] * A[:, j])

est_max = np.zeros(T, dtype=int)
est_max[-1] = np.argmax(delta[-1])
for t in reversed(range(1, T)):
    est_max[t-1] = ptr[t, est_max[t]]

secuencia_viterbi = [estados[i] for i in est_max]

print("Alpha (Forward):", alpha)
print("Gamma (Suavizado):", gamma)
print("Secuencia más probable (Viterbi):", secuencia_viterbi)