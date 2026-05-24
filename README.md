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

# Descripción General del Proyecto

Durante el módulo se desarrollará un modelo individual que servirá como base para la evidencia individual del reto. La solución puede seguir la misma temática del reto o una temática diferente. En caso de seleccionar la misma temática del reto, se espera el desarrollo de un segundo modelo para la evidencia final.

El proyecto se desarrollará de manera incremental durante las sesiones del módulo con el objetivo de realizar revisiones intermedias y corregir posibles errores antes de la entrega final.

El desarrollo del proyecto estará respaldado por artículos científicos relacionados con el estado del arte en Machine Learning y análisis de datos.

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

## Generación o selección del set de datos

Durante esta etapa se realizó la selección de un dataset relacionado con salud mental adolescente y uso de redes sociales.

Actividades realizadas:

- Obtención del dataset
- Exploración inicial de los datos
- Separación de datos de entrenamiento y prueba

## Preprocesado de los datos

Durante esta etapa se realizaron tareas de preparación y transformación de datos para dejarlos listos para futuros modelos de Machine Learning.

Actividades realizadas:

- Revisión de valores nulos
- Eliminación de duplicados
- Transformación de variables categóricas mediante One Hot Encoding
- Aplicación de técnicas de escalamiento utilizando StandardScaler

## Exploratory Data Analysis (EDA)

Durante esta etapa se realizó un análisis exploratorio de los datos con el objetivo de comprender mejor la estructura del dataset y detectar posibles patrones o problemas en la información.

Actividades realizadas:

- Visualización de la distribución de la variable objetivo
- Análisis de distribución de edades
- Visualización de distribución por género
- Análisis de correlación entre variables numéricas
- Exploración inicial del dataset

---

# Descripción del Proyecto

Este proyecto tiene como objetivo analizar la relación entre el uso de redes sociales y la salud mental en adolescentes mediante técnicas de Machine Learning.

El objetivo principal es predecir la variable:

```python
depression_label
```

la cual representa si un adolescente presenta indicadores de depresión.

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