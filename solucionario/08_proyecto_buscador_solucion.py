"""
Solución de referencia -- 08_proyecto_buscador.py (Proyecto final)
SOLO para el docente. No repartir a los alumnos.
"""

from pathlib import Path

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords", quiet=True)


def reto14a_indexar(carpeta="data/documentos"):
    rutas = sorted(Path(carpeta).glob("*.txt"))
    textos = [p.read_text(encoding="utf-8") for p in rutas]
    nombres = [p.name for p in rutas]
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("spanish"))
    X_docs = vectorizer.fit_transform(textos)
    return X_docs, vectorizer, nombres, textos


def reto14b_buscar(query, X_docs, vectorizer, nombres, textos, top_n=5):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, X_docs)[0]
    resultados = list(zip(nombres, scores, textos))
    resultados.sort(key=lambda r: r[1], reverse=True)
    return resultados[:top_n]


def reto14c_interfaz(X_docs, vectorizer, nombres, textos):
    while True:
        query = input("Consulta: ")
        if query.strip().lower() == "salir":
            break
        resultados = reto14b_buscar(query, X_docs, vectorizer, nombres, textos)
        for i, (nombre, score, _texto) in enumerate(resultados, start=1):
            print(f"{i}. {nombre}   {score:.2f}")


if __name__ == "__main__":
    X_docs, vectorizer, nombres, textos = reto14a_indexar()
    reto14c_interfaz(X_docs, vectorizer, nombres, textos)
