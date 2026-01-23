---
theme: default
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Machine Learning en Finanzas: El Panorama
  Clase 1 - Introducción
  
  Basado en: Machine Learning and Data Science Blueprints for Finance
drawings:
  persist: false
transition: slide-left
title: Machine Learning en Finanzas
mdc: true
colorSchema: dark
---

# Machine Learning en Finanzas por Walduin
## El Panorama

<div class="pt-12">
  <span class="text-lg opacity-70">Clase 1 - Introducción</span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://sli.dev" target="_blank" alt="Slidev" title="Slidev"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
  </a>
</div>

<div class="abs-bl m-6 text-sm opacity-50">
  <span>Basado en: Machine Learning and Data Science Blueprints for Finance</span><br>
  <span>Hariom Tatsat, Sahil Puri, Brad Lookabaugh</span>
</div>

<!-- Component usage:
     this will be invisible until you press "next" -->
<v-click> Hello World! </v-click>

<!-- Directive usage:
     this will be invisible until you press "next" the second time -->
<div v-click class="text-xl"> Hey! </div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/portada_ml_finanzas.jpg
---

# Objetivos de la Clase

<div class="text-left">

- Comprender el estado actual del Machine Learning en finanzas
- Identificar los tres pilares fundamentales para el éxito de ML en finanzas
- Conocer los diferentes tipos de Machine Learning aplicables
- Entender el panorama futuro de la industria

</div>

<div class="mt-8">
  <img src="../ML_Finanzas/imagenes/objetivos_ml.gif" class="w-64 mx-auto rounded-lg shadow-lg" />
</div>

<!--
**Notas del Presentador:**

- Bienvenida a la clase
- Presentar el curso y su estructura
- Explicar que estos objetivos guiarán toda la clase
- Mencionar que al final haremos un resumen para verificar que se cumplieron
-->

---
layout: image-right
image: ../ML_Finanzas/imagenes/industria_financiera.jpg
---

# El Panorama Actual

## Adopción Rápida en la Industria Financiera

<div class="text-left space-y-4">

- **Hedge Funds**: Inversión masiva en tecnologías de ML
- **Bancos de Inversión**: Implementación de sistemas inteligentes
- **Bancos Minoristas**: Automatización y personalización
- **Firmas FinTech**: Innovación disruptiva

</div>

---
layout: two-cols
---

# Factores de Crecimiento

## ¿Por qué ahora?

::left::

<div class="space-y-6 text-left">

### 1. Disponibilidad de Datos
- Volúmenes masivos de información financiera
- Datos estructurados y no estructurados
- Acceso a datos en tiempo real

### 2. Poder Computacional Asequible
- Cloud computing
- Procesamiento distribuido
- GPUs y TPUs

</div>

::right::

<div class="space-y-4">
  <img src="../ML_Finanzas/imagenes/big_data_finanzas.jpg" class="w-full rounded-lg shadow-lg" />
  <img src="../ML_Finanzas/imagenes/cloud_computing.gif" class="w-full rounded-lg shadow-lg" />
</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/tres_pilares_ml.jpg
---

# Los Tres Pilares Fundamentales

<div class="text-left space-y-6">

Para el éxito de Machine Learning en finanzas se requieren:

### 1. 🏗️ Infraestructura Eficiente
- Arquitectura escalable
- Procesamiento de datos en tiempo real
- Almacenamiento robusto

### 2. 🛠️ Selección Correcta de Herramientas
- Stack tecnológico apropiado
- Librerías y frameworks adecuados
- Ecosistema Python para finanzas

### 3. 🧠 Aplicación Apropiada de Algoritmos
- Elección del modelo correcto
- Entendimiento del problema de negocio
- Validación y evaluación rigurosa

</div>

<!--
**Notas del Presentador:**

- Estos tres pilares son FUNDAMENTALES - sin uno, el proyecto falla
- Analogía: Como construir una casa - necesitas cimientos, herramientas y conocimiento
- Ejemplos:
  1. Infraestructura: AWS, Google Cloud, sistemas distribuidos
  2. Herramientas: Python, TensorFlow, pero también bases de datos, APIs
  3. Algoritmos: No usar deep learning para todo - elegir el modelo correcto
