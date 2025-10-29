import random

# Función que calcula el número de conflictos si var = valor
def contar_conflictos(var, valor, asignacion, restricciones):
    return sum(not restricciones(var, valor, v, asignacion[v]) 
               for v in asignacion if v != var)  # contar violaciones

# Algoritmo min‑conflicts para CSP
def min_conflicts(variables, dominios, restricciones, max_pasos=10000):
    # asignación inicial completa al azar
    asignacion = {v: random.choice(dominios[v]) for v in variables}  
    for paso in range(max_pasos):
        # encontrar variables en conflicto
        conflictuadas = [v for v in variables 
                         if any(not restricciones(v, asignacion[v], u, asignacion[u]) 
                                for u in variables if u != v)]
        if not conflictuadas:
            return asignacion  # solución encontrada
        var = random.choice(conflictuadas)  # elegir variable en conflicto al azar
        # elegir valor que minimiza conflictos
        valor_mejor = min(dominios[var], key=lambda val: contar_conflictos(var, val, asignacion, restricciones))
        asignacion[var] = valor_mejor  # asignar nuevo valor
    return None  # no se encontró solución en el límite de pasos

# Ejemplo de uso
if __name__ == "__main__":
    variables = ['A','B','C']  # definir variables
    dominios = {
        'A': [1,2,3],
        'B': [1,2,3],
        'C': [1,2,3]
    }
    def restriccion(var1, val1, var2, val2):
        return val1 != val2  # ejemplo: valores distintos

    solucion = min_conflicts(variables, dominios, restriccion, max_pasos=1000)
    print("Solución encontrada:", solucion)