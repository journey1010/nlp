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
# DEMO -- ver el problema antes de resolverlo
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
# 🧩 RETO 4 -- Quitar URLs y puntuación
# ---------------------------------------------------------------------------
def reto4_quitar_ruido(texto):
    """
    Objetivo:
        Devolver el texto en minúsculas, sin URLs y sin signos de
        puntuación (dejar solo letras, números y espacios).
    Restricciones:
        - Usar re.sub para URLs (patrón tipo http... o www...).
        - Usar re.sub o str.translate para quitar puntuación.
        - El orden importa: primero URLs, luego puntuación.
    Resultado esperado:
        Mismo texto, en minúsculas, sin "https://..." y sin "!", ".", ",".
        Ej: "visita  ahora es genial de verdad"
    """
    # TODO: texto = texto.lower()
    # TODO: quitar URLs con re.sub(r"https?://\S+|www\.\S+", "", texto)
    # TODO: quitar puntuación con re.sub(r"[^\w\s]", "", texto)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 5 -- Tokenizar y quitar stopwords
# ---------------------------------------------------------------------------
def reto5_quitar_stopwords(texto_limpio):
    """
    Objetivo:
        Tokenizar el texto (ya limpio del reto 4) y quitar las stopwords
        en español (nltk.corpus.stopwords.words("spanish")).
    Restricciones:
        - Usar word_tokenize.
        - Comparar en minúsculas.
    Resultado esperado:
        Lista de tokens sin "de", "la", "el", "es", etc. Discutir en grupo:
        ¿qué pasaría si el texto fuera de sentimiento y tuviera "no"?
    """
    # TODO: stop_es = set(stopwords.words("spanish"))
    # TODO: tokens = word_tokenize(texto_limpio, language="spanish")
    # TODO: filtrar tokens que no estén en stop_es
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 6 -- Stemming vs lematización, lado a lado
# ---------------------------------------------------------------------------
def reto6_stemming_lematizacion(tokens):
    """
    Objetivo:
        Para la misma lista de tokens, generar dos listas: una con
        SnowballStemmer("spanish") y otra con WordNetLemmatizer().
        Imprimir una tabla comparando palabra original / stem / lema.
    Restricciones:
        - Un stemmer y un lemmatizer por lista, no mezclar.
        - Nota: WordNetLemmatizer está pensado para inglés -- en español el
          resultado a veces no cambia nada. Es intencional: sirve para
          discutir la limitación en el grupo.
    Resultado esperado:
        Tabla tipo:
            original       stem           lema
            corriendo      corr           corriendo
            jugadores      jugador        jugadores
    """
    # TODO: stemmer = SnowballStemmer("spanish")
    # TODO: lemmatizer = WordNetLemmatizer()
    # TODO: para cada token, imprimir original, stemmer.stem(token),
    #       lemmatizer.lemmatize(token)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 7 -- Armar el pipeline completo de limpieza en una función
# ---------------------------------------------------------------------------
def reto7_pipeline_limpieza(texto):
    """
    Objetivo:
        Encadenar reto4 -> reto5 -> stemming, en UNA sola función que
        reciba texto crudo y devuelva la lista final de stems limpios.
        Esta función se va a reutilizar en E3/E4/E5 -- que quede genérica.
    Restricciones:
        - No repetir código: llamar a las funciones ya escritas arriba.
    Resultado esperado:
        limpiar("Visita https://x.com AHORA!!! Es GENIAL")
        -> ["visit", "genial"]  (aprox., depende del stemmer)
    """
    # TODO: texto_limpio = reto4_quitar_ruido(texto)
    # TODO: tokens = reto5_quitar_stopwords(texto_limpio)
    # TODO: stemmer = SnowballStemmer("spanish")
    # TODO: return [stemmer.stem(t) for t in tokens]
    raise NotImplementedError


if __name__ == "__main__":
    demo()
    print("\n--- Retos ---")
    # texto = open("data/corpus.txt", encoding="utf-8").read()
    # limpio = reto4_quitar_ruido(texto)
    # tokens = reto5_quitar_stopwords(limpio)
    # reto6_stemming_lematizacion(tokens[:15])
    # print(reto7_pipeline_limpieza("Visita https://x.com AHORA!!! Es GENIAL"))
