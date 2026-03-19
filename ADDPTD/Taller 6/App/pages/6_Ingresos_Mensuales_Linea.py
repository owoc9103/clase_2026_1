# -*- coding: utf-8 -*-
"""
Punto 6: Cómo varían los ingresos mensuales en el período de análisis
Gráfica: Línea
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Punto 6 - Ingresos mensuales", layout="wide")

st.title("📈 Punto 6: Variación de ingresos mensuales en el período de análisis")
st.caption("Indicador: Gráfica de línea | Variables: Fecha, Cantidad de ventas, Precio")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df = df.dropna(subset=['Fecha'])
df['Mes'] = df['Fecha'].dt.to_period('M').astype(str)
df['Ingresos'] = df['Cantidad Ventas'] * df['Precio (MXN)']

mensual = df.groupby('Mes')['Ingresos'].sum().reset_index()
mensual.columns = ['Mes', 'Ingresos_Total']

st.info("📎 **Importante:** Incluya esta gráfica en el documento Word del taller y agregue su interpretación.")

fig = px.line(mensual, x='Mes', y='Ingresos_Total', markers=True,
              title="Evolución de los ingresos mensuales",
              labels={'Ingresos_Total': 'Ingresos (MXN)', 'Mes': 'Mes'})
fig.update_traces(line_color='#2ecc71', line_width=2)
fig.update_layout(height=500)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretación")
st.markdown("""
- La gráfica muestra la **tendencia** de ingresos a lo largo del tiempo.
- Se pueden identificar picos, valles y estacionalidad.
- **Recomendación para el Word:** Copie la gráfica en el documento, describa los meses con mayor y menor ingreso, y plantee posibles causas o decisiones.
""")
