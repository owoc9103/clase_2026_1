# -*- coding: utf-8 -*-
"""Punto 4: Distribución de ventas por mes - Barras apiladas."""

import streamlit as st
import pandas as pd
from utils import load_data

st.set_page_config(page_title="Punto 4 - Ventas por mes", page_icon="📊", layout="wide")

st.markdown("## Punto 4: Distribución de Ventas por Mes y Cantidad de Piezas")

st.markdown("""
**Pregunta del taller:** ¿Cómo se distribuye la cantidad total de ventas por mes y por cantidad de piezas?

**Gráfica:** Barras apiladas.  
**Variables:** Fecha, Cantidad de ventas.
""")

st.warning("⚠️ **Importante:** Lleva la gráfica o solución a tu documento Word y **siempre interpreta** los resultados.")

df = load_data()
if df is None:
    st.stop()

df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
df = df.dropna(subset=["Fecha"])
df["Mes"] = df["Fecha"].dt.to_period("M").astype(str)
df["Año"] = df["Fecha"].dt.year

ventas_mes = df.groupby("Mes").agg({"Cantidad Ventas": "sum"}).reset_index()

import plotly.express as px
fig = px.bar(ventas_mes, x="Mes", y="Cantidad Ventas",
             title="Cantidad total de ventas por mes",
             labels={"Cantidad Ventas": "Cantidad de ventas", "Mes": "Mes"})
st.plotly_chart(fig, use_container_width=True)

bins = [0, 20, 50, 100, 500]
labels = ["1-20", "21-50", "51-100", ">100"]
df["Rango piezas"] = pd.cut(df["Cantidad Ventas"], bins=bins, labels=labels, include_lowest=True)
ventas_apiladas = df.groupby(["Mes", "Rango piezas"]).agg({"Cantidad Ventas": "sum"}).reset_index()

fig2 = px.bar(ventas_apiladas, x="Mes", y="Cantidad Ventas", color="Rango piezas",
              title="Barras apiladas: Ventas por mes y rango de cantidad de piezas",
              barmode="stack")
fig2.update_layout(yaxis_title="Cantidad de ventas")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
### 📝 Interpretación
Las barras apiladas permiten ver la composición de las ventas por mes según el tamaño de cada transacción.
Así se identifican patrones estacionales y si predominan ventas pequeñas o grandes.
""")
