import numpy as np

# Número de partículas
N = 1000

# Función de transición del estado (modelo simple)
def transicion(x):
    return x + np.random.normal(0, 0.5)  # ruido de proceso

# Función de observación
def observacion(x):
    return x + np.random.normal(0, 0.2)  # ruido de medición

# Secuencia de observaciones
z = [0.5, 1.0, 0.8, 1.2, 0.7]

# Inicializar partículas uniformes
particulas = np.random.uniform(0, 1, N)
pesos = np.ones(N) / N

for obs in z:
    # PROPAGACIÓN: mover partículas según modelo
    particulas = transicion(particulas)
    
    # PONDERACIÓN: comparar con observación
    pesos *= (1 / np.sqrt(2*np.pi*0.2**2)) * np.exp(-0.5 * ((obs - particulas)/0.2)**2)
    pesos /= np.sum(pesos)
    
    # RE-SAMPLING: generar nuevas partículas según pesos
    indices = np.random.choice(range(N), size=N, p=pesos)
    particulas = particulas[indices]
    pesos = np.ones(N) / N
    
    # Estimación del estado
    x_est = np.mean(particulas)
    print(f"Observación: {obs:.2f}, Estimación: {x_est:.2f}")