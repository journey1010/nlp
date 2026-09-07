"""
Solución de referencia -- 05_sentimientos.py (E3)
SOLO para el docente. No repartir a los alumnos.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def reto8_vectorizar(ruta_csv="data/opiniones.csv"):
    df = pd.read_csv(ruta_csv)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["texto"])
    y = df["sentimiento"]
    return X, y, vectorizer


def reto9_entrenar(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    modelo = MultinomialNB()
    modelo.fit(X_train, y_train)
    return modelo, X_test, y_test


def reto10_evaluar(modelo, X_test, y_test):
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))


def reto11_predictor(modelo, vectorizer):
    while True:
        frase = input("> ")
        if frase.strip().lower() == "salir":
            break
        vector = vectorizer.transform([frase])
        print("Predicción:", modelo.predict(vector)[0])


if __name__ == "__main__":
    X, y, vectorizer = reto8_vectorizar()
    modelo, X_test, y_test = reto9_entrenar(X, y)
    reto10_evaluar(modelo, X_test, y_test)
    reto11_predictor(modelo, vectorizer)
