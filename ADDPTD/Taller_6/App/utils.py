# -*- coding: utf-8 -*-
"""Utilidades compartidas para la aplicación del Taller 6."""

import pandas as pd
import streamlit as st
from pathlib import Path

SESSION_DATA_KEY = "taller6_data"
INSUMOS_DIR = Path(__file__).parent.parent / "Insumos"
DATA_PATH_CSV = INSUMOS_DIR / "taller6-dataset_punto_venta.csv"


def _normalize_dataframe(df):
    """Normaliza fechas y valida el dataframe."""
    if df is None or "Fecha" not in df.columns:
        return None
    df = df.copy()
    col = df["Fecha"]
    if pd.api.types.is_datetime64_any_dtype(col):
        return df
    if col.dtype in ("int64", "float64") or "int" in str(col.dtype) or "float" in str(col.dtype):
        s = col.dropna().astype(int).astype(str).str.zfill(8)
        df.loc[col.notna(), "Fecha"] = pd.to_datetime(s, format="%Y%m%d", errors="coerce")
        return df
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="mixed", errors="coerce")
    return df


def load_default_data():
    """Carga los datos por defecto desde el CSV del repositorio."""
    if DATA_PATH_CSV.exists():
        try:
            df = pd.read_csv(DATA_PATH_CSV)
            return _normalize_dataframe(df)
        except Exception:
            pass
    return None


def load_data():
    """Carga el dataset (prioriza session_state, luego CSV por defecto)."""
    if SESSION_DATA_KEY in st.session_state and st.session_state[SESSION_DATA_KEY] is not None:
        return st.session_state[SESSION_DATA_KEY]
    df = load_default_data()
    if df is not None:
        return df
    st.error("No hay datos cargados. Ve a la página principal (Home) y carga el archivo CSV.")
    return None
