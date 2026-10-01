# INF-8239 · Unidad 02 · Proyecto NLP

**Autor académico:** Edwin Ramón José Nolasco

Proyecto base para LAB04–LAB06. No sustituya la comprensión por ejecución mecánica.

## Estudiante

**Laudys Jerusi Zapata**

**Programa:** Maestría en Ciencia de Datos e Inteligencia Artificial

**Universidad:** Universidad Autónoma de Santo Domingo (UASD)

**Asignatura:** Ciencia de Datos II

---

## Inicio rápido

El proyecto utiliza `uv` para garantizar un entorno reproducible.

```bash

uv python install 3.12

uv sync

uv run pytest -q

uv run python scripts/audit_data.py

```

Para configurar el dataset:

```text

Copie .env.example como .env y configure el dataset aprobado.

```

El archivo `.env` contiene la configuración local de la fuente de datos y no se versiona.

---

# LAB04 · Localización, aprobación y auditoría del corpus

## Candidatos evaluados

Se revisaron dos candidatos públicos antes de seleccionar el corpus utilizado en el proyecto:

| Dataset          | Licencia                                | Idioma  | Registros | Variable objetivo | Decisión  |

| ---------------- | --------------------------------------- | ------- | --------: | ----------------- | --------- |

| INTENT-ES        | No identificada en la fuente consultada | Español |     8,113 | intent            | Rechazado |

| HorecaReviews-ES | MIT                                     | Español |     5,716 | estilo            | Aprobado  |

El corpus aprobado corresponde a `mrcsgh/horeca-spanish-reviews`, publicado en Hugging Face.

La ficha completa del dataset se encuentra en:

`docs/DATASET_CARD.md`

## Dataset aprobado

El corpus contiene reseñas sintéticas en español relacionadas con el sector HORECA.

Variables principales:

* `negocio`

* `texto`

* `estrellas`

* `estilo`

La variable objetivo utilizada posteriormente en LAB05 es `estilo`, con nueve categorías:

* breve

* formal

* coloquial

* neutral

* crítico

* anecdótico

* sarcástico

* entusiasta

* constructivo

## Auditoría

La auditoría local produjo:

* **5,716 registros**

* **4 columnas**

* **0 valores nulos** en `texto`

* **0 valores nulos** en `estilo`

* **23 textos duplicados**

* Longitud media: **86.01 caracteres**

* Mediana: **87 caracteres**

* Mínimo: **5 caracteres**

* Máximo: **247 caracteres**

* Percentil 90: **131 caracteres**

* Percentil 99: **177 caracteres**

La clase más frecuente es `breve` con 19.37 % y la menos frecuente es `constructivo` con 7.49 %.

SHA-256 del archivo generado:

```text

e316af29487e9f2f74115990b725b659640a7909296cd4cfa8ad172864946863

```

## Limitaciones del corpus

El corpus es sintético y está especializado en el dominio HORECA. Por tanto, no representa directamente reseñas reales ni constituye una muestra estadísticamente representativa de consumidores, establecimientos HORECA o hablantes de español.

Los resultados obtenidos con este corpus no deben generalizarse automáticamente a otros dominios o población real.

---

# LAB05 · Clasificación de texto

## Objetivo

Evaluar modelos clásicos de clasificación de texto utilizando TF-IDF y comparar:

1. `DummyClassifier` como línea base.

2. `Complement Naive Bayes`.

3. `Logistic Regression`.

El vectorizador TF-IDF permanece dentro de cada pipeline para evitar fuga de información entre entrenamiento y prueba.

La división de los datos se realizó mediante un único `train/test split` estratificado con `random_state=42`.

## Resultados

La métrica principal utilizada fue **F1 Macro**, debido a que permite considerar el desempeño de las nueve clases sin depender únicamente de la clase mayoritaria.

| Modelo                 |   F1 Macro |

| ---------------------- | ---------: |

| Logistic Regression    | **0.7021** |

