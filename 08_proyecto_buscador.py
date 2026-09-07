"""
Proyecto final -- Mini buscador inteligente (5:10-6:00)

Todo lo del taller converge acá:

    documentos (data/documentos, 20 .txt)
        -> TF-IDF de los documentos (fit)
    query del usuario
        -> TF-IDF de la query (transform, mismo vocabulario)
    cosine_similarity(query, documentos)
        -> ranking
        -> top-N documentos más relevantes

Resultado esperado, ejemplo real con la data de data/documentos:

    Consulta: python programación
    1. doc01.txt  0.71
    2. doc20.txt  0.55
    3. doc02.txt  0.42
    ...

Este archivo asume que 07_similitud_tfidf.py (reto12/reto13) ya está
resuelto -- es la misma idea, cerrada en un producto usable.
"""

from pathlib import Path

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords", quiet=True)


# ---------------------------------------------------------------------------
# RETO 14a -- Indexar el corpus (fit del vectorizer sobre los documentos)
# ---------------------------------------------------------------------------
def reto14a_indexar(carpeta="data/documentos"):
    """
    Objetivo:
        Cargar los 20 documentos, entrenar UN SOLO TfidfVectorizer sobre
        ellos (fit_transform) y devolver (X_docs, vectorizer, nombres,
        textos). Este vectorizer se reutiliza para cada consulta -- no se
        vuelve a entrenar.
    Restricciones:
        - Reutilizar la lógica de 07_similitud_tfidf.reto12_tfidf_documentos,
          incluyendo stop_words=stopwords.words("spanish").
    Resultado esperado:
        X_docs.shape -> (20, N).
    """
    rutas = sorted(Path(carpeta).glob("*.txt"))
    textos = [p.read_text(encoding="utf-8") for p in rutas]
    nombres = [p.name for p in rutas]
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("spanish"))
    X_docs = vectorizer.fit_transform(textos)
    return X_docs, vectorizer, nombres, textos


# ---------------------------------------------------------------------------
# RETO 14b -- Buscar: query -> transform -> similitud -> ranking top-N
# ---------------------------------------------------------------------------
def reto14b_buscar(query, X_docs, vectorizer, nombres, textos, top_n=5):
    """
    Objetivo:
        Vectorizar la query con vectorizer.transform([query]) (NO fit),
        calcular cosine_similarity(query_vec, X_docs), y devolver una
        lista de (nombre_doc, score, texto) ordenada de mayor a menor
        score, con los top_n resultados.
    Restricciones:
        - vectorizer.transform, jamás fit_transform para la query (el
          vocabulario se fija con los documentos, no con la consulta).
        - cosine_similarity espera 2D: query_vec ya es 2D si viene de
          transform([query]).
    Resultado esperado:
        Lista de tuplas ordenada, ej:
        [("doc01.txt", 0.71, "Python es un lenguaje..."), ...]
        Si la query no comparte ninguna palabra con el corpus, todos los
        scores dan 0 -- es una limitación real de TF-IDF puro, buen punto
        de discusión de cierre.
    """
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, X_docs)[0]
    resultados = list(zip(nombres, scores, textos))
    resultados.sort(key=lambda r: r[1], reverse=True)
    return resultados[:top_n]


# ---------------------------------------------------------------------------
# RETO 14c -- Interfaz de consola del buscador
# ---------------------------------------------------------------------------
def reto14c_interfaz(X_docs, vectorizer, nombres, textos):
    """
    Objetivo:
        Loop con input("Consulta: ") -> reto14b_buscar -> imprimir el
        ranking con formato "1. doc03.txt   0.82". Salir con "salir".
    Restricciones:
        - Reusar reto14b_buscar, no reimplementar la búsqueda acá.
    Resultado esperado (demo en vivo para cerrar el taller):
        Consulta: python programación
        1. doc01.txt   0.71
        2. doc20.txt   0.55
        3. doc02.txt   0.42
        Consulta: salir
    """
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
