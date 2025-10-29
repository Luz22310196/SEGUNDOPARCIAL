import math
import random
import heapq

# Temple Simulado
def temple_simulado(objetivo, x0, temp_inicial=100, enfriamiento=0.95, iteraciones=1000, paso=1.0):
    x = x0
    t = temp_inicial

    for _ in range(iteraciones):
        x_nuevo = x + random.uniform(-paso, paso)  # Generar vecino aleatorio
        delta = objetivo(x_nuevo) - objetivo(x)     # Cambio en la función objetivo

        if delta < 0 or random.random() < math.exp(-delta / t):  # Aceptar mejora o con probabilidad
            x = x_nuevo

        t *= enfriamiento  # Reducir temperatura

    return x

# Búsqueda de Haz Local
def busqueda_haz_local(objetivo, x_iniciales, ancho_haz=2, iteraciones=10, paso=1.0):
    haz = [(objetivo(x), x) for x in x_iniciales]  # Inicializar haz con evaluaciones

    for _ in range(iteraciones):
        candidatos = []
        for _, x in haz:
            vecinos = [x + paso, x - paso]  # Generar vecinos
            for v in vecinos:
                candidatos.append((objetivo(v), v))
        haz = heapq.nlargest(ancho_haz, candidatos, key=lambda item: item[0])  # Mantener mejores

    return max(haz, key=lambda item: item[0])[1]  # Retornar mejor solución

# Ejemplo de uso
if __name__ == "__main__":
    def objetivo(x):
        return -x**2 + 10  # Función a maximizar

    mejor_ts = temple_simulado(objetivo, x0=5)  # Ejecutar Temple Simulado
    print("Temple Simulado -> Mejor solución:", mejor_ts, "Valor objetivo:", objetivo(mejor_ts))

    iniciales = [0, 2, 5, -3]  # Soluciones iniciales para haz
    mejor_haz = busqueda_haz_local(objetivo, iniciales)  # Ejecutar Haz Local
    print("Haz Local -> Mejor solución:", mejor_haz, "Valor objetivo:", objetivo(mejor_haz))