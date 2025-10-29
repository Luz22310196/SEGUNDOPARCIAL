from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos la red: Enfermo -> Prueba -> Resultado
modelo = BayesianNetwork([('Enfermo', 'Prueba'), ('Prueba', 'Resultado')])

# Probabilidades
cpd_enfermo = TabularCPD('Enfermo', 2, [[0.99], [0.01]])  # 0:Sano,1:Enfermo
cpd_prueba = TabularCPD('Prueba', 2, [[0.95, 0.2],[0.05,0.8]], evidence=['Enfermo'], evidence_card=[2])
cpd_resultado = TabularCPD('Resultado', 2, [[0.9,0.1],[0.1,0.9]], evidence=['Prueba'], evidence_card=[2])

# Agregamos CPDs
modelo.add_cpds(cpd_enfermo, cpd_prueba, cpd_resultado)
assert modelo.check_model()

# Inferencia por eliminación de variables
infer = VariableElimination(modelo)
res = infer.query(variables=['Enfermo'], evidence={'Resultado': 1})  # Prob Enf dado Resultado positivo

print("P(Enfermo | Resultado positivo):", round(res.values[1],4))