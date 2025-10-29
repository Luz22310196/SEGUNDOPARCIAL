from collections import defaultdict

# Corpus paralelo simple
corpus = [
    ("hola mundo", "hello world"),
    ("buenos días", "good morning"),
    ("adiós", "goodbye")
]

# Contar traducciones palabra a palabra
translation_prob = defaultdict(lambda: defaultdict(float))
for src, tgt in corpus:
    src_words = src.split()
    tgt_words = tgt.split()
    for s in src_words:
        for t in tgt_words:
            translation_prob[s][t] += 1

# Normalizar probabilidades
for s in translation_prob:
    total = sum(translation_prob[s].values())
    for t in translation_prob[s]:
        translation_prob[s][t] /= total

# Traducir frase fuente simple
source = "hola mundo".split()
translation = [max(translation_prob[s], key=translation_prob[s].get) for s in source]
print("Traducción:", " ".join(translation))
