def cbj(variables, dominios, restricciones, asignacion={}, conflicto={}):
    if len(asignacion) == len(variables):  # todas las variables asignadas
        return asignacion                   # solución encontrada

    var = next(v for v in variables if v not in asignacion)  # seleccionar variable no asignada
    conflicto[var] = set()  # inicializar conjunto de conflicto

    for valor in dominios[var]:
        asignacion[var] = valor
        fallido = False

        # revisar restricciones con variables asignadas
        for v in asignacion:
            if v != var and not restricciones(var, asignacion, v, asignacion[v]):
                fallido = True
                conflicto[var].add(v)  # registrar variable causante del conflicto

        if not fallido:
            resultado = cbj(variables, dominios, restricciones, asignacion, conflicto)
            if resultado:
                return resultado

        asignacion.pop(var)  # retroceder

    # si hay conflicto, retroceder al causante más reciente
    if conflicto[var]:
        return None  # en un CBJ completo se podría saltar al causante más reciente

    return None  # no se encontró solución

if __name__ == "__main__":
    variables = ['X', 'Y', 'Z']  # definir variables
    dominios = {
        'X': [1, 2, 3],
        'Y': [1, 2, 3],
        'Z': [1, 2, 3]
    }

    def restriccion(var1, asignacion, var2, valor2):
        if valor2 is None:  # variable aún no asignada
            return True
        return asignacion[var1] != valor2  # valores distintos

    solucion = cbj(variables, dominios, restriccion)
    print("Solución encontrada:", solucion)