# Estados posibles
estados = ['lluvia', 'soleado']

# Probabilidades de transición entre estados (t -> t+1)
transiciones = {
    'lluvia': {'lluvia': 0.7, 'soleado': 0.3},
    'soleado': {'lluvia': 0.2, 'soleado': 0.8}
}

# Probabilidades de observación P(o|s)
observaciones = {
    'nublado': {'lluvia': 0.9, 'soleado': 0.2},
    'despejado': {'lluvia': 0.1, 'soleado': 0.8}
}

# Estado de creencia inicial
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

# Simular evolución en el tiempo
def simular_DBN(observaciones_seq):
    creencia_actual = creencia
    for obs in observaciones_seq:
        creencia_actual = actualizar_creencia(creencia_actual, obs)
        print(f"Después de observar {obs}: creencia = {creencia_actual}")

if __name__ == "__main__":
    observaciones_seq = ['nublado', 'despejado', 'nublado']  # ejemplo de observaciones
    simular_DBN(observaciones_seq)  # simular DBN