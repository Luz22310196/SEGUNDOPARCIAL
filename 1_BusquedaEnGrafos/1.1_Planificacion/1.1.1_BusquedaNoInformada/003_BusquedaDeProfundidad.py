def dfs(graph, start, visited=None)
    # Inicializa el conjunto de nodos visitados
    if visited is None:
        visited = set()
    
    # Marca el nodo actual como visitado
    visited.add(start)
    print(f"Visitando: {start}")

    # Recorre los vecinos del nodo actual
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    # Retorna los nodos visitados
    return visited


# Ejemplo de uso
if __name__ == "__main__":
    # Grafo representado como diccionario
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Llamada a la función DFS
    print("Resultado DFS:", dfs(graph, 'A'))