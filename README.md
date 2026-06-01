# Impacto de las Redes Sociales en la Salud Mental de los Adolescentes

Repositorio para la entrega individual del Módulo 2 de Inteligencia Artificial.

---

# Información del Alumno

| Dato | Información |
|---|---|
| Nombre | Yael Cortés Rubio |
| Matrícula | A01275893 |
| Materia | Desarrollo de aplicaciones avanzadas de ciencias computacionales |
| Profesor | Dr. Benjamín Valdés Aguirre |

---

# Introducción

El uso de las redes sociales en adolescentes ha incrementado significativamente durante los ultimos años. Plataforma digitales como Instagram, TikTok y X forman parte de la vida cotidiana de millones de jovenes y han cambiado la manera en la que interactúan socialmente.

Sin embargo, diversos estudios han señalado que el uso excesivo de redes sociales puede relacionarse con problemas como:

- Ansiedad
- Estrés
- Baja calidad de sueño
- Aislamiento social
- Depresión  

Debido a esto, el presente proyecto busca analizar la relación entre hábitos digitales y salud mental adolescentes mediante técnicas de Machine Learning supervisado.

El objetivo principal es indentificar patrones dentro del dataset que permitan predecir indicadores de depresión utilizando variables relacionadas con comportamientos social, emocional y académico. 

---

---

# Objetivo del proyecto

El objetivo principal del proyecto es desarrollar un modelo de clasificación capaz de predecir la variable:

```python
depression_label
```
La cual representa si un adolescente presenta indicadores asociados a depresión.

Las variables utilizadas incluyen información relacionadas con:

- Uso de redes sociales
- Ansiedad 
- Estrés
- Calidad de sueño
- Interacción social
- Rendimiento académico

---


# Entregables del Módulo

|  Semana  |                Actividad                |   Porcentaje  |
|----------|-----------------------------------------|---------------|
| Semana 2 | Generación o selección del set de datos |      20%      |
| Semana 2 | Preprocesado de los datos               |      20%      |
| Semana 3 | Implementación del modelo               |      20%      |
| Semana 3 | Evaluación inicial del modelo           |      20%      |
| Semana 4 | Refinamiento del modelo                 |      20%      |
| Semana 5 | Entrega final y correcciones            | Entrega final |

---

# Criterios de Evaluación

## Semana 2 — Generación o selección del set de datos

- Obtener, generar o aumentar un set de datos
- Realizar la separación de datos de entrenamiento y prueba

## Semana 2 — Preprocesado de los datos

- Aplicar técnicas de escalamiento
- Realizar el preprocesamiento pertinente de los datos

## Semana 3 — Implementación del modelo

- Seleccionar un modelo respaldado por artículos científicos
- Implementar el modelo utilizando un framework adecuado

## Semana 3 — Evaluación inicial del modelo

- Seleccionar métricas adecuadas
- Reportar e interpretar resultados obtenidos

## Semana 4 — Refinamiento del modelo

- Medir el desempeño del modelo actual
- Ajustar hiperparámetros o arquitectura
- Comparar resultados y reportar mejoras

## Semana 5 — Entrega final

- Documentar correcciones realizadas
- Entregar versión final corregida

---

# Avance 1: Generación o selección del set de datos y preprocesado

Durante esta primera etapa se realizó la selección y preparación del dataset que será utilizado para entrenar futuros modelos de clasificación supervisada. El objetivo principal de esta fase fue garantizar que los datos tuvieran una estructura adecuada para el entrenamiento y evaluación de modelos de Machine Learning.

## Selección del set de datos

Se seleccionó un dataset relacionado con la salud mental adolescente y uso de redes sociales obtenido desde Kaggle.
El dataset contiene variables relacionadas con:

- Ansiedad
- Estrés
- Calidad de sueño
- Iteración social
- Rendimiento académico
- Tiempo de uso de redes sociales

La selección de este dataset se realizó debido a que representa un problema relevante actualmente dentro del área de salud mental adolescente.

## Análisis Inicial

Durante la exploración inicial se analizaron:

- Dimensiones del dataset
- Tipos de datos
- Valores nulos
- Registros duplicados
- Distribución de variables

Estas tareas permitieron comprender la estructura general de los datos.

## Limpieza y preprocesado de los datos

Posteriormente se realizaron tareas de preparación de datos para dejar el dataset listo.

