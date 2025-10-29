import math

def branch_and_bound(estado, generar_vecinos, objetivo, mejor_valor=-math.inf, mejor_estado=None):
    # calcular valor del estado actual
    valor_actual = objetivo(estado)
    if valor_actual > mejor_valor:  # actualizar mejor si es mejor
        mejor_valor = valor_actual
        mejor_estado = estado

    for vecino in generar_vecinos(estado):
        # poda: si el vecino no puede superar el mejor valor, se descarta
        if objetivo(vecino) > mejor_valor:
            mejor_valor, mejor_estado = branch_and_bound(vecino, generar_vecinos, objetivo, mejor_valor, mejor_estado)

    return mejor_valor, mejor_estado

# Ejemplo de uso
if __name__ == "__main__":
    # función objetivo (a maximizar)
    def objetivo(x):
        return - (x-5)**2 + 25  # pico en x=5

    # generador de vecinos
    def generar_vecinos(x, paso=1):
        return [x+paso, x-paso]

    estado_inicial = 0
    mejor_valor, mejor_estado = branch_and_bound(estado_inicial, generar_vecinos, objetivo)
    print("Mejor estado:", mejor_estado, "Valor objetivo:", mejor_valor)