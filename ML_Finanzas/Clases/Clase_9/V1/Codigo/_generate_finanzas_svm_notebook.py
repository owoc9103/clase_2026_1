# -*- coding: utf-8 -*-
"""
Genera scoring_riesgo_credito_ejercicio.csv (mismos números que pulsar_stars.csv)
y svm-scoring-riesgo-credito-colab-es.ipynb a partir de svm-clasificador-pulsar-colab-es.ipynb.
"""
import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "..", "Data")
PULSAR_CSV = os.path.join(DATA, "pulsar_stars.csv")
FIN_CSV = os.path.join(DATA, "scoring_riesgo_credito_ejercicio.csv")
BASE_NB = os.path.join(ROOT, "svm-clasificador-pulsar-colab-es.ipynb")
OUT_NB = os.path.join(ROOT, "svm-scoring-riesgo-credito-colab-es.ipynb")

# Nombres financieros (mismo orden que columnas tras strip en el CSV original)
COL_FIN = [
    "rend_medio",  # media de perfil integrado -> indicador de rentabilidad media (normalizado)
    "vol_rent",  # volatilidad del rendimiento
    "curt_rent",  # exceso de curtosis del rendimiento
    "asim_rent",  # asimetría del rendimiento
    "liq_medio",  # media bloque liquidez/cobertura (DM-SNR en origen)
    "vol_flujo",  # volatilidad del flujo / ratio
    "curt_flujo",  # curtosis en exceso del bloque liquidez-flujo
    "asim_flujo",  # asimetría del bloque liquidez-flujo
    "incumple_12m",  # 1 = evento de incumplimiento a 12 meses, 0 = no
]


def escribir_csv_financiero():
    import pandas as pd

    df = pd.read_csv(PULSAR_CSV)
    df.columns = [c.strip() for c in df.columns]
    assert len(df.columns) == len(COL_FIN), (len(df.columns), len(COL_FIN))
    df.columns = COL_FIN
    df.to_csv(FIN_CSV, index=False)
    print("CSV financiero:", FIN_CSV, "filas:", len(df))


def src_join(s: str):
    if not s:
        return []
    return s.splitlines(keepends=True)


def aplicar_reemplazos_codigo_y_texto(s: str) -> str:
    """Sustituye nombres de columnas y frases recurrentes (orden: cadenas largas primero)."""
    reps = [
        ("/content/pulsar_stars.csv", "/content/scoring_riesgo_credito_ejercicio.csv"),
        ("pulsar_stars.csv", "scoring_riesgo_credito_ejercicio.csv"),
        ("Descargue pulsar_stars.csv", "Descargue scoring_riesgo_credito_ejercicio.csv"),
        ("ha subido `pulsar_stars.csv`", "ha subido `scoring_riesgo_credito_ejercicio.csv`"),
        ("'DM-SNR Kurtosis'", "'curt_flujo'"),
        ("'DM-SNR Skewness'", "'asim_flujo'"),
        ("'DM-SNR Mean'", "'liq_medio'"),
        ("'DM-SNR Sd'", "'vol_flujo'"),
        ("'IP Kurtosis'", "'curt_rent'"),
        ("'IP Skewness'", "'asim_rent'"),
        ("'IP Mean'", "'rend_medio'"),
        ("'IP Sd'", "'vol_rent'"),
        ("column='DM-SNR Kurtosis'", "column='curt_flujo'"),
        ("column='DM-SNR Skewness'", "column='asim_flujo'"),
        ("column='DM-SNR Mean'", "column='liq_medio'"),
        ("column='DM-SNR Sd'", "column='vol_flujo'"),
        ("column='IP Kurtosis'", "column='curt_rent'"),
        ("column='IP Skewness'", "column='asim_rent'"),
        ("column='IP Mean'", "column='rend_medio'"),
        ("column='IP Sd'", "column='vol_rent'"),
        ("df['DM-SNR Kurtosis']", "df['curt_flujo']"),
        ("df['DM-SNR Skewness']", "df['asim_flujo']"),
        ("df['DM-SNR Mean']", "df['liq_medio']"),
        ("df['DM-SNR Sd']", "df['vol_flujo']"),
        ("df['IP Kurtosis']", "df['curt_rent']"),
        ("df['IP Skewness']", "df['asim_rent']"),
        ("df['IP Mean']", "df['rend_medio']"),
        ("df['IP Sd']", "df['vol_rent']"),
        ("set_xlabel('DM-SNR Kurtosis')", "set_xlabel('curt_flujo')"),
        ("set_xlabel('DM-SNR Skewness')", "set_xlabel('asim_flujo')"),
        ("set_xlabel('DM-SNR Mean')", "set_xlabel('liq_medio')"),
        ("set_xlabel('DM-SNR Sd')", "set_xlabel('vol_flujo')"),
        ("set_xlabel('IP Kurtosis')", "set_xlabel('curt_rent')"),
        ("set_xlabel('IP Skewness')", "set_xlabel('asim_rent')"),
        ("set_xlabel('IP Mean')", "set_xlabel('rend_medio')"),
        ("set_xlabel('IP Sd')", "set_xlabel('vol_rent')"),
        ("set_ylabel('DM-SNR Kurtosis')", "set_ylabel('curt_flujo')"),
        ("set_ylabel('DM-SNR Skewness')", "set_ylabel('asim_flujo')"),
        ("set_ylabel('DM-SNR Mean')", "set_ylabel('liq_medio')"),
        ("set_ylabel('DM-SNR Sd')", "set_ylabel('vol_flujo')"),
        ("set_ylabel('IP Kurtosis')", "set_ylabel('curt_rent')"),
        ("set_ylabel('IP Skewness')", "set_ylabel('asim_rent')"),
        ("set_ylabel('IP Mean')", "set_ylabel('rend_medio')"),
        ("set_ylabel('IP Sd')", "set_ylabel('vol_rent')"),
        ("['IP Mean', 'IP Sd', 'IP Kurtosis', 'IP Skewness',", "['rend_medio', 'vol_rent', 'curt_rent', 'asim_rent',"),
        ("'DM-SNR Mean', 'DM-SNR Sd', 'DM-SNR Kurtosis', 'DM-SNR Skewness', 'target_class']", "'liq_medio', 'vol_flujo', 'curt_flujo', 'asim_flujo', 'incumple_12m']"),
        ("target_class", "incumple_12m"),
        ("Número de candidatos", "Número de expedientes"),
        ("Curva ROC — clasificador de púlsares", "Curva ROC — scoring de incumplimiento"),
        ("'Real positivo:1', 'Real negativo:0'", "'Real incumple:1', 'Real no incumple:0'"),
        ("'Predicho positivo:1', 'Predicho negativo:0'", "'Predicho incumple:1', 'Predicho no incumple:0'"),
    ]
    for old, new in reps:
        s = s.replace(old, new)
    return s


