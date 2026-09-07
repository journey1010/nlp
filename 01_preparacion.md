# De texto a inteligencia: construyendo aplicaciones NLP con Python

Taller práctico de 6 horas · NLP + NLTK + scikit-learn

## Objetivo

Minimizar teoría pasiva. El alumno escribe código todo el taller; el docente
explica el concepto justo antes de que se necesite, no antes. Cada ejercicio
produce un resultado visible en consola (números, tablas, predicciones).

Mecánica de cada bloque: **problema → alumno implementa → docente explica
concepto necesario → se observa el resultado → se mejora.** Nunca al revés.

## Pipeline central (se repite en todo el taller)

```
Texto
 ↓
Tokenización
 ↓
Limpieza / normalización
 ↓
Representación numérica
 ↓
Machine Learning
 ↓
Predicción / similitud
```

## Mensaje central

**NLTK no es "todo NLP".** NLTK cubre procesamiento lingüístico:
tokenización, stopwords, stemming, POS tagging, corpus, herramientas
lingüísticas. **scikit-learn** lleva ese texto ya procesado hacia Machine
Learning: representación BoW/TF-IDF, clasificación, métricas, similitud.
El taller conecta ambos mundos.

```
NLTK                          scikit-learn
├ tokenización                ├ representación BoW/TF-IDF
├ stopwords                   ├ clasificación
├ stemming                    ├ métricas
├ POS tagging                 └ similitud
├ corpus
└ herramientas lingüísticas
```

## Cronograma (6h)

| Hora        | Bloque                                          |
|-------------|--------------------------------------------------|
| 0:00–0:30   | Intro + setup: NLP, corpus, tokens, NLTK          |
| 0:30–1:20   | E1 Analizador de texto: tokenización + frecuencia |
| 1:20–2:10   | E2 Limpieza: stopwords + stemming + lematización  |
| 2:10–2:25   | Descanso                                          |
| 2:25–3:15   | E3 Sentimientos: features + clasificación         |
| 3:15–4:05   | E4 Clasificación de textos: Naive Bayes           |
| 4:05–4:20   | Descanso                                          |
| 4:20–5:10   | E5 Similitud: BoW + TF-IDF + cosine similarity    |
| 5:10–6:00   | Proyecto final: mini buscador NLP                 |

## Archivos del taller

```
01_prevaracion.md          este archivo (guía + setup)
requirements.txt           dependencias
02_datos.py                genera TODA la data usada en el taller
03_analizador.py           E1 — retos para el alumno
04_limpieza.py             E2 — retos para el alumno
05_sentimientos.py         E3 — retos para el alumno
06_clasificacion.py        E4 — retos para el alumno
07_similitud_tfidf.py      E5 — retos para el alumno
08_proyecto_buscador.py    Proyecto final — retos para el alumno
solucionario/              referencia SOLO para el docente (no repartir)
```

Cada archivo de ejercicio trae, en este orden:
1. Un **demo mínimo** ya funcionando (para que el alumno vea el patrón antes
   de tocarlo).
2. Bloques `# RETO N` con **objetivo + restricciones + resultado
   esperado** en el docstring y `# TODO` donde el alumno escribe código.
   Nunca se entrega la solución completa ahí.

El `solucionario/` tiene la implementación completa de cada reto — es la
referencia del docente para guiar o destrabar, no para proyectar.

## Setup (0:00–0:30)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python 02_datos.py               # genera ./data con todo el corpus del taller
```

Descarga de recursos NLTK (correr una vez, dentro de Python):

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")
```

Verificación rápida (resultado visible, primer "wow" del taller):

```python
import nltk
from nltk.tokenize import word_tokenize

texto = "El PLN convierte lenguaje humano en datos que una máquina procesa."
print(word_tokenize(texto))
```

Conceptos de esta sección (breve, ~10 min, el resto es hacer el setup y
correr `02_datos.py` en vivo):

- **NLP (Procesamiento de Lenguaje Natural):** convertir lenguaje humano en
  algo que un algoritmo pueda procesar matemáticamente.
- **Corpus:** conjunto de textos que usamos como materia prima.
- **Token:** unidad mínima de procesamiento (palabra, signo, número).
- **NLTK:** caja de herramientas para el lado lingüístico de ese proceso
  (no para el ML — eso lo hace scikit-learn más adelante).

## Datos del taller

Todo el corpus se genera con `02_datos.py` (sin depender de internet ni de
datasets externos). Produce:

- `data/corpus.txt` — texto crudo con URLs y puntuación real, para E1/E2.
- `data/opiniones.csv` — columnas `texto,sentimiento` (positivo/negativo), E3.
- `data/noticias.csv` — columnas `texto,categoria` (deportes/política/
  tecnología), E4.
- `data/documentos/doc01.txt` … `doc20.txt` — 20 documentos cortos, E5 y
  proyecto final.

Correr de nuevo `02_datos.py` siempre reproduce la misma data (semilla fija),
así todos los alumnos trabajan sobre los mismos números.
