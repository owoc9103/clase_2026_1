# Taller: Clasificación — Detección de fraude en transacciones bancarias

**Datos:** `Bank_Transaction_Fraud_Detection.csv`.  
**Versión tejible:** `Taller_Clasificacion_Deteccion_Fraude_Transacciones.Rmd`

---

## Descripción ampliada del problema

La banca digital (apps, pagos con tarjeta, transferencias inmediatas, comercio electrónico) multiplicó el volumen de transacciones que una entidad debe vigilar. Eso abre dos frentes: **pérdidas por fraude** (cargos no autorizados, suplantación, malware) y **fricción con el cliente** si el sistema bloquea pagos legítimos o pide demasiadas verificaciones.

En este taller trabajas con un conjunto de datos de **transacciones etiquetadas** (`Is_Fraud`: 0 legítima, 1 fraude). Cada fila combina datos del cliente (edad, género, estado, ciudad, tipo de cuenta), del canal (dispositivo, tipo de dispositivo) y de la operación (monto, saldo, tipo de transacción, categoría del comercio, ubicación, descripción). Variables con muchos identificadores únicos (IDs, correos, teléfonos) suelen **excluirse** del modelado por sobreajuste y privacidad.

El problema es **una clasificación binaria supervisada** con **clases desbalanceadas**: habrá muchas más transacciones legítimas que fraudulentas. Una *accuracy* alta puede ocultar que el modelo **casi nunca predice fraude**. Por eso debes usar **precisión, recall y F1 por clase**, matriz de confusión y **ROC AUC**, y vincular falsos negativos y falsos positivos al coste de negocio.

El flujo recomendado incluye: limpieza, EDA, fechas como features, `LabelEncoder`, correlaciones, importancias con Random Forest, selección de variables, PCA para visualizar, split, escalado, y comparación de modelos con **GridSearchCV** / técnicas frente al desbalance (**SMOTE**, **class_weight**). Debes **replicar e interpretar** si el sistema detecta fraude o solo favorece la clase mayoritaria.

---

## Objetivos del caso (*Objectives for Bank Transaction Fraud Detection*) — versión ampliada

Objetivos listados a continuación, **extendidos** con entregables en el taller.

1. **Detección de fraude (supervisada).** **En el taller:** `y = df['Is_Fraud']`; entrenar el **catálogo ampliado** de la sección *Catálogo ampliado de modelos e hiperparámetros* (mínimo **12 modelos**); el resto opcional por tiempo.
2. **Patrones anómalos (EDA).** **En el taller:** por cada hallazgo, una frase interpretativa con gráfico o tabla.
3. **Análisis de variables.** **En el taller:** correlaciones e **importancias** del Random Forest; justificar eliminación de constantes e IDs.
4. **Rendimiento y errores.** **En el taller:** informe con métricas para **ambas** clases; no solo accuracy.
5. **Despliegue / tiempo real.** **En el taller:** qué pasos son costosos (grid masivo, SMOTE) y qué harías en producción.
6. **Cliente legítimo.** **En el taller:** contrastar distribuciones `Is_Fraud` 0 vs 1 en el EDA.
7. **Dispositivo y ubicación.** **En el taller:** relevancia en correlación e importancias.
8. **Recomendaciones.** **En el taller:** al menos tres acciones concretas para el banco.

---

## Dependencias (Python)

```text
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost lightgbm catboost
```

---

## Verificación al cargar datos

```python
import pandas as pd

file_path = "Bank_Transaction_Fraud_Detection.csv"
df = pd.read_csv(file_path)
print(df.shape)
print(df["Is_Fraud"].value_counts(normalize=True))
print(df["Is_Fraud"].value_counts())
```

---

## Instrucciones generales

1. Avanza por las **etapas 1 … 17** en orden, siguiendo esta guía.
2. Tras cada bloque, 1–3 frases de qué hiciste y qué observas.
3. Si falla un paquete, instálalo o omite ese modelo sin romper el flujo global.

