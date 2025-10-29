from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Documentos
docs = [
    "El perro juega en el jardín",
    "El gato duerme en la casa",
    "El perro y el gato son amigos"
]

# Consulta
query = ["perro juega"]

# Convertir a vectores TF-IDF
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(docs)
query_vector = vectorizer.transform(query)

# Calcular similitud coseno
similarity = cosine_similarity(query_vector, doc_vectors)
ranking = similarity.argsort()[0][::-1]

print("Ranking de documentos más relevantes:", ranking)