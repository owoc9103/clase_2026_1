"""
Script para actualizar el notebook del caso práctico con las nuevas variables macroeconómicas
"""

import json
import os

# Ruta del notebook
notebook_path = 'Ejemplo_Practico_PD_Cuantitativa.ipynb'

# Leer el notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Variables macroeconómicas completas
variables_completas = [
    'desempleo', 'pib_crecimiento', 'tasa_interes', 'inflacion',
    'confianza_empresarial', 'volatilidad_mercado', 'tipo_cambio',
    'deficit_fiscal', 'credito_privado', 'produccion_industrial',
    'balanza_comercial', 'spread_credito', 'reservas_internacionales',
    'ipc', 'tasa_ahorro'
]

# Diccionario de interpretaciones
interpretaciones = {
    'desempleo': 'Cambio en PD por cada 1% de aumento en desempleo',
    'pib_crecimiento': 'Cambio en PD por cada 1% de aumento en crecimiento del PIB',
    'tasa_interes': 'Cambio en PD por cada 1% de aumento en tasa de interés',
    'inflacion': 'Cambio en PD por cada 1% de aumento en inflación',
    'confianza_empresarial': 'Cambio en PD por cada punto de aumento en confianza empresarial',
    'volatilidad_mercado': 'Cambio en PD por cada punto de aumento en volatilidad',
    'tipo_cambio': 'Cambio en PD por cada 10 puntos de depreciación del tipo de cambio',
    'deficit_fiscal': 'Cambio en PD por cada 1% de aumento en déficit fiscal (% PIB)',
    'credito_privado': 'Cambio en PD por cada 10 puntos de aumento en crédito privado (% PIB)',
    'produccion_industrial': 'Cambio en PD por cada 10 puntos de aumento en producción industrial',
    'balanza_comercial': 'Cambio en PD por cada 1% de mejora en balanza comercial (% PIB)',
    'spread_credito': 'Cambio en PD por cada 1% de aumento en spread de crédito',
    'reservas_internacionales': 'Cambio en PD por cada 10 mil millones de aumento en reservas',
    'ipc': 'Cambio en PD por cada 10 puntos de aumento en IPC',
    'tasa_ahorro': 'Cambio en PD por cada 10 puntos de aumento en tasa de ahorro (% PIB)'
}

