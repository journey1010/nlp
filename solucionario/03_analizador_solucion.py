"""
Solución de referencia -- 03_analizador.py (E1)
SOLO para el docente. No repartir a los alumnos.
"""

from collections import Counter

import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


def reto1_tokenizar(ruta_corpus="data/corpus.txt"):
    texto = open(ruta_corpus, encoding="utf-8").read()
    tokens = word_tokenize(texto, language="spanish")
    return tokens


def reto2_frecuencias(tokens):
    tokens_lower = [t.lower() for t in tokens]
    counter = Counter(tokens_lower)
    total_tokens = len(tokens_lower)
    palabras_unicas = len(counter)
    return total_tokens, palabras_unicas, counter


def reto3_top10(counter):
    top10 = counter.most_common(10)
    for palabra, frecuencia in top10:
        print(f"{palabra} -> {frecuencia}")
    return top10


if __name__ == "__main__":
    tokens = reto1_tokenizar()
    total, unicas, counter = reto2_frecuencias(tokens)
    print(f"Total tokens: {total} | Palabras únicas: {unicas}")
    reto3_top10(counter)
