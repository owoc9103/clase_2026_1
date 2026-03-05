"""
Contexto del problema - German Credit
"""
import streamlit as st
from utils_data import prepare_model_data

st.set_page_config(page_title="Contexto - German Credit", page_icon="📋", layout="wide")

# Obtener datos de sesión
df_raw = st.session_state.get("df_raw")
df_modelo = st.session_state.get("df_modelo")
data_ok = df_raw is not None and df_modelo is not None

st.title("📋 Contexto del problema")
st.markdown("---")

if not data_ok:
    st.warning("👆 Primero cargue el archivo de datos en la página **Inicio**.")
else:
    st.markdown("""
    ## Resumen Ejecutivo

    Se ha realizado el **cierre mensual de clientes** junto con la consolidación de las **solicitudes de crédito** 
    recibidas durante el período. En este punto, la compañía debe tomar una **decisión estratégica clave**: 
    determinar a cuáles solicitantes se les aprueba el crédito y a cuáles se les rechaza, buscando equilibrar 
    crecimiento comercial, rentabilidad y control del riesgo.

    Para respaldar esta decisión, se ha desarrollado un **modelo de regresión logística** utilizando la base de datos 
    histórica de la compañía. Este modelo permite estimar la probabilidad de que un solicitante sea clasificado como 
    **buen pagador (good)** o **mal pagador (bad)**, a partir de variables demográficas, financieras y de comportamiento 
    previamente registradas en el sistema interno.

    La regresión logística transforma la información de múltiples variables en una **probabilidad individual de incumplimiento**. 
    Con base en dicha probabilidad y en el nivel de apetito de riesgo definido por la compañía, se puede establecer un 
    **umbral de aprobación** que permita optimizar la relación entre riesgo asumido y rentabilidad esperada.

    **Este enfoque aporta:**
    - Mayor objetividad en la asignación de crédito.
    - Estandarización del proceso de evaluación.
    - Reducción potencial de pérdidas por incumplimiento.
    """)

    st.markdown("---")
    st.subheader("¿Qué significa esta base de datos?")

    st.markdown("""
    La base de datos recopila información de **solicitantes de crédito** de la compañía. Cada fila representa una 
    solicitud evaluada con el desenlace histórico: si el cliente resultó **buen pagador (good)** o **mal pagador (bad)**.
    Esta información permite construir un modelo predictivo para **nuevas solicitudes**: antes de aprobar el crédito, 
    estimamos la probabilidad de que el solicitante cumpla.
    """)

    st.markdown("---")
    st.subheader("Objetivo a modelar")

    st.info("""
    **Objetivo:** Predecir la probabilidad de que un solicitante sea **buen pagador (good)**.

    La variable respuesta es **Risk** (riesgo), que toma dos valores:
    - **good**: buen pagador – cumple con sus obligaciones.
    - **bad**: mal pagador – presenta incumplimiento.

    El modelo de regresión logística estima la probabilidad de **good** a partir de 
    variables demográficas, financieras y del propósito del crédito.
    """)

    st.markdown("---")
    st.subheader("Variables que influyen en el modelo")

    st.markdown("""
    El modelo utiliza las siguientes variables **que sí influyen** en la predicción:

    | Variable | Descripción | Efecto en el modelo |
    |----------|-------------|---------------------|
    | **Age** | Edad del solicitante | Numérica |
    | **Duration** | Duración del crédito (meses) | Numérica |
    | **Sex** (female) | Género femenino vs masculino | Dummy |
    | **Saving accounts** | Nivel de ahorro (little, rich) | Dummy |
    | **Checking account** | Nivel de cuenta corriente (little, moderate, rich) | Dummy |
    """)

    st.markdown("---")
    st.subheader("Variables que no se utilizan en el modelo")

    st.markdown("""
    Estas variables están en la base de datos pero **no forman parte del modelo definitivo** 
    (por diseño, para mantener un modelo parsimonioso):

    | Variable | Descripción |
    |----------|-------------|
    | Job | Tipo de empleo |
    | Housing | Tipo de vivienda (own, free, rent) |
    | Credit amount | Monto del crédito solicitado |
    | Purpose | Propósito del crédito (car, education, etc.) |
    """)

    st.markdown("---")
    st.subheader("Resumen del dataset cargado")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total solicitudes", f"{len(df_raw):,}")
    col2.metric("Buen pagador (good)", f"{(df_raw['Risk']=='good').sum():,} ({100*(df_raw['Risk']=='good').mean():.1f}%)")
    col3.metric("Mal pagador (bad)", f"{(df_raw['Risk']=='bad').sum():,} ({100*(df_raw['Risk']=='bad').mean():.1f}%)")
    col4.metric("Observaciones para modelo*", f"{len(df_modelo):,}")
    st.caption("*Tras excluir registros con NA en Saving/Checking account")
