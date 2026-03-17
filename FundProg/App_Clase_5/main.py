# -*- coding: utf-8 -*-
"""
Clase 5: Errores, Clases y Biblioteca Estándar
Aplicación interactiva de Fundamentos de Programación
"""

import streamlit as st
from utils.theme import inject_theme_styles

st.set_page_config(
    page_title="Clase 5 - Errores, Clases y Biblioteca",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

inject_theme_styles()

st.markdown("""
<div class="main-header">
    <h1>🏦 Clase 5: Errores, Clases y Biblioteca Estándar</h1>
    <p>Fundamentos de Programación - Aplicación Interactiva</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## Bienvenido a la aplicación de la Clase 5")

st.markdown("""
Esta aplicación te permite **aprender, practicar y validar** los conceptos de la Clase 5 de forma interactiva.
Usa el menú lateral para navegar entre los temas.
""")

st.markdown("### 📚 Objetivos de aprendizaje")

objetivos = [
    "Dominar el manejo de errores y excepciones (`try`, `except`, `else`, `finally`)",
    "Crear excepciones personalizadas",
    "Comprender programación orientada a objetos (POO) en Python",
    "Crear clases con métodos especiales (`__init__`, `__str__`, etc.)",
    "Entender herencia, encapsulación y polimorfismo",
    "Explorar la biblioteca estándar de Python",
    "Aplicar conocimientos en un proyecto práctico progresivo"
]

for i, obj in enumerate(objetivos, 1):
    st.markdown(f"""
    <div class="objetivo-card">
        <strong>{i}.</strong> {obj}
    </div>
    """, unsafe_allow_html=True)

st.markdown("### 📋 Estructura de la sesión")

st.markdown("""
| Bloque | Tema |
|--------|------|
| 8 | Errores y excepciones |
| 9 | Clases y POO |
| 10 | Biblioteca estándar |
| — | Proyecto práctico integrador |
""")

st.markdown("---")
st.markdown("""
<div class="app-theme-tip-text">
    💡 <strong>Tip:</strong> En cada página encontrarás teoría ampliada, preguntas de comprensión 
    y un editor de código para practicar y validar tus respuestas.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="app-theme-info-box">
    <strong>🤖 Ejercicio con IA (Clases y POO):</strong> En la página <strong>Clases y POO</strong> encontrarás 
    la pestaña <strong>Ejercicio con IA</strong>, donde te sugerimos usar ChatGPT, Claude o Cursor para desarrollar 
    un ejercicio pequeño sobre clases, paso a paso, con explicación en cada uno. Incluye un prompt listo para copiar.
</div>
""", unsafe_allow_html=True)
