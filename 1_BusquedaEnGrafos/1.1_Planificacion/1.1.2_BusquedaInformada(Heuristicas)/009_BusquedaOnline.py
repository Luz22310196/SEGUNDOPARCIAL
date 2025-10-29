import random

# Algoritmo de búsqueda en línea genérico
def busqueda_online(objetivo, estado_inicial, generador_vecino, max_iter=1000):
    estado = estado_inicial  # inicializar estado
    mejor = estado            # mejor estado encontrado hasta ahora

    for i in range(max_iter):
        vecino = generador_vecino(estado)            # generar vecino del estado actual
        if objetivo(vecino) > objetivo(mejor):       # si el vecino es mejor
            mejor = vecino                            # actualizar mejor
        # decidir si moverse al vecino (ejemplo simple: mover siempre)
        estado = vecino                               # mover estado al vecino

    return mejor                                      # devolver mejor estado

# Ejemplo de uso
if __name__ == "__main__":
    # definir función objetivo (a maximizar)
    def objetivo(x):
        return - (x-3)**2 + 10  # pico en x=3

    # generador de vecinos: suma o resta pequeño valor
    def generador_vecino(x, rango=1.0):
        return x + random.uniform(-rango, rango)

    estado0 = 0.0                                      # estado inicial
    mejor = busqueda_online(objetivo, estado0, generador_vecino, max_iter=500)
    print("Mejor solución encontrada:", mejor, "valor objetivo:", objetivo(mejor))