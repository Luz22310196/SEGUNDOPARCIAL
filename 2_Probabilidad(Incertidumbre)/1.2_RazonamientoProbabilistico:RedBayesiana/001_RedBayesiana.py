from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creamos la red
modelo = BayesianNetwork([('Enfermo', 'Sintoma')])  # Enfermo -> Sintoma

# Probabilidades iniciales
cpd_enfermo = TabularCPD(variable='Enfermo', variable_card=2, values=[[0.99], [0.01]])  # 0:Sano, 1:Enfermo
cpd_sintoma = TabularCPD(variable='Sintoma', variable_card=2,
                         values=[[0.95, 0.1],  # Sintoma=0 dado Enfermo
                                 [0.05, 0.9]], # Sintoma=1 dado Enfermo
                         evidence=['Enfermo'], evidence_card=[2])

# Agregamos CPDs al modelo
modelo.add_cpds(cpd_enfermo, cpd_sintoma)

# Comprobamos consistencia
assert modelo.check_model()

# Inferencia
infer = VariableElimination(modelo)
res = infer.query(variables=['Enfermo'], evidence={'Sintoma': 1})
print("Probabilidad de estar enfermo dado síntoma:", round(res.values[1],4))