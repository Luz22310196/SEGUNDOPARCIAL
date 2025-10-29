# Matriz de pagos para jugador 1
pagos_j1 = [
    [3, 1],  # estrategias del jugador 2: [estrategia_0, estrategia_1]
    [0, 2]
]

# Matriz de pagos para jugador 2
pagos_j2 = [
    [2, 1],
    [0, 3]
]

# Lista de estrategias
estrategias = [0, 1]

# Buscar equilibrio de Nash puro
def equilibrio_nash():
    equilibria = []
    for s1 in estrategias:
        for s2 in estrategias:
            mejor_s1 = all(pagos_j1[s1][s2] >= pagos_j1[alt_s1][s2] for alt_s1 in estrategias)  # jugador 1 no mejora
            mejor_s2 = all(pagos_j2[s1][s2] >= pagos_j2[s1][alt_s2] for alt_s2 in estrategias)  # jugador 2 no mejora
            if mejor_s1 and mejor_s2:
                equilibria.append((s1, s2))
    return equilibria

if __name__ == "__main__":
    equilibrios = equilibrio_nash()  # calcular equilibrios
    print("Equilibrios de Nash encontrados:", equilibrios)  # mostrar resultados