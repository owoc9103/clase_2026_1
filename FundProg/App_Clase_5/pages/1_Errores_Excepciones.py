# -*- coding: utf-8 -*-
"""
Página: Errores y Excepciones
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.preguntas import pregunta_con_ampliar
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Errores y Excepciones", page_icon="⚠️", layout="wide")
inject_theme_styles()

st.title("⚠️ Errores y Excepciones")
st.markdown("---")

tab_teoria, tab_preguntas, tab_codigo = st.tabs(["📖 Teoría", "❓ Preguntas", "📋 Código para copiar"])

with tab_teoria:
    st.header("8.1 ¿Qué son los errores?")
    st.markdown("""
    **¿Por qué este tema importa?** Porque programar no consiste en evitar todos los errores para siempre, 
    sino en **entenderlos, anticiparlos y responder bien cuando aparezcan**.
    
    En Python hay dos tipos principales de errores:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Errores de sintaxis (`SyntaxError`)")
        st.markdown("""
        - Ocurren cuando Python **no puede interpretar** el código
        - Se detectan **antes** de ejecutar el programa
        - Ejemplos: falta de dos puntos (`:`), paréntesis no balanceados, indentación incorrecta
        """)
    with col2:
        st.subheader("Excepciones (`Exceptions`)")
        st.markdown("""
        - Ocurren **durante** la ejecución del programa
        - El código sí arranca, pero en algún momento algo sale mal
        - Pueden manejarse con `try` y `except`
        - Ejemplos: `ZeroDivisionError`, `ValueError`, `KeyError`, `FileNotFoundError`
        """)
    
    st.info("**Resumen:** Los errores de sintaxis se detectan antes de ejecutar; las excepciones ocurren durante la ejecución y pueden manejarse con `try`/`except`.")
    
    with st.expander("💡 Explicación ampliada (estilo tutor)"):
        st.markdown("""
        **¿Por qué es importante manejar errores bien?** En la vida real, los programas reciben datos 
        inesperados: usuarios que escriben texto donde se espera un número, archivos que no existen, 
        conexiones que fallan. Si no manejas estos casos, tu programa se detendrá abruptamente. 
        Con `try/except` le dices a Python: "si algo sale mal aquí, haz esto en lugar de crashear".
        
        **Analogía:** Imagina que manejas un auto. Un SyntaxError sería como tener el motor mal ensamblado 
        (el auto ni arranca). Una excepción sería un pinchazo en plena carretera: el auto sí arrancó, 
        pero en el camino algo falló. El `try/except` es como tener una rueda de repuesto y saber cambiarla.
        
        **Tip:** Puedes usar ChatGPT o similar para pedir ejemplos adicionales o aclarar dudas sobre 
        excepciones específicas. Por ejemplo: "Explícame con un ejemplo cuándo usar else vs finally en Python".
        """)
    
    st.header("8.2 Excepciones comunes")
    
    excepciones = {
        "ZeroDivisionError": "División por cero (ej: `10 / 0`). Ocurre en operaciones como `a / 0` o `a % 0`.",
        "ValueError": "Valor incorrecto (ej: `int('abc')`). La función recibe el tipo correcto pero el valor no es válido.",
        "KeyError": "Clave no existe en diccionario. Ej: `d['x']` cuando `'x'` no está en `d`.",
        "IndexError": "Índice fuera de rango en lista/tupla/cadena. Ej: `lista[10]` cuando la lista tiene 3 elementos.",
        "TypeError": "Operación en tipo incorrecto. Ej: `'texto' + 5` (concatenar string con int).",
        "FileNotFoundError": "Archivo no encontrado en la ruta especificada al abrir con `open()`."
    }
    for exc, desc in excepciones.items():
        st.markdown(f"- **`{exc}`**: {desc}")
    
    st.header("8.3 Manejo: try / except / else / finally")
    st.code("""
try:
    # Código que puede fallar
except TipoExcepcion:
    # Qué hacer si falla
else:
    # Se ejecuta solo si NO hubo excepciones
finally:
    # Siempre se ejecuta (útil para liberar recursos)
""", language="python")
    
    st.markdown("""
    **Buenas prácticas:**
    - **Específico es mejor**: captura excepciones concretas, no genéricas
    - **No silencies errores**: si algo falla, debe quedar claro qué ocurrió
    - **Mensajes claros**: el error debe servir para depurar o corregir
    """)
    
    st.header("8.4 Lanzar excepciones (`raise`)")
    st.markdown("""
    Puedes lanzar excepciones manualmente con `raise` para validar datos. Por ejemplo, si una función 
    recibe una edad negativa, puedes hacer `raise ValueError("La edad no puede ser negativa")`. 
    Esto comunica el error de forma explícita y permite que quien llame a la función lo maneje con `try/except`.
    """)
    
    st.header("8.5 Excepciones personalizadas")
    st.markdown("""
    Crea tus propias excepciones heredando de `Exception` (o de excepciones más específicas) para comunicar 
    problemas de dominio de forma precisa. Por ejemplo, `SaldoInsuficienteError` es más claro que un genérico 
    `ValueError` cuando intentas retirar más de lo que hay en una cuenta. Las excepciones personalizadas 
    facilitan el manejo selectivo: puedes capturar solo `SaldoInsuficienteError` y tratar otros errores por separado.
    """)

