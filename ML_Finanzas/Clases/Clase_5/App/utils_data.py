"""Módulo compartido: carga y preparación de datos German Credit."""
import pandas as pd


def parse_uploaded_csv(uploaded_file):
    """Parsea el CSV subido al formato esperado (German Credit)."""
    df = pd.read_csv(uploaded_file)
    if df.shape[1] == 11:
        df = df.iloc[:, 1:]
    df.columns = [
        "Age", "Sex", "Job", "Housing", "Saving_accounts",
        "Checking_account", "Credit_amount", "Duration", "Purpose", "Risk"
    ]
    return df


def prepare_model_data(df):
    """Crea variables dummy y filtra NA para el modelo."""
    data = df.copy()
    data["female"] = (data["Sex"] == "female").astype(int)
    data["s_little"] = (data["Saving_accounts"] == "little").astype(int)
    data["s_rich"] = (data["Saving_accounts"] == "rich").astype(int)
    data["c_little"] = (data["Checking_account"] == "little").astype(int)
    data["c_moderate"] = (data["Checking_account"] == "moderate").astype(int)
    data["c_rich"] = (data["Checking_account"] == "rich").astype(int)
    data["good"] = (data["Risk"] == "good").astype(int)
    return data.dropna(subset=["Saving_accounts", "Checking_account"])


MODEL_FEATURES = ["Age", "Duration", "female", "s_little", "s_rich", "c_little", "c_moderate", "c_rich"]
