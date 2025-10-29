# Definir la utilidad de una política
def utilidad_politica(politica, estado):
    if politica == 'politica_A':
        return 10 if estado == 'positivo' else -5  # política A favorece estados positivos
    elif politica == 'politica_B':
        return 8 if estado == 'positivo' else -2   # política B es menos agresiva
    elif politica == 'politica_C':
        return 5 if estado == 'positivo' else 0    # política C es conservadora

# Evaluar la combinación de dos políticas
def utilidad_combinada(politica1, politica2, estado):
    # interacción simple: promedio de utilidades de ambas políticas
    return (utilidad_politica(politica1, estado) + utilidad_politica(politica2, estado)) / 2

# Comparar varias combinaciones de políticas
def mejor_combinacion(politicas, estados):
    mejor = None
    mejor_valor = -float('inf')
    for p1 in politicas:
        for p2 in politicas:
            u_total = sum(utilidad_combinada(p1, p2, e) for e in estados)  # sumar utilidades sobre todos los estados
            if u_total > mejor_valor:
                mejor_valor = u_total
                mejor = (p1, p2)
    return mejor

if __name__ == "__main__":
    politicas = ['politica_A', 'politica_B', 'politica_C']
    estados = ['positivo', 'negativo']
    combinacion = mejor_combinacion(politicas, estados)  # calcular mejor combinación
    print("Mejor combinación de políticas:", combinacion)