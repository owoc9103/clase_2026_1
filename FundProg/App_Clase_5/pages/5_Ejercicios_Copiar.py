# -*- coding: utf-8 -*-
"""
Página: Ejercicios para copiar en Colab o IA
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Ejercicios para copiar", page_icon="📋", layout="wide")
inject_theme_styles()

st.title("📋 Ejercicios para copiar")
st.markdown("---")

st.info("""
**Copia** cada bloque de código (usa el botón **Copy** o Ctrl+C) y pégalo en **Google Colab** 
o en tu **asistente de IA** (ChatGPT, Claude, Cursor) para ejecutarlo y practicar.
""")

ejercicio = st.selectbox(
    "Selecciona un ejercicio",
    [
        "Ejercicio 1: Función dividir con try/except",
        "Ejercicio 2: Función validar_edad con raise",
        "Ejercicio 3: Clase CuentaBancaria",
        "Ejercicio 4: Clase CuentaAhorros (herencia)",
        "Ejercicio 5: Estadísticas con statistics"
    ]
)

CODIGOS = {
    "Ejercicio 1: Función dividir con try/except": {
        "instrucciones": "Implementa una función `dividir(a, b)` que retorne a/b o None si hay ZeroDivisionError.",
        "codigo": '''def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None

# Prueba
print(dividir(10, 2))   # 5.0
print(dividir(10, 0))   # None (con mensaje)
'''
    },
    "Ejercicio 2: Función validar_edad con raise": {
        "instrucciones": "Implementa `validar_edad(edad)`: lanza ValueError si edad < 0 o > 150, TypeError si no es número; retorna True si es válida.",
        "codigo": '''def validar_edad(edad):
    if not isinstance(edad, (int, float)):
        raise TypeError(f"La edad debe ser un número, recibido: {type(edad).__name__}")
    if edad < 0:
        raise ValueError(f"La edad no puede ser negativa: {edad}")
    if edad > 150:
        raise ValueError(f"La edad no puede ser mayor a 150: {edad}")
    return True

# Prueba
try:
    validar_edad(25)
    print("Edad 25: Válida")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
'''
    },
    "Ejercicio 3: Clase CuentaBancaria": {
        "instrucciones": "Clase con titular, saldo, depositar(), retirar() y __str__().",
        "codigo": '''class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            return True
        return False
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo:,.2f}"

# Prueba
c = CuentaBancaria("Juan", 1000)
c.depositar(500)
c.retirar(200)
print(c)
'''
    },
    "Ejercicio 4: Clase CuentaAhorros (herencia)": {
        "instrucciones": "CuentaAhorros hereda de CuentaBancaria, añade tasa_interes y aplicar_interes().",
        "codigo": '''class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa_interes=0.02):
        super().__init__(titular, saldo)
        self.tasa_interes = tasa_interes
    
    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        return interes
    
    def __str__(self):
        return f"Cuenta Ahorros de {self.titular}: ${self.saldo:,.2f} ({self.tasa_interes*100}%)"

# Prueba
c = CuentaAhorros("María", 1000, 0.03)
c.aplicar_interes()
print(c)
'''
    },
    "Ejercicio 5: Estadísticas con statistics": {
        "instrucciones": "Usa el módulo statistics para calcular media, mediana y desviación estándar.",
        "codigo": '''import statistics

datos = [85, 90, 78, 92, 88]
print("Media:", statistics.mean(datos))
print("Mediana:", statistics.median(datos))
print("Desv. estándar:", statistics.stdev(datos))
print("Varianza:", statistics.variance(datos))
'''
    }
}

info = CODIGOS.get(ejercicio, {})
if info:
    st.markdown(f"**Instrucciones:** {info['instrucciones']}")
    st.code(info["codigo"], language="python")
    st.caption("👆 Copia el código y pégalo en Colab o pide a tu IA que lo ejecute/explique.")
