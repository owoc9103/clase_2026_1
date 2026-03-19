# -*- coding: utf-8 -*-
"""
Curso: Analítica de Datos para la Toma de Decisiones
Taller 6. Analítica descriptiva: Visualización de datos
Página principal
"""

import streamlit as st
import pandas as pd
from utils import SESSION_DATA_KEY, _normalize_dataframe, _get_excel_engine, load_default_data

st.set_page_config(
    page_title="Taller 6 - Visualización de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS para tarjetas legibles en tema claro y oscuro
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
    transition: transform 0.15s ease;
}
.punto-card:hover {
    transform: translateX(4px);
}
[data-theme="dark"] .punto-card {
    background: #1e3a5f;
    color: #e2e8f0;
    border-left-color: #38bdf8;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    padding: 3rem 2rem;
    background: linear-gradient(135deg, #0c4a6e 0%, #0ea5e9 50%, #38bdf8 100%);
    border-radius: 16px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 40px rgba(14, 165, 233, 0.25);
">
    <h1 style="margin: 0; font-size: 2rem; color: white; text-shadow: 0 1px 2px rgba(0,0,0,0.2);">
        📊 Curso: Analítica de Datos para la Toma de Decisiones
    </h1>
    <p style="margin: 1rem 0 0 0; font-size: 1.3rem; color: rgba(255,255,255,0.95);">
        Taller 6. Analítica descriptiva: Visualización de datos
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🌟 Bienvenido")

st.markdown("""
Esta aplicación permite dar respuesta a cada uno de los puntos del Taller 6, utilizando 
el dataset **taller6-dataset_punto_venta.xlsx** sobre análisis de inventarios en punto de venta.

**Importante:** En cada punto deberás:
1. **Llevar la gráfica o solución al documento Word** del taller
2. **Interpretar** los resultados y plantear conclusiones para la toma de decisiones

Usa el menú lateral para navegar a cada punto del taller.
""")

# Requisito: cargar el archivo del dataset
st.markdown("### 📁 Requisito: Cargar el dataset")
st.markdown("Puedes **subir el archivo** (Excel o CSV) o usar los **datos por defecto** del taller.")

col_btn, col_upload = st.columns([1, 3])
with col_btn:
    if st.button("📂 Cargar datos por defecto", use_container_width=True):
        df_default = load_default_data()
        if df_default is not None:
            st.session_state[SESSION_DATA_KEY] = df_default
            st.success("✅ Datos cargados.")
            if hasattr(st, "rerun"):
                st.rerun()
            else:
                st.experimental_rerun()
        else:
            st.error("No se encontró el archivo de datos. Revisa que exista Insumos/taller6-dataset_punto_venta.csv")

archivo = st.file_uploader(
    "O sube tu archivo (Excel o CSV)",
    type=["xlsx", "xls", "csv"],
    help="Acepta taller6-dataset_punto_venta.xlsx o .csv"
)

if archivo is not None:
    nombre = archivo.name.lower()
    df = None
    try:
        if nombre.endswith(".csv"):
            df = pd.read_csv(archivo)
        else:
            engine = _get_excel_engine()
            if engine is None:
                st.warning(
                    "No hay librería para leer Excel. **Opciones:** 1) Usa el botón «Cargar datos por defecto», "
                    "2) Sube el archivo en formato CSV, o 3) Ejecuta: `pip install openpyxl`"
                )
            else:
                df = pd.read_excel(archivo, engine=engine)
        if df is not None:
            df = _normalize_dataframe(df)
            if df is not None:
                st.session_state[SESSION_DATA_KEY] = df
                st.success(f"✅ Archivo cargado correctamente. {len(df):,} registros disponibles.")
                with st.expander("Ver vista previa de los datos"):
                    st.dataframe(df.head(10), use_container_width=True)
            else:
                st.error("El archivo no tiene la columna 'Fecha' requerida.")
        elif not nombre.endswith(".csv"):
            st.error("Error al leer el archivo Excel. Prueba subiendo el CSV o usa «Cargar datos por defecto».")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
elif SESSION_DATA_KEY not in st.session_state or st.session_state[SESSION_DATA_KEY] is None:
    st.info("💡 Sube un archivo o haz clic en «Cargar datos por defecto» para comenzar.")

st.markdown("### 📋 Puntos del Taller")

puntos = [
    ("Punto 1", "Estadísticas del rating (promedio, desviación estándar, CV)"),
    ("Punto 2", "Suma total de cantidad de ventas en los últimos 225 días"),
    ("Punto 3", "Precio promedio, mínimo y máximo de los productos"),
    ("Punto 4", "Distribución de ventas por mes - Barras apiladas"),
    ("Punto 5", "Relación ingresos totales vs cantidad de ventas - Gráfica combinada"),
    ("Punto 6", "Variación de ingresos mensuales - Gráfica de línea"),
    ("Punto 7", "Ventas por línea y tipo de producto - Barras o árbol"),
    ("Punto 8", "Distribución de ventas totales por fecha"),
    ("Punto 9", "Catálogo dinámico - Productos más vendidos"),
    ("Punto 10", "Catálogo interactivo con filtros (colores, precio, grosor, rating)"),
]

for i, (titulo, desc) in enumerate(puntos, 1):
    st.markdown(
        f'<div class="punto-card"><strong>{titulo}</strong>: {desc}</div>',
        unsafe_allow_html=True
    )

st.markdown("---")
st.info("💡 **Recordatorio:** En cada página encontrarás visualizaciones **Plotly** listas para exportar. Usa el menú de cada gráfico (arriba a la derecha) para descargarla como PNG y pegarla en tu documento Word. No olvides incluir tu interpretación.")
