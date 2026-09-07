"""
Pipeline:
    texto -> word_tokenize -> tokens -> Counter
"""

from collections import Counter

import nltk
from nltk.tokenize import word_tokenize

## punkt es un dataset/modelo para tokenizar [00_view_tokens]
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


def demo():
    texto = "El PLN convierte lenguaje humano en datos que una máquina procesa."
    tokens = word_tokenize(texto, language="spanish")
    print("Texto: ", texto)
    print("Tokens:", tokens)
    print("Cantidad de tokens:", len(tokens))
    print(f"\n{'-'*40}\n")

# ---------------------------------------------------------------------------
# Tokenizar el corpus completo
# ---------------------------------------------------------------------------
def reto1_tokenizar(ruta_corpus="data/corpus.txt"):
    texto = open(ruta_corpus, encoding="utf-8").read()
    tokens = word_tokenize(texto, language="spanish")
    return tokens

# ---------------------------------------------------------------------------
# Contar frecuencias y palabras únicas
# ---------------------------------------------------------------------------

def reto2_frecuencias(tokens):
    tokens_lower = [t.lower() for t in tokens]
    counter = Counter(tokens_lower)
    total_tokens = len(tokens_lower)
    palabras_unicas = len(counter)
    return total_tokens, palabras_unicas, counter


# ---------------------------------------------------------------------------
# Top-10 palabras más frecuentes + frecuencia por palabra
# ---------------------------------------------------------------------------
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
