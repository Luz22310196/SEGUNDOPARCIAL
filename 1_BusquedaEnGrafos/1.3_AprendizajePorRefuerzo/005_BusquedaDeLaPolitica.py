# Estados posibles
estados = ['inicio', 'medio', 'final']

# Acciones posibles por estado
acciones = {
    'inicio': ['avanzar', 'esperar'],
    'medio': ['avanzar', 'retroceder'],
    'final': []
}

# Recompensas R(s,a)
recompensas = {
    ('inicio', 'avanzar'): 0,
    ('inicio', 'esperar'): -1,
    ('medio', 'avanzar'): 10,
    ('medio', 'retroceder'): -2
}

# Probabilidades de transición P(s'|s,a)
transiciones = {
    ('inicio', 'avanzar'): {'medio': 1.0},
    ('inicio', 'esperar'): {'inicio': 1.0},
    ('medio', 'avanzar'): {'final': 1.0},
    ('medio', 'retroceder'): {'inicio': 1.0}
}

# Inicializar valores de estados
V = {s: 0 for s in estados}

gamma = 0.9  # factor de descuento

# Inicializar política arbitraria
politica = {s: acciones[s][0] for s in acciones if acciones[s]}

# Iteración de política
def evaluar_politica():
    for _ in range(100):
        for s in V:
            if acciones.get(s):
                a = politica[s]
                V[s] = sum(transiciones[(s,a)][s_next] * (recompensas[(s,a)] + gamma * V[s_next])
                           for s_next in transiciones[(s,a)])

def mejorar_politica():
    cambio = False
    for s in politica:
        mejor_accion = max(acciones[s], key=lambda a: sum(
            transiciones[(s,a)][s_next] * (recompensas[(s,a)] + gamma * V[s_next])
            for s_next in transiciones[(s,a)]
        ))
        if mejor_accion != politica[s]:
            politica[s] = mejor_accion
            cambio = True
    return cambio

# Búsqueda de política óptima
while True:
    evaluar_politica()  # evaluar política actual
    if not mejorar_politica():  # mejorar política hasta convergencia
        break

if __name__ == "__main__":
    print("Valores de los estados:", V)          # mostrar valores finales
    print("Política óptima:", politica)          # mostrar política óptima por estado