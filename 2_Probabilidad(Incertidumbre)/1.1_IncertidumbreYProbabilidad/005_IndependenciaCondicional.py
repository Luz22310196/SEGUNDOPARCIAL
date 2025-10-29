# Variables posibles
variables = ['A', 'B', 'C']

# Valores posibles de cada variable
valores = {
    'A': [True, False],
    'B': [True, False],
    'C': [True, False]
}

# Probabilidades conjuntas P(A,B,C)
P = {
    (True, True, True): 0.1,
    (True, False, True): 0.2,
    (False, True, True): 0.2,
    (False, False, True): 0.1,
    (True, True, False): 0.05,
    (True, False, False): 0.05,
    (False, True, False): 0.2,
    (False, False, False): 0.1
}

# Calcular P(A,B|C)
def P_A_B_dado_C(a,b,c):
    total_C = sum(P[(aa,bb,c)] for aa in valores['A'] for bb in valores['B'])
    return P[(a,b,c)] / total_C if total_C > 0 else 0

# Calcular P(A|C)
def P_A_dado_C(a,c):
    total_C = sum(P[(aa,bb,c)] for aa in valores['A'] for bb in valores['B'])
    total_A = sum(P[(a,bb,c)] for bb in valores['B'])
    return total_A / total_C if total_C > 0 else 0

# Calcular P(B|C)
def P_B_dado_C(b,c):
    total_C = sum(P[(aa,bb,c)] for aa in valores['A'] for bb i_