---

## Etapa 1 — Importación y lectura

**Debes:** todas las importaciones necesarias; `file_path` local; `read_csv`; `head`, `info`, `shape`, `duplicated`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, accuracy_score

file_path = "Bank_Transaction_Fraud_Detection.csv"
df = pd.read_csv(file_path)
```

---

## Etapa 2 — Preprocesamiento

**Debes:** nulos; tabla `desc`; categóricas; eliminar constantes; eliminar `Customer_Contact`, `Customer_Email`, `Customer_Name`, `Customer_ID`, `Transaction_ID`, `Merchant_ID`.

```python
print(df.isnull().sum())
single_value_columns = [col for col in df.columns if df[col].nunique() == 1]
df = df.drop(columns=single_value_columns)

drop_cols = [
    "Customer_Contact", "Customer_Email", "Customer_Name",
    "Customer_ID", "Transaction_ID", "Merchant_ID",
]
df = df.drop(columns=drop_cols)
```

---

## Etapa 3 — EDA

**Debes:** imputación mediana en numéricos si aplica; gráficos por `Is_Fraud`; categóricas.

```python
numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns
for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())
```

---

## Etapa 4 — Fechas/horas

**Debes:** `to_datetime` `%d-%m-%Y` y `%H:%M:%S`; día/mes/año/hora/min/seg; eliminar columnas originales; revisar constantes.

```python
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"], format="%d-%m-%Y")
df["Transaction_Time"] = pd.to_datetime(df["Transaction_Time"], format="%H:%M:%S")

df["Transaction_Day"] = df["Transaction_Date"].dt.day
df["Transaction_Month"] = df["Transaction_Date"].dt.month
df["Transaction_Year"] = df["Transaction_Date"].dt.year
df["Transaction_Hour"] = df["Transaction_Time"].dt.hour
df["Transaction_Minute"] = df["Transaction_Time"].dt.minute
df["Transaction_Second"] = df["Transaction_Time"].dt.second

df = df.drop(columns=["Transaction_Date", "Transaction_Time"])
```

---

## Etapa 5 — Label encoding

```python
from sklearn.preprocessing import LabelEncoder

categorical_columns = df.select_dtypes(include=["object"]).columns
le = LabelEncoder()
for col in categorical_columns:
    df[col] = le.fit_transform(df[col])
```

---

## Etapa 6 — EDA post-encoding

**Debes:** figuras de EDA tras el encoding.

---

## Etapa 7 — Patrones de fraude

**Debes:** KDE, histogramas y boxplots comparando por `Is_Fraud`.

---

## Etapa 8 — Correlaciones

```python
plt.figure(figsize=(14, 10))
sns.heatmap(df.corr(numeric_only=True), annot=False, cmap="coolwarm", center=0)
plt.title("Matriz de correlación")
plt.tight_layout()
plt.show()
```

---

## Etapa 9 — Random Forest — importancias

```python
X = df.drop(columns=["Is_Fraud"])
y = df["Is_Fraud"]

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y)

feature_importances = pd.DataFrame(
    {"importance": rf.feature_importances_},
    index=X.columns,
).sort_values("importance", ascending=False)
```

---

## Etapa 10 — Selección de variables

```python
important_features = feature_importances[feature_importances["importance"] > 0.01].index
X = df[important_features]
```

---

## Etapa 11 — PCA

**Importante:** el modelado usa **`X` seleccionado**, no `X_pca`; PCA para explorar.

```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="coolwarm", alpha=0.3)
print(pca.explained_variance_ratio_)
```

---

## Etapa 12 — Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## Etapa 13 — Escalado

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## Catálogo ampliado de modelos e hiperparámetros

**Meta:** probar **más allá** de una lista mínima de modelos de partida. Con ~200 000 filas, usa **muestra estratificada** del train o `RandomizedSearchCV(..., n_iter=12, random_state=42)`.

**Imports adicionales:**

```python
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    RandomForestClassifier,
    ExtraTreesClassifier,
    GradientBoostingClassifier,
    HistGradientBoostingClassifier,
    AdaBoostClassifier,
    BaggingClassifier,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.neural_network import MLPClassifier
