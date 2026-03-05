"""
Modelación - Regresión logística, calculadora y métricas
"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, roc_curve, auc
import plotly.graph_objects as go
from utils_data import prepare_model_data, MODEL_FEATURES

st.set_page_config(page_title="Modelación - German Credit", page_icon="📈", layout="wide")

df_raw = st.session_state.get("df_raw")
data_ok = df_raw is not None

st.title("📈 Modelación y predicción")
st.markdown("---")

if not data_ok:
    st.warning("👆 Primero cargue el archivo de datos en la página **Inicio**.")
else:
    df_modelo = st.session_state.df_modelo
    X = df_modelo[MODEL_FEATURES]
    y = df_modelo["good"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_tr, y_tr)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Modelo e interpretación del riesgo",
        "Calculadora de predicción",
        "Matriz de confusión",
        "Curva ROC"
    ])

    # === MODELO + CUÁNDO AUMENTA/DISMINUYE RIESGO ===
    with tab1:
        st.subheader("Modelo de regresión logística")
        st.markdown("**Fórmula:** `good ~ Age + Duration + female + s_little + s_rich + c_little + c_moderate + c_rich`")

        coef_df = pd.DataFrame({
            "Variable": ["Intercepto"] + MODEL_FEATURES,
            "Coeficiente": [model.intercept_[0]] + list(model.coef_[0]),
            "Odds Ratio": [np.exp(model.intercept_[0])] + [np.exp(c) for c in model.coef_[0]]
        })
        st.dataframe(coef_df.round(4), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("¿Cuándo aumenta o disminuye el riesgo?")

        st.markdown("""
        El riesgo de ser **mal pagador (bad)** aumenta o disminuye según el **Odds Ratio** de cada variable:

        - **Odds Ratio > 1**: Mayor probabilidad de ser **buen pagador** → **Riesgo disminuye**
        - **Odds Ratio < 1**: Mayor probabilidad de ser **mal pagador** → **Riesgo aumenta**
        - **Odds Ratio ≈ 1**: La variable no influye de manera relevante
        """)

        # Interpretación automática por variable
        var_labels = {
            "Age": "Edad",
            "Duration": "Duración del crédito (meses)",
            "female": "Ser mujer (vs. hombre)",
            "s_little": "Cuenta de ahorros 'little'",
            "s_rich": "Cuenta de ahorros 'rich'",
            "c_little": "Cuenta corriente 'little'",
            "c_moderate": "Cuenta corriente 'moderate'",
            "c_rich": "Cuenta corriente 'rich'"
        }

        st.write("**Resumen por variable:**")
        for i, var in enumerate(MODEL_FEATURES):
            or_val = np.exp(model.coef_[0][i])
            lbl = var_labels.get(var, var)
            if or_val > 1.05:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): 🟢 Riesgo **disminuye** — mayor probabilidad de buen pagador.")
            elif or_val < 0.95:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): 🔴 Riesgo **aumenta** — mayor probabilidad de mal pagador.")
            else:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): ⚪ Efecto neutro o pequeño.")

    # === CALCULADORA ===
    with tab2:
        st.subheader("Calculadora de predicción")
        st.markdown("Ingrese los datos del solicitante para estimar la probabilidad de ser **buen pagador**.")

        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Edad (Age)", min_value=18, max_value=100, value=35)
            duration = st.number_input("Duración del crédito (meses)", min_value=4, max_value=72, value=18)
            sex = st.selectbox("Sexo", ["male", "female"])
        with col2:
            saving = st.selectbox("Saving accounts", ["little", "moderate", "quite rich", "rich"])
            checking = st.selectbox("Checking account", ["little", "moderate", "rich"])

        x_new = pd.DataFrame([[
            age, duration,
            1 if sex == "female" else 0,
            1 if saving == "little" else 0, 1 if saving == "rich" else 0,
            1 if checking == "little" else 0, 1 if checking == "moderate" else 0, 1 if checking == "rich" else 0
        ]], columns=MODEL_FEATURES)
        proba = model.predict_proba(x_new)[0, 1]
        pred = 1 if proba >= 0.5 else 0

        st.metric("Probabilidad de BUEN pagador", f"{proba:.2%}")
        if pred == 1:
            st.success("**Predicción: Buen pagador ✅** — Riesgo bajo. Se sugiere aprobar el crédito.")
        else:
            st.error("**Predicción: Mal pagador ⚠️** — Riesgo alto. Se sugiere revisar o rechazar.")

    # === MATRIZ DE CONFUSIÓN ===
    with tab3:
        st.subheader("Matriz de confusión")
        st.markdown("""
        La matriz de confusión muestra las predicciones del modelo frente a los valores reales. 
        **Clase positiva = buen pagador (good)**, **Clase negativa = mal pagador (bad)**.
        """)
        y_pred = model.predict(X_te)
        cm = confusion_matrix(y_te, y_pred)
        tn, fp, fn, tp = cm.ravel()
        N = tn + fp + fn + tp

        # Invertir filas para mostrar: 1ª fila = Riesgo malo real, 2ª fila = Riesgo bueno real
        cm_display = np.flipud(cm)
        st.plotly_chart(
            go.Figure(data=go.Heatmap(
                z=cm_display,
                x=["Pred: Bad", "Pred: Good"],
                y=["Real: Good", "Real: Bad"],  # Plotly: primero=abajo, segundo=arriba → arriba=Bad, abajo=Good
                text=cm_display, texttemplate="%{text}", showscale=False,
                colorscale=[[0, "#fee2e2"], [0.5, "#fecaca"], [1, "#22c55e"]]
            )),
            use_container_width=True
        )

        st.markdown("**Estructura de la matriz:**")
        st.markdown("""
        |              | Pred: Bad | Pred: Good |
        |--------------|-----------|------------|
        | **Real: Bad**  | TN        | FP         |
        | **Real: Good** | FN        | TP         |

        - **TN** (Verdaderos negativos): Predijo mal pagador y es mal pagador.  
        - **FP** (Falsos positivos): Predijo buen pagador pero es mal pagador.  
        - **FN** (Falsos negativos): Predijo mal pagador pero es buen pagador.  
        - **TP** (Verdaderos positivos): Predijo buen pagador y es buen pagador.
        """)

        st.markdown("---")
        st.subheader("Indicadores de la matriz de confusión")
        st.markdown(f"**N = {N}** (total de observaciones en la muestra de prueba)")
        st.markdown("---")

        # Cálculos
        accuracy = (tp + tn) / N if N > 0 else 0
        sensibilidad = tp / (tp + fn) if (tp + fn) > 0 else 0
        especificidad = tn / (tn + fp) if (tn + fp) > 0 else 0

        indicadores = [
            ("1) Exactitud / Accuracy", f"(TP + TN) / N = ({tp} + {tn}) / {N}", accuracy,
             "Proporción total de clasificaciones correctas (buen y mal pagador)."),
            ("2) Sensibilidad / Recall (TPR)", f"TP / (TP + FN) = {tp} / ({tp} + {fn})", sensibilidad,
             "De los que son buen pagador, ¿cuántos detectó el modelo correctamente? Capacidad de identificar buenos pagadores."),
            ("3) Especificidad (TNR)", f"TN / (TN + FP) = {tn} / ({tn} + {fp})", especificidad,
             "De los que son mal pagador, ¿cuántos rechazó correctamente? Capacidad de identificar malos pagadores."),
        ]

        for nombre, formula, valor, interpretacion in indicadores:
            with st.expander(f"{nombre} = {valor:.4f}"):
                st.code(formula)
                st.write(f"**Interpretación:** {interpretacion}")

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric("Exactitud", f"{accuracy:.2%}")
        col2.metric("Sensibilidad", f"{sensibilidad:.2%}")
        col3.metric("Especificidad", f"{especificidad:.2%}")

        st.markdown("---")
        st.write("**Reporte de clasificación:**")
        st.code(classification_report(y_te, y_pred, target_names=["Bad", "Good"]))

    # === CURVA ROC ===
    with tab4:
        st.subheader("Curva ROC")
        fpr, tpr, _ = roc_curve(y_te, model.predict_proba(X_te)[:, 1])
        roc_auc = auc(fpr, tpr)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=f"Modelo (AUC = {roc_auc:.3f})", line=dict(color="#22c55e", width=2)))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Azar", line=dict(dash="dash", color="gray")))
        fig.update_layout(title="Curva ROC", xaxis_title="Tasa de falsos positivos", yaxis_title="Tasa de verdaderos positivos")
        st.plotly_chart(fig, use_container_width=True)
        st.metric("AUC", f"{roc_auc:.4f}")
