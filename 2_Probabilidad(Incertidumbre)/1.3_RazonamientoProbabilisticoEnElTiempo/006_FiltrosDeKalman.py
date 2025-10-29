import numpy as np

# Parámetros del sistema
A = 1          # Matriz de transición (estado)
B = 0          # Control (sin control)
H = 1          # Medición
Q = 0.01       # Varianza del proceso
R = 0.1        # Varianza de la medición

# Estado inicial
x = 0          # Estimación inicial
P = 1          # Varianza inicial

# Secuencia de mediciones (ejemplo)
z = [0.39, 0.50, 0.48, 0.29, 0.25]

for measurement in z:
    # Predicción
    x_pred = A * x
    P_pred = A * P * A + Q

    # Actualización (corrección)
    K = P_pred * H / (H * P_pred * H + R)  # Ganancia de Kalman
    x = x_pred + K * (measurement - H * x_pred)
    P = (1 - K * H) * P_pred

    print(f"Medición: {measurement:.2f}, Estimación: {x:.2f}")