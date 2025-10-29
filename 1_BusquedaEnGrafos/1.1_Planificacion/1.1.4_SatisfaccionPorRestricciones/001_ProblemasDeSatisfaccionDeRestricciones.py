def csp_backtracking(variables, dominios, restricciones, asignacion={}):
    if len(asignacion) == len(variables):  # todos los variables asignadas
        return asignacion                   # solución encontrada

    var = next(v for v in variables if v not in asignacion)  # seleccionar variable no asignada

    for valor in dominios[var]:
        asignacion[var] = valor
        if all(restricciones(var, asignacion, v, asignacion.get(v)) for v in asignacion if v != var):  # verificar restricciones locales
            resultado = csp_backtracking(variables, dominios, restricciones, asignacion)
            if resultado:
                return resultado
        asignacion.pop(var)  # backtrack

    return None  # no se encontró solución

if __name__ == "__main__":
    variables = ['A', 'B', 'C']  # definir variables
    dominios = {
        'A': [1, 2, 3],
        'B': [1, 2, 3],
        'C': [1, 2, 3]
    }

    def restriccion(var1, asignacion, var2, valor2):
        if valor2 is None:  # variable aún no asignada
            return True
        return asignacion[var1] != valor2  # valores distintos

    solucion = csp_backtracking(variables, dominios, restriccion)
    print("Solución encontrada:", solucion)