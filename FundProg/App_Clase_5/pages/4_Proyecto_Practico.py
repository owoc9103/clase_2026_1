"""
Página: Proyecto Práctico - Sistema Bancario
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Proyecto Práctico", page_icon="🏦", layout="wide")
inject_theme_styles()

st.title("🏦 Proyecto Práctico: Sistema Bancario con POO")
st.markdown("---")

st.markdown("""
Construcción progresiva de un sistema bancario usando programación orientada a objetos.
Integra: **excepciones**, **clases**, **herencia**, **persistencia** y **biblioteca estándar**.
""")

tab_pasos, tab_codigo = st.tabs(["📋 Pasos del Proyecto", "💻 Tu Código"])

with tab_pasos:
    st.header("Pasos del proyecto")
    
    with st.expander("Paso 1: Clase base CuentaBancaria", expanded=True):
        st.markdown("""
        Crea una clase con:
        - **Atributos**: titular, saldo, numero_cuenta, transacciones (lista)
        - **Métodos**: `__init__`, `depositar`, `retirar`, `consultar_saldo`, `obtener_historial`, `__str__`
        - Usa excepciones personalizadas para errores
        - Valida todos los datos de entrada
        """)
    
    with st.expander("Paso 2: Excepciones personalizadas"):
        st.markdown("""
        Crea: `SaldoInsuficienteError`, `MontoInvalidoError`, `CuentaNoEncontradaError`, `TransaccionInvalidaError`
        """)
    
    with st.expander("Paso 3: Clases derivadas"):
        st.markdown("""
        - **CuentaAhorros**: tasa_interes, aplicar_interes()
        - **CuentaCorriente**: limite_sobregiro, sobrescribe retirar()
        - **CuentaInversion**: tipo_inversion, riesgo, calcular_rendimiento_esperado()
        """)
    
    with st.expander("Paso 4: Clase Banco"):
        st.markdown("""
        - Diccionario de cuentas (clave: numero_cuenta)
        - Métodos: agregar_cuenta, buscar_cuenta, eliminar_cuenta, listar_cuentas, total_depositos, estadisticas
        """)
    
    with st.expander("Paso 5: Persistencia JSON"):
        st.markdown("""
        - guardar_en_archivo(archivo)
        - cargar_desde_archivo(archivo)
        """)
    
    with st.expander("Paso 6: Reportes"):
        st.markdown("""
        - generar_reporte_consola()
        - generar_reporte_archivo(archivo) usando datetime
        """)

with tab_codigo:
    st.header("📋 Código para copiar")
    st.info("**Copia** el código y pégalo en **Google Colab** o en tu **asistente de IA** para ejecutarlo.")
    
    st.subheader("Paso 1: Excepciones y CuentaBancaria base")
    st.code("""# Paso 1: Excepciones y CuentaBancaria base
class SaldoInsuficienteError(Exception):
    pass

class MontoInvalidoError(Exception):
    pass

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacciones = []
    
    def depositar(self, monto):
        if monto <= 0:
            raise MontoInvalidoError("Monto debe ser positivo")
        self.saldo += monto
        self.transacciones.append(("Depósito", monto))
        return True
    
    def retirar(self, monto):
        if monto <= 0:
            raise MontoInvalidoError("Monto debe ser positivo")
        if monto > self.saldo:
            raise SaldoInsuficienteError(f"Saldo: {self.saldo}")
        self.saldo -= monto
        self.transacciones.append(("Retiro", -monto))
        return True
    
    def __str__(self):
        return f"{self.titular}: ${self.saldo:,.2f}"

# Prueba
c = CuentaBancaria("Juan", 1000)
c.depositar(500)
print(c)
c.retirar(200)
print(c)
print("Transacciones:", c.transacciones)
""", language="python")
    st.caption("Implementa los pasos 2-6 en Colab o pide a tu IA que te guíe.")
