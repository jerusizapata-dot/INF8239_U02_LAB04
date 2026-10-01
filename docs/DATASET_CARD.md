# Dataset Card

## Identificación

- Nombre: HorecaReviews-ES
- Fuente original: Hugging Face — mrcsgh/horeca-spanish-reviews
- Responsable: mrcsgh
- Versión o fecha: Repositorio `main`, archivo `dataset.txt`
- Licencia: MIT
- Idioma: Español

## Propósito y variable objetivo

El corpus contiene reseñas sintéticas en español relacionadas con el sector HORECA (hoteles, restaurantes, cafeterías y establecimientos similares).

Fue diseñado para tareas de clasificación de texto y análisis de sentimientos avanzado.

En este proyecto, la variable objetivo es `estilo`, que representa el estilo pragmático de la reseña.

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

El objetivo del laboratorio es disponer de un corpus público, reproducible y auditable para posteriores tareas de procesamiento de lenguaje natural.

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

El archivo fuente utilizado fue `dataset.txt`, descargado mediante la URL directa del archivo.

La descarga se realizó mediante el script reproducible `scripts/download_data.py`, utilizando `uv run`.

El archivo fuente se encuentra delimitado por tabulaciones (TSV) y fue convertido automáticamente a `data/raw/dataset.csv` para facilitar su procesamiento mediante pandas.

SHA-256 del archivo generado:

`e316af29487e9f2f74115990b725b659640a7909296cd4cfa8ad172864946863`

## Ejemplos anonimizados

Los siguientes ejemplos corresponden a cinco registros del corpus. Se muestran únicamente las columnas `texto` y `estilo`; no se incluyen identificadores de establecimientos.

| Ejemplo | Texto | Estilo |
|---|---|---|
| 1 | Mucho minimalismo pero las sillas son insufribles para una cena de dos horas. La ergonomía no debería sacrificarse por el diseño. | crítico |
| 2 | El guiso de ternera tenía demasiados nervios y grasa. | crítico |
| 3 | Llevé a mi padre por su santo. Él quería una caña de toda la vida y el camarero se puso a explicarle notas de cata de lúpulo durante diez minutos. Mi padre se desesperó, aunque la cerveza al final no estaba mal. | anecdótico |
| 4 | La terraza es agradable, pero los taburetes son algo incómodos para estancias largas. | constructivo |
| 5 | Vine solo a tomar una birra y terminé haciendo amigos en la barra gracias al buen rollo que se respira. | anecdótico |

## Transformaciones realizadas

El archivo fuente `dataset.txt` se obtuvo mediante la URL pública documentada en el archivo `.env`.

El archivo original utiliza formato delimitado por tabulaciones (TSV). El script `scripts/download_data.py` realizó una conversión reproducible de TSV a CSV UTF-8 y guardó el resultado como `data/raw/dataset.csv`.

No se eliminaron registros durante esta transformación ni se modificaron manualmente los textos o las etiquetas.

La auditoría se realizó sobre el archivo CSV generado y su integridad se documentó mediante SHA-256.

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

La distribución de la variable objetivo presenta diferencias entre categorías. La clase más frecuente es `breve` (19.37 %) y la menos frecuente es `constructivo` (7.49 %).

Los duplicados de texto deben considerarse durante las etapas posteriores de modelado y evaluación para evitar posibles problemas de fuga de información entre conjuntos de entrenamiento y prueba.

## Población cubierta y excluida

### Población cubierta

El corpus representa reseñas sintéticas en español relacionadas con establecimientos del sector HORECA. Incluye diferentes tipos de negocios y nueve estilos pragmáticos.

### Población excluida

El corpus no representa directamente reseñas reales recopiladas de clientes, ni constituye una muestra estadísticamente representativa de todos los consumidores, establecimientos HORECA o hablantes de español.

También quedan fuera del alcance del corpus otros dominios diferentes al sector HORECA y variedades lingüísticas que no estén reflejadas en los datos generados.

Por tratarse de datos sintéticos y de un dominio específico, los resultados obtenidos con este corpus no deben generalizarse automáticamente a población real sin una validación adicional.

## Riesgos, sesgos y usos prohibidos

### Riesgos y sesgos

- El corpus es sintético y puede contener patrones lingüísticos propios del proceso de generación de los datos.
- Existe un desbalance entre las categorías de `estilo`.
- Se identificaron 23 textos duplicados.
- El dominio está limitado al sector HORECA.
- Las categorías de estilo pueden depender de señales lingüísticas o pragmáticas que no necesariamente se mantienen en otros dominios.
- No debe asumirse representatividad de la población hispanohablante en general.

### Usos prohibidos

No se debe utilizar este corpus como única fuente para tomar decisiones individuales de alto impacto sobre personas.

No debe utilizarse para inferir atributos personales sensibles de individuos reales ni para perfilar personas.

No debe presentarse como evidencia representativa del comportamiento o las opiniones de consumidores reales.

No debe utilizarse para justificar decisiones automatizadas sobre personas o negocios sin validación adicional, revisión humana y evaluación específica del contexto de aplicación.

## Cierre interpretativo

**Resultado principal:** Se seleccionó un corpus público de 5,716 registros de reseñas sintéticas en español del dominio HORECA, con nueve categorías de estilo pragmático.

**Evidencia de calidad y procedencia:** La fuente pública está identificada, declara licencia MIT y puede obtenerse mediante una URL reproducible. La auditoría encontró 0 valores nulos en `texto` y `estilo`, 23 textos duplicados y diferencias en la distribución de las nueve clases.

**Riesgo o sesgo identificado:** El corpus es sintético, está especializado en HORECA y presenta desbalance entre categorías, por lo que puede contener patrones de generación que no se mantienen en datos reales u otros dominios.

**Decisión de aprobación o rechazo:** Se aprobó el corpus para las prácticas de este laboratorio porque cumple los criterios de acceso público, licencia identificable, texto, variable objetivo interpretable y obtención reproducible.

**Limitación que debe comunicarse:** Los resultados obtenidos no deben interpretarse como representativos de consumidores reales, establecimientos HORECA reales ni de la población hispanohablante en general.

**Siguiente verificación:** Antes de utilizar el corpus para modelado, se debe comprobar la separación entre entrenamiento y prueba, controlar los textos duplicados y evaluar el desempeño mediante métricas apropiadas para las nueve clases.