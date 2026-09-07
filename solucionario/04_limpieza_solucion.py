"""
Solución de referencia -- 04_limpieza.py (E2)
SOLO para el docente. No repartir a los alumnos.
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


def reto4_quitar_ruido(texto):
    texto = texto.lower()
    texto = re.sub(r"https?://\S+|www\.\S+", "", texto)
    texto = re.sub(r"[^\w\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


def reto5_quitar_stopwords(texto_limpio):
    stop_es = set(stopwords.words("spanish"))
    tokens = word_tokenize(texto_limpio, language="spanish")
    return [t for t in tokens if t.lower() not in stop_es]


def reto6_stemming_lematizacion(tokens):
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


def reto7_pipeline_limpieza(texto):
    texto_limpio = reto4_quitar_ruido(texto)
    tokens = reto5_quitar_stopwords(texto_limpio)
    stemmer = SnowballStemmer("spanish")
    return [stemmer.stem(t) for t in tokens]


if __name__ == "__main__":
    texto = open("data/corpus.txt", encoding="utf-8").read()
    limpio = reto4_quitar_ruido(texto)
    tokens = reto5_quitar_stopwords(limpio)
    reto6_stemming_lematizacion(tokens[:15])
    print(reto7_pipeline_limpieza("Visita https://x.com AHORA!!! Es GENIAL"))
