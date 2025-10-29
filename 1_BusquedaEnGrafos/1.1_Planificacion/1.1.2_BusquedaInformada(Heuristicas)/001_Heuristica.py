from heapq import heappush, heappop  # Cola de prioridad

def a_star(graph, start, goal, h):
    open_set = []
    # f = g + h, g = costo acumulado, nodo, camino recorrido
    heappush(open_set, (h[start], 0, start, [start]))  
    visitados = set()  # Nodos ya explorados

    while open_set:
        f, g, nodo, path = heappop(open_set)  # Sacamos el nodo con menor f

        if nodo == goal:  # Si llegamos al objetivo
            return path, g

        if nodo in visitados:
            continue
        visitados.add(nodo)  # Marcamos como visitado

        for vecino, costo in graph.get(nodo, []):  # Recorremos vecinos
            if vecino not in visitados:
                g_nuevo = g + costo              # Nuevo costo acumulado
                f_nuevo = g_nuevo + h.get(vecino, 0)  # f = g + h
                heappush(open_set, (f_nuevo, g_nuevo, vecino, path + [vecino]))

    return None, float('inf')  # Si no hay camino


if __name__ == "__main__":
    # Grafo: nodo -> [(vecino, costo)]
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [],
        'E': [('F', 1)],
        'F': []
    }

    # Heurística: estimación hasta el objetivo 'F'
    h = {'A': 3, 'B': 2, 'C': 1, 'D': 4, 'E': 1, 'F': 0}  

    camino, costo = a_star(grafo, 'A', 'F', h)
    print("Camino:", camino)
    print("Costo:", costo)