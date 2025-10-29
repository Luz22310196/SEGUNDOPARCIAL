import spacy

# Cargar modelo en español
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
text = "Juan trabaja en OpenAI y vive en Madrid desde 2020."

# Procesar texto
doc = nlp(text)

# Reconocimiento de entidades
for ent in doc.ents:
    print(ent.text, ent.label_)

# Extraer relaciones simples (heurística)
for token in doc:
    if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
        subj = token.text
        verb = token.head.text
        obj = [child.text for child in token.head.children if child.dep_ == "obj"]
        if obj:
            print("Relación extraída:", subj, verb, obj[0])