"""
Utilidad para ejecutar y validar código Python de forma segura.
"""

import sys
import io
from contextlib import redirect_stdout, redirect_stderr


def ejecutar_codigo(codigo: str, timeout: int = 5) -> tuple[str, str, bool]:
    """
    Ejecuta código Python y captura la salida.
    
    Returns:
        tuple: (stdout, stderr, success)
    """
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    
    try:
        with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
            exec(codigo, {"__builtins__": __builtins__})
        return stdout_capture.getvalue(), stderr_capture.getvalue(), True
    except SyntaxError as e:
        return "", f"Error de sintaxis: {e}", False
    except Exception as e:
        return stdout_capture.getvalue(), f"{type(e).__name__}: {e}", False


def validar_codigo_ejercicio(codigo: str, validaciones: list) -> tuple[bool, list[str]]:
    """
    Valida que el código cumpla con una lista de validaciones.
    Cada validación es una función que recibe el namespace local después de ejecutar
    y retorna (bool, str) indicando si pasó y el mensaje.
    """
    namespace = {}
    try:
        exec(codigo, {"__builtins__": __builtins__}, namespace)
    except Exception as e:
        return False, [f"Error al ejecutar: {type(e).__name__}: {e}"]
    
    resultados = []
    for i, valid in enumerate(validaciones):
        try:
            ok, msg = valid(namespace)
            resultados.append(f"{'✅' if ok else '❌'} {msg}")
        except Exception as e:
            resultados.append(f"❌ Error en validación: {e}")
    
    return all("✅" in r for r in resultados), resultados
