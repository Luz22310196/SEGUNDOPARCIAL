def utilidad(decision):
    valor = decision.get('beneficio', 0)  # obtener beneficio de la decisión
    riesgo = decision.get('riesgo', 0)    # obtener riesgo asociado
    return valor - 2 * riesgo             # función de utilidad lineal: más riesgo reduce utilidad

def mejor_decision(opciones):
    mejor = None                          # inicializar mejor decisión
    mejor_valor = -float('inf')           # inicializar mejor valor con -infinito
    for opcion in opciones:
        u = utilidad(opcion)              # calcular utilidad de la opción actual
        if u > mejor_valor:               # si la utilidad es mejor que la mejor hasta ahora
            mejor_valor = u               # actualizar mejor valor
            mejor = opcion                # actualizar mejor decisión
    return mejor                           # devolver la mejor decisión encontrada

if __name__ == "__main__":
    opciones = [
        {'beneficio': 10, 'riesgo': 3},  # opción 1
        {'beneficio': 8, 'riesgo': 1},   # opción 2
        {'beneficio': 6, 'riesgo': 0}    # opción 3
    ]
    decision = mejor_decision(opciones)  # elegir la mejor opción según utilidad
    print("Mejor decisión:", decision, "con utilidad:", utilidad(decision))  # mostrar resultado