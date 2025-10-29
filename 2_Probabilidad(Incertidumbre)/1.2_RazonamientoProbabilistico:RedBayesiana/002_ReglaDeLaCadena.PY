# Probabilidades simples
P_A = 0.3        # P(A)
P_B_dado_A = 0.6 # P(B|A)
P_C_dado_AB = 0.5 # P(C|A,B)

# Regla de la cadena: P(A,B,C) = P(A) * P(B|A) * P(C|A,B)
P_ABC = P_A * P_B_dado_A * P_C_dado_AB

print("Probabilidad conjunta P(A,B,C):", round(P_ABC,4))