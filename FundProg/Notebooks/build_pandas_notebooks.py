# -*- coding: utf-8 -*-
"""
Genera notebooks de Pandas siguiendo la secuencia Clase_6, Clase_7, Clase_8:
- Clase_N_Teoria_*.ipynb
- Clase_N_Ejemplos_Finanzas.ipynb
- Clase_N_Taller.ipynb
"""
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
PANDAS_IMG = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/240px-Pandas_logo.svg.png"

def load_nb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_nb(nb, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def strip_outputs(cell):
    c = dict(cell)
    if c.get("cell_type") == "code" and "outputs" in c:
        c["outputs"] = []
    if "execution_count" in c:
        c["execution_count"] = None
    return c

def cell_image(title_text):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "<div align=\"center\">\n",
            "\n",
            f"**{title_text}**\n",
            "\n",
            f"<img src=\"{PANDAS_IMG}\" alt=\"Pandas\" width=\"240\"/>\n",
            "\n",
            "</div>"
        ]
    }

def cell_teoria_title(clase_num, titulo, objetivos_list, doc_url):
    lineas = [
        f"# Clase {clase_num}: {titulo}\n",
        "\n",
        "## Contenido Teórico\n",
        "\n",
        f"Basado en: {doc_url}\n",
        "\n",
        "### Objetivos de la clase:\n"
    ]
    for o in objetivos_list:
        lineas.append(f"- {o}\n")
    return {"cell_type": "markdown", "metadata": {}, "source": lineas}

def cell_ejemplos_intro(clase_num, tema):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# Clase {clase_num}: Ejemplos Aplicados en Finanzas\n",
            "\n",
            f"## Aplicando pandas ({tema}) a problemas financieros\n",
            "\n",
            "En este notebook verás ejemplos de uso de pandas en contexto financiero."
        ]
    }

def cell_taller_intro(clase_num, tema):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"# Clase {clase_num}: Taller Práctico\n",
            "\n",
            f"## Ejercicios para reforzar pandas — {tema}\n",
            "\n",
            "Resuelve los siguientes ejercicios aplicando Series, DataFrames y las herramientas vistas en la teoría."
        ]
    }

def empty_code_cell():
    return {"cell_type": "code", "metadata": {}, "outputs": [], "source": ["# Escribe tu código aquí\n", "\n"], "execution_count": None}

# --- Configuración por clase ---
CLASE_6 = {
    "teoria_titulo": "Pandas — Estructura de una base de datos",
    "teoria_objetivos": [
        "Importar pandas y conocer el entorno",
        "Comprender **Series** y **DataFrame** como estructuras de una tabla (una base de datos)",
        "Crear y manipular Series y DataFrames",
        "Trabajar con índices y columnas",
        "Aplicar operaciones básicas sobre una única tabla de datos"
    ],
    "teoria_doc": "[pandas - Entendimiento de los datos (Parte 1)](https://pandas.pydata.org/docs/user_guide/dsintro.html)",
    "ejemplos_tema": "una base de datos (Series y DataFrame)",
    "taller_tema": "estructura de una base de datos",
    "parte_nb": "Pandas - Entendimiento de los datos - Parte 1_B.ipynb",
}

CLASE_7 = {
    "teoria_titulo": "Pandas — Exploración y descripción de datos",
    "teoria_objetivos": [
        "Explorar un conjunto de datos con **.info()** y **.describe()**",
        "Conocer estadística descriptiva con pandas",
        "Realizar visualización básica de datos",
        "Entender tipos de dato y valores faltantes en una tabla"
    ],
    "teoria_doc": "[pandas - Entendimiento de los datos (Parte 2)](https://pandas.pydata.org/docs/user_guide/basics.html)",
    "ejemplos_tema": "exploración y descripción (.info, .describe)",
    "taller_tema": "exploración y descripción de datos",
    "parte_nb": "Pandas - Entendimiento de los datos - Parte 2_B.ipynb",
}

CLASE_8 = {
    "teoria_titulo": "Pandas — Múltiples bases de datos (Joins y Merges)",
    "teoria_objetivos": [
        "Trabajar con **múltiples DataFrames** (varias tablas / bases de datos)",
        "Concatenar tablas con **pd.concat()**",
        "Unir tablas con **pd.merge()** (equivalente a JOIN en SQL)",
        "Usar **.join()** para combinar por índice",
        "Aplicar joins y merges en casos prácticos"
    ],
    "teoria_doc": "[pandas - Merge, join, concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)",
    "ejemplos_tema": "joins y merges (múltiples tablas)",
    "taller_tema": "joins y merges",
}

