# -*- coding: utf-8 -*-
"""
Clase 7 - Código completo para Google Colab
"""

import streamlit as st

st.title("📋 Código completo para Google Colab")

st.markdown("""
Copia cada bloque en orden en un nuevo notebook de Google Colab. 
Ejecuta celda por celda para construir el KNN Regresor desde cero.

Revisa primero el **Ejemplo trivial** para entender la lógica; luego este código aplica lo mismo 
al dataset California Housing.
""")

st.markdown("---")

# ========== Ejemplo trivial (opcional) ==========
st.header("Ejemplo trivial (opcional)")

st.markdown("""
Si quieres empezar con algo mínimo, este bloque implementa el ejemplo trivial de la página anterior 
(5 viviendas, predicción para un punto nuevo). Úsalo para verificar que entiendes la lógica.
""")

st.code("""# Ejemplo trivial: 5 puntos, K=3
import numpy as np

X_train = np.array([[1, 2], [2, 3], [3, 1], [4, 4], [5, 2]])
y_train = np.array([10, 15, 12, 20, 18])
Q = np.array([2.5, 2])
K = 3

distancias = np.sqrt(np.sum((X_train - Q) ** 2, axis=1))
indices = np.argsort(distancias)[:K]
prediccion = np.mean(y_train[indices])
print(f"Predicción: {prediccion:.2f}")  # 12.33""", language="python")

st.markdown("---")
st.header("California Housing - Implementación completa")

# ========== Bloque 1 ==========
st.subheader("Celda 1: Importaciones")
st.code("""import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt""", language="python")

# ========== Bloque 2 ==========
st.subheader("Celda 2: Cargar datos")
st.code("""housing = fetch_california_housing()
X = housing.data
y = housing.target
print(f"Características: {X.shape[1]}")
print(f"Muestras: {X.shape[0]}")""", language="python")

# ========== Bloque 3 ==========
st.subheader("Celda 3: Dividir datos")
st.code("""X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Entrenamiento: {len(X_train)} | Prueba: {len(X_test)}")""", language="python")

# ========== Bloque 4 ==========
st.subheader("Celda 4: Escalar características")
st.code("""scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Escalado aplicado (StandardScaler)")""", language="python")

# ========== Bloque 5 ==========
st.subheader("Celda 5: Entrenar KNN Regresor")
st.code("""k = 5
knn = KNeighborsRegressor(n_neighbors=k)
knn.fit(X_train_scaled, y_train)
print(f"Modelo entrenado con K={k}")""", language="python")

# ========== Bloque 6 ==========
st.subheader("Celda 6: Predecir y evaluar")
st.code("""y_pred = knn.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")
print(f"MAE:  {mae:.4f}")""", language="python")

# ========== Bloque 7 ==========
st.subheader("Celda 7: Buscar K óptimo (opcional)")
st.code("""k_values = range(1, 31)
cv_rmse = []

for k in k_values:
    model = KNeighborsRegressor(n_neighbors=k)
    scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')
    cv_rmse.append(np.sqrt(-scores.mean()))

optimal_k = k_values[np.argmin(cv_rmse)]
print(f"K óptimo: {optimal_k}")""", language="python")

# ========== Bloque 8 ==========
st.subheader("Celda 8: Graficar K vs RMSE (opcional)")
st.code("""plt.figure(figsize=(10, 5))
plt.plot(k_values, cv_rmse, 'b-o', markersize=4)
plt.axvline(x=optimal_k, color='r', linestyle='--', label=f'K óptimo = {optimal_k}')
plt.xlabel('K (número de vecinos)')
plt.ylabel('RMSE (validación cruzada)')
plt.title('Selección de K óptimo para KNN Regresor')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()""", language="python")

# ========== Funciones auxiliares ==========
st.markdown("---")
st.header("Funciones auxiliares (opcional)")

st.subheader("Distancia Euclidiana")
st.code("""def distancia_euclidiana(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Los puntos deben tener la misma dimensión")
    return np.sqrt(sum((a - b)**2 for a, b in zip(p1, p2)))

# Ejemplo:
# d = distancia_euclidiana([1, 2, 3], [4, 5, 6])
# print(d)  # 5.196...""", language="python")

st.subheader("Distancia Manhattan")
st.code("""def distancia_manhattan(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Los puntos deben tener la misma dimensión")
    return sum(abs(a - b) for a, b in zip(p1, p2))

# Ejemplo:
# d = distancia_manhattan([1, 2, 3], [4, 5, 6])
# print(d)  # 9""", language="python")

st.subheader("Función para estandarizar características")
st.code("""def estandarizar(X_train, X_test):
    scaler = StandardScaler()
    X_train_std = scaler.fit_transform(X_train)
    X_test_std = scaler.transform(X_test)
    return X_train_std, X_test_std, scaler

# Uso:
# X_train_std, X_test_std, scaler = estandarizar(X_train, X_test)""", language="python")

st.info("💡 **Tip:** En Colab, cada bloque puede ir en una celda. Usa Shift+Enter para ejecutar.")
