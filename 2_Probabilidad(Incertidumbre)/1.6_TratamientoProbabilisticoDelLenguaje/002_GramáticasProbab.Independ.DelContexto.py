import nltk
from nltk import PCFG

# Definir gramática probabilística
grammar = PCFG.fromstring("""
  S -> NP VP [1.0]
  VP -> V NP [0.7] | V [0.3]
  NP -> 'Juan' [0.5] | 'María' [0.5]
  V -> 'come' [0.6] | 'lee' [0.4]
""")

# Crear parser
parser = nltk.ViterbiParser(grammar)

# Analizar oración
sentence = ['Juan', 'come', 'María']
for tree in parser.parse(sentence):
    print(tree)
    print("Probabilidad:", tree.prob())