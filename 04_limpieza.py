"""
E2 -- Limpieza de texto (1:20-2:10)

Conceptos de esta hora (explicar sobre la marcha, no antes):
    - stopwords != "palabras inútiles". Depende de la tarea: "no" es
      stopword para buscar temas, pero es CLAVE para sentimiento
      ("no me gustó" pierde su significado si se elimina "no").
    - stemming = recorta la palabra con reglas fijas -> puede generar
      raíces que no son palabras reales ("corriendo" -> "corr").
    - lematización = devuelve la forma base real de la palabra (lema),
      lingüísticamente válida ("corriendo" -> "correr").

Pipeline de este archivo:

    texto -> lowercase -> quitar URLs/puntuación -> tokenizar -> stopwords
          -> stemming/lematización -> texto limpio
"""

import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)


# ---------------------------------------------------------------------------
def demo():
    texto = "Visita https://www.nltk.org/ AHORA!!! Es GENIAL, de verdad."
    print("Original:", texto)
    print("Tokens sin limpiar:", word_tokenize(texto, language="spanish"))
    print(
        "-> nota las mayúsculas, la URL completa como 'palabra', y los "
        "signos ¡!!! pegados al texto."
    )


# ---------------------------------------------------------------------------
# Quitar URLs y puntuación
# ---------------------------------------------------------------------------
def quitar_ruido(texto):
    texto = texto.lower()
    texto = re.sub(r"https?://\S+|www\.\S+", "", texto)
    texto = re.sub(r"[^\w\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


# ---------------------------------------------------------------------------
# Tokenizar y quitar stopwords
# ---------------------------------------------------------------------------
def quitar_stopwords(texto_limpio):
    stop_es = set(stopwords.words("spanish"))
    tokens = word_tokenize(texto_limpio, language="spanish")
    return [t for t in tokens if t.lower() not in stop_es]


# ---------------------------------------------------------------------------
# Stemming vs lematización, lado a lado [00_lemantizacion_view]
# ---------------------------------------------------------------------------
def stemming_lematizacion(tokens):
    stemmer = SnowballStemmer("spanish")
    lemmatizer = WordNetLemmatizer()
    print(f"{'original':<15}{'stem':<15}{'lema':<15}")
    filas = []
    for token in tokens:
        stem = stemmer.stem(token)
        lema = lemmatizer.lemmatize(token)
        print(f"{token:<15}{stem:<15}{lema:<15}")
        filas.append((token, stem, lema))
    return filas


def pipeline_limpieza(texto):
    texto_limpio = quitar_ruido(texto)
    tokens = quitar_stopwords(texto_limpio)
    stemmer = SnowballStemmer("spanish")
    return [stemmer.stem(t) for t in tokens]

if __name__ == "__main__":
    texto = open("data/corpus.txt", encoding="utf-8").read()
    limpio = quitar_ruido(texto)
    tokens = quitar_stopwords(limpio)
    stemming_lematizacion(tokens[:15])
    print(pipeline_limpieza("Visita https://x.com AHORA!!! Es GENIAL"))
