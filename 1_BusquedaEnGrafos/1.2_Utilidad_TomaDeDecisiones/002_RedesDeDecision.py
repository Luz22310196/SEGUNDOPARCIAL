prob_lluvia = {'si_nublado': 0.7, 'si_despejado': 0.1}  # P(Lluvia|Clima)

def utilidad(decision, estado):
    if decision == 'llevar_paraguas':
        if estado == 'lluvia':
            return 10  # útil porque evita mojarse
        else:
            return -1  # costo de cargar paraguas innecesario
    else:  # no llevar paraguas
        if estado == 'lluvia':
            return -10  # mojarse es muy malo
        else:
            return 5    # comodidad por no cargar paraguas

def utilidad_esperada(decision):
    estados = ['lluvia', 'no_lluvia']
    probs = [0.7, 0.3]  # simplificado: 0.7 lluvia, 0.3 no lluvia
    return sum(utilidad(decision, estado) * p for estado, p in zip(estados, probs))  # suma ponderada

def mejor_decision():
    decisiones = ['llevar_paraguas', 'no_llevar_paraguas']  # opciones disponibles
    mejor = max(decisiones, key=utilidad_esperada)  # elegir decisión con mayor utilidad esperada
    return mejor

if __name__ == "__main__":
    decision = mejor_decision()  # calcular mejor decisión
    print("Mejor decisión:", decision)  # mostrar decisión óptima
    for d in ['llevar_paraguas', 'no_llevar_paraguas']:
        print(f"Utilidad esperada de {d}:", utilidad_esperada(d))  # mostrar utilidades esperadas
