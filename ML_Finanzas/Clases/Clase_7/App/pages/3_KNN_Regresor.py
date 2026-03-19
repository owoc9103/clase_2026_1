# -*- coding: utf-8 -*-
"""
Clase 7 - KNN Regresor
Predicción de precios de boletos aéreos
Dataset: plataforma BS
"""

import streamlit as st

st.title("📈 KNN Regresor - Precio de boletos aéreos")

st.markdown("""
---

**Contexto de aplicación empresarial: Estimación de precios de boletos aéreos**

**Escenario:**

Una agencia de viajes o plataforma de reservas aéreas maneja ofertas de múltiples aerolíneas entre distintas ciudades. 
Los precios varían según la **aerolínea** (`airline`), la **ruta** (ciudad de origen `source_city` y destino `destination_city`), 
el **número de paradas** (`stops`), la **duración del vuelo** (`duration`), los **días de anticipación** (`days_left`), 
la **clase** (`class`) y las **franjas horarias** de salida y llegada (`departure_time`, `arrival_time`). 
Los gerentes necesitan estimar el precio esperado de un boleto para asesorar a los clientes, definir estrategias de compra anticipada 
y comparar ofertas entre aerolíneas y rutas.

**Problema empresarial:**

Los principales problemas incluyen:

1. **Precios dinámicos y falta de referencia:** Las aerolíneas ajustan los precios según demanda, temporada y disponibilidad. 
   Sin un modelo de estimación, es difícil saber si una oferta es conveniente o si conviene esperar.

2. **Decisión de compra anticipada:** No está claro cuántos días antes (`days_left`) conviene comprar ni cómo influyen 
   la ruta, la clase o el número de paradas en el precio final.

3. **Comparación entre rutas y aerolíneas:** Falta de herramientas para estimar el precio esperado según combinaciones 
   de origen, destino, aerolínea y clase, lo que dificulta recomendar la mejor opción al cliente.

4. **Planificación de presupuestos:** Los clientes corporativos o viajeros frecuentes necesitan estimaciones de costo 
   para planificar viajes sin conocer el precio exacto de antemano.

---

Este ejercicio construye un **modelo KNN para regresión** que predice el **precio** (`price`) a partir de las variables anteriores.

**¿Cómo usarlo?** Copia cada bloque de código en orden en un nuevo notebook de Google Colab. 
Ejecuta celda por celda para construir el flujo completo desde cero: carga de datos, preprocesamiento, 
entrenamiento del modelo, evaluación y búsqueda del valor óptimo de K.

---

**Dataset**

El archivo de datos está disponible en la **plataforma BS**. Antes de empezar:
1. Descarga el CSV de precios de boletos aéreos desde la plataforma.
2. Al ejecutar el **Bloque 2** en Colab, se abrirá un cuadro para subir archivos.
3. Selecciona el archivo que descargaste y el código lo cargará automáticamente.

---

**Variables del dataset (columnas del DataFrame)**

| Columna | Traducción | Descripción | Uso en el modelo |
|---------|------------|-------------|------------------|
| `airline` | Aerolínea | Nombre de la aerolínea | Categórica (One-Hot) |
| `flight` | Vuelo | Código o número del vuelo | No se usa (muy específico) |
| `source_city` | Ciudad de origen | Ciudad desde donde sale el vuelo | Categórica (One-Hot) |
| `departure_time` | Hora de salida | Franja horaria de salida (ej. Morning, Evening) | Categórica (One-Hot) |
| `stops` | Paradas | Número de escalas del vuelo | Numérica (StandardScaler) |
| `arrival_time` | Hora de llegada | Franja horaria de llegada | Categórica (One-Hot) |
| `destination_city` | Ciudad de destino | Ciudad a la que llega el vuelo | Categórica (One-Hot) |
| `class` | Clase | Tipo de asiento (Economy, Business, etc.) | Categórica (One-Hot) |
| `duration` | Duración | Tiempo del vuelo (ej. "2h 50m") | Se convierte a minutos numéricos |
| `days_left` | Días restantes | Días hasta la fecha del vuelo | Numérica (StandardScaler) |
| `price` | Precio | Costo del boleto | **Variable objetivo** (a predecir) |

---

**Objetivo del ejercicio**

Construir un modelo **KNN Regresor** que estime el **precio del boleto** a partir de las características 
del vuelo. Se evalúa con MSE, RMSE, R² y MAE, y se busca el valor óptimo de K mediante validación cruzada.
""")

st.markdown("---")

# ========== Bloque 1: Importaciones ==========
st.header("Bloque 1: Importaciones")

st.markdown("""
**Referencia:** Librerías para datos (pandas, numpy), modelo KNN, preprocesamiento y métricas.
""")

st.code("""# === BLOQUE 1: Importar librerías ===
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')""", language="python")

# ========== Bloque 2: Cargar datos desde BS ==========
st.header("Bloque 2: Cargar el dataset (desde la plataforma BS)")

st.markdown("""
**Referencia:** 1) Descarga el CSV de precios de boletos aéreos desde la plataforma BS.  
2) Ejecuta la celda en Colab; se abrirá un cuadro para **subir el archivo** que descargaste.
""")

st.code("""# === BLOQUE 2: Cargar datos ===
# Descarga el dataset desde la plataforma BS, luego súbelo aquí
from google.colab import files
uploaded = files.upload()  # Selecciona el archivo CSV descargado de BS

# Cargar el CSV (usa el nombre del archivo que subiste)
nombre_archivo = list(uploaded.keys())[0]
df = pd.read_csv(nombre_archivo)
print(f"Filas: {len(df)}, Columnas: {df.columns.tolist()}")
df.head()""", language="python")

# ========== Bloque 3: Exploración y limpieza ==========
st.header("Bloque 3: Exploración y limpieza de datos")

