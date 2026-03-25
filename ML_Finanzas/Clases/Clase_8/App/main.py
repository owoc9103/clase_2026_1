# -*- coding: utf-8 -*-
"""
Clase 7 - K-Nearest Neighbors (KNN) para Regresión
Machine Learning en Finanzas
"""

import streamlit as st

st.set_page_config(
    page_title="KNN para Regresión - ML Finanzas",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<div style="
    text-align: center;
    padding: 2.5rem 2rem;
    background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
    border-radius: 12px;
    margin-bottom: 2rem;
    color: white;
">
    <h1 style="margin: 0; font-size: 2rem;">📈 K-Nearest Neighbors (KNN) para Regresión</h1>
    <p style="margin: 1rem 0 0 0; font-size: 1.2rem;">Clase 7 - Machine Learning en Finanzas</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Bienvenido")

st.markdown("""
Esta aplicación presenta el algoritmo **K-Nearest Neighbors (KNN)** con **énfasis en regresión**.

**Contenido:**
- **Teoría:** Conceptos detallados de KNN, regresor vs clasificador, métricas, distancias y escalado
- **Ejemplo trivial:** Un ejemplo numérico paso a paso para identificar y entender la lógica del algoritmo
- **KNN Regresor:** Implementación con precios de boletos aéreos — bloques para copiar en Google Colab

Usa el menú lateral para navegar.
""")

st.markdown("### 📋 Estructura")

st.markdown("""
| Página | Contenido |
|--------|-----------|
| **1. Teoría KNN** | Conceptos completos, regresor vs clasificador, métricas, distancias, escalado |
| **2. Ejemplo trivial** | Ejemplo numérico paso a paso para entender la lógica de KNN regresión |
| **3. KNN Regresor** | Predicción precios boletos aéreos — bloques para copiar en Google Colab |
""")

st.info("💡 **Tip:** Los bloques de código están en secciones desplegables (haz clic para expandir). Cada uno tiene botón para copiar.")