| Complement Naive Bayes | 0.6590 |

| DummyClassifier        | 0.0356 |

El archivo con los resultados completos se encuentra en:

`reports/text_metrics.csv`

### Interpretación

Los dos modelos supervisados superaron ampliamente la línea base. Logistic Regression obtuvo un F1 Macro de 0.7021, mientras que Complement Naive Bayes obtuvo 0.6590.

La diferencia entre ambos modelos fue de aproximadamente 0.0431 puntos de F1 Macro.

El resultado muestra que las representaciones TF-IDF permiten capturar señales útiles para distinguir los estilos presentes en este corpus. Sin embargo, el desempeño no implica que el modelo pueda clasificar correctamente cualquier texto en español, debido al carácter sintético y específico del dataset.

## Análisis de errores

El conjunto de evaluación produjo **412 errores**.

Se revisaron manualmente los **30 errores** y se clasificaron según la naturaleza observable del caso:

| Categoría          |  Casos |

| ------------------ | -----: |

| Solapamiento de estilos | 9 |

| Señales mixtas | 7 |

| Ironía | 4 |

| Insuficiente texto | 4 |

| Ambigüedad | 4 |

| Lenguaje coloquial | 2 |

| **Total categorizado** | **30** |

Los casos revisados se concentraron principalmente en solapamiento de estilos y señales mixtas. Algunos textos contienen señales compatibles con más de un estilo pragmático.

Los casos de **texto insuficiente** presentan pocas palabras o poca información contextual para distinguir entre categorías. También se observaron casos en los que la interpretación depende de ironía o de señales pragmáticas difíciles de representar mediante características TF-IDF.

El detalle de los errores se conserva en:

`reports/error_analysis.csv`

La matriz de confusión se encuentra en:

`reports/confusion_text.png`

## Principales confusiones

Entre las confusiones observadas en la matriz se encuentran:

* `neutral → formal`: 25 casos

* `coloquial → entusiasta`: 21 casos

* `breve → entusiasta`: 19 casos

* `formal → neutral`: 18 casos

* `breve → coloquial`: 15 casos

* `neutral → constructivo`: 14 casos

* `crítico → constructivo`: 14 casos

Estas confusiones muestran que varias categorías comparten señales lingüísticas y pragmáticas.

---

# Modelo seleccionado para la demostración

Para la demostración de LAB05 se conserva el modelo de **Logistic Regression**, que obtuvo un F1 Macro de 0.7021 en la evaluación realizada.

El modelo serializado se encuentra en:

`models/text_model.joblib`

La prueba de carga y predicción del modelo fue realizada mediante:

```bash

uv run python -c "import joblib; m=joblib.load('models/text_model.joblib'); print(m.predict(['Excelente servicio']))"

```

Resultado obtenido:

```text

['breve']

```

Esta predicción solamente demuestra que el modelo puede cargarse y producir una salida. No constituye evidencia de que la predicción sea semánticamente correcta para un texto nuevo.

---

# Aplicación Streamlit

La aplicación puede ejecutarse localmente mediante:

```bash

uv run streamlit run app/streamlit_app.py

```

La interfaz permite introducir un texto y consultar la clase predicha.

La aplicación incluye una advertencia explícita de alcance:

> Este modelo fue entrenado con reseñas sintéticas del dominio HORECA en español. No debe utilizarse para interpretar textos fuera de ese dominio ni como clasificador general del idioma.

Durante la prueba se evaluaron tanto textos relacionados con el dominio como textos fuera del dominio. Los resultados refuerzan la necesidad de interpretar las predicciones dentro del alcance documentado del dataset.

---

# Pruebas y reproducibilidad

Las pruebas automatizadas se ejecutaron mediante:

```bash

uv run pytest -q

```

Resultado:

```text

6 passed

```

La prueba específica del modelo también fue ejecutada mediante:

```bash

uv run pytest tests/test_text_model.py -q

```