import xgboost as xgb
import lightgbm as lgb
import catboost as cb
```

**`models`** (claves = claves de `param_grids`):

```python
models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, random_state=42),
    "Ridge Classifier": RidgeClassifier(random_state=42),
    "LDA": LinearDiscriminantAnalysis(),
    "QDA": QuadraticDiscriminantAnalysis(),
    "Gaussian NB": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Extra Trees": ExtraTreesClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "Hist Gradient Boosting": HistGradientBoostingClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42, algorithm="SAMME"),
    "Bagging": BaggingClassifier(random_state=42),
    "KNN": KNeighborsClassifier(),
    "SVM (RBF)": SVC(kernel="rbf", probability=True, random_state=42),
    "SVM (Linear)": LinearSVC(random_state=42),
    "XGBoost": xgb.XGBClassifier(
        random_state=42, eval_metric="logloss", use_label_encoder=False
    ),
    "LightGBM": lgb.LGBMClassifier(random_state=42, verbose=-1),
    "CatBoost": cb.CatBoostClassifier(random_state=42, verbose=False),
    "MLP (red neuronal)": MLPClassifier(max_iter=300, random_state=42),
}
```

**Notas:** `LinearSVC` sin `predict_proba` — para AUC usa `decision_function` o `CalibratedClassifierCV`, o `SVC(kernel="linear", probability=True)`. `QDA` puede necesitar `reg_param` > 0. Evita mezclar SMOTE + `class_weight` sin justificar.

**`param_grids` ampliado** (acorta si hace falta):

```python
param_grids = {
    "Logistic Regression": {
        "C": [0.01, 0.1, 1.0, 10.0],
        "penalty": ["l2"],
        "solver": ["lbfgs", "liblinear"],
        "class_weight": [None, "balanced"],
    },
    "Ridge Classifier": {
        "alpha": [0.01, 0.1, 1.0, 10.0],
        "class_weight": [None, "balanced"],
    },
    "LDA": {"solver": ["svd", "lsqr", "eigen"]},
    "QDA": {"reg_param": [0.0, 0.01, 0.1]},
    "Gaussian NB": {},
    "Decision Tree": {
        "max_depth": [4, 8, 16, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "criterion": ["gini", "entropy"],
        "class_weight": [None, "balanced"],
    },
    "Random Forest": {
        "n_estimators": [100, 200],
        "max_depth": [None, 12, 20],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", 0.3],
        "class_weight": [None, "balanced", "balanced_subsample"],
    },
    "Extra Trees": {
        "n_estimators": [100, 200],
        "max_depth": [None, 12, 20],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", 0.3],
        "class_weight": [None, "balanced"],
    },
    "Gradient Boosting": {
        "n_estimators": [100, 200],
        "learning_rate": [0.05, 0.1],
        "max_depth": [3, 5, 7],
        "subsample": [0.8, 1.0],
    },
    "Hist Gradient Boosting": {
        "learning_rate": [0.05, 0.1],
        "max_depth": [None, 5, 10],
        "max_iter": [100, 200],
        "min_samples_leaf": [10, 20],
        "l2_regularization": [0.0, 0.1],
        "class_weight": [None, "balanced"],
    },
    "AdaBoost": {
        "n_estimators": [100, 200],
        "learning_rate": [0.01, 0.1, 0.5],
        "estimator": [
            DecisionTreeClassifier(max_depth=1, random_state=42),
            DecisionTreeClassifier(max_depth=2, random_state=42),
        ],
    },
    "Bagging": {
        "n_estimators": [50, 100],
        "max_samples": [0.7, 0.9, 1.0],
        "max_features": [0.7, 1.0],
    },
    "KNN": {
        "n_neighbors": [3, 5, 11, 21],
        "weights": ["uniform", "distance"],
        "p": [1, 2],
    },
    "SVM (RBF)": {
        "C": [0.1, 1, 10],
        "gamma": ["scale", "auto", 0.01, 0.1],
    },
    "SVM (Linear)": {"C": [0.1, 1, 10]},
    "XGBoost": {
        "n_estimators": [100, 200],
        "max_depth": [4, 6],
        "learning_rate": [0.05, 0.1],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
        "reg_alpha": [0.0, 0.1],
        "scale_pos_weight": [1.0],
    },
    "LightGBM": {
        "n_estimators": [100, 200],
        "learning_rate": [0.05, 0.1],
        "max_depth": [-1, 5, 10],
        "num_leaves": [31, 63],
        "min_child_samples": [10, 30],
        "subsample": [0.8, 1.0],
        "colsample_bytree": [0.8, 1.0],
        "class_weight": [None, "balanced"],
    },
    "CatBoost": {
        "depth": [4, 6, 8],
        "iterations": [200, 400],
        "learning_rate": [0.05, 0.1],
        "l2_leaf_reg": [1, 3, 9],
    },
    "MLP (red neuronal)": {
        "hidden_layer_sizes": [(32,), (64, 32), (128, 64)],
        "alpha": [1e-4, 1e-3],
        "activation": ["relu"],
    },
}
```

Opcional — **`Gaussian NB`** con `var_smoothing`:

```python
import numpy as np
param_grids["Gaussian NB"] = {
    "var_smoothing": np.logspace(-12, -6, num=7),
}
```

**Mínimo sugerido (12 modelos):** Logistic Regression, Ridge, LDA, Gaussian NB, Decision Tree, Random Forest, Extra Trees, Gradient Boosting *o* Hist Gradient Boosting, XGBoost, LightGBM, KNN, SVM (RBF o Linear). **Ampliación:** QDA, AdaBoost, Bagging, CatBoost, MLP.

**Compatibilidad:** en scikit-learn antiguo, `AdaBoostClassifier` puede usar `base_estimator` en lugar de `estimator` en la rejilla.

---

## Etapa 14 — Entrenamiento y evaluación

**Debes:** unificar `models` y `param_grids`; `GridSearchCV` o `RandomizedSearchCV`; `StratifiedKFold`; **SMOTE** / pesos según tu diseño (coherente con el protocolo elegido); guardar mejores parámetros, accuracy train/test, ROC AUC, `classification_report`.

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold

cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

for name, est in models.items():
    grid = GridSearchCV(
        estimator=est,
        param_grid=param_grids[name],
        scoring="roc_auc",
        cv=cv,
        n_jobs=-1,
        refit=True,
        verbose=1,
    )
    # grid.fit(X_train_scaled, y_train)  # o train con SMOTE
```

---

## Etapa 15 — Resultados

**Debes:** tabla con todas las métricas; ordenar por métrica que defiendas para fraude.

---

## Etapa 16 — Train vs test accuracy

**Debes:** gráfico comparativo y comentario de sobreajuste.

---

## Etapa 17 — Conclusiones

**Debes:** accuracy vs desbalance, AUC, clase 1, mejoras (SMOTE, pesos, umbrales).

*Etapa 18 (opcional): cierre.*

---

## Entregables sugeridos

- Implementación en Python (Jupyter o script) con ruta local.
- Informe corto: contexto, EDA, modelos, interpretación por clase.

---

## Criterios de evaluación orientadores

- Catálogo mínimo de **12 modelos** con búsqueda de hiperparámetros (documentar submuestreo o `RandomizedSearchCV` si aplica).
- Interpretación de **métricas por clase** y desbalance.
- Comentarios sobre importancias, correlaciones y train vs test.
