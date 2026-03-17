# -*- coding: utf-8 -*-
"""
Página: Biblioteca Estándar de Python
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.code_executor import ejecutar_codigo
from utils.preguntas import pregunta_con_ampliar
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Biblioteca Estándar", page_icon="📚", layout="wide")
inject_theme_styles()

st.title("📚 Biblioteca Estándar de Python")
st.markdown("---")

tab_teoria, tab_preguntas, tab_codigo = st.tabs(["📖 Teoría", "❓ Preguntas", "💻 Editor de Código"])

with tab_teoria:
    st.header("Módulos esenciales")
    
    with st.expander("10.1 `math` - Funciones matemáticas", expanded=True):
        st.markdown("""
        Proporciona constantes y funciones matemáticas: `pi`, `e`, `sqrt`, `pow`, `ceil`, `floor`, 
        `log`, `log10`, `sin`, `cos`, `tan`, `factorial`. Útil para cálculos científicos, financieros 
        o cualquier operación que requiera precisión matemática. Por ejemplo, `math.sqrt(16)` devuelve 4.0; 
        `math.ceil(4.3)` redondea hacia arriba a 5; `math.floor(4.7)` redondea hacia abajo a 4.
        """)
    
    with st.expander("10.2 `datetime` - Fechas y tiempos"):
        st.markdown("""
        - **`datetime.now()`**: obtiene la fecha y hora actual del sistema
        - **`timedelta`**: representa intervalos (días, horas, minutos) para sumar/restar a fechas
        - **`strftime`**: formatea una fecha como cadena (ej: `'%Y-%m-%d'` para `2024-03-15`)
        - **`strptime`**: convierte una cadena en objeto datetime (inverso de strftime)
        Es esencial para aplicaciones que trabajan con fechas: reportes, vencimientos, logs, etc.
        """)
    
    with st.expander("10.3 `time` - Medición y control"):
        st.markdown("""
        - **`time.time()`**: retorna el timestamp Unix (segundos desde 1970); útil para medir duración de operaciones
        - **`time.sleep(segundos)`**: pausa la ejecución del programa
        - **`time.ctime()`**: convierte timestamp a formato legible
        Útil para benchmarking, control de flujo temporal o generar valores únicos basados en tiempo.
        """)
    
    with st.expander("10.4 `statistics` - Medidas estadísticas"):
        st.markdown("""
        - **`mean`**: promedio aritmético
        - **`median`**: valor central (ordenando los datos)
        - **`mode`**: valor más frecuente
        - **`stdev`**: desviación estándar
        - **`variance`**: varianza
        Pensado para listas de números; más claro y probado que implementar estas fórmulas a mano.
        """)
    
    with st.expander("10.5 `os` y `pathlib` - Sistema de archivos"):
        st.markdown("""
        - **`os`**: `getcwd()` (directorio actual), `exists()`, `isfile()`, `mkdir()`, etc.
        - **`pathlib.Path`**: API orientada a objetos y multiplataforma. `Path('archivo.txt').exists()`, 
        `Path('carpeta') / 'archivo.txt'`, `.name`, `.parent`, `.suffix`. `pathlib` es la opción recomendada 
        en código nuevo por su legibilidad y manejo correcto de rutas en Windows/Linux/Mac.
        """)
    
    st.code("""
import math
print(math.pi, math.sqrt(16))

from datetime import datetime, timedelta
hoy = datetime.now()
print(hoy.strftime('%Y-%m-%d'))