- Énfasis: El éxito requiere los TRES, no solo uno
-->

---
layout: default
---

# Tipos de Machine Learning

<div class="grid grid-cols-3 gap-6 mt-8">

<div class="border rounded-lg p-4">

## 📊 Aprendizaje Supervisado

<img src="../ML_Finanzas/imagenes/supervised_learning.jpg" class="w-full rounded-lg mb-4" />

- **Clasificación**: Detección de fraude, scoring crediticio
- **Regresión**: Predicción de precios, valoración de activos

</div>

<div class="border rounded-lg p-4">

## 🔍 Aprendizaje No Supervisado

<img src="../ML_Finanzas/imagenes/unsupervised_learning.jpg" class="w-full rounded-lg mb-4" />

- **Clustering**: Segmentación de clientes
- **Detección de anomalías**: Identificación de transacciones sospechosas

</div>

<div class="border rounded-lg p-4">

## 🎯 Aprendizaje por Refuerzo

<img src="../ML_Finanzas/imagenes/reinforcement_learning.gif" class="w-full rounded-lg mb-4" />

- **Trading algorítmico**: Optimización de estrategias
- **Robo-advisors**: Gestión automatizada de portafolios

</div>

</div>

---
layout: default
---

# Aplicaciones en Finanzas

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="border rounded-lg p-4">

## 📈 Trading y Mercados

<img src="../ML_Finanzas/imagenes/trading_algoritmico.jpg" class="w-full rounded-lg mb-3" />

- Estrategias de trading algorítmico
- Predicción de movimientos de precios
- Arbitraje y market making

</div>

<div class="border rounded-lg p-4">

## ⚠️ Gestión de Riesgos

<img src="../ML_Finanzas/imagenes/gestion_riesgos.jpg" class="w-full rounded-lg mb-3" />

- Modelos de riesgo crediticio
- Value at Risk (VaR)
- Stress testing

</div>

<div class="border rounded-lg p-4">

## 🤖 Servicios Financieros

<img src="../ML_Finanzas/imagenes/robo_advisor.gif" class="w-full rounded-lg mb-3" />

- Robo-advisors
- Chatbots y atención al cliente
- Personalización de productos

</div>

</div>

---
layout: default
---

# Trading Algorítmico

<div class="text-left space-y-6">

## ¿Qué es?

**Trading algorítmico** (o simplemente "algo trading") es el uso de algoritmos para realizar transacciones de forma autónoma.

## Orígenes

- Se remonta a la década de **1970**
- También conocido como **"Sistemas de Trading Automatizados"** (más preciso)

## Funcionamiento

- Instrucciones de trading preprogramadas y automatizadas
- Decisiones de trading **extremadamente rápidas** y objetivas

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/trading_algoritmico.jpg
---

# Machine Learning en Trading Algorítmico

<div class="text-left space-y-4">

## El Rol de ML

Machine Learning está llevando el trading algorítmico a **nuevos niveles**.

### Ventajas de ML:

- ✅ Estrategias **más avanzadas** que se adaptan en tiempo real
- ✅ Técnicas basadas en ML ofrecen **más vías** para obtener insights especiales sobre movimientos del mercado
- ✅ Calibración de decisiones de trading **en tiempo real**

### Práctica de la Industria

La mayoría de hedge funds e instituciones financieras **no revelan abiertamente** sus enfoques basados en ML (por buenas razones).

</div>

<!--
**Notas del Presentador:**

- Contexto histórico: Trading algorítmico existe desde los 70s, pero ML lo está revolucionando
- Ejemplos de ventajas:
  - Detección de patrones complejos que humanos no ven
  - Adaptación automática a cambios de mercado
  - Procesamiento de datos no estructurados (noticias, redes sociales)
- Por qué no revelan estrategias: Ventaja competitiva - si todos saben, deja de funcionar
- Ejemplo: Renaissance Medallion Fund - uno de los más exitosos, muy secreto
- Pregunta para reflexión: ¿Es ético mantener estas estrategias secretas?
-->

---
layout: default
---

# Gestión de Portafolios y Robo-Advisors

<div class="text-left space-y-6">

## Exploración de IA

Las firmas de gestión de activos y riqueza están explorando soluciones de **Inteligencia Artificial (IA)** para:

