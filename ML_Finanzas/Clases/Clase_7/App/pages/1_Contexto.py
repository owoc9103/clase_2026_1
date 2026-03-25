"""
Contexto del problema - Churn Modelling
"""
import streamlit as st
from utils_data import prepare_model_data

st.set_page_config(page_title="Contexto - Churn Modelling", page_icon="📋", layout="wide")

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

    Se ha consolidado la **base de datos de clientes bancarios** para apoyar la **decisión estratégica de retención**.
    El banco debe identificar qué clientes tienen mayor probabilidad de **abandonar (churn)** para priorizar acciones
    de fidelización y reducir la pérdida de ingresos.

    Para respaldar esta decisión, se ha desarrollado un **modelo de regresión logística con ajustes**:
    - **SMOTE**: balanceo de clases mediante oversampling de la clase minoritaria (clientes que abandonaron).

    El modelo transforma múltiples variables en una **probabilidad individual de abandono**. Con base en dicha
    probabilidad, el área de retención puede diseñar campañas dirigidas a los clientes de mayor riesgo.

    **Este enfoque aporta:**
    - Identificación proactiva de clientes en riesgo de abandono.
    - Priorización de esfuerzos de retención.
    - Reducción potencial de la pérdida de ingresos por churn.
    """)

    st.markdown("---")
    st.subheader("¿Qué significa esta base de datos?")

    st.markdown("""
    La base de datos recopila información de **clientes bancarios**. Cada fila representa un cliente con su historial:
    si **permaneció (Exited=0)** o **abandonó el banco (Exited=1)**. Esta información permite construir un modelo
    predictivo para **nuevos clientes**: se estima la probabilidad de que abandonen antes de que ocurra.
    """)

    st.markdown("---")
    st.subheader("Objetivo a modelar")

    st.info("""
    **Objetivo:** Predecir la probabilidad de que un cliente **abandone el banco (churn)**.

    La variable respuesta es **Exited**, que toma dos valores:
    - **0**: el cliente permaneció (no churn).
    - **1**: el cliente abandonó el banco (churn).

    El modelo de regresión logística estima la probabilidad de **churn** a partir de variables demográficas,
    financieras y de comportamiento.
    """)

    st.markdown("---")
    st.subheader("Variables que influyen en el modelo")

    st.markdown("""
    El modelo utiliza las siguientes variables:

    | Variable | Descripción | Tipo |
    |----------|-------------|------|
    | **CreditScore** | Puntuación crediticia del cliente | Numérica |
    | **Geography** | País (France, Germany, Spain) — dummys: Germany vs France, Spain vs France | Categórica |
    | **Gender** | Género (Female, Male) — dummy: Male vs Female | Categórica |
    | **Age** | Edad del cliente | Numérica |
    | **Tenure** | Años de antigüedad en el banco | Numérica |
    | **Balance** | Saldo de la cuenta | Numérica |
    | **NumOfProducts** | Número de productos bancarios | Numérica |
    | **HasCrCard** | Tiene tarjeta de crédito (0/1) | Binaria |
    | **IsActiveMember** | ¿Cliente activo? (0/1) | Binaria |
    | **EstimatedSalary** | Salario estimado | Numérica |
    """)

    st.markdown("---")
    st.subheader("Variables que no se utilizan en el modelo")

    st.markdown("""
    Estas variables están en la base de datos pero **no forman parte del modelo** (no aportan información predictiva):

    | Variable | Descripción |
    |----------|-------------|
    | RowNumber | Índice secuencial |
    | CustomerId | Identificador único del cliente |
    | Surname | Apellido del cliente |
    """)

    st.markdown("---")
    st.subheader("Resumen del dataset cargado")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total clientes", f"{len(df_raw):,}")
    col2.metric("Permanecen (Exited=0)", f"{(df_raw['Exited']==0).sum():,} ({100*(df_raw['Exited']==0).mean():.1f}%)")
    col3.metric("Abandonaron (Exited=1)", f"{(df_raw['Exited']==1).sum():,} ({100*(df_raw['Exited']==1).mean():.1f}%)")
    col4.metric("Observaciones para modelo", f"{len(df_modelo):,}")
