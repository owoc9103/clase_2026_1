"""
Churn Modelling - Predicción de abandono de clientes
Dashboard gerencial para apoyar decisiones de retención de clientes bancarios.
"""
import streamlit as st
from utils_data import parse_uploaded_csv, prepare_model_data

st.set_page_config(
    page_title="Churn Modelling - Retención de Clientes",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar sesión
if "df_raw" not in st.session_state:
    st.session_state.df_raw = None
    st.session_state.df_modelo = None

# === INICIO - MENSAJE GERENCIAL ===
st.title("🏦 Dashboard de Predicción de Churn")
st.markdown("---")

st.markdown("""
### Resumen Ejecutivo

Se ha consolidado la **base de datos de clientes bancarios** para apoyar la **decisión estratégica** de retención: 
identificar qué clientes tienen mayor probabilidad de abandonar el banco (churn) y priorizar acciones de fidelización.

Para respaldar esta decisión, se ha desarrollado un **modelo de regresión logística** con ajustes:
- **SMOTE** para balancear las clases (oversampling de la clase minoritaria).

El modelo estima la probabilidad de que un cliente **abandone (Exited=1)** a partir de variables demográficas, 
financieras y de comportamiento registradas en el sistema.

**Pasos sugeridos:**
1. **Cargar los datos** en esta sección (Churn_Modelling.csv).
2. Revisar el **contexto** del problema y las variables.
3. Explorar el **análisis descriptivo** (univariado, bivariado y tablas de contingencia).
4. Usar la **modelación** y la calculadora para estimar el riesgo de churn de cada cliente.
""")

st.markdown("---")
st.subheader("📂 Cargar archivo de datos")

uploaded = st.file_uploader(
    "Suba el archivo **Churn_Modelling.csv** con los datos de clientes",
    type=["csv"],
    help="Columnas: RowNumber, CustomerId, Surname, CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Exited"
)

if uploaded is not None:
    try:
        df_raw = parse_uploaded_csv(uploaded)
        df_modelo = prepare_model_data(df_raw)
        st.session_state.df_raw = df_raw
        st.session_state.df_modelo = df_modelo
        st.success(f"✅ **Datos cargados:** {len(df_raw):,} clientes × {len(df_raw.columns)} variables")
        with st.expander("Vista previa de los datos"):
            st.dataframe(df_raw.head(20), use_container_width=True)
        with st.expander("Información del dataset"):
            st.write("**Columnas:**", list(df_raw.columns))
            st.write("**Valores faltantes por columna:**")
            st.write(df_raw.isna().sum())
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")
        st.session_state.df_raw = None
        st.session_state.df_modelo = None
else:
    st.info("👆 Suba su archivo CSV (Churn_Modelling.csv) para habilitar las demás secciones del dashboard.")
