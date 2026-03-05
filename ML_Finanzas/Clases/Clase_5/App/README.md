# App German Credit - Predicción de Riesgo de Crédito

Dashboard gerencial para apoyo en decisiones de asignación de crédito.

## Estructura

```
App/
├── main.py              # Página de inicio (carga de datos)
├── utils_data.py        # Funciones compartidas
├── requirements.txt
├── README.md
└── pages/
    ├── 1_Contexto.py           # Base de datos, objetivo, variables
    ├── 2_Análisis_Descriptivo.py # Univariado, bivariado, tablas de contingencia
    └── 3_Modelación.py          # Modelo, cuándo aumenta/disminuye riesgo, calculadora
```

## Ejecución

```bash
cd App
streamlit run main.py
```

## Secciones (menú lateral)

1. **Inicio** - Mensaje gerencial y carga del archivo `german_credit_data.csv`
2. **Contexto** - Significado de la base, objetivo a modelar, variables que influyen o no
3. **Análisis Descriptivo** - Univariado, bivariado y tablas de contingencia con Chi-cuadrado
4. **Modelación** - Modelo, interpretación (cuándo aumenta/disminuye riesgo), calculadora, matriz de confusión
