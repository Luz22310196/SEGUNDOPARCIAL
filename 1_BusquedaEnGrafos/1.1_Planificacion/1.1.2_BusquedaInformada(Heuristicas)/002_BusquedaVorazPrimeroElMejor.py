from heapq import heappush, heappop  # Cola de prioridad

def greedy_best_first(graph, start, goal, h):
    open_set = []
    heappush(open_set, (h[start], start, [start]))  # (heurística, nodo, camino)
    visitados = set()  # Nodos ya visitados

    while open_set:
        h_nodo, nodo, path = heappop(open_set)  # Nodo con menor h

        if nodo == goal:  # Si llegamos al objetivo
            return path

        if nodo in visitados:
            continue
        visitados.add(nodo)  # Marcamos como visitado

        for vecino in graph.get(nodo, []):  # Recorremos vecinos
            if vecino not in visitados:
                heappush(open_set, (h.get(vecino, 0), vecino, path + [vecino]))

    return None  # Si no se encuentra camino


if __name__ == "__main__":
    # Grafo: nodo -> lista de vecinos
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Heurística: estimación hasta el objetivo 'F'
    h = {'A': 3, 'B': 2, 'C': 1, 'D': 4, 'E': 1, 'F': 0}

    camino = greedy_best_first(grafo, 'A', 'F', h)
    print("Camino encontrado:", camino)