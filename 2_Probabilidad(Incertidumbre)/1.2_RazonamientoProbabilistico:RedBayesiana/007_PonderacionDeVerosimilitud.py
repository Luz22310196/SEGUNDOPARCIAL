import numpy as np

# Distribución simple de variables
# X -> Y
P_X = [0.6, 0.4]           # P(X=0)=0.6, P(X=1)=0.4
P_Y_dado_X = [[0.7, 0.3],  # P(Y=0|X=0), P(Y=1|X=0)
               [0.2, 0.8]]  # P(Y=0|X=1), P(Y=1|X=1)

# Evidencia: Y=1
evidencia = 1
N = 1000  # número de muestras

# Ponderación de verosimilitud
pesos = []
muestras_X = []
for _ in range(N):
    # muestreo de X
    x = np.random.choice([0,1], p=P_X)
    # peso según evidencia
    peso = P_Y_dado_X[x][evidencia]
    muestras_X.append(x)
    pesos.append(peso)

# Estimación P(X=1|Y=1)
muestras_X = np.array(muestras_X)
pesos = np.array(pesos)
resultado = np.sum(pesos[muestras_X==1]) / np.sum(pesos)

print("P(X=1|Y=1) estimada:", round(resultado,4))
