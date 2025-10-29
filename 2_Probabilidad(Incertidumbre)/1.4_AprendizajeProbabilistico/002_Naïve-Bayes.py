import numpy as np

# Datos: [altura, peso], clase: 0=bajo, 1=alto
X = np.array([[1.6, 50],
              [1.7, 65],
              [1.8, 70],
              [1.55, 48],
              [1.9, 80]])
y = np.array([0, 1, 1, 0, 1])

# Estimación de probabilidades
classes = np.unique(y)
probs = {}

for c in classes:
    X_c = X[y==c]
    mean = X_c.mean(axis=0)
    var = X_c.var(axis=0)
    prior = len(X_c)/len(X)
    probs[c] = {"mean": mean, "var": var, "prior": prior}

# Función de densidad gaussiana
def gaussian(x, mean, var):
    return (1/np.sqrt(2*np.pi*var)) * np.exp(-(x-mean)**2/(2*var))

# Clasificación de un nuevo dato
x_new = np.array([1.65, 55])
post = []

for c in classes:
    likelihood = np.prod(gaussian(x_new, probs[c]["mean"], probs[c]["var"]))
    posterior = likelihood * probs[c]["prior"]
    post.append(posterior)

clase_pred = classes[np.argmax(post)]
print("Clase predicha:", clase_pred)