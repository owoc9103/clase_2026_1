# -*- coding: utf-8 -*-
"""Estilos compartidos de la aplicación Streamlit (modo claro y oscuro)."""

CUSTOM_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero (siempre fondo oscuro, texto claro) ── */
    .hero {
        text-align: center;
        padding: 2rem 2rem 1.5rem;
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        border-radius: 16px;
        margin-bottom: 1.5rem;
        color: #ffffff !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.18);
    }
    .hero h1, .hero p, .hero span, .hero strong {
        color: #ffffff !important;
    }
    .hero h1 { margin: 0; font-size: 2rem; font-weight: 700; }
    .hero p  { margin: 0.75rem 0 0; opacity: 0.95; font-size: 1.05rem; }

    /* ── Cajas informativas — MODO CLARO ── */
    .step-card {
        background: #ffffff;
        border-left: 4px solid #2c5364;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.25rem;
        margin: 0.75rem 0;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
        color: #0f172a !important;
    }
    .step-card h4 { margin: 0 0 0.4rem; color: #203a43 !important; }
    .step-card p, .step-card li, .step-card span, .step-card em, .step-card code {
        color: #334155 !important;
    }
    .step-card code {
        background: #f1f5f9 !important;
        padding: 0.1em 0.35em;
        border-radius: 4px;
    }

    .context-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin: 1rem 0;
        line-height: 1.65;
        color: #0f172a !important;
    }
    .context-box code {
        color: #1e40af !important;
        background: #e2e8f0 !important;
        padding: 0.1em 0.35em;
        border-radius: 4px;
    }
    .context-box h3, .context-box h4, .context-box p, .context-box li,
    .context-box span, .context-box strong, .context-box em {
        color: #0f172a !important;
    }
    .context-box h4 {
        margin: 1rem 0 0.4rem;
        font-size: 1rem;
    }

    .interpret-box {
        background: #f0f7ff;
        border: 1px solid #bfdbfe;
        border-radius: 10px;
        padding: 0.85rem 1rem;
        margin: 0.5rem 0;
        font-size: 0.9rem;
        line-height: 1.55;
        color: #0f172a !important;
    }
    .interpret-box ol, .interpret-box ul {
        margin: 0.35rem 0 0.75rem 1.1rem;
        padding-left: 1rem;
    }
    .interpret-box p, .interpret-box li,
    .interpret-box span, .interpret-box strong, .interpret-box em {
        color: #0f172a !important;
    }
    .interpret-box li {
        margin-bottom: 0.35rem;
        line-height: 1.5;
    }
    .interpret-box code {
        color: #1e40af !important;
        background: #dbeafe !important;
        padding: 0.12em 0.4em;
        border-radius: 4px;
        font-size: 0.88em;
    }

    .reflection-box {
        background: linear-gradient(145deg, #fffbeb, #fef3c7);
        border: 1px solid #fcd34d;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin: 1rem 0;
        color: #422006 !important;
    }
    .reflection-box h3, .reflection-box p, .reflection-box li,
    .reflection-box span, .reflection-box strong {
        color: #422006 !important;
    }

    .math-box {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin: 1rem 0 1.5rem 0;
        line-height: 1.65;
        color: #0f172a !important;
    }
    .math-box h3, .math-box h4, .math-box p, .math-box li,
    .math-box span, .math-box strong, .math-box em {
        color: #0f172a !important;
    }
    .math-box code {
        color: #1e40af !important;
        background: #e2e8f0 !important;
        padding: 0.1em 0.35em;
        border-radius: 4px;
    }

    /* Sidebar — modo claro */
    .stApp[data-theme="light"] div[data-testid="stSidebar"],
    .stApp:not([data-theme="dark"]) div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8fafc 0%, #eef2f7 100%);
    }

    /* ── Cajas informativas — MODO OSCURO ── */
    .stApp[data-theme="dark"] .step-card {
        background: #1e293b;
        border-left-color: #38bdf8;
        box-shadow: 0 2px 12px rgba(0,0,0,0.35);
        color: #e2e8f0 !important;
    }
    .stApp[data-theme="dark"] .step-card h4 { color: #f1f5f9 !important; }
    .stApp[data-theme="dark"] .step-card p,
    .stApp[data-theme="dark"] .step-card li,
    .stApp[data-theme="dark"] .step-card span,
    .stApp[data-theme="dark"] .step-card em {
        color: #cbd5e1 !important;
    }
    .stApp[data-theme="dark"] .step-card code {
        color: #7dd3fc !important;
        background: #0f172a !important;
    }

    .stApp[data-theme="dark"] .context-box {
        background: #1e293b;
        border-color: #475569;
        color: #e2e8f0 !important;
    }
    .stApp[data-theme="dark"] .context-box h3,
    .stApp[data-theme="dark"] .context-box h4,
    .stApp[data-theme="dark"] .context-box p,
    .stApp[data-theme="dark"] .context-box li,
    .stApp[data-theme="dark"] .context-box span,
    .stApp[data-theme="dark"] .context-box strong,
    .stApp[data-theme="dark"] .context-box em {
        color: #e2e8f0 !important;
    }
    .stApp[data-theme="dark"] .context-box code {
        color: #93c5fd !important;
        background: #1e3a8a !important;
    }

    .stApp[data-theme="dark"] .interpret-box {
        background: #172554;
        border-color: #3b82f6;
        color: #f1f5f9 !important;
    }
    .stApp[data-theme="dark"] .interpret-box p,
    .stApp[data-theme="dark"] .interpret-box li,
    .stApp[data-theme="dark"] .interpret-box ul,
    .stApp[data-theme="dark"] .interpret-box ol,
    .stApp[data-theme="dark"] .interpret-box span,
    .stApp[data-theme="dark"] .interpret-box strong,
    .stApp[data-theme="dark"] .interpret-box em {
        color: #f1f5f9 !important;
    }
    .stApp[data-theme="dark"] .interpret-box code {
        color: #93c5fd !important;
        background: #1e3a8a !important;
    }

    .stApp[data-theme="dark"] .reflection-box {
        background: linear-gradient(145deg, #422006, #292524);
        border-color: #ca8a04;
        color: #fef3c7 !important;
    }
    .stApp[data-theme="dark"] .reflection-box h3,
    .stApp[data-theme="dark"] .reflection-box p,
    .stApp[data-theme="dark"] .reflection-box li,
    .stApp[data-theme="dark"] .reflection-box span,
    .stApp[data-theme="dark"] .reflection-box strong {
        color: #fef3c7 !important;
    }

    .stApp[data-theme="dark"] .math-box {
        background: #1e293b;
        border-color: #475569;
        color: #e2e8f0 !important;
    }
    .stApp[data-theme="dark"] .math-box h3,
    .stApp[data-theme="dark"] .math-box h4,
    .stApp[data-theme="dark"] .math-box p,
    .stApp[data-theme="dark"] .math-box li,
    .stApp[data-theme="dark"] .math-box span,
    .stApp[data-theme="dark"] .math-box strong,
    .stApp[data-theme="dark"] .math-box em {
        color: #e2e8f0 !important;
    }
    .stApp[data-theme="dark"] .math-box code {
        color: #93c5fd !important;
        background: #1e3a8a !important;
    }

    .stApp[data-theme="dark"] div[data-testid="stSidebar"] {
        background: var(--secondary-background-color) !important;
    }

    /* Captions y texto auxiliar legible en ambos modos */
    .stApp[data-theme="dark"] .stCaption,
    .stApp[data-theme="dark"] [data-testid="stCaptionContainer"] {
        color: #94a3b8 !important;
    }
</style>
"""


def apply_styles():
    import streamlit as st

    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_hero(title: str, subtitle: str):
    import streamlit as st

    st.markdown(
        f"""
<div class="hero">
    <h1>{title}</h1>
    <p>{subtitle}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def render_interpret_box(html_content: str):
    """Renderiza caja de interpretación con estilos compatibles claro/oscuro."""
    import streamlit as st

    st.markdown(f'<div class="interpret-box">{html_content}</div>', unsafe_allow_html=True)
