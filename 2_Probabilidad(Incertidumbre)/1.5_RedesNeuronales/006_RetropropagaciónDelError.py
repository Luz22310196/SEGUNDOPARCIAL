import numpy as np

# Datos XOR
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

# Funciones de activación
def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_deriv(x):
    return x*(1-x)

# Inicializar pesos y biases
np.random.seed(0)
w0 = np.random.rand(2,4)
b0 = np.zeros((1,4))
w1 = np.random.rand(4,1)
b1 = np.zeros((1,1))
lr = 0.1

# Entrenamiento Backpropagation
for _ in range(10000):
    # Forward
    h = sigmoid(np.dot(X, w0) + b0)
    out = sigmoid(np.dot(h, w1) + b1)
    
    # Error salida
    error_out = y - out
    delta_out = error_out * sigmoid_deriv(out)
    
    # Error capa oculta
    error_h = delta_out.dot(w1.T)
    delta_h = error_h * sigmoid_deriv(h)
    
    # Actualizar pesos y bias
    w1 += h.T.dot(delta_out) * lr
    b1 += np.sum(delta_out, axis=0, keepdims=True) * lr
    w0 += X.T.dot(delta_h) * lr
    b0 += np.sum(delta_h, axis=0, keepdims=True) * lr

# Predicciones finales
pred = np.round(out).astype(int)
print("Predicciones XOR:", pred)