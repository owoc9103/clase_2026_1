import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# Ruta del CSV (portable: desde Pages/ sube a ML_Finanzas_V2/)
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CSV_PATH = BASE_DIR / "Insumos" / "stock_prices_daily.csv"

st.markdown("# Bienvenido a mi aplicación de Streamlit :wave:")

st.markdown("Esta aplicación es un proyecto de prueba para demostrar las capacidades de Streamlit. Aquí puedes encontrar diferentes visualizaciones de precios de acciones.")

df = pd.read_csv(CSV_PATH)

# Convertir fecha y quitar timezone (evita "Invalid comparison between dtype=datetime64[ns, UTC-05:00] and Timestamp")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
if hasattr(df["Date"].dtype, "tz") and df["Date"].dtype.tz is not None:
    df["Date"] = df["Date"].apply(lambda x: x.replace(tzinfo=None) if pd.notna(x) and getattr(x, "tzinfo", None) else x)
    df["Date"] = pd.to_datetime(df["Date"])
df = df.dropna(subset=["Date", "Close"])

with st.expander("📋 Ver datos"):
    st.dataframe(df, use_container_width=True)

st.title("📈 Gráfica de Precio por Fecha")

# Selector de ticker con información de la empresa
tickers = sorted(df["Ticker"].unique())
ticker = st.selectbox("Selecciona el Ticker", tickers)

# Mostrar nombre de la empresa cuando hay info
if "Company_Name" in df.columns:
    empresa = df[df["Ticker"] == ticker]["Company_Name"].iloc[0]
    st.caption(f"📌 {empresa}")

# Filtrar por ticker (mostrar gráfico completo con todos los datos)
df_filtrado = df[df["Ticker"] == ticker].sort_values("Date").copy()

# Opciones adicionales para la gráfica
col1, col2, col3 = st.columns(3)
with col1:
    mostrar_volumen = st.checkbox("Mostrar volumen", value=False)
with col2:
    mostrar_media = st.checkbox("Media móvil (21 días)", value=False)
with col3:
    tema = st.selectbox("Tema", ["plotly_dark", "plotly_white", "seaborn"], index=0)

# Calcular media móvil si se solicita
if mostrar_media and len(df_filtrado) >= 21:
    df_filtrado["MA_21"] = df_filtrado["Close"].rolling(window=21).mean()

# Crear gráfica con Plotly
fig = go.Figure()

# Línea principal de precio
fig.add_trace(go.Scatter(
    x=df_filtrado["Date"],
    y=df_filtrado["Close"],
    mode="lines",
    name="Precio de cierre",
    line=dict(color="#00d4ff", width=2.5),
    fill="tozeroy",
    fillcolor="rgba(0, 212, 255, 0.1)",
    hovertemplate="<b>%{x|%d/%m/%Y}</b><br>Precio: $%{y:,.2f}<extra></extra>"
))

# Media móvil
if mostrar_media and "MA_21" in df_filtrado.columns:
    fig.add_trace(go.Scatter(
        x=df_filtrado["Date"],
        y=df_filtrado["MA_21"],
        mode="lines",
        name="Media 21 días",
        line=dict(color="#ff6b6b", width=2, dash="dash"),
        hovertemplate="<b>%{x|%d/%m/%Y}</b><br>MA: $%{y:,.2f}<extra></extra>"
    ))

# Gráfica de volumen (eje secundario)
if mostrar_volumen and "Volume" in df_filtrado.columns:
    fig.add_trace(go.Bar(
        x=df_filtrado["Date"],
        y=df_filtrado["Volume"],
        name="Volumen",
        opacity=0.3,
        yaxis="y2",
        marker_color="#4ecdc4",
        hovertemplate="<b>%{x|%d/%m/%Y}</b><br>Volumen: %{y:,.0f}<extra></extra>"
    ))

# Layout
layout_config = dict(
    title=dict(
        text=f"Precio de cierre - {ticker}",
        font=dict(size=22),
        x=0.5,
        xanchor="center"
    ),
    xaxis=dict(
        title="Fecha",
        rangeslider=dict(visible=True, thickness=0.05),
        type="date",
        tickformat="%b %Y",
        showgrid=True,
        gridcolor="rgba(128,128,128,0.2)"
    ),
    yaxis=dict(
        title="Precio de Cierre (USD)",
        tickformat="$,.2f",
        showgrid=True,
        gridcolor="rgba(128,128,128,0.2)",
        zeroline=False
    ),
    template=tema,
    hovermode="x unified",
    margin=dict(l=60, r=60, t=80, b=60),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="center",
        x=0.5
    ),
    plot_bgcolor="rgba(0,0,0,0)" if "dark" in tema else "rgba(255,255,255,0)",
    paper_bgcolor="rgba(0,0,0,0)" if "dark" in tema else "rgba(255,255,255,0)"
)

if mostrar_volumen and "Volume" in df_filtrado.columns:
    layout_config["yaxis2"] = dict(
        title="Volumen",
        overlaying="y",
        side="right",
        showgrid=False,
        tickformat=",.0f"
    )

fig.update_layout(**layout_config)

st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": True})