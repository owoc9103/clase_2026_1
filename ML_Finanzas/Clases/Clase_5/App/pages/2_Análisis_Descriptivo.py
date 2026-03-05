"""
Análisis descriptivo - Univariado, bivariado y tablas de contingencia
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

st.set_page_config(page_title="Análisis Descriptivo - German Credit", page_icon="📊", layout="wide")

df_raw = st.session_state.get("df_raw")
data_ok = df_raw is not None

st.title("📊 Análisis descriptivo")
st.markdown("---")

if not data_ok:
    st.warning("👆 Primero cargue el archivo de datos en la página **Inicio**.")
else:
    df = df_raw.fillna({"Saving_accounts": "NA", "Checking_account": "NA"})

    st.markdown("""
    En esta sección se explora la base de datos histórica de solicitudes de crédito mediante:
    - **Análisis univariado**: distribución marginal de cada variable.
    - **Análisis bivariado**: relación de cada variable con la **variable respuesta (Risk: buen/mal pagador)**.
    - **Tablas de contingencia y Chi-cuadrado**: asociación entre variables categóricas y el desenlace (good/bad).
    """)

    tab1, tab2, tab3 = st.tabs(["Univariado", "Bivariado (vs Risk)", "Tablas de contingencia y Chi-cuadrado"])

    # === UNIVARIADO ===
    with tab1:
        st.subheader("Análisis univariado")
        st.write("Distribución marginal de cada variable.")

        tipo = st.radio("Tipo de variable", ["Numéricas", "Categóricas"], key="t1")
        if tipo == "Numéricas":
            v = st.selectbox("Variable numérica", ["Age", "Credit_amount", "Duration"], key="univ_num")
            st.plotly_chart(
                px.histogram(df, x=v, nbins=30, title=f"Distribución de {v}"),
                use_container_width=True
            )
            st.write("**Estadísticos descriptivos:**")
            st.dataframe(df[["Age", "Credit_amount", "Duration"]].describe().round(2), use_container_width=True)
        else:
            v = st.selectbox("Variable categórica", ["Sex", "Housing", "Saving_accounts", "Checking_account", "Purpose"], key="univ_cat")
            c = df[v].value_counts()
            st.plotly_chart(
                px.bar(x=c.index.astype(str), y=c.values, title=f"Distribución de {v}",
                       labels={"x": v, "y": "Frecuencia"}),
                use_container_width=True
            )

    # === BIVARIADO ===
    with tab2:
        st.subheader("Análisis bivariado con la variable respuesta (Risk)")
        st.write("Relación entre cada variable explicativa y Risk (good/bad).")

        tipo2 = st.radio("Tipo de variable", ["Numéricas", "Categóricas"], key="t2")
        if tipo2 == "Numéricas":
            v2 = st.selectbox("Variable numérica", ["Age", "Credit_amount", "Duration"], key="v2")
            st.plotly_chart(
                px.box(df, x="Risk", y=v2, color="Risk",
                       color_discrete_map={"good": "#2ecc71", "bad": "#e74c3c"},
                       title=f"{v2} por Risk"),
                use_container_width=True
            )
            st.write("**Medias por Risk:**")
            st.dataframe(df.groupby("Risk")[v2].agg(["mean", "count"]).round(2), use_container_width=True)
        else:
            v2 = st.selectbox("Variable categórica", ["Sex", "Housing", "Saving_accounts", "Checking_account", "Purpose"], key="v2c")
            ct = pd.crosstab(df[v2], df["Risk"])
            st.plotly_chart(
                px.bar(ct.reset_index().melt(id_vars=v2, var_name="Risk", value_name="count"),
                       x=v2, y="count", color="Risk", barmode="group",
                       color_discrete_map={"good": "#2ecc71", "bad": "#e74c3c"},
                       title=f"{v2} por Risk"),
                use_container_width=True
            )
            st.write("**Tabla de contingencia (conteos):**")
            st.dataframe(pd.crosstab(df[v2], df["Risk"], margins=True), use_container_width=True)
            st.write("**Porcentajes por fila (% dentro de cada categoría que es good/bad):**")
            ct_pct = pd.crosstab(df[v2], df["Risk"], normalize="index").round(3) * 100
            st.dataframe(ct_pct.astype(str).apply(lambda x: x + "%"), use_container_width=True)

    # === TABLAS DE CONTINGENCIA + CHI-CUADRADO ===
    with tab3:
        st.subheader("Tablas de contingencia y prueba Chi-cuadrado")
        st.markdown("""
        La **prueba Chi-cuadrado** mide si existe **asociación significativa** entre una variable categórica 
        y la variable respuesta (Risk). Si p-valor < 0.05, la variable está **asociada** con el riesgo de crédito.
        """)

        vars_cat = ["Sex", "Housing", "Saving_accounts", "Checking_account", "Purpose"]
        var_chi = st.selectbox("Variable categórica", vars_cat, key="chi_var")

        ct = pd.crosstab(df[var_chi], df["Risk"])
        st.write("**Tabla de contingencia:**")
        st.dataframe(pd.crosstab(df[var_chi], df["Risk"], margins=True), use_container_width=True)

        try:
            chi2, p_val, dof, expected = stats.chi2_contingency(ct)
            st.metric("Chi-cuadrado", f"{chi2:.2f}")
            st.metric("p-valor", f"{p_val:.4f}")
            if p_val < 0.05:
                st.success("Hay asociación significativa entre la variable y Risk (p < 0.05).")
            else:
                st.info("No hay asociación significativa (p ≥ 0.05).")
        except Exception as e:
            st.warning("No se pudo calcular Chi-cuadrado (posibles celdas vacías o esperadas < 5).")

        st.markdown("---")
        st.write("**Distribución de Risk (variable respuesta):**")
        st.plotly_chart(
            px.pie(df_raw, names="Risk", color_discrete_map={"good": "#2ecc71", "bad": "#e74c3c"},
                   title="Proporción Good vs Bad"),
            use_container_width=True
        )
