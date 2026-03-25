"""
Modelación - Regresión logística con SMOTE (Churn)
"""
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from imblearn.over_sampling import SMOTE
import plotly.graph_objects as go
from utils_data import prepare_model_data

# Referencias para dummies: Geography (France), Gender (Female)
GEOGRAPHY_DUMMY = {"France": (0, 0), "Germany": (1, 0), "Spain": (0, 1)}  # (Geography_Germany, Geography_Spain)
GENDER_DUMMY = {"Female": 0, "Male": 1}  # Gender_Male

st.set_page_config(page_title="Modelación - Churn", page_icon="📈", layout="wide")

df_raw = st.session_state.get("df_raw")
data_ok = df_raw is not None

st.title("📈 Modelación y predicción de Churn")
st.markdown("---")

if not data_ok:
    st.warning("👆 Primero cargue el archivo de datos en la página **Inicio**.")
else:
    df_modelo = st.session_state.df_modelo
    MODEL_FEATURES = [c for c in df_modelo.columns if c != "Exited"]
    X = df_modelo[MODEL_FEATURES]
    y = df_modelo["Exited"]

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_tr, y_tr)

    logreg = LogisticRegression(random_state=42, max_iter=1000)
    logreg.fit(X_resampled, y_resampled)

    proba_te = logreg.predict_proba(X_te)[:, 1]
    y_pred = (proba_te >= 0.4).astype(int)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Modelo e interpretación del riesgo",
        "Calculadora de predicción",
        "Matriz de confusión",
        "Curva ROC"
    ])

    # === MODELO + BETA POR VARIABLE (DUMMYS) ===
    with tab1:
        st.subheader("Modelo de regresión logística (con SMOTE)")
        st.markdown("**Fórmula:** `Exited ~ CreditScore + Geography (dummys) + Gender (dummy) + Age + Tenure + Balance + NumOfProducts + HasCrCard + IsActiveMember + EstimatedSalary`")
        st.markdown("*Variables categóricas codificadas como dummys: Geography (ref. France), Gender (ref. Female).*")

        var_labels = {
            "CreditScore": "CreditScore (β)",
            "Geography_Germany": "Geography: Germany vs France (β)",
            "Geography_Spain": "Geography: Spain vs France (β)",
            "Gender_Male": "Gender: Male vs Female (β)",
            "Age": "Age (β)",
            "Tenure": "Tenure (β)",
            "Balance": "Balance (β)",
            "NumOfProducts": "NumOfProducts (β)",
            "HasCrCard": "HasCrCard (β)",
            "IsActiveMember": "IsActiveMember (β)",
            "EstimatedSalary": "EstimatedSalary (β)"
        }

        coef_df = pd.DataFrame({
            "Variable": ["Intercepto"] + [var_labels.get(v, v) for v in MODEL_FEATURES],
            "β (Coeficiente)": [logreg.intercept_[0]] + list(logreg.coef_[0]),
            "Odds Ratio": [np.exp(logreg.intercept_[0])] + [np.exp(c) for c in logreg.coef_[0]]
        })
        st.dataframe(coef_df.round(4), use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("¿Cuándo aumenta o disminuye el riesgo de churn?")

        st.markdown("""
        El riesgo de **abandono (churn)** aumenta o disminuye según el **Odds Ratio** de cada variable:

        - **Odds Ratio > 1**: Mayor probabilidad de **churn** → **Riesgo aumenta**
        - **Odds Ratio < 1**: Mayor probabilidad de **permanecer** → **Riesgo disminuye**
        - **Odds Ratio ≈ 1**: La variable no influye de manera relevante

        *Para dummys: el β compara la categoría indicada vs la referencia.*
        """)

        st.write("**Resumen por variable:**")
        for i, var in enumerate(MODEL_FEATURES):
            or_val = np.exp(logreg.coef_[0][i])
            lbl = var_labels.get(var, var)
            if or_val > 1.05:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): 🔴 Riesgo **aumenta** — mayor probabilidad de churn.")
            elif or_val < 0.95:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): 🟢 Riesgo **disminuye** — mayor probabilidad de permanecer.")
            else:
                st.write(f"- **{lbl}** (OR = {or_val:.3f}): ⚪ Efecto neutro o pequeño.")

    # === CALCULADORA ===
    with tab2:
        st.subheader("Calculadora de predicción de churn")
        st.markdown("Ingrese los datos del cliente para estimar la probabilidad de **abandono (churn)**.")

        col1, col2 = st.columns(2)
        with col1:
            credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
            geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
            gender = st.selectbox("Gender", ["Female", "Male"])
            age = st.number_input("Age", min_value=18, max_value=100, value=40)
            tenure = st.number_input("Tenure (años)", min_value=0, max_value=10, value=5)
        with col2:
            balance = st.number_input("Balance", min_value=0.0, max_value=300000.0, value=100000.0, step=1000.0)
            num_products = st.number_input("NumOfProducts", min_value=1, max_value=4, value=1)
            has_cr_card = st.selectbox("HasCrCard", [0, 1])
            is_active = st.selectbox("IsActiveMember", [0, 1])
            salary = st.number_input("EstimatedSalary", min_value=0.0, max_value=300000.0, value=100000.0, step=1000.0)

        geo_germany, geo_spain = GEOGRAPHY_DUMMY[geography]
        gen_male = GENDER_DUMMY[gender]

        # Ordenar según el orden esperado del modelo (columnas de df_modelo)
        x_dict = {
            "CreditScore": credit_score,
            "Geography_Germany": geo_germany,
            "Geography_Spain": geo_spain,
            "Gender_Male": gen_male,
            "Age": age,
            "Tenure": tenure,
            "Balance": balance,
            "NumOfProducts": num_products,
            "HasCrCard": has_cr_card,
            "IsActiveMember": is_active,
            "EstimatedSalary": salary,
        }
        x_new = pd.DataFrame([{c: x_dict.get(c, 0) for c in MODEL_FEATURES}], columns=MODEL_FEATURES)
        proba = logreg.predict_proba(x_new)[0, 1]
        pred = 1 if proba >= 0.4 else 0

        st.metric("Probabilidad de CHURN (abandono)", f"{proba:.2%}")
        if pred == 1:
            st.error("**Predicción: Alto riesgo de churn ⚠️** — Se sugiere priorizar acciones de retención.")
        else:
            st.success("**Predicción: Bajo riesgo de churn ✅** — Cliente con menor probabilidad de abandonar.")

    # === MATRIZ DE CONFUSIÓN ===
    with tab3:
        st.subheader("Matriz de confusión")
        st.markdown("""
        La matriz de confusión muestra las predicciones del modelo frente a los valores reales.
        **Clase positiva = churn (Exited=1)**, **Clase negativa = permanece (Exited=0)**.
        """)
        cm = confusion_matrix(y_te, y_pred)
        tn, fp, fn, tp = cm.ravel()
        N = tn + fp + fn + tp

        # Primera fila: Real: No Churn (arriba), Segunda fila: Real: Churn (abajo)
        # Plotly: y[0] abajo, y[1] arriba. Queremos arriba=No churn, abajo=Churn.
        cm_plot = np.array([cm[1], cm[0]])  # z[0]=Churn abajo, z[1]=No churn arriba
        y_labels = ["Real: Churn", "Real: No Churn"]  # ordenados: Churn abajo, No Churn arriba
        x_labels = ["Pred: No Churn", "Pred: Churn"]  # alfabéticamente

        st.plotly_chart(
            go.Figure(data=go.Heatmap(
                z=cm_plot, x=x_labels, y=y_labels,
                text=cm_plot, texttemplate="%{text}", showscale=False,
                colorscale=[[0, "#22c55e"], [0.5, "#fecaca"], [1, "#fee2e2"]]
            )),
            use_container_width=True
        )

        st.markdown("**Estructura de la matriz:**")
        st.markdown("""
        |              | Pred: No churn | Pred: Churn |
        |--------------|----------------|-------------|
        | **Real: No churn**  | TN            | FP          |
        | **Real: Churn**     | FN            | TP          |

        - **TN**: Predijo permanencia y permaneció.
        - **FP**: Predijo churn pero permaneció.
        - **FN**: Predijo permanencia pero abandonó.
        - **TP**: Predijo churn y abandonó.
        """)

        st.markdown("---")
        st.subheader("Indicadores de la matriz de confusión")
        st.markdown(f"**N = {N}** (total en muestra de prueba)")
        st.markdown("---")

        accuracy = (tp + tn) / N if N > 0 else 0
        sensibilidad = tp / (tp + fn) if (tp + fn) > 0 else 0
        especificidad = tn / (tn + fp) if (tn + fp) > 0 else 0

        indicadores = [
            ("1) Exactitud / Accuracy", f"(TP + TN) / N = ({tp} + {tn}) / {N}", accuracy,
             "Proporción total de clasificaciones correctas."),
            ("2) Sensibilidad / Recall (clase Churn)", f"TP / (TP + FN) = {tp} / ({tp} + {fn})", sensibilidad,
             "De los que abandonaron, ¿cuántos detectó el modelo? Capacidad de identificar clientes en riesgo."),
            ("3) Especificidad", f"TN / (TN + FP) = {tn} / ({tn} + {fp})", especificidad,
             "De los que permanecieron, ¿cuántos clasificó correctamente?"),
        ]

        for nombre, formula, valor, interpretacion in indicadores:
            with st.expander(f"{nombre} = {valor:.4f}"):
                st.code(formula)
                st.write(f"**Interpretación:** {interpretacion}")

        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        col1.metric("Exactitud", f"{accuracy:.2%}")
        col2.metric("Sensibilidad (Recall churn)", f"{sensibilidad:.2%}")
        col3.metric("Especificidad", f"{especificidad:.2%}")

        st.markdown("---")
        st.write("**Reporte de clasificación:**")
        st.code(classification_report(y_te, y_pred, target_names=["No churn", "Churn"]))

    # === CURVA ROC ===
    with tab4:
        st.subheader("Curva ROC")
        fpr, tpr, _ = roc_curve(y_te, logreg.predict_proba(X_te)[:, 1])
        roc_auc = auc(fpr, tpr)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", name=f"Modelo (AUC = {roc_auc:.3f})", line=dict(color="#22c55e", width=2)))
        fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", name="Azar", line=dict(dash="dash", color="gray")))
        fig.update_layout(title="Curva ROC", xaxis_title="Tasa de falsos positivos", yaxis_title="Tasa de verdaderos positivos")
        st.plotly_chart(fig, use_container_width=True)
        st.metric("AUC", f"{roc_auc:.4f}")
