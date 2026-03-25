# -*- coding: utf-8 -*-
"""
Clase 7 - Ejemplo trivial KNN Regresión
"""

import streamlit as st
import numpy as np

st.title("🔢 Ejemplo trivial: KNN Regresión paso a paso")

st.markdown("""
Antes de usar librerías como scikit-learn, es fundamental **entender la lógica** del algoritmo. 
Este ejemplo trivial permite seguir el KNN Regresor **paso a paso**, con números concretos, 
sin distracciones de datasets grandes ni código complejo.

**Objetivo:** Dado un conjunto de puntos con valores conocidos, predecir el valor de un punto nuevo 
usando el promedio de los K vecinos más cercanos.
""")

st.markdown("---")

# ========== Datos de entrenamiento ==========
st.header("Paso 1: Datos de entrenamiento")

st.markdown("""
Supongamos que tenemos **5 viviendas** con dos características cada una:
- **X₁:** Área (en decenas de m²)
- **X₂:** Número de habitaciones

Y queremos predecir el **precio** (en millones de pesos).
""")

# Tabla de datos
datos = [
    ("A", 1, 2, 10),
    ("B", 2, 3, 15),
    ("C", 3, 1, 12),
    ("D", 4, 4, 20),
    ("E", 5, 2, 18),
]
tabla = "| Vivienda | X₁ (área) | X₂ (habitaciones) | Precio (millones) |\n|----------|-----------|-------------------|-------------------|\n"
tabla += "\n".join(f"| {v} | {x1} | {x2} | {p} |" for v, x1, x2, p in datos)
st.markdown(tabla)

st.markdown("""
En notación: cada punto tiene coordenadas **(X₁, X₂)** y un valor objetivo **y** (precio).
Por ejemplo, la vivienda A está en (1, 2) y tiene precio 10.
""")

# ========== Punto a predecir ==========
st.header("Paso 2: Punto a predecir")

st.markdown("""
Llega una **nueva vivienda** con:
- **X₁ = 2.5** (área)
- **X₂ = 2** (habitaciones)

Queremos predecir su **precio**. No lo conocemos; el modelo debe estimarlo.
""")

st.info("**Punto de consulta:** Q = (2.5, 2)")

# ========== Distancias ==========
st.header("Paso 3: Calcular distancias")

st.markdown("""
KNN usa la **distancia** para medir similitud. Puntos más cercanos son más similares.

Existen varias formas de medir distancia. A continuación el mismo ejemplo con **cinco tipos** 
(definidos en la sección de teoría):
""")

Q = np.array([2.5, 2])
puntos = [(np.array([1, 2]), 10), (np.array([2, 3]), 15), (np.array([3, 1]), 12), 
          (np.array([4, 4]), 20), (np.array([5, 2]), 18)]
labels = ["A", "B", "C", "D", "E"]

# --- Euclidiana ---
st.subheader("3.1 Distancia Euclidiana (L2)")

st.markdown("""
Distancia en línea recta. Fórmula:
$$d(Q, P) = \\sqrt{(x_Q-x_P)^2 + (y_Q-y_P)^2}$$
""")

distancias_euc = []
for i, (p, precio) in enumerate(puntos):
    d = np.sqrt(np.sum((Q - p) ** 2))
    distancias_euc.append((labels[i], p[0], p[1], precio, round(d, 4)))

tabla_euc = "| Vivienda | (X₁, X₂) | Precio | Distancia Euclidiana a Q=(2.5, 2) |\n|----------|----------|--------|-------------------------------------|\n"
tabla_euc += "\n".join(f"| {v} | ({x1}, {x2}) | {p} | {d} |" for v, x1, x2, p, d in distancias_euc)
st.markdown(tabla_euc)

st.markdown("""
**Ejemplo de cálculo para A:**  
$d(Q, A) = \\sqrt{(2.5-1)^2 + (2-2)^2} = \\sqrt{2.25 + 0} = 1.5$
""")

# --- Manhattan ---
st.subheader("3.2 Distancia Manhattan (L1)")

