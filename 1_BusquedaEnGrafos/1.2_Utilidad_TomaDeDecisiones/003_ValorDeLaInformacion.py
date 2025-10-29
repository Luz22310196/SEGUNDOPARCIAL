# Función de utilidad según decisión y estado del mundo
def utilidad(decision, estado):
    if decision == 'llevar_paraguas':
        if estado == 'lluvia':
            return 10  # evita mojarse
        else:
            return -1  # cargar paraguas innecesario
    else:
        if estado == 'lluvia':
            return -10  # mojarse es muy malo
        else:
            return 5    # comodidad por no llevar paraguas

# Calcular utilidad esperada de una decisión
def utilidad_esperada(decision, prob_lluvia):
    estados = ['lluvia', 'no_lluvia']
    probs = [prob_lluvia, 1-prob_lluvia]  # probabilidades de cada estado
    return sum(utilidad(decision, estado) * p for estado, p in zip(estados, probs))  # suma ponderada

# Mejor decisión sin información adicional
def mejor_decision(prob_lluvia):
    decisiones = ['llevar_paraguas', 'no_llevar_paraguas']
    return max(decisiones, key=lambda d: utilidad_esperada(d, prob_lluvia))  # decisión con mayor utilidad esperada

if __name__ == "__main__":
    prob_lluvia = 0.3  # probabilidad inicial de lluvia
    decision_sin_info = mejor_decision(prob_lluvia)  # mejor decisión sin información extra
    util_sin_info = utilidad_esperada(decision_sin_info, prob_lluvia)

    prob_lluvia_perfecta = 0.7  # ejemplo: información perfecta indica alta probabilidad
    decision_con_info = mejor_decision(prob_lluvia_perfecta)  # mejor decisión con información
    util_con_info = utilidad_esperada(decision_con_info, prob_lluvia_perfecta)

    valor_informacion = util_con_info - util_sin_info  # diferencia: valor de la información
    print("Valor de la información:", valor_informacion)