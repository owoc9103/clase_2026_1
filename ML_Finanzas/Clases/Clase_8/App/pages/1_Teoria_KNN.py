# -*- coding: utf-8 -*-
"""
Clase 7 - Teoría KNN
"""

import streamlit as st

st.title("📚 Teoría de K-Nearest Neighbors (KNN)")

st.markdown("""
En esta página se presentan los conceptos fundamentales del algoritmo KNN, con énfasis en su uso para **regresión**.
""")

# ========== ¿Qué es KNN? ==========
st.header("¿Qué es el algoritmo KNN?")

st.markdown("""
**K-Nearest Neighbors (KNN)** es un algoritmo de aprendizaje supervisado usado tanto para **clasificación** 
como para **regresión**. Es uno de los algoritmos más intuitivos en machine learning: se basa en la idea de que 
**objetos similares tienden a tener resultados similares**.

A diferencia de modelos como la regresión lineal, KNN no construye una función explícita a partir de los datos. 
En su lugar, **almacena** todos los datos de entrenamiento y, cuando llega un punto nuevo, busca los K puntos 
más cercanos (vecinos) y predice en función de ellos.
""")

st.subheader("Funcionamiento paso a paso")

st.markdown("""
1. **Inicialización:** Se elige un valor para **K**, que representa el número de vecinos a considerar. 
   Este es el hiperparámetro principal del modelo.

2. **Fase de entrenamiento:** En KNN, el "entrenamiento" es mínimo: el algoritmo simplemente **guarda** 
   los vectores de características (X) y sus valores objetivo (y). No hay optimización de pesos ni ajuste 
   iterativo como en redes neuronales o regresión lineal.

3. **Fase de predicción:** Cuando llega un punto nuevo del que queremos predecir su valor:
   - Se calcula la **distancia** entre el punto nuevo y cada punto del conjunto de entrenamiento.
   - Se ordenan las distancias de menor a mayor.
   - Se seleccionan los **K puntos más cercanos** (los K vecinos).
   - **En regresión:** La predicción es el **promedio** (o promedio ponderado por distancia) de los valores 
     objetivo de esos K vecinos.
   - **En clasificación:** La predicción es la **clase más frecuente** entre los K vecinos (votación por mayoría).

4. **Evaluación:** Se usan métricas apropiadas: MSE, RMSE, R² para regresión; accuracy, precisión, recall para clasificación.
""")

st.subheader("Consideraciones clave")

st.markdown("""
- **Sensibilidad a K:** Un K muy pequeño hace el modelo sensible al ruido (cada predicción depende de pocos puntos). 
  Un K muy grande suaviza demasiado y puede perder patrones locales.

- **Costo computacional:** Para cada predicción, KNN debe calcular la distancia a **todos** los puntos de entrenamiento. 
  Con conjuntos muy grandes, esto puede ser lento. Se usan estructuras como KD-Tree o Ball-Tree para acelerar.

- **Escalado de características:** Las distancias dependen de las escalas. Si una variable va de 0 a 1000 y otra de 0 a 1, 
  la primera dominará el cálculo. Por eso es fundamental escalar o normalizar las características antes de usar KNN.

- **Algoritmo no paramétrico:** KNN no asume ninguna forma específica para la relación entre X e y. 
  Puede capturar relaciones no lineales complejas, pero requiere suficientes datos.
""")

# ========== Regresor vs Clasificador ==========
st.header("KNN Clasificador vs KNN Regresor")

st.markdown("""
La misma lógica (buscar K vecinos más cercanos) se aplica de forma distinta según el tipo de problema:
""")

st.markdown("""
| Aspecto | KNN Clasificador | KNN Regresor |
|---------|------------------|--------------|
| **Tarea** | Asignar etiquetas de clase (categorías) | Predecir valores numéricos continuos |
| **Salida** | Etiqueta discreta (ej. "spam", "no spam") | Valor numérico (ej. 2.5 millones de pesos) |
| **Regla de predicción** | Mayoría de clases entre los K vecinos | Promedio (o promedio ponderado) de los valores de los K vecinos |
| **Uso típico** | Imágenes, spam, diagnóstico médico, sentiment analysis | Precios de viviendas, acciones, temperatura, demanda |
""")

st.markdown("""
**KNN Regresor en detalle:**  
Para un punto nuevo, se obtienen los K vecinos más cercanos. Si sus valores objetivo son, por ejemplo, 
10, 15 y 12, la predicción será (10+15+12)/3 = 12.33. La idea es que puntos cercanos en el espacio 
de características tienden a tener valores objetivo similares.
""")