st.markdown("""
Suma de las diferencias absolutas en cada dimensión (como moverse en una cuadrícula):
$$d(Q, P) = |x_Q - x_P| + |y_Q - y_P|$$
""")

distancias_man = []
for i, (p, precio) in enumerate(puntos):
    d = np.sum(np.abs(Q - p))
    distancias_man.append((labels[i], p[0], p[1], precio, round(d, 4)))

tabla_man = "| Vivienda | (X₁, X₂) | Precio | Distancia Manhattan a Q=(2.5, 2) |\n|----------|----------|--------|--------------------------------------|\n"
tabla_man += "\n".join(f"| {v} | ({x1}, {x2}) | {p} | {d} |" for v, x1, x2, p, d in distancias_man)
st.markdown(tabla_man)

st.markdown("""
**Ejemplo de cálculo para A:**  
$d(Q, A) = |2.5-1| + |2-2| = 1.5 + 0 = 1.5$

**Ejemplo para B:**  
$d(Q, B) = |2.5-2| + |2-3| = 0.5 + 1 = 1.5$
""")

# --- Minkowski ---
st.subheader("3.3 Distancia Minkowski (generalización)")

st.markdown("""
Generaliza Euclidiana y Manhattan. Con parámetro $p$:
$$d(Q, P) = \\left( |x_Q-x_P|^p + |y_Q-y_P|^p \\right)^{1/p}$$

- $p=1$ → Manhattan  
- $p=2$ → Euclidiana  
- $p=3$ → Mayor peso a diferencias grandes
""")

p_mink = 3
distancias_min = []
for i, (p, precio) in enumerate(puntos):
    d = np.power(np.sum(np.power(np.abs(Q - p), p_mink)), 1/p_mink)
    distancias_min.append((labels[i], p[0], p[1], precio, round(d, 4)))

tabla_min = f"| Vivienda | (X₁, X₂) | Precio | Distancia Minkowski (p={p_mink}) a Q=(2.5, 2) |\n|----------|----------|--------|----------------------------------------|\n"
tabla_min += "\n".join(f"| {v} | ({x1}, {x2}) | {p} | {d} |" for v, x1, x2, p, d in distancias_min)
st.markdown(tabla_min)

st.markdown("""
**Ejemplo de cálculo para A (p=3):**  
$d(Q, A) = \\left( |1.5|^3 + |0|^3 \\right)^{1/3} = (3.375 + 0)^{1/3} = 1.5$

**Ejemplo para B (p=3):**  
$d(Q, B) = \\left( |0.5|^3 + |1|^3 \\right)^{1/3} = (0.125 + 1)^{1/3} \\approx 1.04$
""")

# --- Chebyshev ---
st.subheader("3.4 Distancia Chebyshev")

st.markdown("""
Máxima diferencia absoluta entre las coordenadas (distancia del rey en ajedrez):
$$d(Q, P) = \\max(|x_Q - x_P|, |y_Q - y_P|)$$
""")

distancias_cheb = []
for i, (p, precio) in enumerate(puntos):
    d = np.max(np.abs(Q - p))
    distancias_cheb.append((labels[i], p[0], p[1], precio, round(d, 4)))

tabla_cheb = "| Vivienda | (X₁, X₂) | Precio | Distancia Chebyshev a Q=(2.5, 2) |\n|----------|----------|--------|----------------------------------|\n"
tabla_cheb += "\n".join(f"| {v} | ({x1}, {x2}) | {p} | {d} |" for v, x1, x2, p, d in distancias_cheb)
st.markdown(tabla_cheb)

st.markdown("""
**Ejemplo de cálculo para A:**  
$d(Q, A) = \\max(|2.5-1|, |2-2|) = \\max(1.5, 0) = 1.5$

**Ejemplo para B:**  
$d(Q, B) = \\max(|2.5-2|, |2-3|) = \\max(0.5, 1) = 1$
""")

# --- Coseno ---
st.subheader("3.5 Distancia Coseno")

