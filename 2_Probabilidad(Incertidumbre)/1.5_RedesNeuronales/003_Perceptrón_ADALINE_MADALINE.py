import numpy as np

# Datos AND
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Perceptrón
w_p = np.zeros(2)
b_p = 0
lr = 0.1

for _ in range(10):
    for xi, target in zip(X, y):
        pred = np.dot(xi, w_p) + b_p
        pred_label = 1 if pred >= 0 else 0
        error = target - pred_label
        w_p += lr * error * xi
        b_p += lr * error

print("Perceptrón: Pesos:", w_p, "Bias:", b_p)

# Adaline
w_a = np.zeros(2)
b_a = 0

for _ in range(10):
    for xi, target in zip(X, y):
        pred = np.dot(xi, w_a) + b_a
        error = target - pred
        w_a += lr * error * xi
        b_a += lr * error

print("Adaline: Pesos:", w_a, "Bias:", b_a)

# Madaline
w_m1 = np.zeros(2)
b_m1 = 0
w_m2 = np.zeros(2)
b_m2 = 0

for _ in range(10):
    for xi, target in zip(X, y):
        out1 = np.dot(xi, w_m1) + b_m1
        out2 = np.dot(xi, w_m2) + b_m2
        pred_label = 1 if (out1 >= 0 and out2 >= 0) else 0
        error1 = target - (1 if out1 >= 0 else 0)
        error2 = target - (1 if out2 >= 0 else 0)
        w_m1 += lr * error1 * xi
        b_m1 += lr * error1
        w_m2 += lr * error2 * xi
        b_m2 += lr * error2

print("Madaline Neurona1 Pesos:", w_m1, "Bias:", b_m1)
print("Madaline Neurona2 Pesos:", w_m2, "Bias:", b_m2)
