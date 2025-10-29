import numpy as np

# Probabilidades iniciales
P_enfermo = 0.01  # probabilidad de estar enfermo
P_sintoma_dado_enfermo = 0.9  # probabilidad de síntoma si enfermo
P_sintoma_dado_sano = 0.05  # probabilidad de síntoma si sano

# Teorema de Bayes
P_enfermo_dado_sintoma = (P_sintoma_dado_enfermo * P_enfermo) / \
                         (P_sintoma_dado_enfermo * P_enfermo + P_sintoma_dado_sano * (1-P_enfermo))

print(f"Probabilidad de estar enfermo dado el síntoma: {P_enfermo_dado_sintoma:.4f}")