st.markdown("""
Mide el ángulo entre vectores: $d(Q, P) = 1 - \\frac{Q \\cdot P}{\\|Q\\| \\|P\\|}$. 
Valores cercanos a 0 indican vectores en la misma dirección.
""")

distancias_cos = []
for i, (p, precio) in enumerate(puntos):
    dot = np.dot(Q, p)
    norm_q = np.linalg.norm(Q)
    norm_p = np.linalg.norm(p)
    cos_sim = dot / (norm_q * norm_p) if (norm_q * norm_p) > 0 else 0
    d = 1 - cos_sim
    distancias_cos.append((labels[i], p[0], p[1], precio, round(d, 4)))

tabla_cos = "| Vivienda | (X₁, X₂) | Precio | Distancia Coseno a Q=(2.5, 2) |\n|----------|----------|--------|--------------------------------|\n"
tabla_cos += "\n".join(f"| {v} | ({x1}, {x2}) | {p} | {d} |" for v, x1, x2, p, d in distancias_cos)
st.markdown(tabla_cos)

st.markdown("""
**Ejemplo de cálculo para A:**  
$\\cos(\\theta) = \\frac{2.5\\cdot1 + 2\\cdot2}{\\sqrt{2.5^2+2^2} \\cdot \\sqrt{1^2+2^2}} = \\frac{6.5}{\\sqrt{10.25}\\sqrt{5}} \\approx 0.908$  
$d(Q, A) = 1 - 0.908 \\approx 0.092$
""")

# Usar Euclidiana para el resto del flujo
distancias = distancias_euc

st.markdown("""
**Nota:** En este ejemplo seguimos con **distancia Euclidiana**. El orden de los vecinos puede cambiar 
según la métrica: con Manhattan, A, B y C empatan en 1.5; con Minkowski p=3, B y C quedan más cerca que A; 
con Chebyshev, B y C son los más cercanos (d=1); con Coseno, el orden depende del ángulo entre vectores.
""")

# ========== K vecinos más cercanos ==========
st.header("Paso 4: Seleccionar los K vecinos más cercanos")

K = 3
ordenados = sorted(distancias, key=lambda x: x[4])
vecinos = ordenados[:K]

st.markdown(f"""
Elegimos **K = {K}**. Con **distancia Euclidiana**, los {K} puntos **más cercanos** a Q son (ordenados por distancia):
""")

tabla_vec = "| Orden | Vivienda | Distancia | Precio |\n|-------|----------|-----------|--------|\n"
tabla_vec += "\n".join(f"| {i}° | {v} | {d} | {p} |" for i, (v, x1, x2, p, d) in enumerate(vecinos, 1))
st.markdown(tabla_vec)

# ========== Predicción ==========
st.header("Paso 5: Predicción = promedio de los K vecinos")

precios_vecinos = [v[3] for v in vecinos]
prediccion = np.mean(precios_vecinos)

st.markdown(f"""
En **KNN Regresión**, la predicción es el **promedio** de los valores objetivo de los K vecinos:

$$\\hat{{y}} = \\frac{{1}}{{K}} \\sum_{{i=1}}^{{K}} y_i = \\frac{{{' + '.join(map(str, precios_vecinos))}}}{{{K}}} = {prediccion:.2f}$$
""")

st.success(f"**Predicción para Q = (2.5, 2):** {prediccion:.2f} millones de pesos")

st.markdown("""
**Interpretación:** La predicción de 12.33 millones tiene sentido porque las viviendas más cercanas 
a Q (A, B y C) tienen precios 10, 15 y 12. La idea central de KNN es que **objetos similares** 
(cercanos en el espacio de características) tienden a tener **valores similares**. Por eso promediamos 
los precios de las más cercanas.
""")

# ========== Resumen de la lógica ==========
st.markdown("---")
st.header("Resumen: lógica del KNN Regresor")

