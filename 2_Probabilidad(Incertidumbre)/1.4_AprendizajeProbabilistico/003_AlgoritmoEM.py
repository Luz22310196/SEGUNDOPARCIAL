import numpy as np
from scipy.stats import norm

# Datos observados
X = np.array([1.0, 1.2, 0.8, 3.0, 3.2, 2.8])

# Inicializar parámetros
mu = np.array([0.5, 3.5])   # medias
sigma = np.array([1.0, 1.0]) # desviaciones
pi = np.array([0.5, 0.5])    # pesos

for iter in range(10):
    # E-step: calcular responsabilidades
    gamma = np.zeros((len(X), 2))
    for k in range(2):
        gamma[:, k] = pi[k] * norm.pdf(X, mu[k], sigma[k])
    gamma /= gamma.sum(axis=1, keepdims=True)

    # M-step: actualizar parámetros
    N_k = gamma.sum(axis=0)
    mu = (gamma.T @ X) / N_k
    sigma = np.sqrt((gamma.T @ (X[:, None] - mu)**2) / N_k)
    pi = N_k / len(X)

    print(f"Iter {iter}: mu={mu}, sigma={sigma}, pi={pi}")