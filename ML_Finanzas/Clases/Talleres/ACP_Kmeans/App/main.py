# -*- coding: utf-8 -*-
"""
ACP + K-Means — Segmentación de empresas
Página de inicio: contexto, carga de datos y preprocesamiento.
"""
import streamlit as st

from styles import apply_styles, render_hero
from utils import (
    VARIABLE_GROUPS,
    detect_id_column,
    init_session,
    read_uploaded_csv,
    render_progress_sidebar,
    reset_analysis_state,
    run_preprocessing,
)

st.set_page_config(
    page_title="Inicio | ACP + K-Means",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()
apply_styles()

with st.sidebar:
    render_progress_sidebar()

render_hero(
    "📊 Segmentación de Empresas con ACP + K-Means",
    "Machine Learning en Economía y Finanzas — Pontificia Universidad Javeriana",
)

# ── Contextualización ────────────────────────────────────────────────────────
st.markdown("## Contexto del problema")

st.markdown(
    """
<div class="context-box">
<h3>¿Qué es esta base de datos?</h3>
<p>La base <code>datos_empresas.csv</code> consolida información <strong>financiera y estructural</strong>
de aproximadamente <strong>2.620 empresas</strong>. Cada fila corresponde a una observación única
(identificada por <code>empresa_id</code>) y cada columna resume un atributo codificado numéricamente
del negocio. El archivo utiliza separador <code>;</code> y está pensado para análisis multivariado
de perfiles corporativos.</p>

<h4>1. Atributos identificadores y sectoriales</h4>
<p>Describen <em>quién es</em> la empresa y en qué contexto opera. Entre las variables más relevantes:</p>
<ul>
<li><code>sector</code>, <code>sector_naics_2digitos</code>, <code>sector_naics_3digitos</code>,
<code>naics_principal_codificado</code> — clasificación industrial (NAICS).</li>
<li><code>numero_empleados</code>, <code>forma_legal</code>, <code>multiples_industrias</code> —
tamaño y estructura organizacional.</li>
<li><code>anio</code>, <code>fecha_constitucion_1</code>, <code>fecha_constitucion_2</code>,
<code>estado_operativo</code> — antigüedad y situación operativa.</li>
</ul>

<h4>2. Ratios financieros estandarizados</h4>
<p>La mayor parte de la base (~80 indicadores) proviene de estados financieros expresados como
<strong>ratios relativos</strong>, lo que permite comparar empresas de distintos tamaños y sectores
en una escala homogénea. Se agrupan así:</p>

<p><strong>Liquidez y solvencia</strong> — capacidad de cubrir obligaciones de corto plazo:</p>
<ul>
<li><code>efectivo_sobre_ventas</code>, <code>efectivo_sobre_activos_totales</code></li>
<li><code>activos_corrientes_sobre_pasivos_corto_plazo</code>, <code>activos_rapidos_sobre_ingresos_operativos</code></li>
<li><code>pasivos_corto_plazo_sobre_activos_totales</code></li>
</ul>

<p><strong>Rentabilidad y margen operativo</strong> — eficiencia en la generación de utilidades:</p>
<ul>
<li><code>ebit_sobre_activos_totales</code>, <code>ebit_sobre_ingresos_operativos</code></li>
<li><code>utilidad_neta_sobre_patrimonio</code> (ROE), <code>utilidad_neta_sobre_activos_totales</code> (ROA)</li>
<li><code>utilidad_bruta_sobre_ingresos_operativos</code>, <code>ebitda_sobre_activos_totales</code></li>
</ul>

<p><strong>Eficiencia operativa y capital de trabajo</strong> — gestión de inventarios, cobranza y ciclo operativo:</p>
<ul>
<li><code>capital_trabajo</code>, <code>capital_trabajo_sobre_ventas</code>, <code>capital_trabajo_sobre_patrimonio</code></li>
<li><code>inventarios_sobre_ingresos_operativos</code>, <code>ciclo_conversion_efectivo</code>, <code>ciclo_operativo</code></li>
<li><code>dias_rotacion_cuentas_por_cobrar</code>, <code>dias_rotacion_pasivos_corto_plazo</code></li>
</ul>

<p><strong>Apalancamiento, flujo de caja e ingresos</strong> — estructura de deuda y generación de caja:</p>
<ul>
<li><code>flujo_caja_sobre_ingresos_operativos</code>, <code>flujo_caja_sobre_deuda_total</code></li>
<li><code>gasto_intereses_sobre_ingresos</code>, <code>gastos_operativos_sobre_ingresos_operativos</code></li>
<li><code>ingresos_operativos_sobre_activos_totales</code>, <code>indicador_perdida</code></li>
</ul>

<h4>3. ¿Por qué ratios y no montos absolutos?</h4>
<p>Indicadores como <em>utilidad neta sobre activos totales</em> o <em>efectivo sobre ventas</em>
normalizan magnitudes contables. Así, una PYME y una gran corporación pueden compararse en términos
de <strong>perfil financiero relativo</strong> (márgenes, rotación, apalancamiento), que es justamente
lo que el ACP y K-Means buscan agrupar: empresas con comportamiento económico similar, independientemente
de su escala absoluta.</p>

<p><strong>Nota:</strong> para el modelado se excluye <code>empresa_id</code> y se utilizan únicamente
las variables numéricas; los valores faltantes, si existen, se reemplazan por cero antes de estandarizar.</p>
</div>
""",
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🎯 Propósito")
    st.markdown(
        """
El propósito de trabajar con esta base es **descubrir patrones ocultos** en el comportamiento
financiero de las empresas **sin contar con una variable objetivo predefinida** (aprendizaje no supervisado).

En contextos financieros y de riesgo, esto sirve para:

- Identificar **perfiles homogéneos** de empresas (sanidad financiera, apalancamiento, eficiencia).
- Apoyar decisiones de **segmentación de cartera**, **priorización comercial** o **monitoreo de riesgo**.
- Reducir la complejidad de decenas de indicadores a un **espacio de pocas dimensiones** interpretables.
"""
    )

with col2:
    st.markdown("### 🏁 Objetivo del análisis")
    st.markdown(
        """
El objetivo de esta aplicación es guiarte paso a paso para:

1. **Preparar** la base eliminando identificadores y estandarizando variables.
2. Aplicar **Análisis de Componentes Principales (ACP/PCA)** para comprimir la información
   y entender qué ratios explican la variabilidad entre empresas.
3. Ejecutar **K-Means** sobre el espacio PCA para formar **grupos (clusters)** de empresas similares.
4. **Exportar** la base original enriquecida con la etiqueta de cluster para análisis posterior.

> **Resultado esperado:** una segmentación accionable donde cada empresa queda asignada a un grupo
> que puede perfilarse según sus ratios financieros dominantes.
"""
    )

st.markdown("---")
st.markdown("## Estructura de variables")

st.markdown(
    "La base contiene aproximadamente **80 variables numéricas** organizadas conceptualmente en los "
    "siguientes bloques (tras eliminar el identificador `empresa_id`):"
)

for group, vars_list in VARIABLE_GROUPS.items():
    if group == "Identificación y estructura":
        vars_display = [v for v in vars_list if v != "empresa_id"]
    else:
        vars_display = vars_list
    with st.expander(f"📁 {group} ({len(vars_display)} variables)"):
        st.write(", ".join(f"`{v}`" for v in vars_display))

st.markdown("---")
st.markdown("## Metodología en dos etapas")

tab_acp, tab_km = st.tabs(["🔬 Etapa 1 — ACP (PCA)", "🎯 Etapa 2 — K-Means"])

with tab_acp:
    st.markdown(
        """
**Análisis de Componentes Principales** transforma las variables correlacionadas en un conjunto
de componentes ortogonales (PC1, PC2, …) ordenados por varianza explicada.

- **¿Por qué aquí?** Con ~80 ratios, hay redundancia; PCA elimina ruido y facilita la visualización.
- **Qué obtienes:** gráfico de varianza explicada, cargas (loadings) e interpretación de cada componente.
- **Decisión clave:** cuántos componentes conservar (p. ej. 80–90 % de varianza acumulada).
"""
    )

with tab_km:
    st.markdown(
        """
**K-Means** particiona las empresas en *k* grupos minimizando la distancia intra-cluster.

- **¿Por qué sobre PCA?** Clustering en alta dimensionalidad sufre la "maldición de la dimensionalidad";
  PCA ofrece un espacio compacto y más estable.
- **Qué obtienes:** gráficos de codo y Silhouette, visualización de clusters y base exportable.
- **Decisión clave:** número de clusters *k* según criterio de negocio y métricas de calidad.
"""
    )

st.markdown("---")
st.markdown("## 📂 Carga de datos y preprocesamiento")

st.info(
    "👆 Sube el archivo **`datos_empresas.csv`** para habilitar el preprocesamiento "
    "y las demás páginas del análisis."
)

uploaded = st.file_uploader(
    "Arrastra o selecciona tu archivo CSV",
    type=["csv"],
    help="Archivo de referencia: datos_empresas.csv (separador ; o ,)",
)

if uploaded is None:
    st.markdown(
        "**Ruta de referencia:** Debes validar donde se encuentra tu archivo datos_empresas.csv y subirlo para continuar con el análisis."
    )
    st.stop()

if st.session_state.get("uploaded_name") != uploaded.name:
    reset_analysis_state()
    st.session_state.uploaded_name = uploaded.name

df_raw = read_uploaded_csv(uploaded)
st.session_state.df_raw = df_raw

c1, c2, c3 = st.columns(3)
c1.metric("Observaciones (empresas)", f"{df_raw.shape[0]:,}")
c2.metric("Variables totales", df_raw.shape[1])
c3.metric("Archivo cargado", uploaded.name)

with st.expander("👀 Vista previa de la base original", expanded=False):
    st.dataframe(df_raw.head(12), use_container_width=True)

detected_id = detect_id_column(df_raw)
id_options = ["— Sin columna ID —"] + list(df_raw.columns)
default_idx = id_options.index(detected_id) if detected_id in id_options else 0
id_col = st.selectbox(
    "Columna identificador (se excluirá del análisis)",
    id_options,
    index=default_idx,
)
id_col = None if id_col == "— Sin columna ID —" else id_col

st.markdown(
    """
<div class="step-card">
    <h4>Preprocesamiento</h4>
    <p>Se elimina el ID, se verifican faltantes con <code>isna().sum()</code>, se rellenan con 0 si aplica,
    y se aplica <code>StandardScaler</code> seguido de <code>normalize</code> antes del ACP.</p>
</div>
""",
    unsafe_allow_html=True,
)

if st.button("▶️ Ejecutar preprocesamiento", type="primary"):
    df_with_id, cc_data, missing, norm_data = run_preprocessing(df_raw, id_col)
    st.session_state.df_with_id = df_with_id
    st.session_state.cc_data = cc_data
    st.session_state.missing = missing
    st.session_state.norm_data = norm_data
    st.session_state.feature_names = list(cc_data.columns)
    st.session_state.id_col = id_col
    st.session_state.steps_done = {"prep": True, "pca": False, "kmeans": False}
    st.session_state.pop("pca_full", None)
    st.success("Preprocesamiento completado. Continúa en la página **ACP / PCA**.")
    st.rerun()

if st.session_state.get("steps_done", {}).get("prep"):
    cc_data = st.session_state.cc_data
    missing = st.session_state.missing

    st.markdown("#### Resultados del preprocesamiento")

    if st.session_state.id_col:
        st.success(
            f"Columna **`{st.session_state.id_col}`** eliminada. "
            f"**{cc_data.shape[1]}** variables numéricas listas para el ACP."
        )

    missing_df = missing[missing > 0].reset_index()
    missing_df.columns = ["Variable", "Valores faltantes"]
    if len(missing_df) == 0:
        st.success("No se encontraron valores faltantes.")
    else:
        st.warning(f"Faltantes detectados en **{len(missing_df)}** variables → rellenados con **0**.")
        st.dataframe(missing_df, use_container_width=True, hide_index=True)

    st.code(
        "scaler = StandardScaler()\n"
        "scaled_ccData = scaler.fit_transform(ccData)\n"
        "norm_ccData = normalize(scaled_ccData)",
        language="python",
    )
    st.info(
        f"Matriz transformada: **{st.session_state.norm_data.shape[0]:,}** filas × "
        f"**{st.session_state.norm_data.shape[1]}** columnas. "
        "👉 Ve a **ACP / PCA** en el menú lateral."
    )

    with st.expander("Estadísticas descriptivas"):
        st.dataframe(cc_data.describe().T.round(3), use_container_width=True)
else:
    st.warning("Ejecuta el preprocesamiento para continuar con el ACP.")
