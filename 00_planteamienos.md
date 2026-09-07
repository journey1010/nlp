# Aplicaciones reales del PLN
## 1. Principales tareas del Procesamiento del Lenguaje Natural

### 1.1. Reconocimiento del habla

**¿Qué hace?**
Convierte voz en texto.
**Aplicación real:**
Transcripción automática.

---
### 1.2. Síntesis de voz
**¿Qué hace?**
Convierte texto en voz.
**Aplicación real:**
Lectores, asistentes virtuales y sistemas de accesibilidad.
---

### 1.3. Análisis del lenguaje
**¿Qué hace?**
Identifica características y estructura del texto.
**Aplicación real:**
Clasificación de textos, análisis de sentimientos e identificación de intenciones.
---

### 1.4. Comprensión del lenguaje

**¿Qué hace?**
Determina qué significa o qué intenta expresar un texto.
**Aplicación real:**
Asistentes virtuales y chatbots.
---

### 1.5. Generación de lenguaje natural

**¿Qué hace?**
Genera texto automáticamente.
**Aplicación real:**
Generación de informes, resúmenes y respuestas.
**Ejemplo en Iquitos:**
Generar automáticamente un resumen de expedientes.

---

### 1.6. Traducción automática
**¿Qué hace?**
Traduce texto entre diferentes idiomas.
**Aplicación real:**
Turismo, educación y comunicación.

---

### 1.7. Extracción de información
**¿Qué hace?**
Extrae datos estructurados a partir de textos.
**Aplicación real:**
Automatización documental.
**Ejemplo en Iquitos:**
Extraer nombres, fechas, DNI, montos y números de expediente de documentos.

---

# 2. Ejemplos concretos de aplicaciones del PLN

## 2.1. Municipalidad: clasificación de reclamos

Supongamos que una municipalidad recibe los siguientes reclamos:
> "Hay un enorme hueco en la calle Putumayo frente al mercado."
> "El camión de basura no pasa desde hace tres días."
> "Quiero saber cuánto debo pagar de arbitrios."
> "Hay demasiada basura acumulada en mi barrio."

Un sistema de PLN puede clasificar automáticamente los reclamos:

```text
"Hueco en la calle"       → INFRAESTRUCTURA
"Camión de basura"        → LIMPIEZA PÚBLICA
"Cuánto debo pagar"       → TRIBUTOS
"Basura acumulada"        → LIMPIEZA PÚBLICA
```

También se puede agregar un nivel de prioridad:

```text
Texto
  ↓
Clasificador
  ↓
Categoría + prioridad
  ↓
Área responsable
```

---

## 2.2. Extracción de información de documentos

Una institución puede recibir documentos como:

> "El señor Juan Pérez López, identificado con DNI XXXXXXXX, solicita la apertura del expediente N° 2026-00125, presentado el 5 de septiembre de 2026."

Un sistema de PLN podría extraer automáticamente:

```json
{
  "persona": "Juan Pérez López",
  "dni": "XXXXXXXX",
  "expediente": "2026-00125",
  "fecha": "05/09/2026"
}
```
---

## 2.3. Hospital o clínica: clasificación de consultas

Supongamos que un sistema recibe las siguientes consultas:

> "Tengo fiebre y dolor de cabeza."

> "Quiero saber cuándo atiende pediatría."

> "Necesito sacar una cita."

> "¿Dónde está laboratorio?"

El sistema puede identificar la intención:

```text
"Fiebre y dolor de cabeza" → CONSULTA
"Horario de pediatría"     → INFORMACIÓN
"Sacar una cita"           → CITAS
"Ubicación de laboratorio" → UBICACIÓN
```

Resultado -> **chatbot sencillo**.

---

## 2.4. Monitoreo ambiental

Supongamos que se recopilan noticias, reportes o publicaciones:

> "Se detectó tala ilegal cerca de..."
> "Comunidades reportan contaminación..."
> "Se encontraron peces muertos en..."

PLN puede clasificar:

```text
TALA
CONTAMINACIÓN
PESCA
INCENDIO
```

También puede extraer información geográfica:

```text
Lugar: ...
Provincia: ...
Distrito: ...
```

---

# 3. Dificultades en el Procesamiento del Lenguaje Natural

## 3.1. Ambigüedad

### 3.1.1. Ambigüedad léxica

