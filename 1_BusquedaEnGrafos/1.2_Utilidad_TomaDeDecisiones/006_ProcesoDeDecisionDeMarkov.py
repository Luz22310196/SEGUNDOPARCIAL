# Estados posibles
estados = ['inicio', 'medio', 'final']

# Acciones posibles por estado
acciones = {
    'inicio': ['avanzar', 'esperar'],
    'medio': ['avanzar', 'retroceder'],
    'final': []
}

# Probabilidades de transición P(s'|s,a)
transiciones = {
    ('inicio', 'avanzar'): [('medio', 0.8), ('inicio', 0.2)],
    ('inicio', 'esperar'): [('inicio', 1.0)],
    ('medio', 'avanzar'): [('final', 0.9), ('medio', 0.1)],
    ('medio', 'retroceder'): [('inicio', 0.5), ('medio', 0.5)]
}

# Recompensas R(s,a)
recompensas = {
    ('inicio', 'avanzar'): 0,
    ('inicio', 'esperar'): -1,
    ('medio', 'avanzar'): 10,
    ('medio', 'retroceder'): -2
}

# Valor de cada estado inicializado en cero
valores = {s: 0 for s in estados}

gamma = 0.9  # factor de descuento
iteraciones = 10  # número de iteraciones de evaluación de valores

# Iteración de valores para encontrar política óptima
for _ in range(iteraciones):
    nuevos_valores = valores.copy()
    for s in estados:
        if not acciones[s]:
            continue  # saltar estados terminales
        max_valor = max(
            sum(p * (recompensas[(s,a)] + gamma * valores[s_]) for s_, p in transiciones[(s,a)])
            for a in acciones[s]
        )
        nuevos_valores[s] = max_valor
    valores = nuevos_valores

# Determinar política óptima
politica = {}
for s in estados:
    if not acciones[s]:
        politica[s] = None
    else:
        mejor_accion = max(
            acciones[s],
            key=lambda a: sum(p * (recompensas[(s,a)] + gamma * valores[s_]) for s_, p in transiciones[(s,a)])
        )
        politica[s] = mejor_accion

if __name__ == "__main__":
    print("Valores de los estados:", valores)  # mostrar valores de cada estado
    print("Política óptima:", politica)        # mostrar acción óptima por estado