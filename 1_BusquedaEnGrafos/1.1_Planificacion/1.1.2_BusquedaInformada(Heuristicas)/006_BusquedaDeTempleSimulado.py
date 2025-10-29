import math
import random

# Función objetivo: ejemplo simple, minimizar f(x) = x^2
def objetivo(x):
    return x**2

# Genera un vecino aleatorio alrededor de x
def vecino(x, paso=1.0):
    return x + random.uniform(-paso, paso)

# Algoritmo de Temple Simulado
def temple_simulado(x0, temp_inicial, enfriamiento, iteraciones):
    x = x0
    t = temp_inicial

    for i in range(iteraciones):
        x_nuevo = vecino(x)
        delta = objetivo(x_nuevo) - objetivo(x)

        # Acepta si mejora o con cierta probabilidad si empeora
        if delta < 0 or random.random() < math.exp(-delta / t):
            x = x_nuevo

        # Reduce la temperatura
        t *= enfriamiento

    return x

# Ejemplo de uso
if __name__ == "__main__":
    mejor_x = temple_simulado(x0=10, temp_inicial=100, enfriamiento=0.95, iteraciones=1000)
    print("Mejor solución encontrada:", mejor_x)
    print("Valor objetivo:", objetivo(mejor_x))