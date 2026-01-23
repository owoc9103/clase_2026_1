# Machine Learning en Finanzas

Curso de Machine Learning aplicado a Finanzas basado en el libro "Machine Learning and Data Science Blueprints for Finance" de Hariom Tatsat, Sahil Puri y Brad Lookabaugh.

## 📁 Estructura del Proyecto

```
ML_Finanzas/
├── Clases/                    # Material de clases
│   └── Clase 1/              # Clase 1 - Introducción
│       ├── Clase_1.md        # Presentación en formato Marp
│       └── Clase_1_Slidev.md # Presentación en formato Slidev
├── imagenes/                  # Imágenes y recursos visuales
│   ├── *.jpg, *.gif         # Imágenes de las presentaciones
│   ├── descargar_imagenes.py
│   └── ejemplo_urls_imagenes.py
├── Libros/                    # Material bibliográfico
│   └── Machine Learning and Data Science Blueprints for Finance.pdf
├── package.json              # Dependencias Node.js (Slidev) - CENTRALIZADO
├── vite.config.ts            # Configuración de Vite - CENTRALIZADO
├── requirements.txt          # Dependencias Python
├── .gitignore               # Configuración Git unificada
└── README.md                # Este archivo
```

## 🚀 Inicio Rápido

### Prerrequisitos

- **Python 3.8+** para análisis de datos y ML
- **Node.js 16+** para presentaciones Slidev
- **npm/pnpm/yarn** para gestionar dependencias de Slidev

### Instalación

#### 1. Dependencias Python

Instala las dependencias de Python para el análisis de datos:

```bash
pip install -r requirements.txt
```

#### 2. Dependencias Node.js (para Slidev)

Instala las dependencias de Slidev desde la raíz del proyecto:

```bash
npm install
```

o con pnpm:

```bash
pnpm install
```

o con yarn:

```bash
yarn install
```

## 📊 Presentaciones

El curso incluye presentaciones en dos formatos:

### Marp (Clase_1.md)

Presentaciones en formato Marp, compatibles con VS Code y otras herramientas.

- **Ventaja**: Simple, basado en Markdown puro
- **Uso**: Abre el archivo `.md` en un editor con soporte Marp (extensión Marp para VS Code)

### Slidev (Clase_1_Slidev.md) ⭐ Recomendado

Presentaciones interactivas con Slidev, ideales para desarrolladores.

- **Ventaja**: Interactivo, soporte para código, componentes Vue, animaciones
- **Uso**: 
  ```bash
  # Desde la raíz del proyecto
  npm run dev:1
  ```
  Abre `http://localhost:3030` en tu navegador

## 🎮 Comandos Disponibles

Todos los comandos se ejecutan desde la **raíz del proyecto**:

### Desarrollo

```bash
# Ejecutar Clase 1 en modo desarrollo
npm run dev:1

# Ejecutar cualquier archivo Slidev (especifica la ruta)
npm run dev
```

### Construcción

```bash
# Construir Clase 1 como SPA
npm run build:1

# Construir cualquier archivo
npm run build
```

### Exportación

```bash
# Exportar Clase 1 como HTML estático
npm run export:1

# Exportar Clase 1 como PDF
npm run export-pdf:1

# Exportar Clase 1 como imágenes PNG
npm run export-png:1
```

## 📚 Contenido del Curso

### Clase 1: Introducción
- Panorama actual del ML en finanzas
- Tres pilares fundamentales
- Tipos de Machine Learning
- Aplicaciones en finanzas
- Desafíos y consideraciones

## 🛠️ Herramientas Utilizadas

### Python
- **Pandas & NumPy**: Manipulación de datos
- **Scikit-learn**: Machine Learning tradicional
- **Matplotlib & Seaborn**: Visualización
- **YFinance**: Datos financieros
- **Jupyter**: Notebooks interactivos

### Presentaciones
- **Marp**: Presentaciones basadas en Markdown (formato alternativo)
- **Slidev**: Presentaciones interactivas para desarrolladores (formato principal) ⭐

## 🎨 Características de Slidev

Las presentaciones en Slidev incluyen:

- ✨ **Sintaxis Markdown extendida** - Escribe slides fácilmente
- 🎨 **Temas personalizables** - Usa el tema Seriph incluido
- 💻 **Soporte de código** - Syntax highlighting con Shiki
- 🎭 **Componentes Vue** - Crea slides interactivas
- ⚡ **Hot Module Replacement** - Cambios instantáneos
- 📤 **Exportación múltiple** - PDF, PNG, HTML, SPA

## 📖 Recursos

- **Libro Principal**: Machine Learning and Data Science Blueprints for Finance
  - Autores: Hariom Tatsat, Sahil Puri, Brad Lookabaugh
  - Editorial: O'Reilly Media

- **Documentación**:
  - [Slidev](https://sli.dev) - Documentación oficial
  - [Slidev - Guía de Sintaxis](https://sli.dev/guide/syntax.html)
  - [Slidev - Galería de Temas](https://sli.dev/themes/gallery.html)
  - [Marp](https://marp.app)
  - [Pandas](https://pandas.pydata.org)
  - [Scikit-learn](https://scikit-learn.org)

## 💡 Tips para Slidev

- Usa `Space` o las flechas para navegar entre slides
- Presiona `f` para modo pantalla completa
- Presiona `o` para ver el overview de todas las slides
- Presiona `d` para activar el modo dibujo
- Presiona `g` para ir a una slide específica
- Presiona `?` para ver todos los atajos de teclado

## 📝 Notas

- ✅ **Configuración centralizada**: Un solo `package.json` y `vite.config.ts` en la raíz
- ✅ **Git unificado**: Un solo `.gitignore` para todo el proyecto
- ✅ **Rutas relativas**: Las imágenes se referencian con `../imagenes/`
- ✅ **Estructura escalable**: Fácil agregar nuevas clases siguiendo el mismo patrón

## 🔧 Agregar una Nueva Clase

Para agregar una nueva clase:

1. Crea la carpeta `Clases/Clase X/`
2. Crea `Clase_X_Slidev.md` con el contenido
3. Agrega scripts en `package.json`:
   ```json
   "dev:X": "slidev Clases/Clase X/Clase_X_Slidev.md",
   "build:X": "slidev build Clases/Clase X/Clase_X_Slidev.md",
   "export:X": "slidev export Clases/Clase X/Clase_X_Slidev.md"
   ```

## 🤝 Contribuciones

Este es un proyecto educativo. Siéntete libre de sugerir mejoras o correcciones.

## 📄 Licencia

Material educativo para uso académico.
