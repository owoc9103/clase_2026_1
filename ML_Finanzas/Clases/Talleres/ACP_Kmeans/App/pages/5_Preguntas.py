# -*- coding: utf-8 -*-
"""Página 5 — Preguntas de cierre sobre ACP y K-Means."""
import streamlit as st

from styles import apply_styles, render_hero
from utils import init_session, render_progress_sidebar

st.set_page_config(
    page_title="Preguntas | ML Finanzas",
    page_icon="❓",
    layout="wide",
)

init_session()
apply_styles()
render_progress_sidebar()

render_hero(
    "❓ Preguntas",
    "Consignas para discutir el ACP y K-Means en el contexto de segmentación de empresas",
)

st.markdown(
    """
<div class="reflection-box">
<p>Responde apoyándote en tus resultados en la app: preprocesamiento, ACP, heatmaps de cargas,
scatter PCA, diagnóstico de <em>k</em>, heatmap de medias estandarizadas por cluster y archivo
<code>empresas_con_clusters.csv</code>.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("---")
st.markdown("## Preguntas del taller")

st.markdown(
    """
1. ¿Por qué es importante estandarizar los ratios financieros antes de aplicar ACP en una base
   con empresas de diferentes tamaños?

2. Si el ACP permite reducir cerca de 80 ratios financieros a pocos componentes principales,
   ¿qué ventaja tiene esto para el análisis y qué información podría perderse?

3. Al observar las cargas de PC1 y PC2, ¿cómo se puede interpretar cada componente desde una
   perspectiva financiera, por ejemplo, liquidez, rentabilidad, apalancamiento o eficiencia?

4. Si una empresa tiene un valor alto en PC1, ¿qué significa esto en términos de los ratios que
   tienen mayor carga positiva o negativa en ese componente?

5. ¿Qué criterios usarías para decidir cuántos componentes principales conservar antes de aplicar
   K-Means: varianza explicada acumulada, interpretabilidad financiera o visualización de los datos?

6. Al comparar el método del codo y el índice de silueta, ¿qué criterio debería pesar más para
   escoger el número de clusters: la mejor métrica estadística o la utilidad práctica para
   segmentar empresas?

7. Si el método del codo sugiere *k* = 4, pero la silueta es mayor en *k* = 2, ¿cuál escogerías
   y cómo justificarías esa decisión ante un comité financiero?

8. ¿Qué significa que los clusters se vean solapados en el plano PC1–PC2? ¿Esto indica
   necesariamente que el modelo de K-Means es malo?

9. Escoge los **dos clusters** que más te llamen la atención. Para cada uno, realiza un **perfil
   financiero** teniendo en cuenta los ratios más relevantes del heatmap de medias estandarizadas.
   Luego, resalta qué es lo más importante de cada grupo desde el punto de vista empresarial o
   financiero.

10. ¿Qué decisiones de negocio podrían apoyarse en la segmentación obtenida con K-Means, y qué
    decisiones **no** deberían tomarse únicamente con este resultado?
"""
)

st.markdown("---")
st.info("💡 Revisa **Reflexiones** para el marco conceptual (fortalezas, limitaciones e integración ACP + K-Means).")
