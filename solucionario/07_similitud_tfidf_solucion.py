"""
Solución de referencia -- 07_similitud_tfidf.py (E5)
SOLO para el docente. No repartir a los alumnos.
"""

from pathlib import Path

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords", quiet=True)


def reto12_tfidf_documentos(carpeta="data/documentos"):
    rutas = sorted(Path(carpeta).glob("*.txt"))
    textos = [p.read_text(encoding="utf-8") for p in rutas]
    nombres = [p.name for p in rutas]
    # Sin quitar stopwords, palabras como "de"/"la"/"es" (presentes en casi
    # todos los documentos) meten ruido en la similitud -- por eso se
    # reutiliza el concepto de E2 acá.
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("spanish"))
    X = vectorizer.fit_transform(textos)
    return X, vectorizer, nombres, textos


def reto13_similitud(X, nombres, referencia="doc01.txt", top_n=5):
    sim = cosine_similarity(X)
    idx_ref = nombres.index(referencia)
    similitudes = [
        (nombres[i], score) for i, score in enumerate(sim[idx_ref]) if i != idx_ref
    ]
    similitudes.sort(key=lambda par: par[1], reverse=True)
    print(f"Documentos más parecidos a {referencia}:")
    for nombre, score in similitudes[:top_n]:
        print(f"  {nombre}  {score:.2f}")
    return similitudes[:top_n]


if __name__ == "__main__":
    X, vectorizer, nombres, textos = reto12_tfidf_documentos()
    print("Tamaño vocabulario:", len(vectorizer.get_feature_names_out()))
    reto13_similitud(X, nombres)