Las técnicas aplicadas son:

- Eliminación de registros duplicados
- Transformación de variables categóricas mediante One Hot Encoding
- División de datos de entrenamiento y prueba
- Escalamiento de variables numéricas mediante StandarScaler

Estas transformaciones ayudan a mejorar la calidad de los datos y permiten que los algoritmos trabajen correctamente con variables numéricas normalizadas.

---

# Metodología de Trabajo

El proyecto sigue un flujo de trabajo típico utilizado en proyectos de Ciencia de Datos y Machine Learning supervisado. 

La estructura general del análisis fui inspirada en notebooks introductorios de Kaggle relacionados con clasificación supervisada, particularmente ejemplos basados en el dataset Titanic.

Referencia utilizada:

https://www.kaggle.com/datasets/algozee/teenager-menthal-healy 

Las etapas principales implementadas fueron:

1. Exploración inicial del dataset
2. Análisis Exploratorio de Datos (EDA)
3. Limpieza de datos
4. Transformación de variables
5. División de entrenamiento y prueba
6. Escalamiento de variables
7. Preparación para entrenamiento de modelos

Posteriormente, dichas técnicas fueron adaptadas al contexto específico del presente proyecto enfocado en salud mental adolescentes y uso de redes sociales.

---

# Dataset

El dataset contiene:

- 1200 registros
- 13 variables
- Información relacionada con:

|        Variable       |         Descripción         |
|-----------------------|-----------------------------|
|     Redes sociales    | Tiempo y frecuencia de uso  |
|        Ansiedad       |      Nivel de ansiedad      |
|         Estrés        |       Nivel de estrés       |
|         Sueño         |      Calidad del sueño      |
| Rendimiento académico |      Desempeño escolar      |
|   Interacción social  | Nivel de interacción social |

---

## EDA

Se realizó un análisis exploratorio de datos el objetivo de comprender mejor el comportamiento del dataset y detectar posibles patrones relevantes relacionadas con salud mental adolescente.

---

## Distribución de la Variables Ojetivo

La siguiente visualización muestra la distribución de la variable objetivo:

```python
depression_label
```
![alt text](/images/image.png)

La distribución observada permite validar si el problema puede abordarse correctamente mediante clasificación binaria supervisada

## Distribución de Edades

La siguiente gráfica representa la distribución de edades dentro del dataset:

![alt text](images/Edad.png)

La mayoria de los registros se concentra en determinados rangos de edad, lo cual puede influir en la capacidad de generalización del modelo. Esto significa que el modelo podría funcionar mejor para grupos de edad más representados dentro del dataset

## Distribución por Género

La siguiente gráfica muestra la distribución de registros por género:

![alt text](images/Genero.png)

El análisis por género permite detectar posibles sesgos demográficos dentro del dataset. Mantener una distribución relativamente equilibrada ayuda a reducir problemas de sesgos durante el entrenamiento del modelo.

## Matriz de Correlación

![alt text](images/MC.png)

Esta matriz muestra la correlación entre variables numericas del dataset, dicha matriz permitió identificar relaciones importantes entre variables psicológicas y hábitos digitales.

Se observaron las siguientes relaciones:

Se observó una correlación positiva entre las horas de uso de redes sociales y la variable `depression_label` (0.18).
Aunque la correlación no es alta, el resultado sugiere que un mayor tiempo de uso de redes sociales podría relacionarse con mayores indicadores de depresión en adolescentes.

Así mismo, también se observa una correlación negativa entre las variables hora de sueño y depresión, ya que mientras menos horas duermen, más depresión aparece.

De igual forma, se observó una correclación positiva de las variables de `stress_level` y `anxiety_level` con `depression_label`(0.17). Esto indica que entre más altos niveles de estrés y ansiedad tiende a relacionarse con mayores indicadores depresión

---

# Preprocesamiento de Datos

Antes de entrenar el modelo, se realizaron distintas técnicas de limpieza y transformación con el objetivo de preparar el dataset y garantizar que los pudieran trabajar correctamente con la información disponible.
Para comenzar se realizó una exploración inicial del dataset utilizando funciones como:

```python
df.head() # Mostar los primeros 5 datos del dataset
df.info() # Información general 
df.shape() # Muestra el tamaño del dataset (Filas, columnas)
```

---


# Tecnologías y Librerías

## Lenguaje utilizado

- Python

