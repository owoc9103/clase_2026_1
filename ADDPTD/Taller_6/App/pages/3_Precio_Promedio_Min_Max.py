# -*- coding: utf-8 -*-
"""Punto 3: Precio promedio, mínimo y máximo de los productos."""

import streamlit as st
from utils import load_data

st.set_page_config(page_title="Punto 3 - Precios", page_icon="💰", layout="wide")

st.markdown("## Punto 3: Estadísticas de Precios")

st.markdown("""
**Pregunta del taller:** ¿Cuál es el precio promedio, mínimo y máximo de los productos?

**Indicador:** Precio promedio, mínimo y máximo.  
**Variable:** Precio.
""")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.stop()

precio = df["Precio (MXN)"].dropna()
promedio = precio.mean()
minimo = precio.min()
maximo = precio.max()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Precio promedio (MXN)", f"${promedio:,.2f}")
with col2:
    st.metric("Precio mínimo (MXN)", f"${minimo:,.2f}")
with col3:
    st.metric("Precio máximo (MXN)", f"${maximo:,.2f}")

import plotly.express as px
fig = px.box(df, y="Precio (MXN)", title="Distribución de precios de los productos (MXN)")
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 📝 Interpretación
El rango entre mínimo y máximo indica la amplitud de la oferta de precios. El promedio ayuda a entender el 
nivel típico de precios. Esta información es clave para estrategias de precios y promociones.
""")