# ========== Métricas de rendimiento ==========
st.header("Métricas de rendimiento para KNN Regresor")

st.markdown("""
Para evaluar qué tan bien predice el modelo, se comparan las predicciones con los valores reales 
en un conjunto de prueba. Las métricas más usadas son:
""")

st.subheader("1. Error Cuadrático Medio (MSE)")

st.markdown("""
Promedio de las diferencias al cuadrado entre valores reales y predichos. Penaliza más los errores grandes 
porque se elevan al cuadrado.

$$MSE = \\frac{1}{n} \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2$$

- **Ventaja:** Diferenciable, útil para optimización.
- **Desventaja:** No está en las mismas unidades que la variable objetivo.
""")

st.subheader("2. Raíz del Error Cuadrático Medio (RMSE)")

st.markdown("""
Raíz cuadrada del MSE. Tiene las **mismas unidades** que la variable objetivo (ej. millones de pesos), 
lo que facilita la interpretación.

$$RMSE = \\sqrt{MSE}$$

- **Interpretación:** En promedio, las predicciones se desvían RMSE unidades del valor real.
""")

st.subheader("3. R-cuadrado (R²)")

st.markdown("""
Proporción de la varianza de la variable objetivo que es explicada por el modelo. Varía entre 0 y 1 
(teóricamente puede ser negativo si el modelo es muy malo).

$$R^2 = 1 - \\frac{\\sum (y_i - \\hat{y}_i)^2}{\\sum (y_i - \\bar{y})^2}$$

- **R² = 1:** Predicciones perfectas.
- **R² = 0:** El modelo no explica mejor que predecir siempre la media.
- **R² < 0:** El modelo es peor que predecir la media.
""")

st.subheader("4. Error Absoluto Medio (MAE)")

st.markdown("""
Promedio de las diferencias absolutas. Es menos sensible a outliers que el MSE.

$$MAE = \\frac{1}{n} \\sum_{i=1}^{n} |y_i - \\hat{y}_i|$$
""")

# ========== Maldición de la dimensionalidad ==========
st.header("Maldición de la dimensionalidad")

st.markdown("""
En espacios de **alta dimensión** (muchas características), KNN puede degradarse por varios motivos:
""")

st.markdown("""
1. **Datos dispersos:** A medida que aumenta el número de dimensiones, el volumen del espacio crece 
   exponencialmente. Los puntos tienden a estar muy separados; la noción de "vecino cercano" pierde sentido 
   porque casi todos los puntos están a distancias similares.

2. **Mayor costo computacional:** Calcular distancias en muchas dimensiones es más costoso. Además, 
   estructuras como KD-Tree pierden eficiencia en alta dimensión.

3. **Overfitting:** Con muchas características, algunas pueden ser ruidosas o irrelevantes. Es más fácil 
   encontrar "vecinos cercanos" que en realidad no son similares en las dimensiones que importan.

4. **Necesidad de más datos:** Para cubrir adecuadamente un espacio de alta dimensión, se necesitan 
   muchos más datos. Con pocas muestras, el espacio está muy vacío.
""")

st.markdown("""
**Mitigaciones:**
- **Reducción de dimensionalidad:** PCA, selección de características, o técnicas como t-SNE para visualización.
- **Escalado de características:** Asegurar que todas contribuyan de forma equilibrada.
- **Considerar otros algoritmos:** En alta dimensión, modelos lineales o basados en árboles pueden rendir mejor.
""")

# ========== Distancias ==========
st.header("Métricas de distancia en KNN")

st.markdown("""
La **distancia** define qué puntos se consideran "cercanos". scikit-learn ofrece varias opciones 
en el parámetro `metric` de `KNeighborsRegressor`. Las más usadas son:
""")

st.subheader("Distancia Euclidiana (L2) — `metric='euclidean'`")

st.markdown("""
Es la distancia "en línea recta" que conocemos del plano cartesiano, generalizada a n dimensiones:

$$d(p_1, p_2) = \\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + ... + (z_1-z_2)^2}$$

- **Interpretación geométrica:** Longitud del segmento que une los dos puntos.
- **Propiedad:** Sensible a la escala de las características; las de mayor magnitud dominan.
- **Uso:** Cuando las relaciones entre características son aproximadamente lineales y las escalas son similares.
""")

st.subheader("Distancia Manhattan (L1) — `metric='manhattan'`")

