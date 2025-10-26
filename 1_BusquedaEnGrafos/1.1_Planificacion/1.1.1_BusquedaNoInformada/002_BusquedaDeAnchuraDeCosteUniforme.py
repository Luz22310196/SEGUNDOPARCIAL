import heapq  # Importamos heapq para usar una cola de prioridad (min-heap)

# Definimos el grafo con sus costos
grafo = {
    'A': [('B', 2), ('C', 5)],  # Desde A se puede ir a B (2) o a C (5)
    'B': [('D', 4), ('E', 1)],  # Desde B se puede ir a D (4) o E (1)
    'C': [('F', 2)],            # Desde C se puede ir a F (2)
    'D': [],                    # D no tiene conexiones
    'E': [('F', 3)],            # Desde E se puede ir a F (3)
    'F': []                     # F no tiene conexiones
}

def busqueda_coste_uniforme(grafo, inicio, objetivo):
    # Creamos la cola de prioridad con una tupla (costo_total, nodo_actual, camino)
    cola = [(0, inicio, [inicio])]
    visitados = set()  # Conjunto para registrar los nodos visitados

    # Mientras haya elementos en la cola...
    while cola:
        # Sacamos el nodo con el menor costo acumulado (heapq mantiene el menor primero)
        costo, nodo, camino = heapq.heappop(cola)
        print(f"Visitando: {nodo} con costo {costo}")  # Mostramos el nodo y su costo

        # Si encontramos el nodo objetivo, terminamos
        if nodo == objetivo:
            print("\n¡Nodo encontrado!")                          # Confirmación
            print(f"Camino: {' -> '.join(camino)}")               # Mostramos el camino completo
            print(f"Costo total: {costo}")                        # Mostramos el costo total
            return costo, camino                                  # Devolvemos los resultados

        # Si el nodo no ha sido visitado aún
        if nodo not in visitados:
            visitados.add(nodo)  # Marcamos el nodo como visitado

            # Recorremos todos los vecinos del nodo actual
            for vecino, costo_extra in grafo[nodo]:
                if vecino not in visitados:  # Si el vecino no ha sido visitado
                    nuevo_costo = costo + costo_extra   # Sumamos el nuevo costo acumulado
                    nuevo_camino = camino + [vecino]    # Guardamos el camino recorrido
                    # Agregamos el nuevo estado a la cola de prioridad
                    heapq.heappush(cola, (nuevo_costo, vecino, nuevo_camino))

    # Si no se encuentra el objetivo después de vaciar la cola
    print("No se encontró el nodo objetivo.")
    return None, []  # Devolvemos None indicando que no se encontró


# --- Ejemplo de uso del algoritmo ---
if __name__ == "__main__":
    inicio = 'A'     # Nodo desde donde iniciamos la búsqueda
    objetivo = 'F'   # Nodo que queremos alcanzar

    print("Iniciando búsqueda de costo uniforme...\n")  # Mensaje inicial
    busqueda_coste_uniforme(grafo, inicio, objetivo)    # Llamada al algoritmo
