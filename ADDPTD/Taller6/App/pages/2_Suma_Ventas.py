# -*- coding: utf-8 -*-
"""Punto 2: Suma total de ventas en los últimos 225 días."""

import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Punto 2 - Suma de Ventas", page_icon="📈", layout="wide")

st.markdown("## Punto 2: Suma Total de Ventas")

st.markdown("""
**Pregunta del taller:** ¿Cuál es la suma total de la cantidad de ventas en los últimos 225 días?

**Indicador:** Suma de ventas.  
**Variable:** Cantidad de ventas.
""")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.stop()

df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df = df.dropna(subset=["Fecha"])
fecha_max = df["Fecha"].max()
fecha_limite = fecha_max - pd.Timedelta(days=225)
df_225 = df[df["Fecha"] >= fecha_limite]

suma_ventas = df_225["Cantidad Ventas"].sum()
st.metric("Suma total de ventas (últimos 225 días)", f"{int(suma_ventas):,}")
st.caption(f"Período: {fecha_limite.strftime('%Y-%m-%d')} a {fecha_max.strftime('%Y-%m-%d')}")

import plotly.express as px
fig = px.pie(values=[suma_ventas], names=["Total ventas"], title="Representación del total de ventas (últimos 225 días)",
             color_discrete_sequence=["#1e3a5f"])
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 📝 Interpretación
La suma total de ventas representa el volumen total de unidades vendidas en el período analizado. Este indicador 
es fundamental para planificar el reabastecimiento y evaluar el desempeño general del punto de venta.
""")
