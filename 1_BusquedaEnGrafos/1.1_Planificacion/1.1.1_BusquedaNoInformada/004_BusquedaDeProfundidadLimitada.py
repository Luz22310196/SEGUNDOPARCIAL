def dls(graph, start, limit, visited=None, depth=0):
    # Inicializa el conjunto de visitados
    if visited is None:
        visited = set()

    print(f"Visitando: {start} (profundidad {depth})")
    visited.add(start)

    # Si alcanzamos el límite, detenemos la exploración
    if depth >= limit:
        return visited

    # Recorre los vecinos si aún no se alcanzó el límite
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dls(graph, neighbor, limit, visited, depth + 1)

    return visited


# Ejemplo de uso
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    limite = 2  # profundidad máxima
    print(f"--- DFS limitada a profundidad {limite} ---")
    resultado = dls(graph, 'A', limite)
    print("Nodos visitados:", resultado)