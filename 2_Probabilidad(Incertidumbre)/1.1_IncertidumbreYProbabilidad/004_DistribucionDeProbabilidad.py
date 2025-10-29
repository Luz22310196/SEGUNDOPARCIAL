# Eventos posibles
eventos = ['cara', 'cruz']

# Probabilidades asignadas a cada evento
probabilidades = {
    'cara': 0.5,
    'cruz': 0.5
}

# Función para seleccionar un evento según la distribución
import random
def tirar_moneda():
    r = random.random()  # número aleatorio entre 0 y 1
    acumulado = 0
    for evento, prob in probabilidades.items():
        acumulado += prob
        if r <= acumulado:
            return evento

# Simular múltiples tiradas
resultados = [tirar_moneda() for _ in range(1000)]

# Contar ocurrencias para verificar distribución
conteo = {evento: resultados.count(evento)/1000 for evento in eventos}

if __name__ == "__main__":
    print("Distribución simulada:", conteo)  # mostrar distribución aproximada