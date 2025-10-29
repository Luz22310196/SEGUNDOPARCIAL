# Estados posibles
estados = ['lluvia', 'soleado']

# Acciones posibles
acciones = ['llevar_paraguas', 'no_llevar_paraguas']

# Probabilidades de transición P(s'|s,a)
transiciones = {
    'lluvia': {'lluvia': 0.7, 'soleado': 0.3},
    'soleado': {'lluvia': 0.2, 'soleado': 0.8}
}

# Probabilidades de observación P(o|s)
observaciones = {
    'nublado': {'lluvia': 0.9, 'soleado': 0.2},
    'despejado': {'lluvia': 0.1, 'soleado': 0.8}
}

# Función de utilidad
def utilidad(accion, estado):
    if accion == 'llevar_paraguas':
        return 10 if estado == 'lluvia' else -1
    else:
        return -10 if estado == 'lluvia' else 5

# Estado de creencia inicial: probabilidad de lluvia
creencia = {'lluvia': 0.5, 'soleado': 0.5}

# Actualizar creencia según observación
def actualizar_creencia(creencia, observacion):
    nueva_creencia = {}
    for s in estados:
        p_obs = observaciones[observacion][s]
        p_s = sum(transiciones[sp][s] * creencia[sp] for sp in estados)
        nueva_creencia[s] = p_obs * p_s
    # Normalizar
    total = sum(nueva_creencia.values())
    for s in nueva_creencia:
        nueva_creencia[s] /= total
    return nueva_creencia

# Calcular utilidad esperada dado el estado de creencia
def utilidad_esperada(accion, creencia):
    return sum(creencia[s] * utilidad(accion, s) for s in estados)

# Elegir mejor acción según la creencia actual
def mejor_accion(creencia):
    return max(acciones, key=lambda a: utilidad_esperada(a, creencia))

if __name__ == "__main__":
    observacion_actual = 'nublado'  # ejemplo de observación
    creencia = actualizar_creencia(creencia, observacion_actual)  # actualizar creencia según observación
    accion = mejor_accion(creencia)  # elegir mejor acción
    print("Creencia actual:", creencia)
    print("Mejor acción según creencia:", accion)