# -*- coding: utf-8 -*-
"""
Clase 7 - KNN Regresor
Implementación con California Housing
"""

import streamlit as st

st.title("📈 KNN Regresor - California Housing")

st.markdown("""
En esta página se presenta la implementación del **KNN Regresor** usando el dataset 
**California Housing** de scikit-learn. El objetivo es predecir el **valor mediano de las viviendas** 
en cada bloque censal de California, a partir de variables como ingreso mediano, antigüedad de la vivienda, 
número de habitaciones, etc.

Si ya revisaste el **ejemplo trivial**, aquí verás la misma lógica aplicada a un dataset real.
""")

# ========== Elección de K ==========
st.header("Elección del valor óptimo de K")

st.markdown("""
El valor de **K** (número de vecinos) es el hiperparámetro principal de KNN. Su elección afecta el rendimiento:

- **K muy pequeño (ej. K=1):** El modelo es muy sensible al ruido; cada predicción depende de un solo vecino. 
  Puede dar predicciones erráticas si hay outliers.

- **K muy grande:** El modelo se "suaviza" demasiado; la predicción se acerca al promedio global de todos los datos, 
  perdiendo capacidad de captar patrones locales.

**Métodos para elegir K:**

1. **Validación cruzada (k-fold):** Dividir los datos en K particiones, entrenar en K-1 y evaluar en la restante; 
   repetir K veces. El K que minimice el error promedio es una buena candidato.

2. **Grid Search:** Probar un rango de valores (1, 3, 5, 7, ..., 31) y elegir el que mejor rendimiento tenga 
   en validación cruzada.

3. **Regla práctica:** K ≈ √n, donde n es el número de muestras. Es solo una guía inicial.

4. **K impar:** En clasificación binaria evita empates; en regresión no es crítico, pero se suele usar por convención.
""")

# ========== Código paso 1: Imports ==========
st.header("Paso 1: Importaciones")

st.markdown("""
Antes de empezar, importamos las librerías necesarias:

- **numpy:** Operaciones numéricas y arrays.
- **sklearn.datasets:** Para cargar California Housing.
- **sklearn.model_selection:** Para dividir datos (train_test_split) y validación cruzada.
- **sklearn.neighbors:** KNeighborsRegressor.
- **sklearn.preprocessing:** StandardScaler para escalar características.
- **sklearn.metrics:** MSE, R², MAE para evaluar el modelo.
""")

st.code("""import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error""", language="python")

# ========== Código paso 2: Cargar datos ==========
st.header("Paso 2: Cargar datos")

st.markdown("""
`fetch_california_housing()` devuelve un objeto con:
- **data:** Matriz de características (ingreso mediano, antigüedad, habitaciones, etc.).
- **target:** Valor mediano de las viviendas (variable a predecir).

Separamos en **X** (características) e **y** (objetivo). Cada fila es un bloque censal.
""")

st.code("""housing = fetch_california_housing()
X = housing.data   # Características (MedInc, HouseAge, etc.)
y = housing.target # Valor mediano de viviendas""", language="python")

# ========== Código paso 3: Dividir datos ==========
st.header("Paso 3: Dividir en entrenamiento y prueba")

st.markdown("""
Dividimos los datos en dos conjuntos:
- **Entrenamiento (80%):** Sobre el cual el modelo "aprende" (en KNN, simplemente los almacena).
- **Prueba (20%):** Para evaluar el rendimiento en datos no vistos.

`random_state=42` asegura reproducibilidad.
""")

st.code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)""", language="python")

# ========== Código paso 4: Escalado ==========
st.header("Paso 4: Escalar características (importante en KNN)")

st.markdown("""
KNN usa **distancias** entre puntos. Si una característica tiene rango (0, 1000) y otra (0, 1), 
la primera dominará el cálculo de distancia aunque no sea más relevante.

**StandardScaler** transforma cada característica para que tenga media 0 y desviación estándar 1:
$$x_{scaled} = \\frac{x - \\mu}{\\sigma}$$

Importante: se ajusta **solo con el conjunto de entrenamiento** (`fit_transform` en train, `transform` en test) 
para evitar filtrado de información (data leakage).
""")

st.code("""scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)""", language="python")

# ========== Código paso 5: Entrenar modelo ==========
st.header("Paso 5: Crear y entrenar el KNN Regresor")

st.markdown("""
Creamos el modelo con `n_neighbors=5` (K=5). En KNN, el "entrenamiento" consiste en almacenar 
los datos de entrenamiento; no hay optimización de parámetros como en regresión lineal.

`fit()` guarda los datos escalados para usarlos en las predicciones.
""")

st.code("""k = 5
knn_regressor = KNeighborsRegressor(n_neighbors=k)
knn_regressor.fit(X_train_scaled, y_train)""", language="python")

# ========== Código paso 6: Predecir y evaluar ==========
st.header("Paso 6: Predecir y evaluar")

st.markdown("""
Para cada punto de prueba, el modelo:
1. Calcula la distancia a todos los puntos de entrenamiento.
2. Selecciona los K más cercanos.
3. Predice el promedio de sus valores objetivo.

Luego evaluamos con:
- **MSE:** Penaliza más los errores grandes.
- **RMSE:** Misma unidad que la variable objetivo.
- **R²:** Proporción de varianza explicada (0 a 1).
- **MAE:** Error promedio en valor absoluto.
""")

st.code("""y_pred = knn_regressor.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²: {r2:.4f}")
print(f"MAE: {mae:.4f}")""", language="python")

# ========== Código K óptimo ==========
st.header("Encontrar K óptimo con validación cruzada")

st.markdown("""
En lugar de fijar K=5, podemos probar varios valores y elegir el que minimice el error promedio 
en validación cruzada. `cross_val_score` divide los datos en 5 folds, entrena en 4 y evalúa en 1, 
repitiendo 5 veces. Usamos `neg_mean_squared_error` porque scikit-learn maximiza las métricas; 
negando el MSE, maximizar el score equivale a minimizar el MSE.
""")

st.code("""from sklearn.model_selection import cross_val_score

k_values = range(1, 31)
cv_rmse = []

for k in k_values:
    knn = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(knn, X_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')
    rmse_scores = np.sqrt(-scores)
    cv_rmse.append(rmse_scores.mean())

optimal_k = k_values[np.argmin(cv_rmse)]
print(f"K óptimo: {optimal_k}")
print(f"RMSE con K óptimo: {min(cv_rmse):.4f}")""", language="python")

st.info("💡 Copia cada bloque en orden en un notebook de Google Colab para construir la implementación desde cero.")