- Mejorar sus decisiones de inversión
- Aprovechar sus **trozos de datos históricos**

## ¿Qué son los Robo-Advisors?

Algoritmos construidos para **calibrar un portafolio financiero** según:
- Los objetivos del usuario
- La tolerancia al riesgo del usuario

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/robo_advisor.gif
---

# Funcionamiento de Robo-Advisors

<div class="text-left space-y-4">

## Servicios Proporcionados

Proporcionan **orientación y servicio financiero automatizado** a inversores finales y clientes.

## Proceso de Usuario

1. **Input del usuario:**
   - Objetivos financieros (ej: "jubilarme a los 65 con $250,000")
   - Edad, ingresos, activos financieros actuales

2. **Asignación:**
   - El asesor (el asignador) distribuye inversiones
   - Entre clases de activos e instrumentos financieros
   - Para alcanzar los objetivos del usuario

3. **Calibración dinámica:**
   - Se adapta a cambios en objetivos del usuario
   - Cambios en tiempo real del mercado
   - Siempre buscando el mejor ajuste para los objetivos originales

</div>

<!--
**Notas del Presentador:**

- Ejemplos reales: Betterment, Wealthfront, Vanguard Personal Advisor
- Demostración práctica: Mostrar cómo funciona el proceso
- Ventajas vs. asesores humanos:
  - Disponibilidad 24/7
  - Sin sesgos emocionales
  - Costos más bajos
- Limitaciones:
  - No reemplaza completamente el asesoramiento humano para casos complejos
  - Depende de la calidad de los datos del usuario
- Caso de uso: Millennials y Gen Z prefieren robo-advisors
- Pregunta: ¿Alguien ha usado un robo-advisor?
-->

---
layout: default
---

# Tracción de Robo-Advisors

<div class="grid grid-cols-2 gap-6 mt-8">

<div class="border rounded-lg p-6">

## Aceptación del Mercado

Los robo-advisors han ganado **traction significativa** entre consumidores que:

- No necesitan un asesor humano
- Se sienten cómodos invirtiendo de forma automatizada

</div>

<div class="border rounded-lg p-6">

## Ventajas

- ✅ **Accesibilidad**: Servicios de inversión para más personas
- ✅ **Bajo costo**: Comisiones reducidas vs. asesores tradicionales
- ✅ **Automatización**: Rebalanceo continuo del portafolio
- ✅ **Personalización**: Adaptado a objetivos y riesgo individual

</div>

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/futuro_finanzas.jpg
---

# El Panorama Futuro

## Transformación de la Industria

<div class="text-left space-y-4">

- **Próximas Décadas**: La industria financiera será transformada por ML y Data Science
- **Demanda de Expertos**: Crecimiento exponencial en la necesidad de profesionales especializados
- **Nuevas Oportunidades**: Aplicaciones emergentes en áreas como:
  - 💰 Criptomonedas y DeFi
  - 🌱 Finanzas sostenibles (ESG)
  - 📋 RegTech y Compliance automatizado

</div>

---
layout: default
---

# Desafíos y Consideraciones

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="border rounded-lg p-4">

## 📜 Regulación y Compliance

<img src="../ML_Finanzas/imagenes/regulacion.jpg" class="w-full rounded-lg mb-3" />

- Explicabilidad de modelos
- Transparencia algorítmica
- Cumplimiento normativo

</div>

<div class="border rounded-lg p-4">

## ⚡ Riesgos Tecnológicos

<img src="../ML_Finanzas/imagenes/riesgos_tecnicos.gif" class="w-full rounded-lg mb-3" />

- Overfitting y validación
- Datos de baja calidad
- Sesgos en los modelos

</div>

<div class="border rounded-lg p-4">

## ⚖️ Ética y Responsabilidad

<img src="../ML_Finanzas/imagenes/etica_ia.jpg" class="w-full rounded-lg mb-3" />

- Uso responsable de datos
- Prevención de discriminación
- Privacidad del cliente

</div>

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/stack_tecnologico.jpg
---

# Stack Tecnológico

## Herramientas Principales

<div class="text-left space-y-4">

**💻 Lenguajes:**
- Python (principal)
- R (análisis estadístico)

