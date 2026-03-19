# -*- coding: utf-8 -*-
"""
Curso: Analítica de Datos para la Toma de Decisiones
Taller 6. Analítica descriptiva: Visualización de datos
"""

import streamlit as st
import pandas as pd
from utils import SESSION_DATA_KEY, _normalize_dataframe, load_default_data

st.set_page_config(
    page_title="Taller 6 - Visualización de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.punto-card {
    background: #e8f4f8;
    color: #1a202c;
    border-left: 4px solid #0ea5e9;
    padding: 1rem 1.25rem;
    margin: 0.6rem 0;
    border-radius: 0 10px 10px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
[data-theme="dark"] .punto-card {
    background: #1e3a5f;
    color: #e2e8f0;
    border-left-color: #38bdf8;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 3rem 2rem; background: linear-gradient(135deg, #0c4a6e 0%, #0ea5e9 50%, #38bdf8 100%); border-radius: 16px; margin-bottom: 2rem;">
    <h1 style="margin: 0; color: white;">📊 Curso: Analítica de Datos para la Toma de Decisiones</h1>
    <p style="margin: 1rem 0 0 0; color: rgba(255,255,255,0.95);">Taller 6. Analítica descriptiva: Visualización de datos</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📁 Cargar el dataset")
st.markdown("Debes cargar el archivo **taller6-dataset_punto_venta.csv** para utilizar la aplicación.")

col_btn, col_up = st.columns([1, 3])
with col_btn:
    if st.button("📂 Cargar datos por defecto", use_container_width=True):
        df = load_default_data()
        if df is not None:
            st.session_state[SESSION_DATA_KEY] = df
            st.success("✅ Datos cargados.")
            st.rerun()
        else:
            st.error("No se encontró el CSV en Insumos/.")

archivo = st.file_uploader(
    "O sube tu archivo CSV",
    type=["csv"],
    help="Archivo: taller6-dataset_punto_venta.csv"
)

if archivo is not None:
    try:
        df = pd.read_csv(archivo)
        df = _normalize_dataframe(df)
        if df is not None:
            st.session_state[SESSION_DATA_KEY] = df
            st.success(f"✅ Archivo cargado. {len(df):,} registros.")
            with st.expander("Vista previa"):
                st.dataframe(df.head(10), use_container_width=True)
        else:
            st.error("El archivo debe tener la columna 'Fecha'.")
    except Exception as e:
        st.error(f"Error al leer: {e}")
elif SESSION_DATA_KEY not in st.session_state or st.session_state[SESSION_DATA_KEY] is None:
    st.info("💡 Sube el CSV o haz clic en «Cargar datos por defecto».")

st.markdown("### 📋 Puntos del Taller")
puntos = [
    ("Punto 1", "Estadísticas del rating (promedio, desviación estándar, CV)"),
    ("Punto 2", "Suma total de cantidad de ventas en los últimos 225 días"),
    ("Punto 3", "Precio promedio, mínimo y máximo"),
    ("Punto 4", "Distribución de ventas por mes - Barras apiladas"),
    ("Punto 5", "Relación ingresos vs ventas - Gráfica combinada"),
    ("Punto 6", "Variación de ingresos mensuales - Gráfica de línea"),
    ("Punto 7", "Ventas por línea y tipo de producto"),
    ("Punto 8", "Distribución de ventas por fecha"),
    ("Punto 9", "Catálogo dinámico - Productos más vendidos"),
    ("Punto 10", "Catálogo con filtros (colores, precio, grosor, rating)"),
]
for titulo, desc in puntos:
    st.markdown(f'<div class="punto-card"><strong>{titulo}</strong>: {desc}</div>', unsafe_allow_html=True)

st.markdown("---")
st.info("💡 En cada página, exporta las gráficas (PNG) e inclúyelas en tu documento Word con tu interpretación.")
