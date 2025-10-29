def hill_climbing(graph, start, h):
    nodo_actual = start
    path = [nodo_actual]  # Camino recorrido

    while True:
        vecinos = graph.get(nodo_actual, [])
        if not vecinos:
            break  # Sin vecinos, fin

        vecino_mejor = min(vecinos, key=lambda n: h.get(n, float('inf')))

        if h[vecino_mejor] >= h[nodo_actual]:
            break  # No hay mejora

        nodo_actual = vecino_mejor
        path.append(nodo_actual)

    return path, h[nodo_actual]  # Camino y valor final


# Ejemplo
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    h = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

    camino, valor = hill_climbing(grafo, 'A', h)
    print("Camino Hill Climbing:", camino)
    print("Valor final:", valor)