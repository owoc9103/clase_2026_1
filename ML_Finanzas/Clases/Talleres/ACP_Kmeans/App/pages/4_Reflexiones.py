# -*- coding: utf-8 -*-
"""Página 4 — Reflexiones sobre ACP y K-Means."""
import streamlit as st

from styles import apply_styles, render_hero
from utils import init_session, render_progress_sidebar

st.set_page_config(
    page_title="Reflexiones | ML Finanzas",
    page_icon="💡",
    layout="wide",
)

init_session()
apply_styles()
render_progress_sidebar()

render_hero(
    "💡 Reflexiones: ACP y K-Means en Finanzas",
    "Aprendizajes, limitaciones y buenas prácticas del taller",
)

st.markdown("## Síntesis del pipeline")

steps = st.session_state.get("steps_done", {})
if steps.get("kmeans"):
    st.success(
        f"Completaste el análisis completo: **{st.session_state.n_components}** componentes PCA, "
        f"**k = {st.session_state.k_selected}** clusters, "
        f"**{len(st.session_state.df_with_id):,}** empresas segmentadas."
    )
elif steps.get("pca"):
    st.info("Avanzaste hasta el ACP. Ejecuta K-Means y exporta la base para cerrar el ciclo analítico.")
else:
    st.info("Esta página es de cierre conceptual; puedes leerla en cualquier momento del taller.")

st.markdown("---")

# ── ACP ───────────────────────────────────────────────────────────────────────
st.markdown("## 🔬 Reflexiones sobre el ACP (PCA)")

st.markdown(
    """
<div class="reflection-box">
<h3>¿Qué aportó el ACP en este contexto?</h3>
<p>El ACP convirtió un espacio de <strong>decenas de ratios financieros correlacionados</strong> en un conjunto
menor de <strong>componentes ortogonales</strong> que capturan la mayor parte de la variabilidad entre empresas.
En finanzas, muchos indicadores de rentabilidad, liquidez y eficiencia se mueven en conjunto;
el ACP separa esa estructura común en ejes interpretables (PC1, PC2, …).</p>
</div>
""",
    unsafe_allow_html=True,
)

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### ✅ Fortalezas")
    st.markdown(
        """
- **Reducción de ruido y redundancia** entre ratios derivados del mismo estado financiero.
- **Visualización** en 2D/3D que facilita explorar la nube de empresas antes de clusterizar.
- **Interpretabilidad** mediante cargas: saber qué ratios dominan cada componente.
- **Preparación del clustering**: K-Means funciona mejor en pocas dimensiones estables.
"""
    )

with col_b:
    st.markdown("### ⚠️ Limitaciones y cuidados")
    st.markdown(
        """
- Los componentes son **combinaciones lineales**; pueden ser difíciles de traducir a lenguaje de negocio.
- PCA asume **relaciones lineales**; patrones no lineales pueden perderse.
- La **escala importa**: por eso estandarizamos antes del ACP.
- Elegir cuántos componentes conservar es una **decisión analítica**, no automática.
- Outliers extremos (empresas atípicas) pueden distorsionar las primeras componentes.
"""
    )

st.markdown("---")

# ── K-Means ───────────────────────────────────────────────────────────────────
st.markdown("## 🎯 Reflexiones sobre K-Means")

st.markdown(
    """
<div class="reflection-box">
<h3>¿Qué aportó K-Means?</h3>
<p>K-Means particionó el espacio PCA en <strong>grupos disjuntos</strong> de empresas con perfiles similares.
A diferencia de un modelo supervisado, aquí <strong>no hay etiqueta correcta</strong>: la calidad del resultado
depende de la coherencia interna de los clusters y de su utilidad para la decisión de negocio.</p>
</div>
""",
    unsafe_allow_html=True,
)

col_c, col_d = st.columns(2)

with col_c:
    st.markdown("### ✅ Fortalezas")
    st.markdown(
        """
- **Simple y escalable** para miles de observaciones como en `datos_empresas.csv`.
- **Interpretación directa**: cada cluster puede perfilarse con promedios de ratios originales.
- Métricas como **Silhouette** y el **método del codo** orientan la elección de *k*.
- Útil para **segmentación de cartera**, **benchmarking** y **detección de grupos atípicos**.
"""
    )

with col_d:
    st.markdown("### ⚠️ Limitaciones y cuidados")
    st.markdown(
        """
- K-Means asume clusters **esféricos** y de tamaño similar; no siempre refleja la realidad financiera.
- Es **sensible a outliers** y a la inicialización (mitigado con `random_state` y `n_init`).
- La elección de **k es subjetiva**: 3 clusters pueden ser útiles para narrativa, pero no siempre óptimos.
- Clustering en PCA **depende de cuántos componentes** elegiste antes.
- Los clusters **no son estables en el tiempo** si los estados financieros cambian; conviene reentrenar.
"""
    )

st.markdown("---")

# ── Integración ───────────────────────────────────────────────────────────────
st.markdown("## 🔗 Integración ACP + K-Means")

st.markdown(
    """
| Aspecto | ACP | K-Means |
|---------|-----|---------|
| **Rol** | Comprimir e interpretar variabilidad | Agrupar observaciones similares |
| **Salida** | Componentes y cargas | Etiqueta de cluster por empresa |
| **Decisión clave** | Número de componentes | Número de clusters (*k*) |
| **Riesgo principal** | Pérdida de información | Clusters sin sentido de negocio |

**Flujo recomendado post-exportación:**

1. Descarga `empresas_con_clusters.csv`.
2. Cruza **cluster** con variables originales y con el heatmap de medias estandarizadas de la app.
3. Selecciona 3–5 empresas por cluster (p. ej. cercanas al centroide en PCA) y valida si su perfil
   contable coincide con la interpretación del heatmap.
4. Asigna un **nombre de negocio** a cada grupo y documenta qué ratios lo justifican (z-scores).
5. Valida con expertos de dominio antes de usar los clusters en decisiones automatizadas.

**Alternativas a explorar:** DBSCAN (clusters de forma arbitraria), clustering jerárquico
(dendrogramas), o t-SNE/UMAP solo para visualización (no para clustering directo).
"""
)

st.markdown("---")
st.info("👉 Continúa en **Preguntas** para las consignas de discusión del taller.")
st.markdown("### 📚 Referencia del taller")
st.markdown(
    "Este flujo replica la lógica del notebook *Cluster Tarjetas de Crédito (PCA + Kmeans)*, "
    "adaptado al contexto de **segmentación de empresas** con ratios financieros."
)