st.markdown("""
Suma de las diferencias absolutas en cada dimensión. Recibe su nombre por el movimiento en una cuadrícula 
(tipo calles de Manhattan):

$$d(p_1, p_2) = |x_1-x_2| + |y_1-y_2| + ... + |z_1-z_2|$$

- **Interpretación geométrica:** Distancia recorrida moviéndose solo a lo largo de los ejes.
- **Propiedad:** Menos sensible a outliers que la Euclidiana (no eleva al cuadrado las diferencias).
- **Uso:** Cuando hay outliers o cuando las dimensiones tienen significados muy distintos.
""")

st.subheader("Distancia Minkowski — `metric='minkowski'`")

st.markdown("""
Generaliza Euclidiana y Manhattan. Con el parámetro $p$:

$$d(p_1, p_2) = \\left( |x_1-x_2|^p + |y_1-y_2|^p + ... + |z_1-z_2|^p \\right)^{1/p}$$

- **p=1:** Equivale a Manhattan.
- **p=2:** Equivale a Euclidiana.
- **p>2:** Da más peso a las dimensiones con mayor diferencia.

En scikit-learn: `KNeighborsRegressor(metric='minkowski', p=3)` para p=3.
""")

st.subheader("Distancia Chebyshev — `metric='chebyshev'`")

st.markdown("""
Máxima diferencia absoluta entre las coordenadas (distancia del rey en ajedrez):

$$d(p_1, p_2) = \\max(|x_1-x_2|, |y_1-y_2|, ..., |z_1-z_2|)$$

- **Interpretación geométrica:** La dimensión en la que más difieren los puntos.
- **Propiedad:** Solo considera la dimensión con mayor diferencia; ignora las demás.
- **Uso:** Cuando interesa la peor discrepancia en una sola dimensión.
""")

st.subheader("Distancia Coseno — `metric='cosine'`")

st.markdown("""
Mide el ángulo entre dos vectores (similitud de dirección, no magnitud):

$$d(p_1, p_2) = 1 - \\frac{p_1 \\cdot p_2}{\\|p_1\\| \\|p_2\\|} = 1 - \\cos(\\theta)$$

- **Interpretación:** 0 si los vectores son paralelos; 2 si son opuestos.
- **Propiedad:** No depende de la magnitud, solo de la dirección. Útil cuando el tamaño absoluto no importa.
- **Uso:** Textos, recomendaciones, cuando la orientación es más importante que la escala.
""")

st.subheader("Otras métricas en scikit-learn")

st.markdown("""
| Métrica | Parámetro | Descripción |
|---------|-----------|-------------|
| Euclidiana | `metric='euclidean'` | L2, por defecto |
| Manhattan | `metric='manhattan'` | L1 |
| Minkowski | `metric='minkowski', p=k` | Generalización (p=1→Manhattan, p=2→Euclidiana) |
| Chebyshev | `metric='chebyshev'` | Máximo de diferencias absolutas |
| Coseno | `metric='cosine'` | 1 - coseno del ángulo |
| Haversine | `metric='haversine'` | Para coordenadas geográficas (lat/lon) |
""")

# ========== Escalado de características ==========
st.header("Rol del escalado de características en KNN")

st.markdown("""
KNN es un algoritmo **basado en distancias**. Si una característica tiene valores entre 0 y 100.000 
y otra entre 0 y 1, la primera dominará completamente el cálculo de distancia, aunque no sea más relevante 
para la predicción.

**Objetivo del escalado:** Hacer que todas las características contribuyan de forma equilibrada, 
normalmente poniéndolas en rangos o escalas comparables.
""")

st.subheader("Métodos comunes")

st.markdown("""
1. **StandardScaler (estandarización):** Transforma cada característica para que tenga media 0 y desviación estándar 1.
   $$x_{scaled} = \\frac{x - \\mu}{\\sigma}$$
   - Útil cuando los datos siguen aproximadamente una distribución normal.

2. **MinMaxScaler (normalización):** Escala al rango [0, 1].
   $$x_{scaled} = \\frac{x - x_{min}}{x_{max} - x_{min}}$$
   - Útil cuando se quiere un rango fijo; sensible a outliers.

3. **RobustScaler:** Usa la mediana y el rango intercuartílico (IQR). Menos sensible a outliers.
   $$x_{scaled} = \\frac{x - median}{IQR}$$
""")

st.markdown("""
**Importante:** El escalado debe ajustarse **solo con los datos de entrenamiento** y luego aplicarse 
a los de prueba. Si se usa información del conjunto de prueba (ej. su media o máximo), se introduce 
**data leakage** y se sobrestima el rendimiento.
""")
