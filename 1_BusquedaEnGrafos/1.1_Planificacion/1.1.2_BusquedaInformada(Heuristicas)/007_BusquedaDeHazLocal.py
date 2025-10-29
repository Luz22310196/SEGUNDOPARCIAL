import heapq

# Función objetivo: ejemplo simple, maximizar f(x) = -x^2 + 10
def objetivo(x):
    return -x**2 + 10

# Genera vecinos posibles alrededor de x
def vecinos(x, paso=1.0):
    return [x + paso, x - paso]

# Algoritmo de búsqueda de haz local
def busqueda_haz_local(x_iniciales, ancho_haz, iteraciones):
    haz = [(objetivo(x), x) for x in x_iniciales]

    for _ in range(iteraciones):
        candidatos = []
        for _, x in haz:
            for v in vecinos(x):
                candidatos.append((objetivo(v), v))

        # Mantiene solo los mejores según el ancho del haz
        haz = heapq.nlargest(ancho_haz, candidatos, key=lambda item: item[0])

    # Retorna la mejor solución encontrada
    return max(haz, key=lambda item: item[0])[1]

# Ejemplo de uso
if __name__ == "__main__":
    x_iniciales = [0, 5, -5]  # haz inicial
    mejor_x = busqueda_haz_local(x_iniciales, ancho_haz=2, iteraciones=10)
    print("Mejor solución encontrada:", mejor_x)
    print("Valor objetivo:", objetivo(mejor_x))