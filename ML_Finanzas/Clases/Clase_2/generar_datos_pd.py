"""
Script para generar base de datos histórica de Probabilidad de Incumplimiento (PD)
y variables macroeconómicas.

Este script genera datos simulados pero realistas para el caso práctico de modelado de PD.

Autor: Curso ML en Finanzas
Fecha: 2026
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def generar_datos_pd(n_meses=60, semilla=42, guardar=True, ruta_archivo=None):
    """
    Genera base de datos histórica de PD y variables macroeconómicas.
    
    Parámetros:
    -----------
    n_meses : int
        Número de meses de datos históricos a generar (default: 60 = 5 años)
    semilla : int
        Semilla para reproducibilidad (default: 42)
    guardar : bool
        Si True, guarda los datos en CSV (default: True)
    ruta_archivo : str
        Ruta donde guardar el archivo CSV. Si None, usa ruta por defecto.
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame con los datos generados
    """
    
    # Configurar semilla para reproducibilidad
    np.random.seed(semilla)
    
    # Crear fechas mensuales
    fecha_inicio = datetime(2019, 1, 1)
    fechas = [fecha_inicio + timedelta(days=30*i) for i in range(n_meses)]
    
    # ============================================================================
    # GENERAR VARIABLES MACROECONÓMICAS (Variables Independientes)
    # ============================================================================
    
    # 1. Tasa de Desempleo (%)
    # Simulamos una tendencia con variabilidad y algunos shocks
    tendencia_desempleo = np.linspace(5.0, 7.5, n_meses)  # Tendencia creciente
    ciclo_desempleo = 1.5 * np.sin(2 * np.pi * np.arange(n_meses) / 12)  # Ciclo anual
    ruido_desempleo = np.random.normal(0, 0.3, n_meses)
    desempleo = tendencia_desempleo + ciclo_desempleo + ruido_desempleo
    desempleo = np.clip(desempleo, 3.0, 12.0)  # Limitar entre 3% y 12%
    
    # 2. Crecimiento del PIB (% anual)
    # Relación inversa con desempleo (ley de Okun)
    pib_base = 3.0
    pib = pib_base - 0.5 * (desempleo - 6.0) + np.random.normal(0, 0.5, n_meses)
    pib = np.clip(pib, -2.0, 6.0)  # Limitar entre -2% y 6%
    
    # 3. Tasa de Interés de Referencia (%)
    # Relacionada con inflación y crecimiento
    inflacion_base = 2.5 + 0.3 * (desempleo - 6.0)  # Curva de Phillips simplificada
    inflacion = inflacion_base + np.random.normal(0, 0.4, n_meses)
    inflacion = np.clip(inflacion, 0.5, 8.0)
    
    tasa_interes = 2.0 + 1.5 * inflacion + 0.3 * (pib - 3.0) + np.random.normal(0, 0.3, n_meses)
    tasa_interes = np.clip(tasa_interes, 0.5, 10.0)
    
    # 4. Índice de Confianza Empresarial (0-100)
    # Relacionado inversamente con desempleo y directamente con crecimiento
    confianza_base = 50 - 3 * (desempleo - 6.0) + 2 * pib
    confianza = confianza_base + np.random.normal(0, 3, n_meses)
    confianza = np.clip(confianza, 20, 80)
    
    # 5. Volatilidad del Mercado (VIX-like, 0-100)
    # Mayor en períodos de incertidumbre
    volatilidad_base = 15 + 2 * np.abs(pib - 3.0) + 1.5 * (desempleo - 6.0)
    volatilidad = volatilidad_base + np.random.normal(0, 2, n_meses)
    volatilidad = np.clip(volatilidad, 10, 50)
    
    # 6. Tipo de Cambio (índice, base 100)
    # Se deprecia con mayor inflación y menor crecimiento
    tipo_cambio_base = 100.0
    depreciacion = 0.5 * (inflacion - 2.5) - 0.3 * (pib - 3.0) + np.random.normal(0, 0.8, n_meses)
    tipo_cambio = tipo_cambio_base + np.cumsum(depreciacion)
    tipo_cambio = np.clip(tipo_cambio, 80, 130)  # Variación razonable
    
    # 7. Déficit Fiscal (% del PIB)
    # Aumenta en recesiones y disminuye en crecimiento
    deficit_base = 3.0 - 0.4 * (pib - 3.0) + 0.2 * (desempleo - 6.0)
    deficit = deficit_base + np.random.normal(0, 0.5, n_meses)
    deficit = np.clip(deficit, -1.0, 8.0)  # Puede haber superávit o déficit
    
    # 8. Crédito Bancario al Sector Privado (% del PIB)
    # Relacionado con crecimiento y confianza
    credito_base = 50.0 + 2 * pib + 0.5 * (confianza - 50.0)
    credito = credito_base + np.random.normal(0, 2, n_meses)
    credito = np.clip(credito, 30, 80)
    
    # 9. Índice de Producción Industrial (base 100)
    # Relacionado con crecimiento del PIB
    produccion_base = 100.0
    crecimiento_produccion = 0.8 * pib + np.random.normal(0, 0.5, n_meses)
    produccion = produccion_base + np.cumsum(crecimiento_produccion)
    produccion = np.clip(produccion, 85, 120)
    
    # 10. Balanza Comercial (% del PIB)
    # Mejora con crecimiento y tipo de cambio competitivo
    balanza_base = 0.5 - 0.3 * (tipo_cambio - 100) / 10 + 0.2 * pib
    balanza = balanza_base + np.random.normal(0, 0.8, n_meses)
    balanza = np.clip(balanza, -5.0, 5.0)
    
    # 11. Spread de Crédito (diferencia entre tasa corporativa y tasa libre de riesgo, %)
    # Aumenta con incertidumbre y riesgo
    spread_base = 2.0 + 0.5 * (volatilidad - 20) / 10 + 0.3 * (desempleo - 6.0)
    spread = spread_base + np.random.normal(0, 0.3, n_meses)
    spread = np.clip(spread, 0.5, 6.0)
    
    # 12. Reservas Internacionales (miles de millones USD)
    # Relacionadas con balanza comercial y tipo de cambio
    reservas_base = 50.0
    cambio_reservas = 0.5 * balanza - 0.2 * (tipo_cambio - 100) / 10 + np.random.normal(0, 0.5, n_meses)
    reservas = reservas_base + np.cumsum(cambio_reservas)
    reservas = np.clip(reservas, 20, 100)
    
    # 13. Índice de Precios al Consumidor (IPC, base 100)
    # Relacionado con inflación
    ipc_base = 100.0
    crecimiento_ipc = inflacion / 12  # Inflación mensual aproximada
    ipc = ipc_base * np.exp(np.cumsum(crecimiento_ipc / 100))
    ipc = np.clip(ipc, 95, 140)
    
    # 14. Tasa de Ahorro Nacional (% del PIB)
    # Relacionada con confianza y crecimiento
    ahorro_base = 20.0 + 0.5 * (confianza - 50.0) / 10 - 0.3 * (tasa_interes - 4.0)
    ahorro = ahorro_base + np.random.normal(0, 1.5, n_meses)
    ahorro = np.clip(ahorro, 10, 35)
    
    # ============================================================================
    # GENERAR PD CUANTITATIVA (Variable Dependiente)
    # ============================================================================
    
    # La PD depende de las variables macroeconómicas
    # Relación esperada:
    # - PD aumenta con desempleo
    # - PD disminuye con crecimiento del PIB
    # - PD aumenta con tasa de interés (mayor costo de financiamiento)
    # - PD aumenta con volatilidad
    # - PD disminuye con confianza empresarial
    
    # PD base (en porcentaje, luego convertimos a decimal)
    # La PD depende de múltiples variables macroeconómicas
    pd_porcentaje = (
        2.0  # PD base
        + 0.4 * (desempleo - 6.0)  # +0.4% por cada punto de desempleo sobre 6%
        - 0.3 * (pib - 3.0)  # -0.3% por cada punto de crecimiento sobre 3%
        + 0.2 * (tasa_interes - 4.0)  # +0.2% por cada punto de interés sobre 4%
        + 0.15 * (volatilidad - 20.0)  # +0.15% por cada punto de volatilidad sobre 20
        - 0.1 * (confianza - 50.0)  # -0.1% por cada punto de confianza sobre 50
        + 0.08 * (tipo_cambio - 100.0) / 10  # +0.08% por cada 10 puntos de depreciación
        + 0.12 * (deficit - 3.0)  # +0.12% por cada punto de déficit sobre 3%
        - 0.05 * (credito - 50.0) / 10  # -0.05% por cada 10 puntos de crédito sobre 50%
        - 0.06 * (produccion - 100.0) / 10  # -0.06% por cada 10 puntos de producción sobre 100
        - 0.1 * balanza  # -0.1% por cada punto de balanza comercial positiva
        + 0.15 * (spread - 2.0)  # +0.15% por cada punto de spread sobre 2%
        - 0.02 * (reservas - 50.0) / 10  # -0.02% por cada 10 puntos de reservas sobre 50
        + 0.05 * (inflacion - 2.5)  # +0.05% por cada punto de inflación sobre 2.5%
        - 0.04 * (ahorro - 20.0) / 10  # -0.04% por cada 10 puntos de ahorro sobre 20%
        + np.random.normal(0, 0.3, n_meses)  # Ruido aleatorio
    )
    
    # Asegurar que PD esté entre 0% y 15% (límite realista)
    pd_porcentaje = np.clip(pd_porcentaje, 0.1, 15.0)
    
    # Convertir a decimal (0-1)
    pd_decimal = pd_porcentaje / 100.0
    
    # Crear DataFrame con todas las variables
    datos_pd = pd.DataFrame({
        'fecha': fechas,
        'pd_porcentaje': pd_porcentaje,
        'pd_decimal': pd_decimal,
        # Variables macroeconómicas originales
        'desempleo': desempleo,
        'pib_crecimiento': pib,
        'tasa_interes': tasa_interes,
        'inflacion': inflacion,
        'confianza_empresarial': confianza,
        'volatilidad_mercado': volatilidad,
        # Variables macroeconómicas adicionales
        'tipo_cambio': tipo_cambio,
        'deficit_fiscal': deficit,
        'credito_privado': credito,
        'produccion_industrial': produccion,
        'balanza_comercial': balanza,
        'spread_credito': spread,
        'reservas_internacionales': reservas,
        'ipc': ipc,
        'tasa_ahorro': ahorro
    })
    
    # Guardar en CSV si se solicita
    if guardar:
        if ruta_archivo is None:
            # Ruta por defecto: misma carpeta que el script
            directorio_actual = os.path.dirname(os.path.abspath(__file__))
            ruta_archivo = os.path.join(directorio_actual, 'datos_pd_historico.csv')
        
        datos_pd.to_csv(ruta_archivo, index=False, encoding='utf-8')
        print(f"[OK] Base de datos guardada exitosamente en: {ruta_archivo}")
        print(f"  - Numero de observaciones: {len(datos_pd)}")
        print(f"  - Periodo: {fechas[0].strftime('%Y-%m-%d')} a {fechas[-1].strftime('%Y-%m-%d')}")
        print(f"  - Variables: {len(datos_pd.columns)} columnas")
    
    return datos_pd


if __name__ == "__main__":
    # Generar y guardar los datos
    print("=" * 80)
    print("GENERADOR DE BASE DE DATOS: PROBABILIDAD DE INCUMPLIMIENTO (PD)")
    print("=" * 80)
    print("\nGenerando datos históricos...")
    
    datos = generar_datos_pd(n_meses=60, semilla=42, guardar=True)
    
    print("\n" + "=" * 80)
    print("RESUMEN DE LA BASE DE DATOS GENERADA")
    print("=" * 80)
    print("\nPrimeras 5 observaciones:")
    print(datos.head().to_string(index=False))
    print("\nÚltimas 5 observaciones:")
    print(datos.tail().to_string(index=False))
    print("\nEstadísticas descriptivas:")
    print(datos.describe().round(2))
    print("\n" + "=" * 80)
    print("[OK] Proceso completado exitosamente")
    print("=" * 80)