## Librerías utilizadas

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
```

## Herramientas utilizadas

- Jupyter Notebook
- Python
- GitHub

---

# Pipeline de Preparación de Datos

El pipeline implementado en el notebook incluye las siguientes etapas:

1. Carga del dataset
2. Exploración inicial de datos
3. Análisis exploratorio (EDA)
4. Detección de valores nulos
5. Eliminación de duplicados
6. Transformación de variables categóricas
7. Separación de variables predictoras y variable objetivo
8. División de datos de entrenamiento y prueba
9. Escalamiento de variables numéricas

# Visualizaciones Realizadas

Durante el análisis exploratorio se realizaron las siguientes visualizaciones:

- Distribución de la variable objetivo
- Histograma de edades
- Distribución de género
- Matriz de correlación entre variables numéricas

Estas visualizaciones permiten comprender mejor el comportamiento y estructura del dataset antes del entrenamiento del modelo.

# División de Datos

Se realizó una separación de:

- 80% para entrenamiento
- 20% para prueba

Esto permite entrenar y evaluar correctamente futuros modelos de Machine Learning.

---

# Ejecución del Proyecto

## 1. Clonar el repositorio

```bash
git clone https://github.com/YaoCr003/IA.git 
```

## 2. Ejecutar el notebook

Abrir y ejecutar el archivo:

```text
ia.ipynb
```

---

# Estructura del Repositorio

```text
IA/
│
├── data/
│   └── Teen_Mental_Health_Dataset.csv
│
├── notebooks/
│   └── ia.ipynb
│
├── images/
│   └── image.png
│
└── README.md
```


# Fuente del Dataset

Dataset obtenido de Kaggle:

https://www.kaggle.com/datasets/algozee/teenager-menthal-healy

---

# Recomendaciones de Visualización

Para una mejor visualización del código en Visual Studio Code se recomienda utilizar la extensión:

- Better Comments:

![alt text](./images/image.png)

---

# Modificaciones Avance 1




# Avance 2: Implementación del Modelo

En esta segunda etapa del proyecto se comenzará a trabajar con la construcción del modelo de Machine Learning. El objetivo principal de esta fase es entrenar el algoritmo capaz de aprender patrones dentro del dataset para posteriormente predecir si un adolescente presenta indicadores de depresión a partir de variables relacionadas con ansiedad, éstres, sueño, desempeño académico y uso de redes sociales.

## Selección del Modelo

El dataset utilizado corresponde a un conjunto de datos tabular relacionado con la salud mental adolescente y uso de redes sociales. La variable `depression_label` representa un problema de clasificación binaria, ya que únicamente puede tomar dos valores (depresion y no depresión).

Debido a estas características, se evaluarón distintos modelos comunmente utilizados en problemas de clasificación supervisada sobre datos tabulares, entre ellos:

### Decision Tree

Este modelo funciona creando reglas de decisión basadas en las variables del dataset. Los árboles de decisión son fáciles de interpretar visualmente, ya que estos modelos están diseñados para procesar colecciones de instancias etiquetadas y transformarlas en reglas lógicas, aunque pueden presentar problemas de sobreajuste cuando el árbol crece demasiado.

### Logistic Regression

Es un modelo estadístico diseñado para analizar la relación entre una variable de respuesta binomial (que solo tiene dos posibles resultados) y una o más variables explicativas. Su procedimiento es similar al de la regresión lineal múltiple, pero se diferencia en que está específicamente estructurado para predecir la probabilidad de que ocurra un evento de interés basándose en características individuales. Este modelo destaca por su versatilidad, ya que puede manejar simultáneamente variables continuas y variables categóricas.


### Modelo a usar

Para este proyecto se seleccionó el modelo de `Logistic Regression` ya que al saber que el dataset utilizado es un conjunto de datos tabular, este modelo se convierte en una muy buena opción ya que este algoritmo es ampliamente utilizado en tareas de clasificación binaria, como lo es en este caso donde la variable objetivo `depression_label` solamente puede tomar dos valores (con depresión o sin depresión). Además resulta un modelo muy apropiado ya que funciona con datasets relativamente pequeños o medianos, como para este proyecto, el cual se esta usando un dataset con aproximadamente 1200 datos.


## Métricas

Para determinar las métricas a usar se realizó una investigación acerca de artículos relacionados con Machine Learning aplicado a la salud mental.

Como lo es el caso del [Articulo 1](Docs/article1.pdf) el cual analiza cómo el aprendizaje automático puede predecir y diagnosticar la depresión utilizando registros médicos electrónicos (EHR). Dentro de los cuales menciona que las métricas usadas son (Accuracy, Precision, Recall y F1-Score)

O el [Articulo 2](Docs/article2.pdf), el cual presenta el desarrollo de un modelo de aprendizaje profundo diseñado para identificar trastornos mentales mediante el análisis de publicaciones en la red social Reddit. Hablando de las métricas, se utilizaron cuatro métricas fundamentales para validar el rendimiento de los modelos de clasificación (XGBoost y CNN), (Accuracy, Precision, Recall y F1-Score).

Analizando ambos artículos sabemos que las métricas más utilizadas para evaluar modelos son `Accuracy, Precision, Recall y F1-Score`. Estas métricas son ampliamente utilizadas dentro del estado del arte debido a que permiten analizar distintos aspectos del desempeño del modelo y proporcionan una evaluación más completa.

- **Accuracy:** Representa la proporción de observaciones correctamente clasificadas respecto al total de observaciones evaluadas. Un valor de accuracy cercano a 1 indica que el modelo realiza una gran cantidad de predicciones correctas.

    - Formula:![alt text](./images/accuracy.png)

- **Precision:** Mide qué proporción de las observaciones clasificadas como positivas realmente pertenecen a dicha clase. Es especialmente importante cuando los falsos positivos representan un problema relevante

    - Formula: ![alt text](./images/precision.png)

- **Recall:** Mide la capacidad del modelo para identificar correctamente todos los casos positivos existentes en el conjunto de datos. Un valor elevado de recall indica que el modelo detecta la mayoría de los casos positivos reales.

    - Formula: ![alt text](./images/recall.png) 

- **F1-Score:** Combina la precisión y el recall en una única métrica, resulta particularmente útil cuando existe un desbalance entre clases, ya que considera simultáneamente la capacidad del modelo para identificar correctamente los casos positivos

    - Formula: ![alt text](./images/F1.png)


## Implementación

Tanto el modelo como las métricas seleccionadas fueron implementadas utilizando la libreria `Scikit-learn`.

```python
from sklearn.linear_model import LogisticRegression
```
Aquí se importa el algoritmo `Logistic Regression`. Este framework proporciona implementaciones ya optimizadas de distintos modelos de Machine Learning, permitiendo entrenar modelos sin necesidad de programar manualmente todas las operaciones matemáticas.

```python
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
```
Posteriormente importamos las métricas de evaluación que se utilizarán para analizar el desempeño del modelo una vez finalizado el entrenamiento. Además de las métricas númericas, tambien se importó `confusion_matrix`, la cual es una herramienta que permite vizualizar gráficamente los aciertos y errores cometidos (TP, TN, FP, FN) por el modelo durante la clasificación.

De igual forma se importo `classification_report` que genera un resumen completo con todas las métricas principales obtenidas durante la evaluación.

Apesar que el proyecto ya cuenta con datos organizados y preprocesados, todavia no existe ningún sistema capaz de aprender patrones o realizar clasificaciones automáticamente, Por ello crearemos primero el modelo:

```python
model = LogisticRegression()
```
Se crea una instancia del algoritmo Logistic Regression con sus parametros iniciales por defecto. Lo cual el framework prepara toda la lógica matemática necesaria para trabajar con problemas de clasificación binaria.

Después de crear el modelo empezamos el entrenamiento, el algoritmo intenta encontrar la mejor combinación de pesos matemáticos para cada variable predictora con el objetivo de clasificar correctamente los registros entre las clases 0 y 1.
Logistic Regression analiza cada registro del conjunto de entrenamiento y busca identificar relaciones entre las variables de entrada y la variable objetivo

```python
model.fit(x_train_scaled, y_train)
```
El entrenamiento se implementa usando la función `fit()` donde `x_train_scaled` contiene las variables predictoras ya escaladas (calculadas en el preprocesamiento) porque Logistic Regression presenta un mejor desempeño cuando todas las variables poseen magnitudes similares, mientras que `y_train` contiene las etiquetas reales asociadas a cada registro,con el objetivo de aprender patrones que permitan clasificar correctamente nuevos registros.

El modelo ya aprendió patrones matemáticos relacionados con las variables del proyecto, sin embargo, unicamente ha trabajado con los datos de entrenamiento. Por ello es necesario evaluar si el modelo realmente aprendió patrones útiles, para comprobar esto se utilizan los datos de prueba (`x_train_scaled`). Por ello generaremos predicciones.

```python
y_pred = model.predict(x_test_scaled)
```
Logistic Regression toma cada registro de `x_test_scaled` y aplica la ecuación matemática aprendida durante el entrenamiento. Para cada adolescente del dataset, el modelo calcula una probabilidad de pertenecer a la clase positiva.

Internamente ocurre esto:

1. El modelo recibe las variables predictoras del adolescente.
2. Utiliza los pesos aprendidos durante el entrenamiento.
3. Calcula un valor numérico utilizando la ecuación de regresión logística. 

    - ![alt text](./images/FormulaLR.png)

4. Aplica la función sigmoide para transformar el resultado en una probabilidad entre 0 y 1.

    - ![alt text](./images/FuncionSi.png)

5. Finalmente, clasifica el registro como:
    - 0 -> Sin depresión.
    - 1 -> Con depresión.

En este punto se ya generó una clasificación para cada registro, sin embargo, aún no sabemos si esas predicciones son correctas o incorrectas. Las metricas funcionan comparando los valores reales(`y_test`) contra las predicciones del modelo (`y_pred`).

**Accuracy**

```python
accuracy = accuracy_score(y_test, y_pred)
```
Esto permite medir qué tan frecuentemente el modelo acierta.

**Precision**

```python
precision = precision_score(y_test, y_pred)
```
Mide la confiabilidad del modelo cuando detecta casos positivos, es decir, analiza cuántas veces el modelo dijo “sí hay depresión” y cuántas de esas veces realmente era cierto.

**Recall**

```python
recall = recall_score(y_test, y_pred)
```
Recall compara todos los casos reales positivos, contra los que el modelo logró detectar correctamente, esta metrica es importante porque puede indicar que cuando señala un falso negativo significa que existe un adolescente con depresión que el modelo NO detectó.

**F1-Score**

```python
f1 = f1_score(y_test, y_pred)
```
Esta métrica combina precision y recall en una sola medida balanceada, el punto de esta métrica es, entre detectar casos positivos

Despues de verificar el comportamiento del modelo mediante las métricas, realizamos _Matriz de confusión_, la cual permite visualizar de manera detallada qué tipos de aciertos y errores está cometiendo el modelo graficamente, permite observar exactamente cuántos registros fueron clasificados correctamente y cuántos fueron clasificados incorrectamente.

```python
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")

