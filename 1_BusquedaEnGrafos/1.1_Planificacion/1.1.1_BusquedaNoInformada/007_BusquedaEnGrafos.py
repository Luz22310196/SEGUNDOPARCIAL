from collections import deque  # Para usar una cola eficiente en BFS

def bfs(graph, start):
    visitados = set()           # Guarda los nodos ya visitados
    cola = deque([start])       # Cola con el nodo inicial
    recorrido = []              # Orden del recorrido

    while cola:                 # Mientras haya nodos por visitar
        nodo = cola.popleft()   # Saca el primero
        if nodo not in visitados:
            print(f"Visitando (BFS): {nodo}")
            visitados.add(nodo)
            recorrido.append(nodo)
            for vecino in graph.get(nodo, []):  # Recorre sus vecinos
                if vecino not in visitados:
                    cola.append(vecino)         # Agrega a la cola
    return recorrido


def dfs(graph, start, visitados=None, recorrido=None):
    if visitados is None:
        visitados = set()       # Crea conjunto de visitados
    if recorrido is None:
        recorrido = []          # Crea lista de recorrido

    print(f"Visitando (DFS): {start}")
    visitados.add(start)        # Marca el nodo actual
    recorrido.append(start)     # Guarda el orden de visita

    for vecino in graph.get(start, []):  # Explora vecinos
        if vecino not in visitados:
            dfs(graph, vecino, visitados, recorrido)  # Llamada recursiva

    return recorrido


if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],       # A conecta con B y C
        'B': ['A', 'D', 'E'],  # B conecta con A, D y E
        'C': ['A', 'F'],       # C conecta con A y F
        'D': ['B'],            # D conecta con B
        'E': ['B', 'F'],       # E conecta con B y F
        'F': ['C', 'E']        # F conecta con C y E
    }

    print("\n=== BFS ===")
    print("Recorrido BFS:", bfs(grafo, 'A'))   # Llama a BFS

    print("\n=== DFS ===")
    print("Recorrido DFS:", dfs(grafo, 'A'))   # Llama a DFS