Resultado:

```text

1 passed

```

Las dependencias para ejecución portable fueron exportadas mediante:

```bash

uv export --format requirements.txt --output-file requirements-cloud.txt

```

---

# Conclusión de LAB05

**Resultado principal:** El experimento permitió construir un flujo reproducible de clasificación de texto a partir de un corpus público de reseñas sintéticas del dominio HORECA en español. La auditoría inicial registró 5,716 observaciones y detectó 23 textos duplicados, además de un texto con etiquetas conflictivas. Para el modelado se excluyeron las observaciones asociadas al conflicto y posteriormente se eliminaron los duplicados restantes, obteniendo 5,692 registros. Se compararon DummyClassifier, Complement Naive Bayes y Logistic Regression utilizando TF-IDF dentro de pipelines y una partición estratificada con semilla 42.

**Modelo seleccionado y evidencia:** Logistic Regression obtuvo un F1 Macro de 0.7021, frente a 0.6590 para Complement Naive Bayes y 0.0356 para DummyClassifier. La diferencia entre Logistic Regression y Complement Naive Bayes fue de aproximadamente 0.0431 puntos de F1 Macro. El modelo fue serializado en `models/text_model.joblib`, cargado posteriormente y utilizado para generar una predicción de prueba. Esto confirma la reproducibilidad de la carga del artefacto, pero no demuestra que una predicción individual sea correcta.

**Clase con mayor dificultad:** La clase `coloquial` presentó un desempeño relativamente bajo, con recall de 0.54 y F1 de 0.61 en la ejecución actual. Esto indica que una parte de los ejemplos pertenecientes a esta clase fue asignada a otras categorías. Las confusiones entre estilos cercanos muestran que algunas expresiones comparten características léxicas o pragmáticas.

**Tipo de error más frecuente:** Se identificaron 412 errores en el conjunto de evaluación y se categorizaron manualmente 30. Las categorías utilizadas fueron solapamiento de estilos, señales mixtas, ironía, insuficiente texto, ambigüedad y lenguaje coloquial. Estos casos muestran que algunas decisiones de etiquetado dependen del contexto y de señales pragmáticas que TF-IDF no representa completamente.

**Impacto en el contexto:** Una predicción incorrecta puede producir una interpretación equivocada del estilo de una reseña. Por ello, las salidas deben considerarse resultados del modelo y no verdades sobre el texto. La aplicación incluye una advertencia explícita sobre el alcance de la herramienta.

**Limitación del dataset:** El corpus es sintético y específico del dominio HORECA. Aunque posee una licencia identificada y un proceso reproducible de obtención, no representa estadísticamente reseñas reales de toda la población hispanohablante ni permite asumir comportamiento equivalente en otros dominios. Además, la auditoría identificó 23 textos duplicados y un conflicto de etiquetas que fueron tratados antes del modelado.

**Decisión antes del despliegue:** El sistema queda documentado como una demostración académica reproducible. Antes de cualquier utilización fuera del laboratorio sería necesario realizar una evaluación adicional con datos reales e independientes, revisar la estabilidad de las métricas, comprobar el comportamiento por clase y validar que las categorías sean apropiadas para el nuevo contexto.

## Estructura relevante

```text

app/

└── streamlit_app.py

data/

├── raw/

├── processed/

└── sample/

    └── demo_text.csv

docs/

├── DATASET_CARD.md

└── dataset_candidates.csv

models/

└── text_model.joblib

reports/

├── confusion_text.png

├── error_analysis.csv

└── text_metrics.csv

scripts/

├── audit_data.py

├── download_data.py

└── train_text.py

src/

└── inf8239_u02/

tests/

└── test_text_model.py

requirements-cloud.txt

pyproject.toml

uv.lock

README.md

```

## Principio de interpretación

Toda conclusión del proyecto debe separar **observación, evidencia, interpretación y decisión**, evitando generalizaciones que no estén respaldadas por los datos.