# --- Contenido Teoría Clase 8 (joins/merges) ---
CELLS_TEORIA_8 = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## 1. Múltiples bases de datos\n",
            "\n",
            "En la práctica trabajamos con **varias tablas** (varios DataFrames). Para combinarlas usamos **concat**, **merge** y **join**.\n",
            "\n",
            "### 1.1 Importar pandas"
        ]
    },
    {"cell_type": "code", "metadata": {}, "outputs": [], "source": ["import pandas as pd\n", "import numpy as np"], "execution_count": None},
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 1.2 pd.concat() — Concatenar DataFrames\n", "\n", "**pd.concat()** apila varios DataFrames (filas o columnas). Útil cuando las tablas tienen la **misma estructura**."]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "outputs": [],
        "source": [
            "df1 = pd.DataFrame({\"A\": [1, 2], \"B\": [3, 4]})\n",
            "df2 = pd.DataFrame({\"A\": [5, 6], \"B\": [7, 8]})\n",
            "pd.concat([df1, df2], ignore_index=True)"
        ],
        "execution_count": None
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 1.3 pd.merge() — Unir tablas (JOIN)\n", "\n", "**pd.merge()** une dos DataFrames por **columnas clave**. Equivale a JOIN en SQL (inner, left, right, outer)."]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "outputs": [],
        "source": [
            "ventas = pd.DataFrame({\"id\": [1, 2, 3], \"producto\": [\"A\", \"B\", \"C\"], \"monto\": [100, 200, 150]})\n",
            "clientes = pd.DataFrame({\"id\": [1, 2, 4], \"nombre\": [\"Ana\", \"Luis\", \"María\"]})\n",
            "pd.merge(ventas, clientes, on=\"id\", how=\"left\")"
        ],
        "execution_count": None
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": ["### 1.4 .join() — Unir por índice\n", "\n", "El método **.join()** une por **índice**."]
    },
    {
        "cell_type": "code",
        "metadata": {},
        "outputs": [],
        "source": [
            "izq = pd.DataFrame({\"X\": [10, 20]}, index=[\"a\", \"b\"])\n",
            "der = pd.DataFrame({\"Y\": [30, 40]}, index=[\"a\", \"b\"])\n",
            "izq.join(der)"
        ],
        "execution_count": None
    },
]

