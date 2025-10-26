from collections import deque  # Importamos deque para usarlo como cola (queue)

# Definimos el grafo como un diccionario (lista de adyacencia)
grafo = {
    'A': ['B', 'C'],   # Desde A se puede ir a B y C
    'B': ['D', 'E'],   # Desde B se puede ir a D y E
    'C': ['F'],        # Desde C se puede ir a F
    'D': [],           # D no tiene conexiones
    'E': ['F'],        # Desde E se puede ir a F
    'F': []            # F no tiene conexiones
}

def busqueda_anchura(grafo, inicio, objetivo):
    cola = deque([inicio])   # Creamos una cola y metemos el nodo inicial
    visitados = set()        # Conjunto para guardar los nodos que ya visitamos

    # Mientras haya elementos en la cola...
    while cola:
        nodo = cola.popleft()      # Sacamos el primer nodo de la cola (FIFO)
        print(f"Visitando: {nodo}")  # Mostramos qué nodo se está visitando

        # Si el nodo actual es el que buscamos, terminamos
        if nodo == objetivo:
            print("¡Nodo encontrado!")  # Mensaje cuando se encuentra el objetivo
            return True                 # Devolvemos True indicando éxito

        # Si el nodo no ha sido visitado todavía
        if nodo not in visitados:
            visitados.add(nodo)         # Marcamos el nodo como visitado

            # Recorremos todos los vecinos del nodo actual
            for vecino in grafo[nodo]:
                # Si el vecino aún no ha sido visitado, lo añadimos a la cola
                if vecino not in visitados:
                    cola.append(vecino)

    # Si la cola se vacía y no se encontró el objetivo, mostramos mensaje
    print("No se encontró el nodo objetivo.")
    return False  # Devolvemos False porque no se encontró nada


# --- Ejemplo de uso del algoritmo ---
if __name__ == "__main__":
    inicio = 'A'     # Nodo desde donde comenzamos
    objetivo = 'F'   # Nodo que queremos encontrar

    print("Iniciando búsqueda en anchura...\n")  # Mensaje inicial
    busqueda_anchura(grafo, inicio, objetivo)    # Llamamos a la función
