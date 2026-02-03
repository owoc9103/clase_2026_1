# -*- coding: utf-8 -*-
"""
Integra la mayoría de los ejercicios de Clase_6_Teoria_Pandas_Una_Base_de_Datos.ipynb
en Clase_6_Ejemplos_Finanzas.ipynb.
"""
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
TEORIA = os.path.join(DIR, "Clase_6_Teoria_Pandas_Una_Base_de_Datos.ipynb")
EJEMPLOS = os.path.join(DIR, "Clase_6_Ejemplos_Finanzas.ipynb")

def load_nb(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_nb(nb, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

def clean_cell(cell):
    """Elimina outputs y execution_count; devuelve copia."""
    c = dict(cell)
    if c.get("cell_type") == "code":
        c["outputs"] = []
        c["execution_count"] = None
    return c

def main():
    teoria = load_nb(TEORIA)
    ejemplos = load_nb(EJEMPLOS)

    # Celdas a incluir del notebook de teoría (en orden); saltar portada duplicada (primeras 2 celdas)
    teoria_cells = []
    for cell in teoria["cells"][2:]:
        c = clean_cell(cell)
        if c["cell_type"] == "markdown":
            teoria_cells.append(c)
        elif c["cell_type"] == "code":
            source = c.get("source") or []
            text = "".join(source) if isinstance(source, list) else source
            if "drive.mount" in text or "files.download" in text:
                continue
            # Adaptar rutas /content/ -> directorio actual (ej. "ejemplo.csv")
            if isinstance(source, list):
                new_source = [s.replace("/content/", "").replace("'/content/", "'") for s in source]
            else:
                new_source = [source.replace("/content/", "").replace("'/content/", "'")]
            c["source"] = new_source
            teoria_cells.append(c)

    # Nuevo notebook: intro (0-3) + título sección ejercicios + teoría + aplicación (S&P 500, FRED)
    intro_cells = ejemplos["cells"][:4]  # título, intro, pregunta objetivo, fuentes

    seccion_ejercicios = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "---\n",
            "\n",
            "## Ejercicios realizados en clase (teoría)\n",
            "\n",
            "A continuación se reproducen la **mayoría de los ejercicios** del notebook de teoría "
            "(*Clase_6_Teoria_Pandas_Una_Base_de_Datos*), para que puedas practicarlos. "
            "Después verás los mismos conceptos aplicados a datos reales (S&P 500 y PIB FRED).\n"
        ]
    }

    aplicacion_cells = ejemplos["cells"][4:]  # desde "## 1. DataFrame con datos reales..."

    # Quitar outputs de celdas de aplicación
    aplicacion_cells = [clean_cell(c) for c in aplicacion_cells]

    new_cells = intro_cells + [seccion_ejercicios] + teoria_cells + aplicacion_cells

    ejemplos["cells"] = new_cells
    save_nb(ejemplos, EJEMPLOS)
    print("OK: Clase_6_Ejemplos_Finanzas.ipynb actualizado con", len(teoria_cells), "celdas de teoría + aplicación.")

if __name__ == "__main__":
    main()
