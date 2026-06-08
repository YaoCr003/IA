import streamlit as st
import pandas as pd
import numpy as np
import joblib

from tensorflow.keras.models import load_model

#! Carga del modelo entrenado

model = load_model("./models/depression_model.keras")
scaler = joblib.load("./models/scaler.pkl")
columns = joblib.load("./models/columns.pkl")


#! Creación de la interfaz

st.title("Predicción de Depresión en Adolescentes")

st.write(
    "Ingrese los datos para estimar la probabilidad de depresión."
)

age = st.number_input(
    "Edad",
    min_value=13,
    max_value=19,
    value=16
)

gender = st.selectbox(
    "Género",
    ["female", "male"]
)

daily_social_media_hours = st.number_input(
    "Horas diarias en redes sociales",
    min_value=0.0,
    max_value=24.0,
    value=4.0
)

sleep_hours = st.number_input(
    "Horas de sueño",
    min_value=0.0,
    max_value=12.0,
    value=8.0
)

screen_time_before_sleep = st.number_input(
    "Tiempo de pantalla antes de dormir (horas)",
    min_value=0.0,
    max_value=5.0,
    value=1.0
)

academic_performance = st.slider(
    "Rendimiento académico",
    1,
    10,
    5
)

physical_activity = st.slider(
    "Actividad física",
    1,
    10,
    5
)

stress_level = st.slider(
    "Nivel de estrés",
    1,
    10,
    5
)

anxiety_level = st.slider(
    "Nivel de ansiedad",
    1,
    10,
    5
)

addiction_level = st.slider(
    "Nivel de adicción",
    1,
    10,
    5
)

platform_usage = st.selectbox(
    "Plataforma más utilizada",
    [
        "Instagram",
        "TikTok",
        "Other"
    ]
)

social_interaction_level = st.selectbox(
    "Nivel de interacción social",
    [
        "low",
        "medium",
        "high"
    ]
)


#! Predicción

if st.button("Predecir"):

    data = pd.DataFrame([{

        "age": age,
        "gender": gender,
        "daily_social_media_hours":
            daily_social_media_hours,

        "sleep_hours":
            sleep_hours,

        "screen_time_before_sleep":
            screen_time_before_sleep,

        "academic_performance":
            academic_performance,

        "physical_activity":
            physical_activity,

        "stress_level":
            stress_level,

        "anxiety_level":
            anxiety_level,

        "addiction_level":
            addiction_level,

        "platform_usage":
            platform_usage,

        "social_interaction_level":
            social_interaction_level
    }])

    #* Transforma las variables categoricas 

    data = pd.get_dummies(
        data,
        drop_first=True
    )

    #* Columnas originales

    data = data.reindex(
        columns=columns,
        fill_value=0
    )

    #* Escalamiento

    data_scaled = scaler.transform(
        data
    )

    #* Predicción

    probability = model.predict(
        data_scaled
    )[0][0]

    prediction = int(
        probability > 0.3
    )

    #* Resultados

    st.subheader("Resultado")

    st.write(
        f"Probabilidad de depresión: {probability:.2%}"
    )

    st.write(
        f"Probabilidad de no depresión: {(1-probability):.2%}"
    )

    if prediction == 1:

        st.error(
            "Posible presencia de depresión"
        )

    else:

        st.success(
            "No se detectan indicadores de depresión"
        )