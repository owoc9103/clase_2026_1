# -*- coding: utf-8 -*-
"""
Punto 7: Ventas por línea y tipo de producto
Gráfica: Barras o árbol
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.set_page_config(page_title="Punto 7 - Ventas por línea/tipo", layout="wide")

st.title("📦 Punto 7: Ventas por línea y tipo de producto")
st.caption("Indicador: Gráfica de barras o árbol | Variables: ID producto, Nombre producto, Cantidad de ventas")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

by_tipo = df.groupby('Nombre Producto')['Cantidad Ventas'].sum().reset_index()
by_tipo = by_tipo.sort_values('Cantidad Ventas', ascending=True)

st.info("📎 **Importante:** Incluya la gráfica seleccionada en el documento Word del taller y agregue su interpretación.")

tipo_grafica = st.radio("Tipo de gráfica", ["Barras horizontales", "Barras verticales", "Treemap (árbol)"], horizontal=True)

if tipo_grafica == "Barras horizontales":
    fig = px.bar(by_tipo, x='Cantidad Ventas', y='Nombre Producto', orientation='h',
                 title="Ventas por tipo de producto",
                 labels={'Cantidad Ventas': 'Cantidad de ventas', 'Nombre Producto': 'Tipo/Línea de producto'})
    fig.update_layout(height=450)
elif tipo_grafica == "Barras verticales":
    fig = px.bar(by_tipo, x='Nombre Producto', y='Cantidad Ventas',
                 title="Ventas por tipo de producto",
                 labels={'Cantidad Ventas': 'Cantidad de ventas', 'Nombre Producto': 'Tipo/Línea de producto'})
    fig.update_xaxis(tickangle=-45)
    fig.update_layout(height=500)
else:
    fig = px.treemap(by_tipo, path=['Nombre Producto'], values='Cantidad Ventas',
                     title="Ventas por tipo de producto (Treemap)")
    fig.update_layout(height=500)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretación")
st.markdown("""
- Se identifica qué **líneas o tipos de producto** venden más y cuáles menos.
- Útil para priorizar reposición e inventario.
- **Recomendación para el Word:** Copie la gráfica elegida y redacte conclusiones sobre los productos más y menos vendidos.
""")