import statistics
datos = [1, 2, 3, 4, 5]
print(statistics.mean(datos))
""", language="python")
    
    with st.expander("💡 Explicación ampliada (estilo tutor)"):
        st.markdown("""
        **¿Por qué usar la biblioteca estándar?** Python viene con módulos listos para usar. 
        No reinventes la rueda: `statistics.mean()` es más claro y probado que escribir un bucle 
        para promediar. `datetime` maneja años bisiestos, zonas horarias y formatos por ti.
        
        **pathlib vs os.path:** `pathlib.Path` es más moderno y orientado a objetos. 
        `Path("carpeta/archivo.txt").exists()` es más legible que `os.path.exists("carpeta/archivo.txt")`.
        
        **Tip:** Pregunta a ChatGPT: "¿Cómo formatear una fecha en español con datetime en Python?" 
        para ver ejemplos con locale.
        """)

with tab_preguntas:
    st.header("Preguntas de comprensión")
    st.caption("Selecciona tu respuesta y haz clic en **Enviar respuesta**. Luego podrás ampliar con ejemplos para copiar al notebook.")
    
    pregunta_con_ampliar(
        key_prefix="bib_q1",
        pregunta="1. ¿Qué módulo usarías para calcular la media de una lista?",
        opciones=["math", "statistics", "datetime"],
        correcta="statistics",
        explicacion_correcta="Correcto. El módulo `statistics` tiene `mean()`, `median()`, `stdev()`, etc.",
        explicacion_incorrecta="El módulo `statistics` está diseñado para medidas estadísticas como la media.",
        ejemplos_notebook=[
            {"titulo": "statistics.mean, median, stdev",
             "explicacion": "mean es el promedio; median el valor central; stdev mide la dispersión de los datos.",
             "codigo": "import statistics\ndatos = [85, 90, 78, 92, 88]\nprint('Media:', statistics.mean(datos))\nprint('Mediana:', statistics.median(datos))\nprint('Desv. estándar:', statistics.stdev(datos))"},
            {"titulo": "math vs statistics",
             "explicacion": "math para operaciones matemáticas puras; statistics para análisis de conjuntos de datos.",
             "codigo": "# math: operaciones matemáticas (sqrt, sin, log)\nimport math\nprint(math.sqrt(16), math.pi)\n\n# statistics: medidas de datos\nimport statistics\nprint(statistics.mean([1,2,3,4,5]))"},
            {"titulo": "Estadísticas completas",
             "explicacion": "mode devuelve el valor más frecuente; variance es el cuadrado de la desviación estándar.",
             "codigo": "import statistics\ndatos = [1, 2, 2, 3, 3, 3, 4, 5]\nprint('Media:', statistics.mean(datos))\nprint('Mediana:', statistics.median(datos))\nprint('Moda:', statistics.mode(datos))\nprint('Varianza:', statistics.variance(datos))"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="bib_q2",
        pregunta="2. ¿Qué hace `datetime.strftime`?",
        opciones=[
            "Convierte string a fecha",
            "Formatea una fecha como string",
            "Calcula diferencia entre fechas"
        ],
        correcta="Formatea una fecha como string",
        explicacion_correcta="Correcto. `strftime` formatea un objeto datetime como cadena de texto.",
        explicacion_incorrecta="`strftime` formatea una fecha como string. Para string a fecha se usa `strptime`.",
        ejemplos_notebook=[
            {"titulo": "strftime - formatear fecha",
             "codigo": "from datetime import datetime\nhoy = datetime.now()\nprint(hoy.strftime('%Y-%m-%d'))\nprint(hoy.strftime('%d/%m/%Y'))\nprint(hoy.strftime('%A %d de %B'))"},
            {"titulo": "Códigos de formato comunes",
             "codigo": "# %Y=año, %m=mes, %d=día\n# %H=hora, %M=minuto, %S=segundo\n# %A=día semana, %B=mes nombre\nhoy = datetime.now()\nprint(hoy.strftime('%H:%M:%S'))\nprint(hoy.strftime('%A'))"},
            {"titulo": "strptime - string a fecha (inverso)",
             "codigo": "from datetime import datetime\ntexto = '2024-03-15'\nfecha = datetime.strptime(texto, '%Y-%m-%d')\nprint(fecha)\nprint(type(fecha))"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="bib_q3",
        pregunta="3. ¿Para qué sirve `pathlib.Path`?",
        opciones=[
            "Solo para rutas de Windows",
            "API moderna para manejar rutas de archivos",
            "Para abrir archivos"
        ],
        correcta="API moderna para manejar rutas de archivos",
        explicacion_correcta="Correcto. `pathlib.Path` ofrece una API orientada a objetos para rutas multiplataforma.",
        explicacion_incorrecta="`pathlib.Path` es una API moderna para rutas, funciona en Windows, Linux y Mac.",
        ejemplos_notebook=[
            {"titulo": "Path básico",
             "codigo": "from pathlib import Path\nruta = Path('carpeta/archivo.txt')\nprint(ruta.name)\nprint(ruta.parent)\nprint(ruta.suffix)\nprint(ruta.exists())"},
            {"titulo": "Path vs os.path",
             "codigo": "import os\nfrom pathlib import Path\n\n# os.path (antiguo)\nprint(os.path.exists('main.py'))\nprint(os.path.join('carpeta', 'archivo.txt'))\n\n# pathlib (moderno)\nprint(Path('main.py').exists())\nprint(Path('carpeta') / 'archivo.txt')"},
            {"titulo": "Listar archivos con Path",
             "codigo": "from pathlib import Path\n# Listar .py en directorio actual\nfor f in Path('.').glob('*.py'):\n    print(f.name)"},
        ]
    )

with tab_codigo:
    st.header("Editor de código")
    st.markdown("Practica con los módulos de la biblioteca estándar.")
    
    codigo_default = '''# Ejemplo: math y statistics
import math
import statistics

datos = [85, 90, 78, 92, 88]
print("Promedio:", statistics.mean(datos))
print("Raíz de 144:", math.sqrt(144))
print("Pi:", math.pi)
'''
    
    codigo = st.text_area("Código Python", value=codigo_default, height=200)
    
    if st.button("▶️ Ejecutar"):
        stdout, stderr, success = ejecutar_codigo(codigo)
        if success:
            if stdout:
                st.text("Salida:")
                st.code(stdout)
            else:
                st.success("Código ejecutado correctamente.")
        else:
            st.error(stderr)
    
    st.subheader("Ejercicio sugerido")
    st.markdown("""
    Usa `datetime` para:
    1. Obtener la fecha actual
    2. Calcular la fecha de hace 7 días
    3. Formatear ambas como 'YYYY-MM-DD'
    """)
