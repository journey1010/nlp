"""
02_datos.py
Genera TODA la data que se usa en el taller. Correr una sola vez al inicio
(0:00-0:30, junto con el setup):

    python 02_datos.py

Usa una semilla fija -> todos los alumnos obtienen exactamente la misma
data, aunque el texto se arma con plantillas + aleatoriedad (no hay
archivos "hardcodeados" gigantes, así se ve cómo se gesta el dataset).

Genera:
    data/corpus.txt              texto crudo (URLs, mayúsculas, puntuación)
    data/opiniones.csv           texto,sentimiento
    data/noticias.csv            texto,categoria
    data/documentos/docNN.txt    20 documentos cortos para similitud/buscador
"""

import csv
import random
from pathlib import Path

random.seed(42)

DATA_DIR = Path(__file__).parent / "data"
DOCS_DIR = DATA_DIR / "documentos"


# ---------------------------------------------------------------------------
# 1. corpus.txt -- para E1 (tokenización/frecuencia) y E2 (limpieza)
# ---------------------------------------------------------------------------
def generar_corpus_txt():
    parrafos = [
        "El Procesamiento de Lenguaje Natural (NLP) permite que las "
        "computadoras entiendan texto escrito en lenguaje humano. Visita "
        "https://www.nltk.org para más info!!! También revisa "
        "http://scikit-learn.org, son las dos librerías centrales de este "
        "taller.",
        "Python se usa muchísimo en Ciencia de Datos, en Machine Learning y "
        "en NLP. Con Python, con NLTK y con scikit-learn se puede construir "
        "un clasificador de texto en pocas líneas de código... ¿no es "
        "increíble?",
        "Los tokens son las unidades mínimas de un texto: palabras, signos "
        "de puntuación, números. Tokenizar un texto es el primer paso de "
        "CUALQUIER pipeline de NLP, sin excepción.",
        "Un corpus es una colección de documentos. Puede ser un conjunto de "
        "tweets, de noticias, de reseñas de productos, de correos, o incluso "
        "de libros completos. Todo depende del problema que se quiera "
        "resolver.",
        "La limpieza de texto (quitar URLs, quitar signos, pasar a "
        "minúsculas) reduce el ruido antes de vectorizar. Sin limpieza, el "
        "modelo aprende cosas irrelevantes, como que 'Python.' y 'python' "
        "son palabras distintas.",
        "El objetivo final de este taller es construir un mini buscador "
        "inteligente: dado un texto de consulta, el sistema encuentra los "
        "documentos más parecidos usando TF-IDF y similitud de coseno.",
    ]
    random.shuffle(parrafos)
    contenido = "\n\n".join(parrafos)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    (DATA_DIR / "corpus.txt").write_text(contenido, encoding="utf-8")
    print(f"[ok] data/corpus.txt ({len(contenido)} caracteres)")