# Celdas cuyo texto se sustituye por completo (índice 0-based)
MARKDOWN_OVERRIDES = {
    0: """<a class="anchor" id="0"></a>
# **SVM para scoring de riesgo de incumplimiento (ejercicio)**

En este cuaderno se entrena un **clasificador SVM** para distinguir expedientes con **evento de incumplimiento a 12 meses** (`incumple_12m` = 1) frente a **no incumplimiento** (`incumple_12m` = 0), usando indicadores numéricos de **rentabilidad, volatilidad, forma de la distribución** y **liquidez/flujo** derivados de un fichero renombrado con **contexto financiero**.

**Nota didáctica:** los valores numéricos conservan la estructura del conjunto público de referencia **HTRU2** (detección de señales astrofísicas); aquí se **reinterpretan** como variables de un **ejercicio de riesgo de crédito** sin pretender ser estados contables reales.

Ejecute las celdas en orden (en Google Colab: **Entorno de ejecución → Ejecutar todo** tras subir `scoring_riesgo_credito_ejercicio.csv`).
""",
    1: """*ML Finanzas (Clase 9) — ejercicio de scoring y máquinas de vectores de soporte.*
""",
    15: """# **5. Descripción del conjunto de datos** <a class="anchor" id="5"></a>

[Índice](#0.1)

Se trabaja con el archivo **`scoring_riesgo_credito_ejercicio.csv`**, filas **expedientes de crédito** (empresas u operaciones homogéneas) y columnas **indicadores calculados al momento de la concesión o revisión anual**.

La variable objetivo **`incumple_12m`** toma valor **1** si en la ventana siguiente se registra un **evento de incumplimiento** (mora material, reestructuración con pérdida, etc.) y **0** en caso contrario. La clase positiva (**incumplimiento**) suele ser **minoritaria**, lo que obliga a interpretar la exactitud junto con otras métricas.

### Atributos (8 predictores continuos + etiqueta)

Bloque **rentabilidad y riesgo de mercado** (cuatro primeras variables):

1. **`rend_medio`** — nivel medio de un indicador de rentabilidad normalizado.  
2. **`vol_rent`** — volatilidad del rendimiento (dispersión).  
3. **`curt_rent`** — exceso de curtosis: colas pesadas vs. normal.  
4. **`asim_rent`** — asimetría de la distribución del rendimiento.

Bloque **liquidez y flujo** (cuatro siguientes):

5. **`liq_medio`** — nivel medio de un ratio de liquidez / cobertura.  
6. **`vol_flujo`** — volatilidad asociada al flujo o a la cobertura de cargas financieras.  
7. **`curt_flujo`** — exceso de curtosis en el bloque liquidez-flujo.  
8. **`asim_flujo`** — asimetría en ese bloque.

9. **`incumple_12m`** — etiqueta binaria de incumplimiento a 12 meses.

Los números reproducibles coinciden con el dataset de referencia renombrado; el **significado económico** es una **ilustración pedagógica** para el curso.
""",
    25: """Hay **9** variables: **8** continuas y **1** discreta. La variable discreta es **`incumple_12m`**, la **variable objetivo** (riesgo de incumplimiento).

Se revisan los nombres de columna (el fichero del ejercicio ya trae encabezados cortos).""",
    27: """En este fichero los nombres vienen **sin espacios iniciales**; si en otro origen aparecieran, convendría usar `df.columns.str.strip()`.""",
    29: """Comprobación de `df.columns` tras aplicar `strip()` (no altera el fichero del ejercicio si ya está limpio).""",
    31: """El CSV del ejercicio incluye ya **nombres financieros cortos**. La siguiente celda **verifica** que coincidan con la lista esperada (equivalente al bloque de renombrado del cuaderno de referencia sobre el mismo conjunto numérico).""",
    34: """Las variables **`rend_medio` … `asim_flujo`** resumen rentabilidad, riesgo y liquidez. La objetivo es **`incumple_12m`**.""",
    35: """La variable objetivo es **`incumple_12m`**. Se revisa la distribución de frecuencias (clase minoritaria = incumplimientos).""",
    38: """Aproximadamente **90,84 %** de los expedientes son **no incumplimientos** (**0**) y **9,16 %** **incumplimientos** (**1**): hay **desbalance de clases**, típico en carteras de crédito sanas. Por ello no basta con mirar solo la exactitud.""",
    44: """### Resumen de variables numéricas

- Hay **9** variables numéricas.
- **8** predictoras continuas y **1** discreta (`incumple_12m`).
- No hay valores faltantes en el fichero de ejercicio.""",
    50: """### Valores atípicos y política de originación

En riesgo de crédito, **valores extremos** pueden corresponder a empresas muy apalancadas, picos de volatilidad o errores de datos. Las SVM con **margen suave** penalizan esos puntos mediante **C**: valores **altos de C** penalizan más los errores de clasificación en el entrenamiento y suelen usarse cuando se sospechan outliers pero se desea un límite claro al error.""",
    51: """### Distribución de los indicadores

Histogramas para ver si las variables son simétricas o sesgadas (común en ratios financieros).""",
    53: """Las ocho variables continuas muestran **asimetría**; en scoring suele aplicarse escalado y, en producción, transformaciones o tratamiento de outliers según la política del banco.""",
    59: """# **11. Escalado de características** <a class="anchor" id="11"></a>

[Índice](#0.1)

En modelos basados en distancias y SVM, conviene **estandarizar** los ratios para que magnitudes distintas no dominen el hiperplano.""",
    65: """`X_train` y `X_test` están escalados (media ~0, varianza ~1 por columna) y listos para el modelo SVM.""",
    66: """# **12. SVM con hiperparámetros por defecto** <a class="anchor" id="12"></a>

[Índice](#0.1)

Por defecto en `SVC`: **C=1.0**, **kernel='rbf'** y **gamma** según configuración de scikit-learn (`'scale'` en versiones recientes).""",
    68: """### SVM con núcleo RBF y C=100.0

Con datos financieros ruidosos, suele explorarse **C** más alto para reducir la influencia relativa de observaciones atípicas en el margen suave. Aquí se mantiene el experimento del cuaderno base con **RBF** y **C=100.0**.""",
    81: """Aquí **`y_test`** son incumplimientos reales en el conjunto de prueba y **`y_pred_test`** las predicciones del SVM lineal con **C=1.0** (`linear_svc`).""",
    89: """### Comparar con la exactitud nula

La **exactitud nula** es la que se obtendría prediciendo siempre la clase más frecuente (aquí, “no incumple”). Revise la distribución en prueba:""",
    91: """La mayoría de expedientes en **prueba** son **no incumplimientos** (3306 frente a 274 incumplimientos en el reparto fijo del ejercicio). La exactitud nula es aproximadamente 3306/(3306+274).""",
    93: """El modelo supera la exactitud nula: aporta capacidad predictiva frente a predecir siempre “sin incumplimiento”.""",
    104: """### Comentarios

Con **núcleos RBF o lineal** y **C** adecuado se obtienen las mejores exactitudes de este flujo; ante **desbalance**, priorice **recall del incumplimiento**, **F1** y **AUC** frente a la sola exactitud.""",
    105: """# **16. Matriz de confusión** <a class="anchor" id="16"></a>

[Índice](#0.1)

La matriz de confusión resume **expedientes correctamente clasificados** frente a **falsos positivos** (alarma de incumplimiento sin que ocurra) y **falsos negativos** (incumplimiento no detectado). En riesgo de crédito, el coste de FN y FP no es simétrico.

""",
    107: """Los recuentos concretos dependen de su ejecución; interprete **VP/VN/FP/FN** en términos de **incumplimientos** predichos vs. reales.""",
    129: """# **18. Curva ROC y AUC** <a class="anchor" id="18"></a>

[Índice](#0.1)

### Curva ROC

La curva ROC contrasta la **tasa de verdaderos positivos** (sensibilidad al incumplimiento) con la **tasa de falsos positivos**. Es útil para elegir umbrales de **aprobación** o **revisión** en políticas de originación.

**Nota:** con predicciones duras de la SVM la curva puede verse simplificada; en producción suelen usarse **probabilidades calibradas** o **scores** continuos.

""",
    134: """### Comentarios

- Un **AUC** alto indica buena capacidad de ordenar expedientes según riesgo de incumplimiento.
- En carteras reales conviene complementar con **calibración** y **estabilidad temporal** del modelo.""",
    136: """# **19. Validación cruzada k-fold con mezcla** <a class="anchor" id="19"></a>

[Índice](#0.1)

La validación cruzada estima la estabilidad del score fuera de la muestra. Con **clases desbalanceadas**, **`StratifiedKFold`** mantiene la proporción de incumplimientos en cada pliegue; el código siguiente replica el **KFold con shuffle** del tutorial para comparar.""",
    145: """La validación cruzada puede dar una media ligeramente distinta a un único split; valore **AUC** y **F1** en el segmento de incumplimientos.""",
    151: """# **21. Resultados y conclusiones** <a class="anchor" id="21"></a>

[Índice](#0.1)

1. Los **outliers** en ratios financieros interactúan con **C** y el núcleo; conviene sensibilizar el modelo y la política de datos.

2. Los mejores resultados de exactitud en este cuaderno suelen alcanzarse con **RBF** o **lineal** y **C** alto; la **exactitud sola** puede ocultar un mal seguimiento del **incumplimiento** minoritario.

3. Un **AUC-ROC** alto sugiere buen poder de **ordenación** por riesgo.

4. Use **validación estratificada** si implementa el modelo en un motor de scoring real.

5. **GridSearchCV** ayuda a afinar hiperparámetros; valide siempre en **prueba** y, idealmente, en **ventanas temporales** (no mostrado aquí).

""",
    152: """# **22. Referencias** <a class="anchor" id="22"></a>

[Índice](#0.1)

1. *Hands-On Machine Learning* — Aurélien Géron  
2. *Introduction to Machine Learning with Python* — Müller y Guido  
3. Documentación scikit-learn: `SVC`, `GridSearchCV`, métricas.  
4. Literatura sobre **scoring crediticio**, **Basilea**, **IFRS 9** (expected credit loss) para contextualizar el uso de modelos en banca.

""",
    153: """Fin del cuaderno. Compruebe que ha subido **`scoring_riesgo_credito_ejercicio.csv`** y que **`RUTA_CSV`** apunta al archivo en su sesión de Colab.

**Disclaimer:** ejercicio académico; los datos son una **reinterpretación** del conjunto HTRU2 con nombres financieros.
""",
}