**📚 Librerías Clave:**
- Pandas, NumPy (manipulación de datos)
- Scikit-learn (ML tradicional)
- TensorFlow, PyTorch (Deep Learning)
- QuantLib (finanzas cuantitativas)

**☁️ Infraestructura:**
- Jupyter Notebooks
- Cloud platforms (AWS, GCP, Azure)
- Bases de datos (PostgreSQL, MongoDB)

</div>

---
layout: default
---

# Casos de Estudio del Libro

<div class="grid grid-cols-3 gap-4 mt-6">

<div class="border rounded-lg p-4">

## 📊 Estrategias de Trading

<img src="../ML_Finanzas/imagenes/trading_strategies.jpg" class="w-full rounded-lg mb-3" />

- Desarrollo de algoritmos de trading
- Backtesting y optimización

</div>

<div class="border rounded-lg p-4">

## 🤖 Robo-Advisors

<img src="../ML_Finanzas/imagenes/robo_advisor_caso.jpg" class="w-full rounded-lg mb-3" />

- Construcción de asesores automatizados
- Optimización de portafolios

</div>

<div class="border rounded-lg p-4">

## 📉 Análisis de Riesgo

<img src="../ML_Finanzas/imagenes/analisis_riesgo.gif" class="w-full rounded-lg mb-3" />

- Modelos predictivos
- Scoring y clasificación

</div>

</div>

---
layout: default
---

# Estructura del Curso

<div class="grid grid-cols-2 gap-6 mt-8">

<div class="border rounded-lg p-6">

## Fundamentos (Clases 1-3)

- Introducción al ML en finanzas
- Conceptos fundamentales
- Herramientas y ecosistema

</div>

<div class="border rounded-lg p-6">

## Casos Prácticos (Clases 4+)

- Implementación de estrategias
- Desarrollo de modelos
- Evaluación y optimización

</div>

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/resumen_ml.gif
---

# Resumen

## Puntos Clave

<div class="text-left space-y-3 text-lg">

✅ ML y Data Science están transformando la industria financiera

✅ Tres pilares: Infraestructura, Herramientas, Algoritmos

✅ Múltiples tipos de ML aplicables a diferentes problemas

✅ Oportunidades crecientes para profesionales especializados

✅ Importancia de la ética y el cumplimiento normativo

</div>

---
layout: default
---

# Próximos Pasos

<div class="grid grid-cols-2 gap-6 mt-8">

<div class="border rounded-lg p-6">

## Preparación para la Próxima Clase

1. Revisar conceptos básicos de Python
2. Instalar entorno de desarrollo (Jupyter, librerías)
3. Explorar datasets financieros públicos
4. Leer capítulos 2-3 del libro (fundamentos)

</div>

<div class="border rounded-lg p-6">

## Recursos Adicionales

- Documentación de Pandas y NumPy
- Tutoriales de Scikit-learn
- Datasets: Yahoo Finance, Quandl, Alpha Vantage

</div>

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/discusion.jpg
---

# Preguntas y Discusión

## Temas para Reflexionar

<div class="text-left space-y-4 text-lg">

- 💭 ¿Qué aplicaciones de ML en finanzas conoces?
- 🤔 ¿Cuáles son los principales desafíos que ves?
- 🎯 ¿Qué área de finanzas te interesa más?

</div>

---
layout: image-right
image: ../ML_Finanzas/imagenes/referencias.jpg
---

# Referencias

<div class="text-left space-y-4">

**Libro Principal:**
- Tatsat, H., Puri, S., & Lookabaugh, B. (2020). *Machine Learning and Data Science Blueprints for Finance*. O'Reilly Media.

**Recursos Adicionales:**
- O'Reilly Learning Platform
- GitHub: Repositorios de finanzas cuantitativas
- Papers académicos sobre ML en finanzas

</div>

---
layout: end
class: text-center
image: ../ML_Finanzas/imagenes/cierre_clase.jpg
---

# Fin de la Clase 1

<div class="text-2xl mt-8">

**Próxima clase:** Fundamentos de Machine Learning aplicados a Finanzas

</div>

<div class="text-4xl mt-12">

# ¡Gracias por su atención!

</div>