# ---------------------------------------------------------------------------
# 2. opiniones.csv -- para E3 (sentimiento)
# ---------------------------------------------------------------------------
POSITIVAS = [
    "me encantó el producto, funciona excelente",
    "el servicio fue increíble, muy recomendable",
    "excelente calidad, superó mis expectativas",
    "estoy feliz con la compra, todo perfecto",
    "el curso fue genial, aprendí muchísimo",
    "buenísima atención, volvería a comprar sin dudarlo",
    "el celular llegó rápido y funciona de maravilla",
    "gran experiencia, el equipo es muy profesional",
    "me gustó mucho la película, la actuación fue brillante",
    "la comida estaba deliciosa, el lugar es hermoso",
    "el software es rápido y fácil de usar, lo amo",
    "excelente soporte técnico, resolvieron todo al instante",
    "quedé encantado con el resultado, superó lo esperado",
    "muy buena experiencia de compra, todo llegó a tiempo",
    "el equipo fue amable y resolvió mi duda rapidísimo",
    "hermoso diseño, funciona excelente y se ve genial",
    "recomiendo totalmente este lugar, todo fue perfecto",
    "el hotel estaba impecable, la atención fue excelente",
    "aprendí un montón con este curso, muy bien explicado",
    "el envío llegó antes de lo previsto, todo perfecto",
    "la app es súper intuitiva y funciona sin problemas",
    "gran calidad de producto, definitivamente volveré a comprar",
    "el restaurante tiene un ambiente hermoso y la comida rica",
    "excelente relación calidad precio, muy satisfecho con la compra",
    "todo excelente, quedé muy contento con el servicio",
    "buenísimo el producto, lo recomiendo sin dudarlo",
    "me fascinó la calidad, es justo lo que esperaba",
    "atención maravillosa, todo el personal fue muy amable",
    "compra perfecta, el producto superó mis expectativas",
    "servicio excelente, definitivamente recomiendo esta tienda",
]
NEGATIVAS = [
    "el producto llegó dañado, muy mala experiencia",
    "pésimo servicio, no lo recomiendo para nada",
    "una decepción total, no cumplió lo prometido",
    "estoy furioso con la compra, todo salió mal",
    "el curso fue aburrido, no aprendí nada útil",
    "muy mala atención, no vuelvo a comprar ahí",
    "el celular llegó tarde y no funciona bien",
    "terrible experiencia, el personal fue grosero",
    "no me gustó la película, la actuación fue pésima",
    "la comida estaba fría y el lugar sucio",
    "el software es lento y difícil de usar, lo odio",
    "pésimo soporte técnico, nunca resolvieron mi problema",
    "quedé decepcionado con el resultado, no cumplió nada",
    "muy mala experiencia de compra, todo llegó tarde",
    "el equipo fue grosero y no resolvió mi duda",
    "feo diseño, no funciona bien y se ve horrible",
    "no recomiendo para nada este lugar, todo fue un desastre",
    "el hotel estaba sucio, la atención fue pésima",
    "no aprendí nada con este curso, muy mal explicado",
    "el envío llegó tarde y con el paquete roto",
    "la app es confusa y falla todo el tiempo",
    "mala calidad de producto, jamás volveré a comprar",
    "el restaurante tiene un ambiente feo y la comida mala",
    "pésima relación calidad precio, nada satisfecho con la compra",
    "todo pésimo, quedé muy molesto con el servicio",
    "malísimo el producto, no lo recomiendo para nada",
    "me decepcionó la calidad, no es lo que esperaba",
    "atención horrible, todo el personal fue muy grosero",
    "compra pésima, el producto no cumplió las expectativas",
    "servicio terrible, definitivamente no recomiendo esta tienda",
]


def generar_opiniones_csv():
    filas = []
    for texto in POSITIVAS:
        filas.append((texto, "positivo"))
    for texto in NEGATIVAS:
        filas.append((texto, "negativo"))
    random.shuffle(filas)

    ruta = DATA_DIR / "opiniones.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["texto", "sentimiento"])
        writer.writerows(filas)
    print(f"[ok] data/opiniones.csv ({len(filas)} filas)")


