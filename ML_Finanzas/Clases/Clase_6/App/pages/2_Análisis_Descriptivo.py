"""
Análisis descriptivo - Univariado, bivariado y tablas de contingencia (Churn)
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from scipy import stats

st.set_page_config(page_title="Análisis Descriptivo - Churn", page_icon="📊", layout="wide")

df_raw = st.session_state.get("df_raw")
data_ok = df_raw is not None

st.title("📊 Análisis descriptivo")
st.markdown("---")

if not data_ok:
    st.warning("👆 Primero cargue el archivo de datos en la página **Inicio**.")
else:
    df = df_raw.copy()

    st.markdown("""
    En esta sección se explora la base de datos de clientes mediante:
    - **Análisis univariado**: distribución marginal de cada variable.
    - **Análisis bivariado**: relación de cada variable con la **variable respuesta (Exited: permanece/abandona)**.
    - **Tablas de contingencia y Chi-cuadrado**: asociación entre variables categóricas y el desenlace.
    """)

    tab1, tab2, tab3 = st.tabs(["Univariado", "Bivariado (vs Exited)", "Tablas de contingencia y Chi-cuadrado"])

    # === UNIVARIADO ===
    with tab1:
        st.subheader("Análisis univariado")
        st.write("Distribución marginal de cada variable.")

        tipo = st.radio("Tipo de variable", ["Numéricas", "Categóricas"], key="t1")
        if tipo == "Numéricas":
            v = st.selectbox(
                "Variable numérica",
                ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"],
                key="univ_num"
            )
            st.plotly_chart(
                px.histogram(df, x=v, nbins=30, title=f"Distribución de {v}"),
                use_container_width=True
            )
            st.write("**Estadísticos descriptivos:**")
            st.dataframe(
                df[["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"]].describe().round(2),
                use_container_width=True
            )
        else:
            v = st.selectbox(
                "Variable categórica",
                ["Geography", "Gender", "HasCrCard", "IsActiveMember"],
                key="univ_cat"
            )
            c = df[v].value_counts()
            st.plotly_chart(
                px.bar(x=c.index.astype(str), y=c.values, title=f"Distribución de {v}",
                       labels={"x": v, "y": "Frecuencia"}),
                use_container_width=True
            )

    # === BIVARIADO ===
    with tab2:
        st.subheader("Análisis bivariado con la variable respuesta (Exited)")
        st.write("Relación entre cada variable explicativa y Exited (0=permanece, 1=abandona).")

        tipo2 = st.radio("Tipo de variable", ["Numéricas", "Categóricas"], key="t2")
        df["Exited_str"] = df["Exited"].map({0: "Permanecen", 1: "Abandonan"})
        if tipo2 == "Numéricas":
            v2 = st.selectbox(
                "Variable numérica",
                ["CreditScore", "Age", "Tenure", "Balance", "NumOfProducts", "EstimatedSalary"],
                key="v2"
            )
            st.plotly_chart(
                px.box(df, x="Exited_str", y=v2, color="Exited_str",
                       color_discrete_map={"Permanecen": "#2ecc71", "Abandonan": "#e74c3c"},
                       title=f"{v2} por Exited"),
                use_container_width=True
            )
            st.write("**Medias por Exited:**")
            st.dataframe(df.groupby("Exited")[v2].agg(["mean", "count"]).round(2), use_container_width=True)
        else:
            v2 = st.selectbox(
                "Variable categórica",
                ["Geography", "Gender", "HasCrCard", "IsActiveMember"],
                key="v2c"
            )
            ct = pd.crosstab(df[v2], df["Exited_str"])
            st.plotly_chart(
                px.bar(ct.reset_index().melt(id_vars=v2, var_name="Exited", value_name="count"),
                       x=v2, y="count", color="Exited", barmode="group",
                       color_discrete_map={"Permanecen": "#2ecc71", "Abandonan": "#e74c3c"},
                       title=f"{v2} por Exited"),
                use_container_width=True
            )
            st.write("**Tabla de contingencia (conteos):**")
            st.dataframe(pd.crosstab(df[v2], df["Exited_str"], margins=True), use_container_width=True)
            st.write("**Porcentajes por fila (% dentro de cada categoría):**")
            ct_pct = pd.crosstab(df[v2], df["Exited"], normalize="index").round(3) * 100
            ct_pct.columns = ["Permanecen %", "Abandonan %"]
            st.dataframe(ct_pct.astype(str).apply(lambda x: x + "%"), use_container_width=True)

    # === TABLAS DE CONTINGENCIA + CHI-CUADRADO ===
    with tab3:
        st.subheader("Tablas de contingencia y prueba Chi-cuadrado")
        st.markdown("""
        La **prueba Chi-cuadrado** mide si existe **asociación significativa** entre una variable categórica
        y la variable respuesta (Exited). Si p-valor < 0.05, la variable está **asociada** con el churn.
        """)

        vars_cat = ["Geography", "Gender", "HasCrCard", "IsActiveMember"]
        var_chi = st.selectbox("Variable categórica", vars_cat, key="chi_var")

        ct = pd.crosstab(df[var_chi], df["Exited"])
        st.write("**Tabla de contingencia:**")
        st.dataframe(pd.crosstab(df[var_chi], df["Exited"], margins=True), use_container_width=True)

        try:
            chi2, p_val, dof, expected = stats.chi2_contingency(ct)
            st.metric("Chi-cuadrado", f"{chi2:.2f}")
            st.metric("p-valor", f"{p_val:.4f}")
            if p_val < 0.05:
                st.success("Hay asociación significativa entre la variable y Exited (p < 0.05).")
            else:
                st.info("No hay asociación significativa (p ≥ 0.05).")
        except Exception as e:
            st.warning("No se pudo calcular Chi-cuadrado (posibles celdas vacías o esperadas < 5).")

        st.markdown("---")
        st.write("**Distribución de Exited (variable respuesta):**")
        pie_data = df["Exited"].map({0: "Permanecen", 1: "Abandonan"}).value_counts().reset_index()
        pie_data.columns = ["Exited", "count"]
        st.plotly_chart(
            px.pie(pie_data, values="count", names="Exited",
                   color_discrete_map={"Permanecen": "#2ecc71", "Abandonan": "#e74c3c"},
                   title="Proporción Permanecen vs Abandonan"),
            use_container_width=True
        )
