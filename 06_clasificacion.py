"""
E4 -- Clasificación de textos: deportes / política / tecnología (3:15-4:05)

Mismo pipeline que E3 pero con 3 clases en vez de 2:

    texto -> BoW -> Naive Bayes -> categoría

El resultado final de este bloque es una mini IA clasificadora que
funciona con input() en vivo -- el "producto terminado" más tangible del
taller hasta ahora.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# ---------------------------------------------------------------------------
# DEMO -- confirmar que noticias.csv tiene 3 categorías balanceadas
# ---------------------------------------------------------------------------
def demo():
    df = pd.read_csv("data/noticias.csv")
    print(df["categoria"].value_counts())
    print(df.head())


# ---------------------------------------------------------------------------
# 🧩 RETO 9b -- Vectorizar noticias.csv (3 clases)
# ---------------------------------------------------------------------------
def reto_vectorizar_noticias(ruta_csv="data/noticias.csv"):
    """
    Objetivo:
        Igual que E3/reto8 pero con data/noticias.csv (columnas texto,
        categoria). Devolver (X, y, vectorizer).
    Restricciones:
        - CountVectorizer, sin parámetros extra por ahora.
    Resultado esperado:
        y.unique() -> ['deportes' 'politica' 'tecnologia'] (orden puede
        variar).
    """
    # TODO: reutilizar el mismo patrón de 05_sentimientos.reto8_vectorizar
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 9c -- Entrenar y evaluar el clasificador de 3 clases
# ---------------------------------------------------------------------------
def reto_entrenar_evaluar(X, y):
    """
    Objetivo:
        train_test_split (80/20, random_state=42, stratify=y) ->
        MultinomialNB -> fit -> classification_report. Todo en una función.
    Restricciones:
        - random_state=42, stratify=y (dataset chico: con poca data, la
          evaluación es inestable -- material de discusión en clase).
    Resultado esperado:
        Reporte con las 3 categorías, precision/recall/f1 por clase.
    """
    # TODO: dividir, entrenar MultinomialNB, imprimir classification_report
    # TODO: return el modelo entrenado (se necesita en el siguiente reto)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 11b -- Predictor interactivo de categoría
# ---------------------------------------------------------------------------
def reto_predictor_categoria(modelo, vectorizer):
    """
    Objetivo:
        input() -> vectorizer.transform([texto]) -> modelo.predict(...) ->
        imprimir la categoría predicha. Salir con "salir".
    Restricciones:
        - vectorizer.transform, nunca fit_transform aquí.
    Resultado esperado:
        > el gobierno aprobó una nueva ley
        Categoría: politica
        > salir
    Este es el "mini IA clasificadora" que cierra el bloque E4.
    """
    # TODO: loop input() -> transform -> predict -> print
    raise NotImplementedError


if __name__ == "__main__":
    demo()
    print("\n--- Retos ---")
    # X, y, vectorizer = reto_vectorizar_noticias()
    # modelo = reto_entrenar_evaluar(X, y)
    # reto_predictor_categoria(modelo, vectorizer)
