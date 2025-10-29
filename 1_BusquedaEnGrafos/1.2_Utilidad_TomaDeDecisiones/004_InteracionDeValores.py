# Función que calcula utilidad combinando varios criterios
def utilidad_multicriterio(decision):
    beneficio = decision.get('beneficio', 0)  # valor principal
    riesgo = decision.get('riesgo', 0)        # valor negativo
    costo = decision.get('costo', 0)          # otro valor negativo
    # interacción de valores: ponderar y combinar criterios
    return beneficio - 2*riesgo - costo

# Comparar varias opciones según utilidad combinada
def mejor_decision(opciones):
    mejor = None
    mejor_valor = -float('inf')
    for opcion in opciones:
        u = utilidad_multicriterio(opcion)  # calcular utilidad total
        if u > mejor_valor:
            mejor_valor = u
            mejor = opcion
    return mejor

if __name__ == "__main__":
    opciones = [
        {'beneficio': 10, 'riesgo': 3, 'costo': 2},
        {'beneficio': 8, 'riesgo': 1, 'costo': 1},
        {'beneficio': 6, 'riesgo': 0, 'costo': 0}
    ]
    decision = mejor_decision(opciones)  # calcular mejor opción
    print("Mejor decisión:", decision, "con utilidad:", utilidad_multicriterio(decision))