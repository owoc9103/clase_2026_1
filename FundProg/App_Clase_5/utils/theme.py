# -*- coding: utf-8 -*-
"""
Estilos compatibles con tema claro y oscuro de Streamlit.
"""

import streamlit as st


@st.cache_data
def _get_theme_css() -> str:
    """CSS en caché para no recalcular en cada rerun."""
    return """
    <style>
    /* === Tema claro (default) === */
    .objetivo-card,
    .app-theme-objetivo-card {
        background: #f8f9fa;
        color: #1a1a2e;
        border-left: 4px solid #1e3a5f;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .app-theme-tip-text {
        text-align: center;
        color: #666;
    }
    .app-theme-info-box {
        background: #e8f4fd;
        color: #1a1a2e;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1e3a5f;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white !important;
    }
    .main-header h1, .main-header p {
        color: white !important;
    }

    /* === Tema oscuro === */
    @media (prefers-color-scheme: dark) {
        .objetivo-card, .app-theme-objetivo-card {
            background: #2d3748;
            color: #e2e8f0;
            border-left-color: #63b3ed;
        }
        .app-theme-tip-text { color: #a0aec0; }
        .app-theme-info-box {
            background: #2c5282;
            color: #e2e8f0;
            border-left-color: #63b3ed;
        }
    }

    [data-theme="dark"] .objetivo-card,
    [data-theme="dark"] .app-theme-objetivo-card,
    [data-theme="Dark"] .objetivo-card,
    [data-theme="Dark"] .app-theme-objetivo-card {
        background: #2d3748 !important;
        color: #e2e8f0 !important;
        border-left-color: #63b3ed !important;
    }
    [data-theme="dark"] .app-theme-tip-text,
    [data-theme="Dark"] .app-theme-tip-text {
        color: #a0aec0 !important;
    }
    [data-theme="dark"] .app-theme-info-box,
    [data-theme="Dark"] .app-theme-info-box {
        background: #2c5282 !important;
        color: #e2e8f0 !important;
        border-left-color: #63b3ed !important;
    }

    .stSuccess, .stError { border-radius: 8px; }
    </style>
    """


def inject_theme_styles() -> None:
    """Inyecta CSS para legibilidad en tema claro y oscuro."""
    st.markdown(_get_theme_css(), unsafe_allow_html=True)
