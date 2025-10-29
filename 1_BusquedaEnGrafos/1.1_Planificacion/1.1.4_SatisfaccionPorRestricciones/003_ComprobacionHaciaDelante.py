def forward_checking(variables, dominios, restricciones, asignacion={}):
    if len(asignacion) == len(variables):  # todas las variables asignadas
        return asignacion                   # solución encontrada

    var = next(v for v in variables if v not in asignacion)  # seleccionar variable no asignada

    for valor in dominios[var]:
        asignacion[var] = valor
        dominios_copia = {v: list(dominios[v]) for v in dominios}  # copiar dominios para forward checking

        # eliminar valores incompatibles de los dominios de variables no asignadas
        consistente = True
        for v in variables:
            if v not in asignacion:
                dominios_copia[v] = [val for val in dominios_copia[v] if restricciones(var, asignacion, v, val)]
                if not dominios_copia[v]:  # dominio vacío -> backtrack
                    consistente = False
                    break

        if consistente:
            resultado = forward_checking(variables, dominios_copia, restricciones, asignacion)
            if resultado:
                return resultado

        asignacion.pop(var)  # retroceder (backtrack)

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

    solucion = forward_checking(variables, dominios, restriccion)
    print("Solución encontrada:", solucion)