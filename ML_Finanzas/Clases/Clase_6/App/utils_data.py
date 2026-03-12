"""Módulo compartido: carga y preparación de datos Churn Modelling."""
import pandas as pd

def parse_uploaded_csv(uploaded_file):
    """Parsea el CSV subido al formato esperado (Churn Modelling)."""
    df = pd.read_csv(uploaded_file)
    return df


def prepare_model_data(df):
    """
    Prepara datos para el modelo: elimina columnas irrelevantes,
    crea variables dummy para Geography y Gender (referencias: France, Female).
    """
    data = df.copy()
    data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

    data = pd.get_dummies(data, columns=["Geography", "Gender"], drop_first=True)
    # get_dummies produce Geography_Germany, Geography_Spain, Gender_Male (ref: France, Female)

    feature_cols = [c for c in data.columns if c != "Exited"]
    return data.dropna(subset=feature_cols + ["Exited"])