st.markdown("""
**Referencia:** Revisar valores faltantes. Eliminar filas con `price` faltante.  
Si la columna `duration` viene como texto (ej. "2h 50m"), se convierte a minutos (`duration_min`).
""")

st.code("""# === BLOQUE 3: Exploración y limpieza ===
print(df.info())
print(df.isnull().sum())

# Eliminar filas con precio faltante (columna: price)
df = df.dropna(subset=['price'])

# Si duration es texto (ej. "2h 50m"), convertir a minutos
import re
def duration_to_minutes(s):
    if pd.isna(s): return np.nan
    s = str(s)
    h = re.findall(r'(\\d+)h', s)
    m = re.findall(r'(\\d+)m', s)
    hrs = int(h[0]) if h else 0
    mins = int(m[0]) if m else 0
    return hrs * 60 + mins

if 'duration' in df.columns:
    if df['duration'].dtype == object:
        df['duration_min'] = df['duration'].apply(duration_to_minutes)
    else:
        df['duration_min'] = df['duration']
    df = df.dropna(subset=['duration_min'])
print(df.head())""", language="python")

# ========== Bloque 4: Preparar X e y ==========
st.header("Bloque 4: Preparar características (X) y variable objetivo (y)")

st.markdown("""
**Referencia:** Separar columnas numéricas y categóricas. Objetivo: **price**.  
Columnas según el dataset: airline, source_city, destination_city, class, departure_time, arrival_time (categóricas); duration_min, stops, days_left (numéricas).
""")

st.code("""# === BLOQUE 4: Preparar X e y ===
# Columnas del dataset: airline, flight, source_city, departure_time, stops, arrival_time,
# destination_city, class, duration, days_left, price
target_col = 'price'
numeric_cols = ['duration_min', 'stops', 'days_left']
categorical_cols = ['airline', 'source_city', 'destination_city', 'class', 'departure_time', 'arrival_time']

available_num = [c for c in numeric_cols if c in df.columns]
available_cat = [c for c in categorical_cols if c in df.columns]
if not available_num:
    available_num = [c for c in ['duration_min', 'duration'] if c in df.columns]

X = df[available_num + available_cat].copy()
y = df[target_col]

if available_cat:
    X = pd.get_dummies(X, columns=available_cat, drop_first=True)
X = X.fillna(X.median())
print(X.head())
print(f"\\nVariable objetivo (price) - media: {y.mean():.0f}")""", language="python")

# ========== Bloque 5: Train/Test split ==========
st.header("Bloque 5: Dividir en entrenamiento y prueba")

st.markdown("""
**Referencia:** 80% entrenamiento, 20% prueba. `random_state=42` para reproducibilidad.
""")

st.code("""# === BLOQUE 5: Train/Test split ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Entrenamiento: {len(X_train)} | Prueba: {len(X_test)}")""", language="python")

# ========== Bloque 6: Escalar ==========
st.header("Bloque 6: Escalar características (StandardScaler)")

st.markdown("""
**Referencia:** KNN usa distancias; StandardScaler evita que variables con rango mayor dominen.  
`fit_transform` solo en train, `transform` en test.
""")

st.code("""# === BLOQUE 6: Escalar características ===
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Escalado aplicado.")""", language="python")

# ========== Bloque 7: Entrenar KNN ==========
st.header("Bloque 7: Crear y entrenar el KNN Regresor")

st.markdown("""
**Referencia:** K=5 vecinos. `fit()` almacena los datos para calcular distancias en predict.
""")

st.code("""# === BLOQUE 7: Entrenar KNN Regresor ===
k = 5
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train_scaled, y_train)
print(f"Modelo entrenado con K={k}")""", language="python")

# ========== Bloque 8: Predecir y evaluar ==========
st.header("Bloque 8: Predecir y evaluar")

st.markdown("""
**Referencia:** Predicciones en test. Métricas: MSE, RMSE, R², MAE.
""")

st.code("""# === BLOQUE 8: Predecir y evaluar ===
y_pred = knn.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.4f}")
print(f"MAE:  {mae:.2f}")""", language="python")

# ========== Bloque 9: K óptimo ==========
st.header("Bloque 9: Buscar K óptimo con validación cruzada")

st.markdown("""
**Referencia:** Probar K=1 a 30, elegir el que minimice RMSE en validación cruzada (5 folds).
""")

st.code("""# === BLOQUE 9: Buscar K óptimo ===
k_values = range(1, 31)
cv_rmse = []
for k in k_values:
    model = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')
    cv_rmse.append(np.sqrt(-scores.mean()))

optimal_k = k_values[np.argmin(cv_rmse)]
print(f"K óptimo: {optimal_k}")
print(f"RMSE con K óptimo: {min(cv_rmse):.2f}")""", language="python")

# ========== Bloque 10: Modelo final ==========
st.header("Bloque 10: Modelo final con K óptimo")

st.markdown("""
**Referencia:** Reentrenar con el K elegido y evaluar en test.
""")

st.code("""# === BLOQUE 10: Modelo final con K óptimo ===
knn_final = KNeighborsRegressor(n_neighbors=optimal_k)
knn_final.fit(X_train_scaled, y_train)
y_pred_final = knn_final.predict(X_test_scaled)

print(f"RMSE final: {np.sqrt(mean_squared_error(y_test, y_pred_final)):.2f}")
print(f"R² final:   {r2_score(y_test, y_pred_final):.4f}")""", language="python")

st.info("💡 **Flujo:** 1) Descarga el dataset desde la plataforma BS. 2) Copia cada bloque en Colab en orden. 3) Al ejecutar el Bloque 2, sube el archivo que descargaste. Las columnas del dataset están definidas en la tabla de variables arriba.")
