from collections import deque  # Usamos deque para manejar colas de búsqueda

def bidirectional_search(graph, start, goal):
    # Si el nodo inicial y el objetivo son iguales, ya encontramos la solución
    if start == goal:
        return [start]

    # Conjuntos para marcar nodos visitados desde ambos lados
    visited_start = {start}
    visited_goal = {goal}

    # Colas para los dos frentes de búsqueda
    queue_start = deque([[start]])
    queue_goal = deque([[goal]])

    # Bucle principal: continúa mientras ambas colas tengan nodos por explorar
    while queue_start and queue_goal:
        # Expandir desde el lado inicial
        path = queue_start.popleft()      # Tomamos el primer camino de la cola
        node = path[-1]                   # Último nodo del camino actual

        # Recorremos los vecinos del nodo actual
        for neighbor in graph.get(node, []):
            # Si encontramos un nodo ya visitado desde el lado del objetivo → se cruzan las búsquedas
            if neighbor in visited_goal:
                # Retorna el camino completo uniendo ambos lados
                return path + reconstruct_path(queue_goal, neighbor)

            # Si no fue visitado aún, lo añadimos a la cola y lo marcamos
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append(path + [neighbor])

        # Expandir desde el lado del objetivo
        path = queue_goal.popleft()
        node = path[-1]

        for neighbor in graph.get(node, []):
            if neighbor in visited_start:
                # Se cruzan los caminos
                return reconstruct_path(queue_start, neighbor, reverse=True) + path
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append(path + [neighbor])

    # Si no hay conexión entre los dos nodos
    return None


def reconstruct_path(queue, meet_node, reverse=False):
    """
    Función auxiliar que busca el camino parcial en una cola
    para reconstruir la ruta completa cuando las búsquedas se encuentran.
    """
    for p in queue:
        if p[-1] == meet_node:
            # Si la búsqueda era desde el objetivo, invertimos el camino
            return p[::-1] if reverse else p
    return [meet_node]


# Ejemplo de uso
if __name__ == "__main__":
    # Grafo de ejemplo (no dirigido)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    inicio = 'A'
    objetivo = 'F'

    print(f"Buscando camino entre {inicio} y {objetivo}...\n")
    resultado = bidirectional_search(graph, inicio, objetivo)

    if resultado:
        print("Camino encontrado:", " → ".join(resultado))
    else:
        print("No se encontró un camino.")