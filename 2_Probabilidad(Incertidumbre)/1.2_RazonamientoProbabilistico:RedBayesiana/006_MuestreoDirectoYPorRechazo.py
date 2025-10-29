import numpy as np

# Distribución simple de X
valores = [0, 1]          # posibles valores
probabilidades = [0.7, 0.3]  # P(X=0)=0.7, P(X=1)=0.3

# Muestreo directo
muestras_directas = np.random.choice(valores, size=10, p=probabilidades)
print("Muestras directas:", muestras_directas)

# Muestreo por rechazo
def muestreo_rechazo(n):
    muestras = []
    while len(muestras) < n:
        x = np.random.choice(valores)    # candidato uniforme
        u = np.random.rand()             # número aleatorio
        if u < probabilidades[x]:        # aceptación
            muestras.append(x)
    return muestras

muestras_rechazo = muestreo_rechazo(10)
print("Muestras por rechazo:", muestras_rechazo)
