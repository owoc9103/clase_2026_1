# -*- coding: utf-8 -*-
"""
Punto 10: Catálogo dinámico con filtros por colores, precio, grosor y rating
"""
import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Punto 10 - Catálogo con filtros", layout="wide")

st.title("🎛️ Punto 10: Catálogo dinámico con filtros")
st.caption("Actividad: Crear catálogo con filtros | Variables: Colores disponibles, Precio, Grosor, Calificación promedio")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.error("No se pudo cargar el dataset. Verifique la ruta del archivo.")
    st.stop()

# Productos únicos con características (tomamos el primer registro por ID para evitar duplicados)
productos = df.drop_duplicates(subset=['ID Producto'])[
    ['ID Producto', 'Nombre Producto', 'Colores Disponibles', 'Precio (MXN)', 'Grosor (cm)', 'Rating (Promedio)']
].copy()

ventas_totales = df.groupby('ID Producto')['Cantidad Ventas'].sum().reset_index()
ventas_totales.columns = ['ID Producto', 'Total_Ventas']
productos = productos.merge(ventas_totales, on='ID Producto')

st.info("📎 **Importante:** Incluya capturas del catálogo filtrado en el documento Word y agregue su interpretación.")

with st.sidebar:
    st.header("Filtros")
    
    # Filtro por color (extraer colores únicos)
    colores_texto = productos['Colores Disponibles'].dropna().astype(str)
    todos_colores = set()
    for c in colores_texto:
        todos_colores.update(x.strip() for x in c.replace(',', ' ').split())
    opciones_color = ['Todos'] + sorted(todos_colores)
    color_sel = st.selectbox("Color disponible", opciones_color)
    
    precio_min, precio_max = productos['Precio (MXN)'].min(), productos['Precio (MXN)'].max()
    rango_precio = st.slider("Rango de precio (MXN)", float(precio_min), float(precio_max), (float(precio_min), float(precio_max)))
    
    grosor_min, grosor_max = productos['Grosor (cm)'].min(), productos['Grosor (cm)'].max()
    rango_grosor = st.slider("Rango de grosor (cm)", float(grosor_min), float(grosor_max), (float(grosor_min), float(grosor_max)))
    
    rating_min, rating_max = productos['Rating (Promedio)'].min(), productos['Rating (Promedio)'].max()
    rango_rating = st.slider("Rango de rating", float(rating_min), float(rating_max), (float(rating_min), float(rating_max)))

# Aplicar filtros
filtrado = productos.copy()
filtrado = filtrado[
    (filtrado['Precio (MXN)'] >= rango_precio[0]) & (filtrado['Precio (MXN)'] <= rango_precio[1]) &
    (filtrado['Grosor (cm)'] >= rango_grosor[0]) & (filtrado['Grosor (cm)'] <= rango_grosor[1]) &
    (filtrado['Rating (Promedio)'] >= rango_rating[0]) & (filtrado['Rating (Promedio)'] <= rango_rating[1])
]
if color_sel != 'Todos':
    filtrado = filtrado[filtrado['Colores Disponibles'].astype(str).str.upper().str.contains(color_sel.upper(), na=False)]

st.subheader(f"Productos que cumplen los filtros ({len(filtrado)} resultados)")
st.dataframe(
    filtrado.style.format({'Precio (MXN)': '{:.0f}', 'Grosor (cm)': '{:.1f}', 'Rating (Promedio)': '{:.1f}'}),
    use_container_width=True,
    height=450
)

st.subheader("Interpretación")
st.markdown("""
- Los filtros permiten al cliente explorar productos según **colores, precio, grosor y rating**.
- Use esta interfaz para facilitar la decisión de compra y la gestión del inventario.
- **Recomendación para el Word:** Incluya capturas del catálogo con diferentes filtros aplicados y explique cómo ayudan a la toma de decisiones.
""")
