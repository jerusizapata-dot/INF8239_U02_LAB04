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

| Logistic Regression    | **0.6933** |

| Complement Naive Bayes | **0.6491** |

| DummyClassifier        | **0.0355** |

El archivo con los resultados completos se encuentra en:

`reports/text_metrics.csv`

### Interpretación

Los dos modelos supervisados superaron ampliamente la línea base. Logistic Regression obtuvo un F1 Macro de 0.6933, mientras que Complement Naive Bayes obtuvo 0.6491.

La diferencia entre ambos modelos fue de aproximadamente 0.0442 puntos de F1 Macro.

El resultado muestra que las representaciones TF-IDF permiten capturar señales útiles para distinguir los estilos presentes en este corpus. Sin embargo, el desempeño no implica que el modelo pueda clasificar correctamente cualquier texto en español, debido al carácter sintético y específico del dataset.

## Análisis de errores

El conjunto de evaluación produjo **424 errores**.

Se revisaron manualmente los primeros **20 errores** y se clasificaron según la naturaleza observable del caso:

| Categoría          |  Casos |

| ------------------ | -----: |

| Ambigüedad         |     13 |

| Texto insuficiente |      5 |

| Ironía             |      2 |

| **Total revisado** | **20** |

Los errores de **ambigüedad** fueron los más frecuentes entre los casos revisados. Algunos textos contienen señales compatibles con más de un estilo pragmático.

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

Para la demostración de LAB05 se conserva el modelo de **Logistic Regression**, que obtuvo un F1 Macro de 0.6933 en la evaluación realizada.

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

**Resultado principal:** El experimento permitió transformar el corpus auditado de reseñas sintéticas HORECA en español en un problema reproducible de clasificación de texto. Se compararon un DummyClassifier como referencia, Complement Naive Bayes y regresión logística utilizando TF-IDF dentro de pipelines. La regresión logística obtuvo el mayor F1 macro, con 0.6933, frente a 0.6491 para Naive Bayes y 0.0355 para el baseline Dummy. Esto muestra una mejora clara respecto de la referencia mínima y evidencia que las representaciones TF-IDF permiten capturar patrones útiles para distinguir las nueve clases de estilo.

**Modelo seleccionado y evidencia:** Para la demostración se seleccionó la regresión logística porque obtuvo el mejor F1 macro entre los clasificadores evaluados. El resultado debe interpretarse considerando que la evaluación se realizó mediante una partición estratificada con semilla 42 y que el vectorizador permaneció dentro del pipeline, evitando utilizar información del conjunto de prueba durante el ajuste de la representación textual. Además, el modelo fue guardado como `models/text_model.joblib` y pudo cargarse posteriormente para producir nuevas predicciones.

**Clase con mayor dificultad:** La clase coloquial presentó uno de los desempeños más bajos, con recall de 0.54 y F1 de 0.59. Esto indica que una proporción importante de los ejemplos realmente pertenecientes a esta clase fue asignada a otras categorías. La matriz de confusión muestra además confusiones frecuentes entre clases cercanas, como coloquial y entusiasta, lo que sugiere que algunas características léxicas pueden ser compartidas entre diferentes estilos.

**Tipo de error más frecuente:** En los primeros 20 errores analizados, la categoría predominante fue ambigüedad, con 13 casos, seguida de texto insuficiente con 5 e ironía con 2. Estos errores muestran que una representación basada en palabras puede tener dificultades cuando el estilo depende del contexto, de expresiones breves o de significados que no están explícitos en los términos utilizados.

**Impacto en el contexto:** Las predicciones deben entenderse como resultados condicionados por los datos utilizados para entrenar el modelo. Una etiqueta incorrecta puede afectar la interpretación automática del estilo de una reseña, especialmente cuando existen clases semánticamente cercanas. Por esta razón, la aplicación incorpora una advertencia sobre el alcance del modelo y no debe utilizarse como clasificador general del idioma español.

**Limitación del dataset:** El corpus utilizado corresponde a reseñas sintéticas y está asociado específicamente al dominio HORECA. Aunque cuenta con licencia MIT, una estructura documentada y 5,716 registros auditados, no representa necesariamente reseñas reales de toda la población hispanohablante ni otros dominios textuales. Además, la auditoría identificó 23 textos duplicados, que son eliminados por el flujo de entrenamiento antes de construir los datos utilizados por los modelos.

**Decisión antes del despliegue:** La aplicación local puede utilizarse como demostración técnica y educativa del pipeline desarrollado. Antes de una publicación para uso real sería necesario evaluar el modelo con datos reales e independie

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