# Buscar y actualizar celdas específicas
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        
        # Actualizar código de carga de CSV
        if 'Cargar la base de datos' in source and 'read_csv' in source:
            nuevo_codigo = '''# Cargar la base de datos
# El archivo 'datos_pd_historico.csv' debe estar en la misma carpeta que este notebook

import os

# Intentar diferentes rutas posibles para encontrar el archivo CSV
rutas_posibles = [
    'datos_pd_historico.csv',  # Ruta relativa (misma carpeta que el notebook)
    os.path.join(os.path.dirname(os.path.abspath('')), 'datos_pd_historico.csv'),  # Directorio actual
    os.path.join('..', 'datos_pd_historico.csv'),  # Carpeta padre
    os.path.join(os.getcwd(), 'datos_pd_historico.csv'),  # Directorio de trabajo actual
]

ruta_datos = None
for ruta in rutas_posibles:
    if os.path.exists(ruta):
        ruta_datos = ruta
        break

# Si no se encuentra, usar la ruta por defecto (misma carpeta)
if ruta_datos is None:
    ruta_datos = 'datos_pd_historico.csv'

try:
    # Leer el CSV con encoding UTF-8 para evitar problemas con caracteres especiales
    datos_pd = pd.read_csv(ruta_datos, parse_dates=['fecha'], encoding='utf-8')
    print("=" * 80)
    print("BASE DE DATOS CARGADA EXITOSAMENTE")
    print("=" * 80)
    print(f"\\nArchivo: {os.path.abspath(ruta_datos)}")
    print(f"Número de observaciones: {len(datos_pd)}")
    print(f"Período: {datos_pd['fecha'].min().strftime('%Y-%m-%d')} a {datos_pd['fecha'].max().strftime('%Y-%m-%d')}")
    print(f"\\nVariables en la base de datos ({len(datos_pd.columns)} columnas):")
    for i, col in enumerate(datos_pd.columns, 1):
        print(f"  {i:2d}. {col}")
    print(f"\\n✓ Base de datos lista para análisis")
except FileNotFoundError:
    print("=" * 80)
    print("ERROR: No se encontró el archivo de datos")
    print("=" * 80)
    print(f"\\nBuscado en las siguientes rutas:")
    for ruta in rutas_posibles:
        print(f"  - {os.path.abspath(ruta)}")
    print("\\nPor favor, ejecuta primero el script 'generar_datos_pd.py' para crear la base de datos.")
    print("\\nPuedes ejecutarlo desde la terminal con:")
    print("  python generar_datos_pd.py")
    print("\\nO desde Python/Jupyter:")
    print("  exec(open('generar_datos_pd.py').read())")
except Exception as e:
    print("=" * 80)
    print("ERROR al cargar el archivo")
    print("=" * 80)
    print(f"\\nError: {str(e)}")
    print(f"\\nRuta intentada: {os.path.abspath(ruta_datos)}")
    print("\\nPor favor, verifica que el archivo existe y tiene el formato correcto.")
'''
            cell['source'] = nuevo_codigo.split('\n')
        
        # Actualizar matriz de correlación
        elif 'Matriz de correlación' in source and 'variables_corr' in source:
            nuevo_codigo = '''# Matriz de correlación con todas las variables macroeconómicas
# Excluir fecha y pd_porcentaje (usamos pd_decimal)
variables_corr = [col for col in datos_pd.columns if col not in ['fecha', 'pd_porcentaje']]
corr_matrix = datos_pd[variables_corr].corr()

plt.figure(figsize=(16, 14))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, 
            linewidths=0.5, cbar_kws={"shrink": 0.8}, fmt='.2f', 
            annot_kws={'size': 8})
plt.title('Matriz de Correlación: PD vs Variables Macroeconómicas', 
          fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

print("\\nCorrelaciones con PD (de mayor a menor):")
correlaciones_pd = corr_matrix['pd_decimal'].sort_values(ascending=False)
print(correlaciones_pd[1:])  # Excluir correlación consigo misma
'''
            cell['source'] = nuevo_codigo.split('\n')
        
        # Actualizar variables independientes
        elif 'variables_independientes = [' in source and 'desempleo' in source:
            nuevo_codigo = f'''# Paso 3: Organizar los datos
# Incluir todas las variables macroeconómicas disponibles (excluir fecha y PD)
variables_independientes = {variables_completas}

# Verificar que todas las variables existen en el DataFrame
variables_disponibles = [var for var in variables_independientes if var in datos_pd.columns]
if len(variables_disponibles) != len(variables_independientes):
    faltantes = set(variables_independientes) - set(variables_disponibles)
    print(f"⚠ Advertencia: Las siguientes variables no se encontraron: {{faltantes}}")
    variables_independientes = variables_disponibles

X = datos_pd[variables_independientes].values  # Matriz 2D
y = datos_pd['pd_decimal'].values  # Vector 1D

# Dividir en entrenamiento (80%) y prueba (20%)
# Usamos shuffle=False para mantener el orden temporal
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False, random_state=42
)

print("=" * 80)
print("PASO 3: ORGANIZAR LOS DATOS")
print("=" * 80)
print(f"\\nForma de los datos:")
print(f"  X (características): {{X.shape}} - {{X.shape[0]}} observaciones, {{X.shape[1]}} variables")
print(f"  y (objetivo): {{y.shape}} - {{len(y)}} observaciones")
print(f"\\nDivisión entrenamiento/prueba:")
print(f"  Entrenamiento: {{X_train.shape[0]}} observaciones ({{X_train.shape[0]/len(X)*100:.1f}}%)")
print(f"  Prueba: {{X_test.shape[0]}} observaciones ({{X_test.shape[0]/len(X)*100:.1f}}%)")
print(f"\\nVariables independientes incluidas:")
for i, var in enumerate(variables_independientes, 1):
    print(f"  {{i:2d}}. {{var}}")
'''
            cell['source'] = nuevo_codigo.split('\n')
        
        # Actualizar interpretaciones de coeficientes
        elif 'Coeficientes de regresión' in source and 'Interpretación' in source:
            interpretaciones_lista = [interpretaciones.get(var, f'Cambio en PD por unidad de {var}') 
                                     for var in variables_completas]
            nuevo_codigo = f'''print("\\n  Coeficientes de regresión:")
interpretaciones_dict = {interpretaciones}
coeficientes_df = pd.DataFrame({{
    'Variable': variables_independientes,
    'Coeficiente (β)': modelo_pd.coef_,
    'Interpretación': [interpretaciones_dict.get(var, f'Cambio en PD por unidad de {{var}}') 
                       for var in variables_independientes]
}})
print(coeficientes_df.to_string(index=False))
'''
            # Buscar la parte específica y reemplazarla
            lines = source.split('\n')
            new_lines = []
            skip_until_end = False
            for j, line in enumerate(lines):
                if 'Interpretación' in line and '[' in line:
                    skip_until_end = True
                    new_lines.append('interpretaciones_dict = ' + str(interpretaciones))
                    new_lines.append('coeficientes_df = pd.DataFrame({')
                    new_lines.append("    'Variable': variables_independientes,")
                    new_lines.append("    'Coeficiente (β)': modelo_pd.coef_,")
                    new_lines.append("    'Interpretación': [interpretaciones_dict.get(var, f'Cambio en PD por unidad de {var}')")
                    new_lines.append("                       for var in variables_independientes]")
                    new_lines.append('})')
                    continue
                if skip_until_end and '])' in line:
                    skip_until_end = False
                    continue
                if not skip_until_end:
                    new_lines.append(line)
            cell['source'] = new_lines
        
        # Actualizar escenarios
        elif 'Escenario Base' in source and 'desempleo' in source:
            nuevo_codigo = '''# Definir escenarios con todas las variables macroeconómicas
escenarios = {
    'Escenario Base': {
        'desempleo': 6.0, 'pib_crecimiento': 3.0, 'tasa_interes': 4.0, 'inflacion': 2.5,
        'confianza_empresarial': 50.0, 'volatilidad_mercado': 20.0, 'tipo_cambio': 100.0,
        'deficit_fiscal': 3.0, 'credito_privado': 50.0, 'produccion_industrial': 100.0,
        'balanza_comercial': 0.5, 'spread_credito': 2.0, 'reservas_internacionales': 50.0,
        'ipc': 110.0, 'tasa_ahorro': 20.0
    },
    'Escenario Optimista': {
        'desempleo': 4.5, 'pib_crecimiento': 4.5, 'tasa_interes': 3.0, 'inflacion': 2.0,
        'confianza_empresarial': 65.0, 'volatilidad_mercado': 15.0, 'tipo_cambio': 95.0,
        'deficit_fiscal': 1.5, 'credito_privado': 60.0, 'produccion_industrial': 110.0,
        'balanza_comercial': 2.0, 'spread_credito': 1.5, 'reservas_internacionales': 70.0,
        'ipc': 105.0, 'tasa_ahorro': 25.0
    },
    'Escenario Pesimista': {
        'desempleo': 8.5, 'pib_crecimiento': 1.0, 'tasa_interes': 6.0, 'inflacion': 4.0,
        'confianza_empresarial': 35.0, 'volatilidad_mercado': 35.0, 'tipo_cambio': 110.0,
        'deficit_fiscal': 5.0, 'credito_privado': 40.0, 'produccion_industrial': 90.0,
        'balanza_comercial': -2.0, 'spread_credito': 4.0, 'reservas_internacionales': 35.0,
        'ipc': 120.0, 'tasa_ahorro': 15.0
    },
    'Escenario Crisis': {
        'desempleo': 10.0, 'pib_crecimiento': -1.0, 'tasa_interes': 7.0, 'inflacion': 5.0,
        'confianza_empresarial': 25.0, 'volatilidad_mercado': 45.0, 'tipo_cambio': 120.0,
        'deficit_fiscal': 7.0, 'credito_privado': 35.0, 'produccion_industrial': 85.0,
        'balanza_comercial': -4.0, 'spread_credito': 5.5, 'reservas_internacionales': 25.0,
        'ipc': 130.0, 'tasa_ahorro': 12.0
    }
}
'''
            cell['source'] = nuevo_codigo.split('\n')

# Guardar el notebook actualizado
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)

print(f"✓ Notebook {notebook_path} actualizado exitosamente")
