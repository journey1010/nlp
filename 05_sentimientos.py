"""
E3 -- Sentimientos: features + clasificación (2:25-3:15)

Pregunta que abre el bloque: ¿cómo hace una máquina para saber si un texto
es positivo o negativo, si solo entiende números?

Pipeline de este archivo:

    texto -> preprocesamiento -> features (BoW) -> modelo -> predicción

Concepto clave: representación numérica. "me gusta python" no significa
nada para un modelo hasta que se convierte en un vector, ej:
    ["me", "gusta", "python", "no", "malo"]
    "me gusta python"  -> [1, 1, 1, 0, 0]
Eso es Bag of Words (BoW): un vector con la cuenta de cada palabra del
vocabulario presente en el documento.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


# ---------------------------------------------------------------------------
# DEMO -- ver físicamente texto -> matriz, antes de entrenar nada
# ---------------------------------------------------------------------------
def demo():
    textos = ["me gusta python", "no me gusta el frio", "python es genial"]
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(textos)

    print("Vocabulario:", vectorizer.get_feature_names_out())
    print("Matriz BoW (filas=documentos, columnas=vocabulario):")
    print(X.toarray())


# ---------------------------------------------------------------------------
# 🧩 RETO 8 -- Cargar opiniones.csv y vectorizar con BoW
# ---------------------------------------------------------------------------
def reto8_vectorizar(ruta_csv="data/opiniones.csv"):
    """
    Objetivo:
        Cargar data/opiniones.csv (columnas texto, sentimiento) con pandas,
        vectorizar la columna "texto" con CountVectorizer y devolver
        (X, y, vectorizer).
    Restricciones:
        - Usar pd.read_csv.
        - y = columna "sentimiento" tal cual (strings "positivo"/"negativo").
        - No dividir en train/test todavía, eso es el reto 9.
    Resultado esperado:
        X.shape -> (24, N) donde N es el tamaño del vocabulario.
        print(vectorizer.get_feature_names_out()[:10]) para ver palabras.
    """
    # TODO: df = pd.read_csv(ruta_csv)
    # TODO: vectorizer = CountVectorizer()
    # TODO: X = vectorizer.fit_transform(df["texto"])
    # TODO: y = df["sentimiento"]
    # TODO: return X, y, vectorizer
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 9 -- Entrenar Naive Bayes y predecir
# ---------------------------------------------------------------------------
def reto9_entrenar(X, y):
    """
    Objetivo:
        Dividir X, y en train/test (80/20, random_state=42, stratify=y),
        entrenar un MultinomialNB y devolver (modelo, X_test, y_test).
    Restricciones:
        - Usar train_test_split con random_state=42 y stratify=y
          (reproducible y con las dos clases balanceadas en el test).
        - MultinomialNB, no otro clasificador (es el estándar para BoW).
    Resultado esperado:
        Un modelo entrenado. modelo.predict(X_test) debe correr sin error.
        Nota: con un dataset chico (60 filas) el accuracy no va a ser
        perfecto -- es intencional, buen punto para hablar de cuánta data
        necesita realmente un modelo de ML.
    """
    # TODO: X_train, X_test, y_train, y_test = train_test_split(
    #           X, y, test_size=0.2, random_state=42, stratify=y)
    # TODO: modelo = MultinomialNB()
    # TODO: modelo.fit(X_train, y_train)
    # TODO: return modelo, X_test, y_test
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 10 -- Evaluar: accuracy, precision, recall, F1
# ---------------------------------------------------------------------------
def reto10_evaluar(modelo, X_test, y_test):
    """
    Objetivo:
        Imprimir classification_report(y_test, y_pred). Conectar el
        vocabulario NLP <-> métricas de ML: aquí es donde se ve si el
        preprocesamiento (E2) realmente ayudó al modelo o no.
    Restricciones:
        - Usar sklearn.metrics.classification_report.
    Resultado esperado:
        Tabla con precision/recall/f1-score por clase (positivo/negativo)
        y accuracy general.
    """
    # TODO: y_pred = modelo.predict(X_test)
    # TODO: print(classification_report(y_test, y_pred))
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 🧩 RETO 11 -- Predictor interactivo de sentimiento
# ---------------------------------------------------------------------------
def reto11_predictor(modelo, vectorizer):
    """
    Objetivo:
        Loop con input() que pida una frase al usuario, la transforme con
        vectorizer.transform([frase]) (¡no fit_transform!, el vocabulario
        ya está fijado) y muestre la predicción del modelo.
    Restricciones:
        - vectorizer.transform, no fit_transform (fit ya se hizo en E3/R8).
        - Salir del loop si el usuario escribe "salir".
    Resultado esperado:
        > el servicio fue pesimo
        Predicción: negativo
        > salir
    """
    # TODO: while True:
    #           frase = input("> ")
    #           if frase == "salir": break
    #           vector = vectorizer.transform([frase])
    #           print("Predicción:", modelo.predict(vector)[0])
    raise NotImplementedError


if __name__ == "__main__":
    demo()
    print("\n--- Retos ---")
    # X, y, vectorizer = reto8_vectorizar()
    # modelo, X_test, y_test = reto9_entrenar(X, y)
    # reto10_evaluar(modelo, X_test, y_test)
    # reto11_predictor(modelo, vectorizer)
