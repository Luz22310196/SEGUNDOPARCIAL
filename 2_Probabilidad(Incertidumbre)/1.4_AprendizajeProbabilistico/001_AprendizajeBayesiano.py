import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Datos observados: 1 = éxito, 0 = fracaso
datos = [1, 0, 1, 1, 0, 1]

# Priori Beta(a, b)
a, b = 2, 2  # creencia inicial (suave)

# Actualizar posterior
a_post = a + sum(datos)
b_post = b + len(datos) - sum(datos)

# Distribución posterior
theta = np.linspace(0, 1, 100)
posterior = beta.pdf(theta, a_post, b_post)

# Mostrar resultado
plt.plot(theta, posterior)
plt.title("Distribución posterior de la probabilidad de éxito")
plt.xlabel("θ")
plt.ylabel("Densidad")
plt.show()

print(f"Posterior Beta({a_post}, {b_post})")