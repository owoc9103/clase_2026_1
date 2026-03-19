# -*- coding: utf-8 -*-
"""Punto 1: Promedio, desviación estándar y coeficiente de variación del rating."""

import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Punto 1 - Estadísticas del Rating", page_icon="📊", layout="wide")

st.markdown("## Punto 1: Estadísticas del Rating de Productos")

st.markdown("""
**Pregunta del taller:** ¿Cuál es el promedio, desviación estándar y coeficiente de variación del rating de los productos?

**Indicador:** Promedio, desviación estándar y coeficiente de variación del rating.  
**Variable:** Calificación promedio del cliente.
""")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.stop()

rating_col = "Rating (Promedio)"
rating = df[rating_col].dropna()

promedio = rating.mean()
desv_std = rating.std()
cv = (desv_std / promedio * 100) if promedio != 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Promedio del rating", f"{promedio:.3f}")
with col2:
    st.metric("Desviación estándar", f"{desv_std:.3f}")
with col3:
    st.metric("Coeficiente de variación (%)", f"{cv:.2f}%")

st.markdown("---")
st.markdown("### 📊 Visualización: Distribución del Rating")

import plotly.express as px
fig = px.histogram(df, x=rating_col, nbins=30, title="Distribución de la calificación promedio de los productos",
                   labels={rating_col: "Rating (Promedio)"})
fig.update_layout(yaxis_title="Frecuencia")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 📝 Interpretación
El **promedio** indica la calificación típica que reciben los productos. La **desviación estándar** mide la dispersión 
de las calificaciones. El **coeficiente de variación** permite comparar la variabilidad relativa independientemente 
de la escala. Un CV alto sugiere mayor heterogeneidad en las opiniones de los clientes entre productos.
""")
