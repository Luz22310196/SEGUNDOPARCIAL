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

# Prioridad a priori: guía exploración inicial
prioridad = {
    ('inicio','avanzar'): 5,
    ('inicio','esperar'): 1,
    ('medio','avanzar'): 4,
    ('medio','retroceder'): 2
}

alpha = 0.5   # tasa de aprendizaje
gamma = 0.9   # factor de descuento
epsilon = 0.1 # probabilidad de explorar

# Elegir acción considerando prioridad a priori
def elegir_accion(estado):
    if random.random() < epsilon:
        # explorar acciones con probabilidad proporcional a prioridad
        total = sum(prioridad[(estado,a)] for a in acciones[estado])
        r = random.uniform(0, total)
        acumulado = 0
        for a in acciones[estado]:
            acumulado += prioridad[(estado,a)]
            if r <= acumulado:
                return a
    return max(acciones[estado], key=lambda a: Q[(estado,a)])  # explotar mejor acción

# Entrenamiento Q-Learning guiado por prioridad a priori
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
politica = {s: max(acciones[s], key=lambda a: Q[(estado,a)]) for s in acciones if acciones[s]}

if __name__ == "__main__":
    print("Tabla Q:", Q)            # mostrar valores Q aprendidos
    print("Política óptima:", politica)  # mostrar política óptima considerando prioridad a priori