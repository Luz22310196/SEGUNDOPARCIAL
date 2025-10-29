# Probabilidades
P_enfermo = 0.01                 # P(Enfermo)
P_sintoma_dado_enfermo = 0.9     # P(Sintoma|Enfermo)
P_sintoma_dado_sano = 0.05       # P(Sintoma|Sano)

# Inferencia por enumeración
P_sintoma = P_sintoma_dado_enfermo*P_enfermo + P_sintoma_dado_sano*(1-P_enfermo)
P_enfermo_dado_sintoma = (P_sintoma_dado_enfermo*P_enfermo) / P_sintoma

print("P(Enfermo|Sintoma):", round(P_enfermo_dado_sintoma,4))
