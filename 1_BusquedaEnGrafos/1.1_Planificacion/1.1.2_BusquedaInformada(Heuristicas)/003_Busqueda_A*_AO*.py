from heapq import heappush, heappop  # Cola de prioridad para A*

# A* 
def a_star(graph, start, goal, h):
    open_set = []
    # f = g + h, g = costo acumulado, nodo, camino
    heappush(open_set, (h[start], 0, start, [start]))
    visitados = set()  # Nodos explorados

    while open_set:
        f, g, nodo, path = heappop(open_set)  # Nodo con menor f

        if nodo == goal:  # Si llegamos al objetivo
            return path, g

        if nodo in visitados:
            continue
        visitados.add(nodo)  # Marcamos como visitado

        for vecino, costo in graph.get(nodo, []):  # Recorremos vecinos
            if vecino not in visitados:
                g_nuevo = g + costo
                f_nuevo = g_nuevo + h.get(vecino, 0)  # f = g + h
                heappush(open_set, (f_nuevo, g_nuevo, vecino, path + [vecino]))

    return None, float('inf')  # Si no hay camino

# AO* 
def ao_star(graph, h, start):
    solved = {}  # Nodos solucionados
    cost = dict(h)  # Inicializa costo con heurística

    def recursive_ao(n):
        if n not in graph or n in solved:  # Nodo terminal o resuelto
            return

        min_cost = float('inf')
        best_option = None

        # Explora cada opción del nodo (OR/AND)
        for option in graph[n]:
            total = sum(cost[child] for child in option)  # Suma hijos (AND)
            if total < min_cost:
                min_cost = total
                best_option = option

        cost[n] = min_cost
        solved[n] = best_option  # Guarda mejor opción

        # Recurre en cada hijo de la mejor opción
        for child in best_option:
            recursive_ao(child)

    recursive_ao(start)
    return solved, cost

# EJEMPLOS 
if __name__ == "__main__":
    # Grafo para A* : nodo -> [(vecino, costo)]
    grafo_a = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 1)],
        'D': [],
        'E': [('F', 1)],
        'F': []
    }

    # Heurística A*
    h_a = {'A': 3, 'B': 2, 'C': 1, 'D': 4, 'E': 1, 'F': 0}

    camino, costo = a_star(grafo_a, 'A', 'F', h_a)
    print("A* -> Camino:", camino)
    print("A* -> Costo:", costo)

    # Grafo para AO* : OR nodos con opciones AND
    grafo_ao = {
        'A': [['B', 'C'], ['D']],  # A puede ir a [B y C] o solo [D]
        'B': [['E']],
        'C': [['F']],
        'D': [['F']],
        'E': [],
        'F': []
    }

    # Heurística AO*
    h_ao = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 0}

    solucion, costos = ao_star(grafo_ao, h_ao, 'A')
    print("AO* -> Solución:", solucion)
    print("AO* -> Costos:", costos)