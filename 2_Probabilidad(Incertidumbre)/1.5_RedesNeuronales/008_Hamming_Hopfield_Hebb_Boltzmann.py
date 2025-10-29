import numpy as np
from sklearn.neural_network import BernoulliRBM

# Hamming
a = np.array([1,0,1,1])
b = np.array([1,1,0,1])
hamming_distance = np.sum(a != b)
print("Distancia de Hamming:", hamming_distance)

# Hopfield y Hebb
patterns = np.array([[1, -1, 1, -1],
                     [-1, 1, -1, 1]])
n = patterns.shape[1]

# Inicializar pesos Hopfield con regla de Hebb
W = np.zeros((n, n))
for p in patterns:
    W += np.outer(p, p)
np.fill_diagonal(W, 0)

# Estado inicial
state = np.array([1,1,-1,-1])

# Actualización asincrónica
for _ in range(5):
    for i in range(n):
        state[i] = 1 if np.dot(W[i], state) >= 0 else -1

print("Estado final Hopfield:", state)

# Red Boltzmann
X = np.random.randint(0,2,(6,4))  # datos binarios
rbm = BernoulliRBM(n_components=2, learning_rate=0.1, n_iter=500)
rbm.fit(X)
print("Componentes RBM:\n", rbm.components_)