# -*- coding: utf-8 -*-
"""Utilidades compartidas para la aplicación del Taller 6."""

import pandas as pd
import streamlit as st
from pathlib import Path

# Clave en session_state para los datos cargados por el usuario
SESSION_DATA_KEY = "taller6_data"

# Rutas por defecto (Excel y CSV como fallback sin dependencias extra)
INSUMOS_DIR = Path(__file__).parent.parent / "Insumos"
DATA_PATH_XLSX = INSUMOS_DIR / "taller6-dataset_punto_venta.xlsx"
DATA_PATH_CSV = INSUMOS_DIR / "taller6-dataset_punto_venta.csv"


def _normalize_dataframe(df):
    """Normaliza fechas y valida el dataframe."""
    if df is None or "Fecha" not in df.columns:
        return None
    df = df.copy()
    col = df["Fecha"]
    # Ya es datetime
    if pd.api.types.is_datetime64_any_dtype(col):
        return df
    # Formato YYYYMMDD (int, desde CSV)
    if col.dtype in ("int64", "float64") or "int" in str(col.dtype) or "float" in str(col.dtype):
        s = col.dropna().astype(int).astype(str).str.zfill(8)
        df.loc[col.notna(), "Fecha"] = pd.to_datetime(s, format="%Y%m%d", errors="coerce")
        return df
    # Objeto/texto
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="mixed", errors="coerce")
    return df


def _get_excel_engine():
    """Obtiene el primer motor disponible para leer Excel."""
    for pkg, eng in [("openpyxl", "openpyxl"), ("python_calamine", "calamine")]:
        try:
            __import__(pkg)
            return eng
        except ImportError:
            continue
    return None


def load_default_data():
    """Carga los datos por defecto (CSV o Excel). Prioriza CSV (sin dependencias extra)."""
    if DATA_PATH_CSV.exists():
        try:
            df = pd.read_csv(DATA_PATH_CSV)
            return _normalize_dataframe(df)
        except Exception:
            pass
    engine = _get_excel_engine()
    if engine and DATA_PATH_XLSX.exists():
        try:
            df = pd.read_excel(DATA_PATH_XLSX, engine=engine)
            return _normalize_dataframe(df)
        except Exception:
            pass
    return None


def load_data():
    """Carga el dataset (prioriza session_state, luego datos por defecto CSV/Excel)."""
    if SESSION_DATA_KEY in st.session_state and st.session_state[SESSION_DATA_KEY] is not None:
        return st.session_state[SESSION_DATA_KEY]
    df = load_default_data()
    if df is not None:
        return df
    st.error("No hay datos cargados. Ve a la página principal (Home) y carga el archivo o usa «Cargar datos por defecto».")
    return None


def word_reminder():
    """Mensaje recordatorio para incluir en el documento Word."""
    st.info(
        "📋 **Importante:** Incluye esta gráfica/análisis en tu documento Word del taller "
        "y escribe tu interpretación de los resultados."
    )
