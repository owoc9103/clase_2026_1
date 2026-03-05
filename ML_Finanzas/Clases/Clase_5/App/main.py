"""
German Credit - Predicción de Riesgo de Crédito
Dashboard gerencial para apoyo en decisiones de asignación de crédito.
"""
import streamlit as st
from utils_data import parse_uploaded_csv, prepare_model_data

st.set_page_config(
    page_title="German Credit - Asignación de Crédito",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar sesión
if "df_raw" not in st.session_state:
    st.session_state.df_raw = None
    st.session_state.df_modelo = None

# === INICIO - MENSAJE GERENCIAL ===
st.title("🏦 Dashboard de Asignación de Crédito")
st.markdown("---")

st.markdown("""
### Resumen Ejecutivo

Se ha realizado el **cierre mensual de clientes** junto con la consolidación de las **solicitudes de crédito** 
recibidas durante el período. La compañía debe tomar la **decisión estratégica clave**: determinar a cuáles 
solicitantes se les aprueba el crédito y a cuáles se les rechaza, equilibrando crecimiento comercial, rentabilidad y riesgo.

Para respaldar esta decisión, se ha desarrollado un **modelo de regresión logística** que estima la probabilidad de 
que un solicitante sea **buen pagador (good)** o **mal pagador (bad)**, a partir de variables demográficas, 
financieras y de comportamiento registradas en el sistema.

**Pasos sugeridos:**
1. **Cargar los datos** en esta sección.
2. Revisar el **contexto** del problema y las variables.
3. Explorar el **análisis descriptivo** (univariado, bivariado y tablas de contingencia).
4. Usar la **modelación** y la calculadora para estimar el riesgo de cada solicitante.
""")

st.markdown("---")
st.subheader("📂 Cargar archivo de datos")

uploaded = st.file_uploader(
    "Suba el archivo **german_credit_data.csv** con las solicitudes de crédito",
    type=["csv"],
    help="Formato: Age, Sex, Job, Housing, Saving accounts, Checking account, Credit amount, Duration, Purpose, Risk"
)

if uploaded is not None:
    try:
        df_raw = parse_uploaded_csv(uploaded)
        df_modelo = prepare_model_data(df_raw)
        st.session_state.df_raw = df_raw
        st.session_state.df_modelo = df_modelo
        st.success(f"✅ **Datos cargados:** {len(df_raw):,} solicitudes × {len(df_raw.columns)} variables")
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
    st.info("👆 Suba su archivo CSV para habilitar las demás secciones del dashboard.")
