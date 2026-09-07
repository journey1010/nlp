"""
Solución de referencia -- 06_clasificacion.py (E4)
SOLO para el docente. No repartir a los alumnos.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def reto_vectorizar_noticias(ruta_csv="data/noticias.csv"):
    df = pd.read_csv(ruta_csv)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["texto"])
    y = df["categoria"]
    return X, y, vectorizer


def reto_entrenar_evaluar(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    modelo = MultinomialNB()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))
    return modelo


def reto_predictor_categoria(modelo, vectorizer):
    while True:
        texto = input("> ")
        if texto.strip().lower() == "salir":
            break
        vector = vectorizer.transform([texto])
        print("Categoría:", modelo.predict(vector)[0])


if __name__ == "__main__":
    X, y, vectorizer = reto_vectorizar_noticias()
    modelo = reto_entrenar_evaluar(X, y)
    reto_predictor_categoria(modelo, vectorizer)
