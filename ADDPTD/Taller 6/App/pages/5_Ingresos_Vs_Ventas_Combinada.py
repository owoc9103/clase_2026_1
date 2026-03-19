# -*- coding: utf-8 -*-
"""
Punto 5: Relación entre ingresos totales y cantidad de ventas por mes
Gráfica combinada (línea y barras)
"""
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from utils import load_data

st.set_page_config(page_title="Punto 5 - Ingresos vs Ventas", layout="wide")

st.title("📊 Punto 5: Relación entre ingresos totales y cantidad de ventas por mes")
st.caption("Indicador: Gráfica combinada (línea y barras) | Variables: Fecha, Cantidad de ventas, Precio")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

# Convertir Fecha y calcular agregados por mes
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df = df.dropna(subset=['Fecha'])
df['Mes'] = df['Fecha'].dt.to_period('M').astype(str)
df['Ingresos'] = df['Cantidad Ventas'] * df['Precio (MXN)']

mensual = df.groupby('Mes').agg(
    Ingresos_Total=('Ingresos', 'sum'),
    Cantidad_Ventas=('Cantidad Ventas', 'sum')
).reset_index()

st.info("📎 **Importante:** Incluya esta gráfica en el documento Word del taller y agregue su interpretación.")

fig = make_subplots(specs=[[{"secondary_y": True}]])
fig.add_trace(
    go.Bar(x=mensual['Mes'], y=mensual['Cantidad_Ventas'], name="Cantidad de ventas", marker_color='#3498db'),
    secondary_y=False
)
fig.add_trace(
    go.Scatter(x=mensual['Mes'], y=mensual['Ingresos_Total'], name="Ingresos totales (MXN)", 
               line=dict(color='#e74c3c', width=3), mode='lines+markers'),
    secondary_y=True
)
fig.update_layout(
    title="Relación: Ingresos totales vs Cantidad de ventas por mes",
    xaxis_title="Mes",
    height=500,
    showlegend=True
)
fig.update_yaxes(title_text="Cantidad de ventas", secondary_y=False)
fig.update_yaxes(title_text="Ingresos (MXN)", secondary_y=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretación")
st.markdown("""
- **Barras (azul):** Representan la cantidad total de ventas por mes.
- **Línea (roja):** Representa los ingresos totales (cantidad × precio) por mes.
- Permite ver si meses con más ventas generan más ingresos y si hay patrones de precio (productos más caros en ciertos meses).
- **Recomendación para el Word:** Copie la gráfica, pegue en el documento y redacte una conclusión breve sobre la relación observada.
""")
