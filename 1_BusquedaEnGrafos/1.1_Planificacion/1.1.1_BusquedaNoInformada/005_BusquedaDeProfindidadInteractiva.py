def dls(graph, start, limit, visited=None, depth=0):
    # Si no existe el conjunto de visitados, lo creamos
    if visited is None:
        visited = set()

    # Marcamos el nodo actual como visitado
    visited.add(start)
    print(f"Visitando: {start} (profundidad {depth})")

    # Si llegamos al límite de profundidad, detenemos la búsqueda
    if depth >= limit:
        return visited

    # Recorremos los vecinos del nodo actual
    for neighbor in graph.get(start, []):
        # Solo visitamos los nodos que aún no se han visitado
        if neighbor not in visited:
            # Llamada recursiva aumentando la profundidad
            dls(graph, neighbor, limit, visited, depth + 1)

    # Retornamos el conjunto de nodos visitados
    return visited


def iddfs(graph, start, max_depth):
    # Repetimos la búsqueda con profundidades crecientes
    for limit in range(max_depth + 1):
        print(f"\n--- Profundidad límite: {limit} ---")

        # Creamos un nuevo conjunto de visitados en cada iteración
        visited = set()

        # Llamamos a la búsqueda en profundidad limitada (DLS)
        dls(graph, start, limit, visited)


# Programa principal
if __name__ == "__main__":
    # Definimos un grafo como diccionario (lista de adyacencia)
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Llamamos a la búsqueda en profundidad iterativa
    # empezando desde 'A' con un máximo de 3 niveles de profundidad
    iddfs(graph, 'A', 3)