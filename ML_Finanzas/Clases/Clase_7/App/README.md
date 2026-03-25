# Clase 6 - Predicción de Churn Bancario

**Curso:** Machine Learning en Finanzas y Economía

Dashboard interactivo para apoyar decisiones de retención de clientes bancarios mediante **regresión logística** con balanceo SMOTE.

## Contenido

- **Contexto**: Base de datos de clientes, variable objetivo (Exited), variables del modelo
- **Análisis descriptivo**: Univariado, bivariado, tablas de contingencia
- **Modelación**: Regresión logística, calculadora de predicción, matriz de confusión, curva ROC

## Estructura

```
Clase_6/
├── App/
│   ├── Clientes.py          # Página principal (carga de datos)
│   ├── utils_data.py        # Funciones compartidas
│   ├── requirements.txt
│   ├── README.md
│   └── pages/
│       ├── 1_Contexto.py
│       ├── 2_Análisis_Descriptivo.py
│       └── 3_Modelación.py
└── Churn_Modelling.csv      # Dataset (en carpeta padre Clase_6)
```

## Ejecución

```bash
cd ML_Finanzas/Clases/Clase_6/App
pip install -r requirements.txt
streamlit run Clientes.py
```

Luego cargue el archivo **Churn_Modelling.csv** (disponible en `Clase_6/`) en la sección de inicio del dashboard.
