def tabu_search(initial, neighbors_func, h, tabu_size=5, max_iter=50):
    current = initial
    best = current
    tabu_list = []  # Lista tabú

    for _ in range(max_iter):
        vecinos = neighbors_func(current)
        vecinos = [v for v in vecinos if v not in tabu_list]  # Filtra tabú
        if not vecinos:
            break

        vecino_mejor = min(vecinos, key=h)  # Mejor vecino
        if h(vecino_mejor) < h(best):
            best = vecino_mejor  # Actualiza mejor solución

        tabu_list.append(vecino_mejor)  # Agrega a tabú
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)  # Mantiene tamaño

        current = vecino_mejor  # Avanza al vecino

    return best


# EJEMPLO 
if __name__ == "__main__":
    # Grafo: nodo -> lista de vecinos
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Heurística: menor es mejor
    h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}
    h_func = lambda n: h[n]

    mejor = tabu_search('A', lambda n: graph[n], h_func, tabu_size=3, max_iter=20)
    print("Mejor estado encontrado:", mejor)