Una misma palabra puede tener varios significados.

**Ejemplo:**

> "El banco está cerrado."

**"banco"** podría referirse a:

* Una institución financiera.
* Un asiento.

---

### 3.1.2. Ambigüedad referencial

Se presenta cuando es necesario determinar a qué entidad hace referencia una expresión dentro de un texto.

**Ejemplo:**

> "Juan habló con Pedro y él estaba preocupado."

¿Quién estaba preocupado?

* Juan
* Pedro

El sistema debe analizar el contexto para determinar a quién hace referencia **"él"**.

La resolución de este problema incluye fenómenos como las **anáforas** y las **catáforas**.


---

### 3.1.3. Ambigüedad estructural

Una oración puede tener diferentes estructuras sintácticas posibles.

**Ejemplo:**

> "Yo vi al hombre con el telescopio"

La estructura de la oración puede generar diferentes interpretaciones.

Para resolver este tipo de problemas es necesario analizar la estructura sintáctica y semántica de la oración.

---

### 3.1.4. Ambigüedad pragmática

Una oración puede no significar exactamente lo que literalmente expresa.

**Ejemplo:**

> "¡Qué puntual!"

Si una persona llega dos horas tarde y alguien dice "¡Qué puntual!", probablemente se trata de **ironía**.

Para interpretar correctamente el mensaje es necesario considerar el contexto y la intención del hablante.

---

---

## 3.2. Detección de separación entre las palabras

En el lenguaje hablado normalmente no existen pausas claras entre cada palabra.

Por ejemplo, al hablar rápidamente:

```text
"vamosacomprarcomida"
```

El sistema debe determinar dónde termina una palabra y comienza la siguiente:

```text
"vamos a comprar comida"
```

Este problema también aparece en determinados sistemas de escritura en los que las palabras no se separan mediante espacios.

La segmentación correcta es importante para poder realizar posteriormente la **tokenización** y el análisis del texto.

---

## 3.3. Recepción imperfecta de datos

Los sistemas de PLN normalmente no reciben textos perfectos.

Los datos pueden contener:

* Acentos regionales.
* Regionalismos.
* Errores de pronunciación.
* Errores de mecanografía.
* Palabras incompletas.
* Expresiones no gramaticales.
* Ruido en grabaciones de audio.
* Errores producidos por sistemas OCR.
* Abreviaturas.
* Lenguaje informal.
* Uso de palabras propias de una región.

**Ejemplo:**

Una persona podría escribir:

> "El camn de basura no paso x mi barrio."

El sistema debe ser capaz de trabajar con un texto que contiene errores:

```text
"camn" → posiblemente "camión"
"paso" → posiblemente "pasó"
"x"    → posiblemente "por"
```


## 4. Pipeline para resolver problemas de PLN


```text
Texto
  ↓
Tokenización
  ↓
Tokens
  ↓
Procesamiento
  ↓
Características
  ↓
Modelo
  ↓
Resultado
```
# 5. Tokenización

# Tokenización en NLP

La **tokenización** es el proceso de dividir un texto en unidades pequeñas llamadas **tokens**, para que podamos procesarlo mediante un programa.

De:
```text
"El gato come pescado."
```

A:

```text
["El", "gato", "come", "pescado", "."]
```

Cada elemento es un **token**.

---

La tokenización permite convertir ese texto en elementos individuales que podemos:

* contar
* analizar
* eliminar
* transformar
* comparar
* convertir en números
* utilizar como entrada para modelos de Machine Learning


---

## Tokenización

Por palabra, resultado:

```text
['El', 'gato', 'come', 'pescado.']
```

Por ejemplo:

```text
"¡Hola, mundo!"
```

puede convertirse en:

```text
['¡', 'Hola', ',', 'mundo', '!']
```


Dependiendo del tokenizador y de la tarea, podemos considerar como tokens:

* palabras
* números
* signos de puntuación
* símbolos
* emojis
* URLs
* etc.

---


### 6 Normalización

Convertir todo a minúsculas:

```text
["python", "es", "genial", ".", "python", "es", "fácil", "."]
```

### 1. Eliminación de stopwords

Podríamos eliminar palabras muy frecuentes como `es`:

```text
["python", "genial", ".", "python", "fácil", "."]
```

### 2. Análisis de frecuencia

```text
python → 2
genial → 1
fácil  → 1
```