with tab_preguntas:
    st.header("Preguntas de comprensión")
    st.caption("Selecciona tu respuesta y haz clic en **Enviar respuesta**. Luego podrás ampliar con ejemplos para copiar al notebook.")
    
    pregunta_con_ampliar(
        key_prefix="err_q1",
        pregunta="1. ¿Cuál es la diferencia entre SyntaxError y una excepción?",
        opciones=[
            "Ambos ocurren durante la ejecución",
            "SyntaxError se detecta antes de ejecutar; las excepciones ocurren durante la ejecución",
            "No hay diferencia"
        ],
        correcta="SyntaxError se detecta antes de ejecutar; las excepciones ocurren durante la ejecución",
        explicacion_correcta="Exacto: SyntaxError impide que el código arranque; las excepciones ocurren en tiempo de ejecución.",
        explicacion_incorrecta="Revisa la teoría: SyntaxError se detecta antes de ejecutar; las excepciones ocurren durante la ejecución.",
        ejemplos_notebook=[
            {"titulo": "SyntaxError - código que no compila",
             "explicacion": "Un SyntaxError impide que el código arranque. La corrección es añadir los dos puntos.",
             "codigo": "# ESTO DA SyntaxError (falta : después del if):\n# if x > 3\n#     print(x)\n\n# Corregido:\nx = 5\nif x > 3:\n    print(x)"},
            {"titulo": "Excepciones en tiempo de ejecución",
             "explicacion": "Con try/except el programa no se detiene; captura el error y continúa.",
             "codigo": "# ZeroDivisionError ocurre al ejecutar\na = 10\nb = 0\ntry:\n    resultado = a / b\nexcept ZeroDivisionError as e:\n    print(f'Error capturado: {e}')\nprint('El programa continúa...')"},
            {"titulo": "Múltiples excepciones",
             "explicacion": "Puedes capturar varios tipos de excepción y dar un mensaje específico a cada uno.",
             "codigo": "def procesar(valor):\n    try:\n        n = int(valor)\n        return 100 / n\n    except ValueError:\n        print('No es un número válido')\n        return None\n    except ZeroDivisionError:\n        print('No se puede dividir por cero')\n        return None\n\nprint(procesar('10'))\nprint(procesar('abc'))\nprint(procesar('0'))"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="err_q2",
        pregunta="2. ¿Cuándo se ejecuta el bloque `finally`?",
        opciones=[
            "Solo cuando hay un error",
            "Solo cuando no hay error",
            "Siempre, haya o no error"
        ],
        correcta="Siempre, haya o no error",
        explicacion_correcta="El bloque finally siempre se ejecuta. Es ideal para liberar recursos (cerrar archivos, conexiones).",
        explicacion_incorrecta="El bloque finally se ejecuta siempre, haya o no excepciones.",
        ejemplos_notebook=[
            {"titulo": "finally siempre se ejecuta",
             "codigo": "def ejemplo():\n    try:\n        print('Dentro del try')\n        resultado = 10 / 2\n        return resultado\n    except ZeroDivisionError:\n        print('Error')\n    finally:\n        print('Esto SIEMPRE se ejecuta')\n\nprint(ejemplo())"},
            {"titulo": "finally con archivos (liberar recursos)",
             "codigo": "archivo = None\ntry:\n    archivo = open('datos.txt', 'r')\n    contenido = archivo.read()\n    print(contenido[:50])\nexcept FileNotFoundError:\n    print('Archivo no encontrado')\nfinally:\n    if archivo:\n        archivo.close()\n        print('Archivo cerrado correctamente')"},
            {"titulo": "else vs finally",
             "codigo": "try:\n    x = int('42')\nexcept ValueError:\n    print('Error de conversión')\nelse:\n    print('Solo si NO hubo error:', x)\nfinally:\n    print('Siempre se ejecuta')"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="err_q3",
        pregunta="3. ¿Qué excepción se lanza al dividir por cero?",
        opciones=["ValueError", "ZeroDivisionError", "TypeError"],
        correcta="ZeroDivisionError",
        explicacion_correcta="Correcto. ZeroDivisionError es la excepción específica para división por cero.",
        explicacion_incorrecta="La excepción correcta es ZeroDivisionError.",
        ejemplos_notebook=[
            {"titulo": "ZeroDivisionError básico",
             "codigo": "try:\n    resultado = 10 / 0\nexcept ZeroDivisionError as e:\n    print(f'Error: {e}')\n    print('No se puede dividir por cero')"},
            {"titulo": "Otras excepciones numéricas",
             "codigo": "# ValueError: int('abc')\ntry:\n    n = int('abc')\nexcept ValueError as e:\n    print(f'ValueError: {e}')\n\n# TypeError: 'texto' + 5\ntry:\n    r = 'texto' + 5\nexcept TypeError as e:\n    print(f'TypeError: {e}')"},
            {"titulo": "Función segura con ZeroDivisionError",
             "codigo": "def dividir_seguro(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n    except TypeError:\n        return None\n\nprint(dividir_seguro(10, 2))\nprint(dividir_seguro(10, 0))\nprint(dividir_seguro('10', 2))"},
        ]
    )

with tab_codigo:
    st.header("📋 Código para copiar")
    st.info("**Copia** el código con el botón Copy y pégalo en **Google Colab** o en tu **asistente de IA** para ejecutarlo.")
    
    st.subheader("Ejemplo: función dividir con manejo de errores")
    st.code("""# Ejemplo: función que divide con manejo de errores
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None

# Prueba
print(dividir(10, 2))
print(dividir(10, 0))
""", language="python")
    
    st.subheader("Ejercicio sugerido")
    st.markdown("""
    Pide a tu IA o implementa en Colab una función `procesar_numero(texto)` que:
    1. Convierta `texto` a float
    2. Calcule 100 / numero
    3. Capture `ValueError` y `ZeroDivisionError` con mensajes claros
    4. Retorne el resultado o None si hay error
    """)
