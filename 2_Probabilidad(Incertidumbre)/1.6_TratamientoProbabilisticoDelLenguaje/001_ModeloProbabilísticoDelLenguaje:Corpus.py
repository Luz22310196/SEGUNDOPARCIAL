import numpy as np
from collections import defaultdict

# Texto de ejemplo
text = "hola mundo hola inteligencia artificial mundo hola"

# Tokenizar
words = text.split()
vocab = list(set(words))

# Construir bigramas
bigram_counts = defaultdict(lambda: defaultdict(int))
for i in range(len(words)-1):
    bigram_counts[words[i]][words[i+1]] += 1

# Convertir a probabilidades
bigram_probs = {}
for w1 in bigram_counts:
    total = sum(bigram_counts[w1].values())
    bigram_probs[w1] = {w2: count/total for w2, count in bigram_counts[w1].items()}

# Predicción de la siguiente palabra
current_word = "hola"
next_word = max(bigram_probs[current_word], key=bigram_probs[current_word].get)
print("Siguiente palabra probable después de 'hola':", next_word)