# ---------------------------------------------------------------------------
# 3. noticias.csv -- para E4 (clasificación multi-clase)
# ---------------------------------------------------------------------------
DEPORTES = [
    "el equipo local ganó el partido con un gol en el último minuto",
    "el tenista clasificó a la final del torneo tras un partido reñido",
    "la selección se prepara para el mundial con nuevos jugadores",
    "el maratón contó con miles de corredores en la capital",
    "el técnico anunció la alineación titular para la final",
    "el boxeador defendió su título con un nocaut en el tercer round",
    "el equipo de básquet remontó veinte puntos en el último cuarto",
    "el ciclista ganó la etapa de montaña en el último kilómetro",
    "el árbitro sancionó un penal decisivo en el segundo tiempo",
    "el club fichó a un delantero para reforzar el ataque",
]
POLITICA = [
    "el congreso debatió la nueva ley de presupuesto público",
    "el presidente anunció reformas al sistema de salud",
    "los candidatos presentaron sus propuestas para las elecciones",
    "el ministro respondió a las críticas de la oposición",
    "el senado aprobó el proyecto de ley tras una larga sesión",
    "el gobierno firmó un acuerdo internacional de comercio",
    "la alcaldesa presentó el plan de obras para la ciudad",
    "los partidos políticos iniciaron la campaña electoral",
    "el tribunal constitucional evaluó la reforma tributaria",
    "el parlamento discutió el aumento del salario mínimo",
]
TECNOLOGIA = [
    "la empresa lanzó un nuevo modelo de inteligencia artificial",
    "el celular incorpora una cámara con mayor resolución",
    "los desarrolladores presentaron una app para aprender idiomas",
    "la startup recaudó fondos para escalar su plataforma",
    "el nuevo procesador promete el doble de rendimiento",
    "la actualización del software corrige varias vulnerabilidades",
    "el laboratorio presentó un robot capaz de aprender tareas nuevas",
    "la compañía anunció un chip más eficiente en consumo de energía",
    "el algoritmo de recomendación mejora la experiencia del usuario",
    "la plataforma en la nube añadió soporte para nuevos lenguajes",
]


def generar_noticias_csv():
    filas = []
    for texto in DEPORTES:
        filas.append((texto, "deportes"))
    for texto in POLITICA:
        filas.append((texto, "politica"))
    for texto in TECNOLOGIA:
        filas.append((texto, "tecnologia"))
    random.shuffle(filas)

    ruta = DATA_DIR / "noticias.csv"
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["texto", "categoria"])
        writer.writerows(filas)
    print(f"[ok] data/noticias.csv ({len(filas)} filas)")


# ---------------------------------------------------------------------------
# 4. documentos/docNN.txt -- para E5 (similitud) y proyecto final (buscador)
# ---------------------------------------------------------------------------
DOCUMENTOS = [
    "Python es un lenguaje de programación usado en ciencia de datos.",
    "Python tiene aplicaciones en desarrollo web, scripts y automatización.",
    "El fútbol es el deporte más popular del mundo, con miles de hinchas.",
    "Los jugadores de fútbol entrenan todos los días para mejorar su nivel.",
    "El aprendizaje automático permite que modelos aprendan de los datos.",
    "Las redes neuronales son un tipo de modelo de aprendizaje automático.",
    "El baloncesto se juega con dos equipos de cinco jugadores en cancha.",
    "El básquet profesional tiene ligas en todo el mundo, como la NBA.",
    "NLTK es una librería de Python para procesamiento de lenguaje natural.",
    "scikit-learn es una librería de Python para machine learning clásico.",
    "La inteligencia artificial busca simular capacidades humanas en máquinas.",
    "El ajedrez es un juego de estrategia jugado por dos personas en un tablero.",
    "Los grandes maestros de ajedrez estudian aperturas y finales de partida.",
    "La receta de pizza lleva harina, agua, levadura, tomate y queso.",
    "La pasta italiana se cocina en agua hirviendo con sal antes de servirla.",
    "El cambio climático afecta los ecosistemas y el nivel del mar.",
    "Las energías renovables como la solar y la eólica reducen las emisiones.",
    "El sistema solar tiene ocho planetas que orbitan alrededor del sol.",
    "Los astronautas viajan al espacio en cohetes desarrollados por agencias.",
    "La programación en Python se usa también para construir modelos de NLP.",
]


def generar_documentos():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for i, texto in enumerate(DOCUMENTOS, start=1):
        ruta = DOCS_DIR / f"doc{i:02d}.txt"
        ruta.write_text(texto, encoding="utf-8")
    print(f"[ok] data/documentos/ ({len(DOCUMENTOS)} archivos)")


if __name__ == "__main__":
    generar_corpus_txt()
    generar_opiniones_csv()
    generar_noticias_csv()
    generar_documentos()
    print("\nListo. Revisa la carpeta ./data")
