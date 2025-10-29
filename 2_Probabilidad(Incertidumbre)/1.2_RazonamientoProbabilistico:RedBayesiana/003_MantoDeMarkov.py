# Estados: 0=Sano, 1=Enfermo
# Probabilidades de transición P(X_t | X_{t-1})
P_trans = {
    0: [0.8, 0.2],  # P(sano->sano)=0.8, P(sano->enfermo)=0.2
    1: [0.3, 0.7]   # P(enfermo->sano)=0.3, P(enfermo->enfermo)=0.7
}

# Prob inicial
P0 = [0.9, 0.1]  # 90% sano, 10% enfermo

# Probabilidad después de un paso
P1 = [P0[0]*P_trans[0][0] + P0[1]*P_trans[1][0], 
      P0[0]*P_trans[0][1] + P0[1]*P_trans[1][1]]

print("Probabilidades después de 1 paso:", [round(p,4) for p in P1])

# Probabilidad después de 2 pasos
P2 = [P1[0]*P_trans[0][0] + P1[1]*P_trans[1][0], 
      P1[0]*P_trans[0][1] + P1[1]*P_trans[1][1]]

print("Probabilidades después de 2 pasos:", [round(p,4) for p in P2])