# --- Generar Clase 6: Teoría, Ejemplos, Taller ---
def build_clase_6():
    p1 = load_nb(os.path.join(DIR, CLASE_6["parte_nb"]))
    tit_cell = cell_teoria_title(6, CLASE_6["teoria_titulo"], CLASE_6["teoria_objetivos"], CLASE_6["teoria_doc"])
    cells_teoria = [cell_image("Clase 6 — Pandas: Estructura de una base de datos"), tit_cell] + [strip_outputs(c) for c in p1["cells"][1:]]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": p1.get("metadata", {}), "cells": cells_teoria},
            os.path.join(DIR, "Clase_6_Teoria_Pandas_Una_Base_de_Datos.ipynb"))
    print("Creado: Clase_6_Teoria_Pandas_Una_Base_de_Datos.ipynb")

    cells_ej = [
        cell_image("Clase 6 — Ejemplos en Finanzas"),
        cell_ejemplos_intro(6, CLASE_6["ejemplos_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 1. Series y DataFrame con datos financieros\n", "\n", "Crea un DataFrame con precios o retornos y explora con `.head()`, `.info()`."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 2. Índices y columnas\n", "\n", "Trabaja con fechas como índice y columnas numéricas (precio, volumen)."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_ej},
            os.path.join(DIR, "Clase_6_Ejemplos_Finanzas.ipynb"))
    print("Creado: Clase_6_Ejemplos_Finanzas.ipynb")

    cells_taller = [
        cell_image("Clase 6 — Taller"),
        cell_taller_intro(6, CLASE_6["taller_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 1: DataFrame de precios\n", "\n", "Crea un DataFrame con al menos 3 columnas: fecha, activo, precio. Usa Series y DataFrame. Muestra `.head()` y `.info()`."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 2: Índice temporal\n", "\n", "Crea un DataFrame con índice de fechas (pd.date_range) y una columna de retornos. Accede por índice y por columna."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_taller},
            os.path.join(DIR, "Clase_6_Taller.ipynb"))
    print("Creado: Clase_6_Taller.ipynb")

# --- Generar Clase 7: Teoría, Ejemplos, Taller ---
def build_clase_7():
    p2 = load_nb(os.path.join(DIR, CLASE_7["parte_nb"]))
    tit_cell = cell_teoria_title(7, CLASE_7["teoria_titulo"], CLASE_7["teoria_objetivos"], CLASE_7["teoria_doc"])
    cells_teoria = [cell_image("Clase 7 — Pandas: Exploración y descripción de datos"), tit_cell] + [strip_outputs(c) for c in p2["cells"][1:]]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": p2.get("metadata", {}), "cells": cells_teoria},
            os.path.join(DIR, "Clase_7_Teoria_Pandas_Exploracion_Descripcion.ipynb"))
    print("Creado: Clase_7_Teoria_Pandas_Exploracion_Descripcion.ipynb")

    cells_ej = [
        cell_image("Clase 7 — Ejemplos en Finanzas"),
        cell_ejemplos_intro(7, CLASE_7["ejemplos_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 1. Cargar datos y explorar\n", "\n", "Carga un CSV financiero (o crea un DataFrame) y aplica `.info()`, `.describe()`."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 2. Estadística descriptiva\n", "\n", "Calcula media, desviación estándar y cuartiles de precios o retornos."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_ej},
            os.path.join(DIR, "Clase_7_Ejemplos_Finanzas.ipynb"))
    print("Creado: Clase_7_Ejemplos_Finanzas.ipynb")

    cells_taller = [
        cell_image("Clase 7 — Taller"),
        cell_taller_intro(7, CLASE_7["taller_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 1: Exploración\n", "\n", "Carga un conjunto de datos (CSV o DataFrame) y muestra `.info()`, `.describe()`. Identifica tipos de dato y valores faltantes."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 2: Resumen por columna\n", "\n", "Para columnas numéricas, calcula min, max, media y cuenta de nulos. Usa métodos de pandas."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_taller},
            os.path.join(DIR, "Clase_7_Taller.ipynb"))
    print("Creado: Clase_7_Taller.ipynb")

# --- Generar Clase 8: Teoría, Ejemplos, Taller ---
def build_clase_8():
    tit_cell = cell_teoria_title(8, CLASE_8["teoria_titulo"], CLASE_8["teoria_objetivos"], CLASE_8["teoria_doc"])
    cells_teoria = [cell_image("Clase 8 — Pandas: Joins y Merges"), tit_cell] + CELLS_TEORIA_8
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_teoria},
            os.path.join(DIR, "Clase_8_Teoria_Pandas_Joins_Merges.ipynb"))
    print("Creado: Clase_8_Teoria_Pandas_Joins_Merges.ipynb")

    cells_ej = [
        cell_image("Clase 8 — Ejemplos en Finanzas"),
        cell_ejemplos_intro(8, CLASE_8["ejemplos_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 1. Unir tabla de operaciones con tabla de clientes\n", "\n", "Crea dos DataFrames (operaciones y clientes) y haz un merge por id de cliente (left join)."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## 2. Concatenar datos de varios períodos\n", "\n", "Concatena en filas varios DataFrames con la misma estructura (ej. precios por mes)."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_ej},
            os.path.join(DIR, "Clase_8_Ejemplos_Finanzas.ipynb"))
    print("Creado: Clase_8_Ejemplos_Finanzas.ipynb")

    cells_taller = [
        cell_image("Clase 8 — Taller"),
        cell_taller_intro(8, CLASE_8["taller_tema"]),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 1: merge\n", "\n", "Crea dos tablas: una de ventas (id_producto, monto) y otra de productos (id_producto, nombre). Haz merge y muestra las ventas con el nombre del producto."]},
        empty_code_cell(),
        {"cell_type": "markdown", "metadata": {}, "source": ["## Ejercicio 2: concat\n", "\n", "Crea dos DataFrames con las mismas columnas (ej. retornos de dos activos en distintos períodos) y concaténalos en filas."]},
        empty_code_cell(),
    ]
    save_nb({"nbformat": 4, "nbformat_minor": 0, "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3"}}, "cells": cells_taller},
            os.path.join(DIR, "Clase_8_Taller.ipynb"))
    print("Creado: Clase_8_Taller.ipynb")

if __name__ == "__main__":
    build_clase_6()
    build_clase_7()
    build_clase_8()
    # Eliminar los notebooks antiguos si existen
    for old in ["Pandas_Clase_1_Una_Base_de_Datos.ipynb", "Pandas_Clase_2_Exploracion_Descripcion.ipynb", "Pandas_Clase_3_Joins_Merges.ipynb"]:
        p = os.path.join(DIR, old)
        if os.path.exists(p):
            os.remove(p)
            print(f"Eliminado: {old}")
    print("Listo.")