st.markdown("""
1. **Entrada:** Un punto nuevo Q (características) y un conjunto de entrenamiento (puntos con valor conocido).
2. **Calcular distancias:** De Q a cada punto del entrenamiento.
3. **Ordenar:** Por distancia (de menor a mayor).
4. **Seleccionar:** Los K puntos más cercanos.
5. **Predecir:** Promedio de los valores objetivo de esos K puntos.

No hay "entrenamiento" en el sentido tradicional: el algoritmo solo **almacena** los datos. 
La "predicción" es un cálculo que se hace cada vez que llega un punto nuevo.
""")

# ========== Código equivalente ==========
st.markdown("---")
st.header("Código equivalente (para Colab)")

st.markdown("El mismo ejemplo implementado en Python:")

with st.expander("📋 Ver código: implementación manual", expanded=False):
    st.code("""import numpy as np

# Datos de entrenamiento: (X1, X2) -> precio
X_train = np.array([[1, 2], [2, 3], [3, 1], [4, 4], [5, 2]])
y_train = np.array([10, 15, 12, 20, 18])

# Punto a predecir
Q = np.array([2.5, 2])
K = 3

# Calcular distancias (Euclidiana)
distancias = np.sqrt(np.sum((X_train - Q) ** 2, axis=1))

# Índices de los K más cercanos
indices_cercanos = np.argsort(distancias)[:K]

# Predicción = promedio de los precios de los K vecinos
prediccion = np.mean(y_train[indices_cercanos])
print(f"Predicción para Q = {Q}: {prediccion:.2f} millones")
# Salida: Predicción para Q = [2.5 2.]: 12.33 millones""", language="python")

st.markdown("---")
st.subheader("Mismo ejemplo usando KNeighborsRegressor (scikit-learn)")

st.markdown("""
El mismo ejemplo con **KNeighborsRegressor** de scikit-learn, probando las cinco métricas de distancia:
""")

with st.expander("📋 Ver código: KNeighborsRegressor con todas las métricas", expanded=False):
    st.code("""import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Datos de entrenamiento
X_train = np.array([[1, 2], [2, 3], [3, 1], [4, 4], [5, 2]])
y_train = np.array([10, 15, 12, 20, 18])
Q = np.array([[2.5, 2]])  # predict() espera 2D
K = 3

# --- Euclidiana (por defecto) ---
knn_euc = KNeighborsRegressor(n_neighbors=K, metric='euclidean')
knn_euc.fit(X_train, y_train)
pred_euc = knn_euc.predict(Q)[0]
print(f"Euclidiana:  {pred_euc:.2f} millones")

# --- Manhattan ---
knn_man = KNeighborsRegressor(n_neighbors=K, metric='manhattan')
knn_man.fit(X_train, y_train)
pred_man = knn_man.predict(Q)[0]
print(f"Manhattan:   {pred_man:.2f} millones")

# --- Minkowski (p=3) ---
knn_min = KNeighborsRegressor(n_neighbors=K, metric='minkowski', p=3)
knn_min.fit(X_train, y_train)
pred_min = knn_min.predict(Q)[0]
print(f"Minkowski p=3: {pred_min:.2f} millones")

# --- Chebyshev ---
knn_cheb = KNeighborsRegressor(n_neighbors=K, metric='chebyshev')
knn_cheb.fit(X_train, y_train)
pred_cheb = knn_cheb.predict(Q)[0]
print(f"Chebyshev:     {pred_cheb:.2f} millones")

# --- Coseno ---
knn_cos = KNeighborsRegressor(n_neighbors=K, metric='cosine')
knn_cos.fit(X_train, y_train)
pred_cos = knn_cos.predict(Q)[0]
print(f"Coseno:        {pred_cos:.2f} millones")

# Salida (el orden de vecinos cambia según la métrica):
# Euclidiana:  12.33 millones  (vecinos: A, B, C)
# Manhattan:   12.33 millones  (vecinos: A, B, C)
# Minkowski p=3: 12.33 millones  (vecinos: B, C, A)
# Chebyshev:    12.33 millones  (vecinos: B, C, A)
# Coseno:       17.67 millones  (vecinos: D, E, B — orden por ángulo)""", language="python")
