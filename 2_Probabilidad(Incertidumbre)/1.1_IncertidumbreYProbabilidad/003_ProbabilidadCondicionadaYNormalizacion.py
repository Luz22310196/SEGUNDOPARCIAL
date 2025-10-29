# Variables posibles
variables = ['Lluvia', 'Riego']

# Valores posibles de cada variable
valores = {
    'Lluvia': [True, False],
    'Riego': [True, False]
}

# Probabilidades condicionales P(Riego|Lluvia)
P = {
    (True, True): 0.01,   # P(Riego=True|Lluvia=True)
    (True, False): 0.99,  # P(Riego=False|Lluvia=True)
    (False, True): 0.4,   # P(Riego=True|Lluvia=False)
    (False, False): 0.6    # P(Riego=False|Lluvia=False)
}

# Calcular probabilidad conjunta no normalizada P(Lluvia,Riego)
def probabilidad_conjunta(lluvia, riego):
    return P[(lluvia, riego)] * 0.2 if lluvia else P[(lluvia, riego)] * 0.8  # P(Lluvia)=0.2

# Normalizar conjunto de probabilidades condicionales
def normalizar(distribucion):
    total = sum(distribucion.values())
    return {k: v/total for k,v in distribucion.items()}  # dividir por la suma total

# Calcular distribución condicional P(Lluvia|Riego=True)
distribucion = {}
for l in valores['Lluvia']:
    distribucion[l] = probabilidad_conjunta(l, True)
distribucion = normalizar(distribucion)

if __name__ == "__main__":
    print("Distribución condicional P(Lluvia|Riego=True):", distribucion)  # mostrar probabilidades normalizadas
