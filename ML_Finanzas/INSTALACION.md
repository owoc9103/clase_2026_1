# 📦 Guía de Instalación - ML Finanzas

Esta guía te ayudará a instalar todas las dependencias necesarias para que el proyecto y las presentaciones funcionen correctamente.

## 🔧 Prerrequisitos

### 1. Python 3.8 o superior

**Verificar instalación:**
```bash
python --version
# o
python3 --version
```

**Si no tienes Python:**
- Descarga desde: https://www.python.org/downloads/
- **Importante**: Marca la opción "Add Python to PATH" durante la instalación

### 2. Node.js 16 o superior (para Slidev)

**Verificar instalación:**
```bash
node --version
npm --version
```

**Si no tienes Node.js:**
- Descarga desde: https://nodejs.org/
- Instala la versión LTS (recomendada)

## 📥 Instalación de Dependencias

### Paso 1: Dependencias Python

Abre una terminal en la raíz del proyecto (`ML_Finanzas`) y ejecuta:

```bash
# Opción 1: Instalación directa
pip install -r requirements.txt

# Opción 2: Usando entorno virtual (RECOMENDADO)
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

**Si tienes problemas:**

```bash
# Actualizar pip primero
python -m pip install --upgrade pip

# Instalar dependencias básicas primero
pip install numpy pandas scikit-learn

# Luego instalar el resto
pip install -r requirements.txt
```

### Paso 2: Dependencias Node.js (Slidev)

En la misma terminal (o una nueva), desde la raíz del proyecto:

```bash
# Instalar dependencias de Slidev
npm install

# O si prefieres usar pnpm (más rápido)
npm install -g pnpm
pnpm install

# O con yarn
yarn install
```

## ✅ Verificar Instalación

### Verificar Python

```bash
python -c "import pandas, numpy, sklearn; print('✅ Python OK')"
```

### Verificar Node.js/Slidev

```bash
npm list @slidev/cli
```

## 🚀 Ejecutar el Proyecto

### Ejecutar Presentaciones Slidev

```bash
# Desde la raíz del proyecto
npm run dev:1

# Luego abre: http://localhost:3030
```

### Ejecutar Scripts Python

```bash
# Asegúrate de estar en el entorno virtual si lo usas
cd imagenes
python descargar_imagenes.py
```

## 🐛 Solución de Problemas

### Error: "pip no se reconoce"

**Solución:**
```bash
python -m pip install -r requirements.txt
```

### Error: "npm no se reconoce"

**Solución:**
1. Reinstala Node.js desde https://nodejs.org/
2. Asegúrate de marcar "Add to PATH" durante la instalación
3. Reinicia la terminal después de instalar

### Error al instalar paquetes Python en Windows

**Solución:**
Algunos paquetes requieren compiladores C++. Instala:
- **Visual Studio Build Tools**: https://visualstudio.microsoft.com/downloads/
- O usa versiones precompiladas: `pip install --only-binary :all: nombre_paquete`

### Error: "ModuleNotFoundError"

**Solución:**
```bash
# Asegúrate de estar en el entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error al ejecutar Slidev

**Solución:**
```bash
# Limpia node_modules y reinstala
rm -rf node_modules package-lock.json
npm install

# O con pnpm
rm -rf node_modules pnpm-lock.yaml
pnpm install
```

## 📋 Dependencias Principales

### Python
- **pandas**: Manipulación de datos
- **numpy**: Cálculos numéricos
- **scikit-learn**: Machine Learning
- **matplotlib/seaborn**: Visualización
- **yfinance**: Datos financieros
- **jupyter**: Notebooks interactivos

### Node.js
- **@slidev/cli**: CLI de Slidev
- **@slidev/theme-seriph**: Tema Seriph
- **@slidev/theme-default**: Tema por defecto

## 💡 Tips

1. **Usa entornos virtuales** para Python para evitar conflictos
2. **Actualiza pip** regularmente: `python -m pip install --upgrade pip`
3. **Mantén Node.js actualizado** para mejor compatibilidad
4. Si trabajas en múltiples proyectos, considera usar `conda` o `poetry` para Python

## 📚 Recursos Adicionales

- [Documentación de Python](https://docs.python.org/)
- [Documentación de Node.js](https://nodejs.org/docs/)
- [Documentación de Slidev](https://sli.dev)
- [Guía de pip](https://pip.pypa.io/)

---

¿Tienes problemas? Revisa la sección de "Solución de Problemas" o consulta la documentación oficial de cada herramienta.
