import numpy as np

# Estados: 0=Sano, 1=Enfermo
P_trans = {0:[0.8,0.2], 1:[0.3,0.7]}  # matriz de transición
estado_inicial = 0                     # comenzamos sano
n_pasos = 10                            # número de pasos a simular
n_cadenas = 1000                        # número de cadenas Monte Carlo

# Guardamos resultados
resultados = np.zeros((n_cadenas, n_pasos))

for i in range(n_cadenas):
    estado = estado_inicial
    for t in range(n_pasos):
        resultados[i,t] = estado
        # muestreo del siguiente estado según la transición
        estado = np.random.choice([0,1], p=P_trans[estado])

# Probabilidades estimadas de estar enfermo en cada paso
prob_enfermo = np.mean(resultados, axis=0)
print("Probabilidad de enfermo por paso:", np.round(prob_enfermo,4))
