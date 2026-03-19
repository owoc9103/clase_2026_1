# -*- coding: utf-8 -*-
"""
Punto 8: Distribución de ventas totales por fecha
Gráfica: Línea o barras
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Punto 8 - Ventas por fecha", layout="wide")

st.title("📅 Punto 8: Distribución de ventas totales por fecha")
st.caption("Indicador: Gráfica de línea o barras | Variables: Fecha, Cantidad de ventas")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df = df.dropna(subset=['Fecha'])
by_fecha = df.groupby('Fecha')['Cantidad Ventas'].sum().reset_index()
by_fecha = by_fecha.sort_values('Fecha')

st.info("📎 **Importante:** Incluya la gráfica seleccionada en el documento Word del taller y agregue su interpretación.")

tipo = st.radio("Tipo de gráfica", ["Línea", "Barras"], horizontal=True)

if tipo == "Línea":
    fig = px.line(by_fecha, x='Fecha', y='Cantidad Ventas', markers=True,
                  title="Ventas totales por fecha",
                  labels={'Cantidad Ventas': 'Cantidad de ventas'})
    fig.update_traces(line_color='#9b59b6')
else:
    fig = px.bar(by_fecha, x='Fecha', y='Cantidad Ventas',
                 title="Ventas totales por fecha",
                 labels={'Cantidad Ventas': 'Cantidad de ventas'})
fig.update_layout(height=500)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretación")
st.markdown("""
- La gráfica muestra la evolución **diaria** de las ventas.
- Permite identificar días pico, tendencias y posibles anomalías.
- **Recomendación para el Word:** Copie la gráfica y explique los patrones observados (días de mayor venta, estacionalidad, etc.).
""")
