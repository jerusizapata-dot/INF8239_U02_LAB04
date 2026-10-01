# Dataset Card



## Identificación



- Nombre: HorecaReviews-ES

- Fuente original: Hugging Face — mrcsgh/horeca-spanish-reviews

- Responsable: mrcsgh

- Versión o fecha: Repositorio `main`, archivo `dataset.txt`

- Licencia: MIT

- Idioma: Español



## Propósito y variable objetivo



El corpus contiene reseñas sintéticas en español relacionadas con el sector

HORECA (hoteles, restaurantes, cafeterías y establecimientos similares).

Fue diseñado para tareas de clasificación de texto y análisis de sentimientos

avanzado.



En este proyecto, la variable objetivo es `estilo`, que representa el estilo

pragmático de la reseña.



Las nueve categorías observadas son:



- breve

- formal

- coloquial

- neutral

- crítico

- anecdótico

- sarcástico

- entusiasta

- constructivo



El objetivo del laboratorio es disponer de un corpus público, reproducible y

auditable para posteriores tareas de procesamiento de lenguaje natural.



## Diccionario de datos



| Columna | Tipo | Descripción | Valores o unidad |

|---|---|---|---|

| `negocio` | texto | Tipo de establecimiento asociado a la reseña. | Restaurante, Mesón, Cervecería, Cafetería, Pub, Bar, Bar de carretera, entre otros |

| `texto` | texto | Contenido de la reseña en español. | Texto libre |

| `estrellas` | entero | Calificación asociada a la reseña. | Escala de 1 a 5 |

| `estilo` | categórica | Estilo pragmático asignado a la reseña. | 9 categorías: breve, formal, coloquial, neutral, crítico, anecdótico, sarcástico, entusiasta y constructivo |



## Procedimiento de obtención



El dataset se obtuvo desde el repositorio público de Hugging Face:



`mrcsgh/horeca-spanish-reviews`



El archivo fuente utilizado fue `dataset.txt`, descargado mediante la URL

directa del archivo.



La descarga se realizó mediante el script reproducible

`scripts/download_data.py`, utilizando `uv run`.



El archivo fuente se encuentra delimitado por tabulaciones (TSV) y fue

convertido automáticamente a `data/raw/dataset.csv` para facilitar su

procesamiento mediante pandas.



SHA-256 del archivo generado:



`e316af29487e9f2f74115990b725b659640a7909296cd4cfa8ad172864946863`



## Calidad observada



La auditoría local realizada sobre `data/raw/dataset.csv` produjo:



- Registros auditados: 5,716

- Columnas: 4

- Valores nulos en `texto`: 0

- Valores nulos en `estilo`: 0

- Textos duplicados: 23

- Longitud media del texto: 86.01 caracteres

- Longitud mínima: 5 caracteres

- Longitud máxima: 247 caracteres

- Mediana: 87 caracteres

- Percentil 90: 131 caracteres

- Percentil 99: 177 caracteres



La distribución de la variable objetivo presenta diferencias entre categorías.

La clase más frecuente es `breve` (19.37 %) y la menos frecuente es

`constructivo` (7.49 %).



Los duplicados de texto deben considerarse durante las etapas posteriores de

modelado y evaluación para evitar posibles problemas de fuga de información

entre conjuntos de entrenamiento y prueba.



## Población cubierta y excluida



### Población cubierta



El corpus representa reseñas sintéticas en español relacionadas con

establecimientos del sector HORECA. Incluye diferentes tipos de negocios y

nueve estilos pragmáticos.



### Población excluida



El corpus no representa directamente reseñas reales recopiladas de clientes,

ni constituye una muestra estadísticamente representativa de todos los

consumidores, establecimientos HORECA o hablantes de español.



También quedan fuera del alcance del corpus otros dominios diferentes al

sector HORECA y variedades lingüísticas que no estén reflejadas en los datos

generados.



Por tratarse de datos sintéticos y de un dominio específico, los resultados

obtenidos con este corpus no deben generalizarse automáticamente a población

real sin una validación adicional.



## Riesgos, sesgos y usos prohibidos



### Riesgos y sesgos



- El corpus es sintético y puede contener patrones lingüísticos propios del

  proceso de generación de los datos.

- Existe un desbalance entre las categorías de `estilo`.

- Se identificaron 23 textos duplicados.

- El dominio está limitado al sector HORECA.

- Las categorías de estilo pueden depender de señales lingüísticas o

  pragmáticas que no necesariamente se mantienen en otros dominios.

- No debe asumirse representatividad de la población hispanohablante en

  general.



### Usos prohibidos



No se debe utilizar este corpus como única fuente para tomar decisiones

individuales de alto impacto sobre personas.



No debe utilizarse para inferir atributos personales sensibles de individuos

reales ni para perfilar personas.



No debe presentarse como evidencia representativa del comportamiento o las

opiniones de consumidores reales.



No debe utilizarse para justificar decisiones automatizadas sobre personas o

negocios sin validación adicional, revisión humana y evaluación específica del

contexto de aplicación.

