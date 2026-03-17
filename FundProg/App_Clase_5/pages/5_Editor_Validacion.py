"""
Página: Editor de Código con Validación
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.code_executor import ejecutar_codigo
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Editor y Validación", page_icon="✅", layout="wide")
inject_theme_styles()

st.title("✅ Editor de Código con Validación")
st.markdown("---")

st.markdown("""
Escribe código para resolver los ejercicios. **Ejecuta** para ver la salida y **valida** 
contra los criterios esperados cuando aplique.
""")

# Selector de ejercicio
ejercicio = st.selectbox(
    "Selecciona un ejercicio para validar",
    [
        "Ejecución libre (sin validación)",
        "Ejercicio 1: Función dividir con try/except",
        "Ejercicio 2: Función validar_edad con raise",
        "Ejercicio 3: Clase CuentaBancaria con depositar/retirar",
        "Ejercicio 4: Clase CuentaAhorros (herencia)",
        "Ejercicio 5: Estadísticas con módulo statistics"
    ]
)

# Código por defecto según ejercicio
codigos = {
    "Ejecución libre (sin validación)": "# Escribe tu código aquí\nprint('Hola')",
    "Ejercicio 1: Función dividir con try/except": """def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None

# Tu código aquí
""",
    "Ejercicio 2: Función validar_edad con raise": """def validar_edad(edad):
    # Debe lanzar ValueError si edad < 0 o edad > 150
    # Debe lanzar TypeError si no es número
    # Retorna True si es válida
    pass

# Tu implementación
""",
    "Ejercicio 3: Clase CuentaBancaria con depositar/retirar": """class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        pass  # Implementa
    
    def depositar(self, monto):
        pass  # Implementa
    
    def retirar(self, monto):
        pass  # Implementa

# Prueba: crear cuenta, depositar 100, retirar 50
""",
    "Ejercicio 4: Clase CuentaAhorros (herencia)": """class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

class CuentaAhorros(CuentaBancaria):
    # Hereda y añade tasa_interes, aplicar_interes()
    pass

# Prueba
""",
    "Ejercicio 5: Estadísticas con módulo statistics": """import statistics

datos = [85, 90, 78, 92, 88]
# Calcula y muestra: media, mediana, desviación estándar
"""
}

codigo = st.text_area("Código", value=codigos.get(ejercicio, ""), height=300)

col1, col2 = st.columns(2)
with col1:
    if st.button("▶️ Ejecutar código"):
        stdout, stderr, success = ejecutar_codigo(codigo)
        if success:
            if stdout:
                st.text("Salida:")
                st.code(stdout)
            else:
                st.success("Ejecutado sin salida visible.")
        else:
            st.error(stderr)
            if stdout:
                st.text("Salida antes del error:")
                st.code(stdout)

with col2:
    if st.button("🔍 Validar"):
        if ejercicio == "Ejecución libre (sin validación)":
            st.info("Este modo solo ejecuta código. Elige un ejercicio para validar.")
        else:
            # Ejecutar y validar según el ejercicio
            stdout, stderr, success = ejecutar_codigo(codigo)
            if not success:
                st.error(f"Error al ejecutar: {stderr}")
            else:
                # Validaciones básicas por ejercicio
                if "Ejercicio 1" in ejercicio:
                    try:
                        ns = {}
                        exec(codigo, ns)
                        dividir = ns.get('dividir')
                        if dividir is None:
                            st.warning("⚠️ Define la función dividir")
                        else:
                            r = dividir(10, 2)
                            z = dividir(10, 0)
                            if r == 5 and z is None:
                                st.success("✅ Correcto: dividir(10,2)=5 y dividir(10,0) maneja el error")
                            else:
                                st.warning(f"⚠️ Revisa: dividir(10,2) debe ser 5 (obtuviste {r}), dividir(10,0) debe retornar None (obtuviste {z})")
                    except Exception as e:
                        st.error(f"Error: {e}")
                elif "Ejercicio 3" in ejercicio:
                    try:
                        ns = {}
                        exec(codigo, ns)
                        C = ns.get('CuentaBancaria')
                        if C:
                            c = C("Test", 100)
                            c.depositar(50)
                            c.retirar(30)
                            if c.saldo == 120:
                                st.success("✅ Correcto: depositar y retirar funcionan")
                            else:
                                st.warning(f"⚠️ Saldo esperado 120, obtuviste {c.saldo}")
                        else:
                            st.warning("⚠️ Define la clase CuentaBancaria")
                    except Exception as e:
                        st.error(f"Error: {e}")
                elif "Ejercicio 4" in ejercicio:
                    try:
                        ns = {}
                        exec(codigo, ns)
                        CA = ns.get('CuentaAhorros')
                        if CA and CA.__bases__:
                            c = CA("Test", 1000, 0.02)
                            if hasattr(c, 'aplicar_interes'):
                                c.aplicar_interes()
                                st.success("✅ CuentaAhorros con herencia y aplicar_interes")
                            else:
                                st.warning("⚠️ Añade el método aplicar_interes")
                        else:
                            st.warning("⚠️ Define CuentaAhorros heredando de CuentaBancaria")
                    except Exception as e:
                        st.error(f"Error: {e}")
                elif "Ejercicio 5" in ejercicio:
                    if "statistics" in codigo and "mean" in codigo:
                        st.success("✅ Usas el módulo statistics correctamente")
                    else:
                        st.warning("⚠️ Usa import statistics y statistics.mean()")
                else:
                    st.info("Ejecución correcta. Revisa manualmente que cumpla los requisitos.")
