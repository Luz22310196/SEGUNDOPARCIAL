import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,200)

# Funciones de activación
sigmoid = 1 / (1 + np.exp(-x))
tanh = np.tanh(x)
relu = np.maximum(0, x)
leaky_relu = np.where(x>0, x, 0.01*x)
softmax = np.exp(x)/np.sum(np.exp(x))  # simple softmax de un vector

# Graficar
plt.figure(figsize=(10,6))
plt.plot(x, sigmoid, label='Sigmoid')
plt.plot(x, tanh, label='Tanh')
plt.plot(x, relu, label='ReLU')
plt.plot(x, leaky_relu, label='Leaky ReLU')
plt.title("Funciones de Activación")
plt.legend()
plt.grid(True)
plt.show()