plt.title("Matriz de Confusión")
plt.xlabel("Predicción")
plt.ylabel("Valor Real")

plt.show()
```

![alt text](./images/MConf.png)

Dentro de los resultados obtenidos se puede decir lo siguiente:

- El modelo clasifico correctamente 234 adolescentes que NO presentaban depresión. (TN)
- El modelo nunca clasificó incorrectamente a un adolescente sano como si tuviera depresión. (FP)
- El sistema no detectó correctamente un posible caso real de depresión, existían 2 adolescentes con depresión real pero el modelo los clasificó como si NO tuvieran depresión. (FN)
- El modelo señalo que existían 4 adolescentes con depresión, y el modelo logró detectarlos correctamente. (TP)

Finalmente imprimimos los resultados obtenidos:

```python
print(classification_report(y_test, y_pred))
```
![alt text](./images/Result.png)

Los resultados obtenidos muestran que el modelo Logistic Regression alcanzó una accuracy de 99%,que indica el modelo acertó aproximadamente el 99% de las predicciones totales. Sin embargo, debido al desbalance presente en el dataset, fue necesario analizar métricas adicionales como Precision, Recall y F1-Score.

El modelo presentó un desempeño casi perfecto para la clase negativa (0), identificando correctamente la mayoría de los adolescentes sin indicadores de depresión. Para la clase positiva (1), el modelo obtuvo una precisión de 1.00, lo que indica que todas las predicciones positivas realizadas fueron correctas.

El recall obtenido para la clase positiva fue de 0.67, lo que significa que algunos casos reales de depresión no fueron detectados por el modelo

El F1-Score de 0.80 refleja un equilibrio adecuado entre precisión y capacidad de detección, aunque todavía existe margen de mejora en la identificación de adolescentes con posibles indicadores de depresión.
