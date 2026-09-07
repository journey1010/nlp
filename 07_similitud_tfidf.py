"""
E5 -- Similitud: BoW + TF-IDF + cosine similarity (4:20-5:10)

Pregunta que abre el bloque: en BoW, "el" y "python" pesan igual si
aparecen la misma cantidad de veces. ¿Cómo le decimos al modelo que
"python" es más importante que "el" para distinguir documentos?

Conceptos:
    TF  (Term Frequency)      -> qué tan frecuente es la palabra DENTRO del
                                  documento.
    IDF (Inverse Doc Frequency)-> qué tan rara es la palabra en TODO el
                                  corpus.
    TF-IDF = TF * IDF          -> alto si la palabra es frecuente en ESE
                                  documento pero rara en el resto del
                                  corpus. Eso es justo lo que hace a una
                                  palabra "importante" para un documento.

Pipeline:

    documentos -> TF-IDF -> cosine_similarity -> ranking
"""

from pathlib import Path

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download("stopwords", quiet=True)


# ---------------------------------------------------------------------------
# DEMO -- 4 documentos de juguete, para ver el patrón D1≈D2, D3≈D4
# ---------------------------------------------------------------------------
def demo():
    docs = [
        "python programación",       # D1
        "python aplicaciones",       # D2
        "futbol deporte",            # D3
        "jugadores futbol",          # D4
    ]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(docs)
    print("Vocabulario:", vectorizer.get_feature_names_out())

    sim = cosine_similarity(X)
    print("Matriz de similitud (4x4):")
    print(sim.round(2))
    print("-> D1 y D2 comparten 'python': similitud alta entre ellos.")
    print("-> D3 y D4 comparten 'futbol': similitud alta entre ellos.")


# ---------------------------------------------------------------------------
# RETO 12 -- Cargar los 20 documentos y vectorizar con TF-IDF
# ---------------------------------------------------------------------------
def reto12_tfidf_documentos(carpeta="data/documentos"):
    """
    Objetivo:
        Leer todos los .txt de data/documentos (20 archivos), vectorizar
        con TfidfVectorizer y devolver (X, vectorizer, nombres_archivos,
        textos).
    Restricciones:
        - Usar pathlib.Path.glob("*.txt"), ordenar los nombres para que el
          orden sea reproducible.
        - Mantener el orden entre nombres_archivos, textos y las filas de X.
        - Pasar stop_words=stopwords.words("spanish") al TfidfVectorizer
          (reutiliza el concepto de E2: sin esto, palabras como "de"/"la"
          meten ruido en la similitud entre documentos).
    Resultado esperado:
        X.shape -> (20, N). print(len(vectorizer.get_feature_names_out()))
        para ver el tamaño del vocabulario del corpus completo.
    """
    rutas = sorted(Path(carpeta).glob("*.txt"))
    textos = [p.read_text(encoding="utf-8") for p in rutas]
    nombres = [p.name for p in rutas]
    # Sin quitar stopwords, palabras como "de"/"la"/"es" (presentes en casi
    # todos los documentos) meten ruido en la similitud -- por eso se
    # reutiliza el concepto de E2 acá.
    vectorizer = TfidfVectorizer(stop_words=stopwords.words("spanish"))
    X = vectorizer.fit_transform(textos)
    return X, vectorizer, nombres, textos


# ---------------------------------------------------------------------------
# RETO 13 -- Similitud entre documentos + ranking del más parecido a doc01
# ---------------------------------------------------------------------------
def reto13_similitud(X, nombres):
    """
    Objetivo:
        Calcular cosine_similarity(X) (matriz 20x20) e imprimir, para
        "doc01.txt", el ranking de los 5 documentos más parecidos a él
        (excluyéndolo a sí mismo).
    Restricciones:
        - cosine_similarity de sklearn.metrics.pairwise.
        - Ordenar de mayor a menor similitud.
    Resultado esperado:
        doc01.txt (python...) más parecido a doc02.txt y doc20.txt (ambos
        hablan de Python), no a los de fútbol/ajedrez/comida.
    """
    sim = cosine_similarity(X)
    idx_doc01 = nombres.index("doc01.txt")
    similitudes = [
        (nombres[i], score) for i, score in enumerate(sim[idx_doc01]) if i != idx_doc01
    ]
    similitudes.sort(key=lambda par: par[1], reverse=True)
    print("Documentos más parecidos a doc01.txt:")
    for nombre, score in similitudes[:5]:
        print(f"  {nombre}  {score:.2f}")
    return similitudes[:5]


if __name__ == "__main__":
    demo()
    print("\n--- Retos ---")
    X, vectorizer, nombres, textos = reto12_tfidf_documentos()
    print("Tamaño vocabulario:", len(vectorizer.get_feature_names_out()))
    reto13_similitud(X, nombres)
