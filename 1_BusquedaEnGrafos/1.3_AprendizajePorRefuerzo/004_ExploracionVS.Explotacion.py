import random

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

# Inicializar tabla Q
Q = {(s,a): 0 for s in acciones for a in acciones[s]}

alpha = 0.5   # tasa de aprendizaje
gamma = 0.9   # factor de descuento
epsilon = 0.2 # probabilidad de explorar

# Elegir acción con política epsilon-greedy (exploración vs explotación)
def elegir_accion(estado):
    if random.random() < epsilon:
        return random.choice(acciones[estado])  # explorar
    return max(acciones[estado], key=lambda a: Q[(estado,a)])  # explotar mejor acción

# Entrenamiento Q-Learning
for _ in range(1000):
    estado = 'inicio'
    while acciones[estado]:
        accion = elegir_accion(estado)
        # siguiente estado determinístico simplificado
        siguiente = 'medio' if estado == 'inicio' and accion == 'avanzar' else \
                    'inicio' if estado == 'medio' and accion == 'retroceder' else 'final'
        # actualizar Q
        max_q_siguiente = max([Q[(siguiente,a)] for a in acciones[siguiente]] or [0])
        Q[(estado, accion)] += alpha * (recompensas[(estado,accion)] + gamma*max_q_siguiente - Q[(estado, accion)])
        estado = siguiente

# Extraer política óptima
politica = {s: max(acciones[s], key=lambda a: Q[(s,a)]) for s in acciones if acciones[s]}

if __name__ == "__main__":
    print("Tabla Q:", Q)            # mostrar valores Q aprendidos
    print("Política óptima:", politica)  # mostrar acción óptima por estado