def parchear_celda_renombrado(s: str) -> str:
    """
    El CSV financiero ya incluye nombres cortos; sustituye el bloque de renombrado
    por una comprobación opcional.
    """
    old = """# Renombrar columnas (abreviaturas)

df.columns = ['rend_medio', 'vol_rent', 'curt_rent', 'asim_rent',
              'liq_medio', 'vol_flujo', 'curt_flujo', 'asim_flujo', 'incumple_12m']
"""
    new = """# El CSV ya trae nombres financieros cortos; comprobar orden y etiquetas
esperadas = ['rend_medio', 'vol_rent', 'curt_rent', 'asim_rent',
             'liq_medio', 'vol_flujo', 'curt_flujo', 'asim_flujo', 'incumple_12m']
assert list(df.columns) == esperadas, list(df.columns)
"""
    if old in s:
        return s.replace(old, new)
    return s


def main():
    escribir_csv_financiero()

    with open(BASE_NB, encoding="utf-8") as f:
        nb = json.load(f)

    for i, cell in enumerate(nb["cells"]):
        s = "".join(cell["source"])
        if i in MARKDOWN_OVERRIDES:
            s = MARKDOWN_OVERRIDES[i]
        else:
            s = aplicar_reemplazos_codigo_y_texto(s)
        s = parchear_celda_renombrado(s)
        cell["source"] = src_join(s)

    with open(OUT_NB, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print("Notebook financiero:", OUT_NB)


if __name__ == "__main__":
    main()
