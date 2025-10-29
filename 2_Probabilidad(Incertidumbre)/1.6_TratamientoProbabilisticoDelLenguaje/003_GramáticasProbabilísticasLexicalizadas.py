import nltk
from nltk import PCFG

# Gramática lexicalizada (simulación simple)
grammar = PCFG.fromstring("""
  S -> NP[Juan] VP[come] [1.0]
  VP[come] -> V[come] NP[María] [0.7] | V[come] [0.3]
  NP[Juan] -> 'Juan' [1.0]
  NP[María] -> 'María' [1.0]
  V[come] -> 'come' [1.0]
""")

# Parser Viterbi
parser = nltk.ViterbiParser(grammar)

sentence = ['Juan', 'come', 'María']
for tree in parser.parse(sentence):
    print(tree)
    print("Probabilidad:", tree.prob())
