# -*- coding: utf-8 -*-
"""
Punto 9: Catálogo dinámico - Características de los productos más vendidos
"""
import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Punto 9 - Catálogo productos más vendidos", layout="wide")

st.title("📋 Punto 9: Catálogo dinámico – Productos más vendidos")
st.caption("Actividad: Crear un catálogo dinámico | Variables: ID producto, Nombre producto, Precio, Grosor, Calificación promedio")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

# Agregar total ventas por producto (ID) manteniendo características
productos = df.groupby(['ID Producto', 'Nombre Producto', 'Precio (MXN)', 'Grosor (cm)', 'Rating (Promedio)']).agg(
    Total_Ventas=('Cantidad Ventas', 'sum')
).reset_index()
productos = productos.sort_values('Total_Ventas', ascending=False)

st.info("📎 **Importante:** Incluya capturas o tabla del catálogo en el documento Word y agregue su interpretación.")

# Filtro por cantidad de productos a mostrar
n = st.slider("Mostrar top N productos más vendidos", 10, 50, 20)
top = productos.head(n)

st.subheader(f"Top {n} productos más vendidos")
st.dataframe(
    top.style.format({'Precio (MXN)': '{:.0f}', 'Grosor (cm)': '{:.1f}', 'Rating (Promedio)': '{:.1f}'}),
    use_container_width=True,
    height=400
)

st.subheader("Interpretación")
st.markdown("""
- Este catálogo permite ver **línea, precio, grosor y rating** de los productos más vendidos.
- Use esta información para priorizar reposición y promoción.
- **Recomendación para el Word:** Exporte o capture la tabla, inclúyala en el documento y describa las características dominantes de los productos más vendidos.
""")
