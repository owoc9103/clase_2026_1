---
theme: seriph
background: linear-gradient(135deg, rgb(42, 67, 176) 0%, rgb(128, 1, 255) 100%)
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

---
layout: cover
background: linear-gradient(135deg, rgb(42, 67, 176) 0%, rgb(128, 1, 255) 100%)
---

# Machine Learning en Finanzas
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
  Basado en: Machine Learning and Data Science Blueprints for Finance<br>
  Tatsat, Puri & Lookabaugh — O'Reilly
</div>

---
layout: intro
class: text-left
---

# Introducción

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }"
  class="text-center mb-8 p-6 bg-gray-800 rounded-lg border-l-4 border-blue-500">

<div class="text-2xl italic text-gray-300 mb-4">
  "Machine learning promises to shake up large swathes of finance"
</div>

<div class="text-sm text-gray-400">
  —The Economist (2017)
</div>

</div>

<div class="space-y-4 text-lg">

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
Hay una <strong>nueva ola de machine learning y data science en finanzas</strong>, y las aplicaciones relacionadas transformarán la industria en las próximas décadas.
</div>

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 400 } }">
Actualmente, la mayoría de firmas financieras, incluyendo <v-click>hedge funds</v-click>, <v-click>bancos de inversión y minoristas</v-click>, y <v-click>firmas fintech</v-click>, están adoptando e invirtiendo fuertemente en machine learning.
</div>

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 600 } }">
En el futuro, las instituciones financieras necesitarán un <strong>número creciente de expertos en machine learning y data science</strong>.
</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Esta cita de The Economist (2017) fue visionaria; estamos en medio de esa transformación.
2. **Ejemplos concretos**: Hedge funds (Renaissance, Two Sigma), bancos (JPMorgan, Goldman Sachs), FinTech (Revolut, Robinhood).
3. **Pregunta**: ¿Conocen algún ejemplo local de adopción de ML en finanzas?
4. **Punto clave**: La demanda de expertos en ML y data science crece exponencialmente.
5. **Transición**: "Ahora veamos por qué esto está sucediendo y qué se necesita para tener éxito..."
-->

---
layout: default
class: text-left
---

# ¿Por qué ahora?

<div class="space-y-6">

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
Machine learning en finanzas se ha vuelto más prominente recientemente debido a:
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 300 } }"
  class="p-6 bg-blue-900/30 rounded-lg border border-blue-500/50">
### 📊 Disponibilidad de Grandes Volúmenes de Datos

<v-click>El acceso a vastas cantidades de datos financieros estructurados y no estructurados ha crecido exponencialmente.</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 500 } }"
  class="p-6 bg-purple-900/30 rounded-lg border border-purple-500/50">
### 💻 Poder Computacional Más Asequible

<v-click>El cloud computing y las GPUs han hecho el procesamiento de ML accesible para más organizaciones.</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 700 } }"
  class="p-6 bg-green-900/30 rounded-lg border border-green-500/50">
### 📈 Crecimiento Exponencial

<v-click>El uso de data science y machine learning está creciendo exponencialmente en todas las áreas de finanzas.</v-click>
</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Hace 10 años esto no era posible; datos y cómputo han cambiado el panorama.
2. **Ejemplos**: Big data, IoT, APIs; AWS, Google Cloud, Azure; uso de ML en trading, riesgo, servicios.
3. **Pregunta**: ¿En qué área de finanzas les gustaría aplicar ML?
4. **Punto clave**: No es una moda; es una tendencia establecida. El éxito requiere tres pilares.
5. **Transición**: "Pero el éxito no es automático: infraestructura, toolkit y algoritmos..."
-->

---
layout: default
class: text-left
---

# Los Pilares del Éxito

<div class="space-y-6">

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
El éxito de machine learning en finanzas depende de:
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }"
  class="p-6 bg-gradient-to-r from-blue-900/40 to-blue-800/40 rounded-lg border-l-4 border-blue-500">
### 🏗️ Construir Infraestructura Eficiente

<v-click>Una arquitectura escalable y robusta que pueda manejar grandes volúmenes de datos y procesamiento en tiempo real.</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 400 } }"
  class="p-6 bg-gradient-to-r from-purple-900/40 to-purple-800/40 rounded-lg border-l-4 border-purple-500">
### 🛠️ Usar el Toolkit Correcto

<v-click>Seleccionar las herramientas, librerías y frameworks apropiados para cada tarea específica.</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 600 } }"
  class="p-6 bg-gradient-to-r from-green-900/40 to-green-800/40 rounded-lg border-l-4 border-green-500">
### 🧠 Aplicar los Algoritmos Correctos

<v-click>Elegir y aplicar los modelos de machine learning adecuados para cada problema de negocio específico.</v-click>
</div>

</div>

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 800 } }"
  class="mt-6 p-4 bg-yellow-900/30 rounded-lg border border-yellow-500/50 text-center">
<strong>Estos conceptos fundamentales se demuestran y utilizan a lo largo de este libro.</strong>
</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Estos pilares son fundamentales; sin uno, el proyecto falla.
2. **Ejemplos**: Infraestructura (AWS, GCP); herramientas (Python, TensorFlow, APIs); algoritmos (elegir modelo, no DL para todo).
3. **Pregunta**: ¿Han visto proyectos fracasar por descuidar alguno de estos pilares?
4. **Punto clave**: El éxito requiere los TRES; analogía: casa = cimientos + herramientas + conocimiento.
5. **Transición**: "En este capítulo exploraremos estos conceptos y más..."
-->

---
layout: two-cols
class: text-left
---

# Objetivos de la Clase

::left::

<div class="text-left">

- <v-click>Comprender el estado actual del Machine Learning en finanzas</v-click> 
- <v-click>Identificar los tres pilares fundamentales para el éxito de ML en finanzas</v-click>
- <v-click>Conocer los diferentes tipos de Machine Learning aplicables</v-click>
- <v-click>Entender el panorama futuro de la industria</v-click>

</div>

::right::

<div class="flex items-center justify-center h-full">
  <img 
    src="https://media.tenor.com/HX2vaHm3wQYAAAAi/windesheim-thumbs-up.gif" 
    class="w-full rounded-lg shadow-lg" 
    alt="Meerkat" />
</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Bienvenida; estos objetivos guían toda la clase.
2. **Ejemplos**: El libro y el curso cubren panorama, pilares, tipos de ML y aplicaciones.
3. **Pregunta**: ¿Qué les gustaría aprender primero?
4. **Punto clave**: Al final haremos un resumen para verificar que se cumplieron.
5. **Transición**: "Veamos el panorama actual de la industria..."
-->

---
layout: default
class: text-left
---

# El Panorama Actual

## Adopción Rápida en la Industria Financiera

<div class="text-left space-y-4">

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
- **Hedge Funds**: Inversión masiva en tecnologías de ML
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
- **Bancos de Inversión**: Implementación de sistemas inteligentes
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 400 } }">
- **Bancos Minoristas**: Automatización y personalización
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 600 } }">
- **Firmas FinTech**: Innovación disruptiva
</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: La industria financiera está en plena transformación.
2. **Ejemplos**: Hedge funds (Renaissance, Two Sigma); bancos (JPMorgan, Goldman Sachs); FinTech (Revolut, Robinhood).
3. **Pregunta**: ¿Conocen algún ejemplo local de adopción de ML?
4. **Punto clave**: Todas las firmas invierten fuertemente en ML.
5. **Transición**: "Ahora veamos por qué esto está sucediendo..."
-->

---
layout: two-cols
---

# Factores de Crecimiento

## ¿Por qué ahora?

::left::

<div class="space-y-6 text-left">

<div
  v-motion
  v-click
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
### 1. Disponibilidad de Datos
- Volúmenes masivos de información financiera
- Datos estructurados y no estructurados
- Acceso a datos en tiempo real
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 400 } }">
### 2. Poder Computacional Asequible
- Cloud computing
- Procesamiento distribuido
- GPUs y TPUs
</div>

</div>

::right::

<div class="space-y-4 text-left">
  <div class="p-4 bg-blue-900/20 rounded-lg">
    <strong>Big Data en Finanzas</strong><br>
    Volúmenes masivos de información financiera
  </div>
  <div class="p-4 bg-purple-900/20 rounded-lg">
    <strong>Cloud Computing</strong><br>
    Procesamiento distribuido y escalable
  </div>
</div>

---
layout: default
class: text-left
---

# Los Tres Pilares Fundamentales

<div class="text-left space-y-6">

Para el éxito de Machine Learning en finanzas se requieren:

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
### 1. 🏗️ Infraestructura Eficiente
- <v-click>Arquitectura escalable</v-click>
- <v-click>Procesamiento de datos en tiempo real</v-click>
- <v-click>Almacenamiento robusto</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 300 } }">
### 2. 🛠️ Selección Correcta de Herramientas
- <v-click>Stack tecnológico apropiado</v-click>
- <v-click>Librerías y frameworks adecuados</v-click>
- <v-click>Ecosistema Python para finanzas</v-click>
</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 600 } }">
### 3. 🧠 Aplicación Apropiada de Algoritmos
- <v-click>Elección del modelo correcto</v-click>
- <v-click>Entendimiento del problema de negocio</v-click>
- <v-click>Validación y evaluación rigurosa</v-click>
</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Estos pilares son fundamentales; sin uno, el proyecto falla.
2. **Ejemplos**: Infraestructura (AWS, GCP); herramientas (Python, TensorFlow, APIs); algoritmos (elegir modelo, no DL para todo).
3. **Pregunta**: ¿Han visto proyectos descuidar alguno de estos pilares?
4. **Punto clave**: El éxito requiere los TRES; analogía: casa = cimientos + herramientas + conocimiento.
5. **Transición**: "Ahora veamos los tipos de ML aplicables..."
-->

---
layout: default
---

# Tipos de Machine Learning

<div class="grid grid-cols-3 gap-6 mt-8">

<div
  v-motion
  v-click
  :initial="{ x: -80, opacity: 0, scale: 0.9 }"
  :enter="{ x: 0, opacity: 1, scale: 1 }"
  class="border rounded-lg p-4">

## 📊 Aprendizaje Supervisado

- **Clasificación**: Detección de fraude, scoring crediticio
- **Regresión**: Predicción de precios, valoración de activos

</div>

<div
  v-motion
  v-click="2"
  :initial="{ y: 80, opacity: 0, scale: 0.9 }"
  :enter="{ y: 0, opacity: 1, scale: 1, transition: { delay: 200 } }"
  class="border rounded-lg p-4">

## 🔍 Aprendizaje No Supervisado

- **Clustering**: Segmentación de clientes
- **Detección de anomalías**: Identificación de transacciones sospechosas

</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: 80, opacity: 0, scale: 0.9 }"
  :enter="{ x: 0, opacity: 1, scale: 1, transition: { delay: 400 } }"
  class="border rounded-lg p-4">

## 🎯 Aprendizaje por Refuerzo

- **Trading algorítmico**: Optimización de estrategias
- **Robo-advisors**: Gestión automatizada de portafolios

</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Tres tipos de ML; cada uno resuelve problemas distintos.
2. **Ejemplos**: Supervisado (fraude, scoring); no supervisado (segmentación, anomalías); refuerzo (trading, robo-advisors).
3. **Pregunta**: ¿Qué tipo usarían para detectar fraude? (Supervisado.)
4. **Punto clave**: Supervisado = etiquetas; no supervisado = patrones; refuerzo = prueba y error.
5. **Transición**: "Veamos dónde se aplican en finanzas..."
-->

---
layout: default
---

# Aplicaciones en Finanzas

<div class="grid grid-cols-3 gap-4 mt-6">

<div
  v-motion
  v-click
  :initial="{ rotateX: -90, opacity: 0 }"
  :enter="{ rotateX: 0, opacity: 1 }"
  class="border rounded-lg p-4">

## 📈 Trading y Mercados

- Estrategias de trading algorítmico
- Predicción de movimientos de precios
- Arbitraje y market making

</div>

<div
  v-motion
  v-click="2"
  :initial="{ rotateX: -90, opacity: 0 }"
  :enter="{ rotateX: 0, opacity: 1, transition: { delay: 200 } }"
  class="border rounded-lg p-4">

## ⚠️ Gestión de Riesgos

- Modelos de riesgo crediticio
- Value at Risk (VaR)
- Stress testing

</div>

<div
  v-motion
  v-click="3"
  :initial="{ rotateX: -90, opacity: 0 }"
  :enter="{ rotateX: 0, opacity: 1, transition: { delay: 400 } }"
  class="border rounded-lg p-4">

## 🤖 Servicios Financieros

- Robo-advisors
- Chatbots y atención al cliente
- Personalización de productos

</div>

</div>

<!--
**Notas del Presentador:**

1. **Contexto**: Tres áreas principales donde ML se aplica en finanzas.
2. **Ejemplos**: Trading (HFT, milisegundos); riesgo (VaR, stress testing); servicios (robo-advisors, chatbots).
3. **Pregunta**: ¿En qué área les gustaría trabajar?
4. **Punto clave**: Trading = velocidad; riesgo = cumplimiento; servicios = experiencia de cliente.
5. **Transición**: "Profundicemos en trading algorítmico..."
-->

---
layout: default
---

# Trading Algorítmico

<div class="text-left space-y-6">

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
## ¿Qué es?

**Trading algorítmico** (o simplemente "algo trading") es el uso de algoritmos para realizar transacciones de forma autónoma.
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 300 } }">
## Orígenes

- <v-click>Se remonta a la década de **1970**</v-click>
- <v-click>También conocido como **"Sistemas de Trading Automatizados"** (más preciso)</v-click>
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 600 } }">
## Funcionamiento

- <v-click>Instrucciones de trading preprogramadas y automatizadas</v-click>
- <v-click>Decisiones de trading **extremadamente rápidas** y objetivas</v-click>
</div>

</div>

<!--
**Notas del Presentador:**

- Definición simple: Algoritmos que compran y venden automáticamente
- Historia: Comenzó en los 70s con sistemas básicos, ahora es extremadamente sofisticado
- Velocidad: Algunos sistemas ejecutan miles de transacciones por segundo
- Ejemplo: High-frequency trading (HFT) - microsegundos importan
- Pregunta: "¿Saben cuánto tiempo tarda una orden en llegar al mercado?" (milisegundos)
- Transición: "Ahora veamos cómo ML está revolucionando esto..."
-->

---
layout: default
class: text-left
---

# Machine Learning en Trading Algorítmico

<div class="text-left space-y-4">

## El Rol de ML

Machine Learning está llevando el trading algorítmico a **nuevos niveles**.

### Ventajas de ML:

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0 }"
  :enter="{ scale: 1, opacity: 1 }">
- <v-click>✅ Estrategias **más avanzadas** que se adaptan en tiempo real</v-click>
</div>

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0 }"
  :enter="{ scale: 1, opacity: 1, transition: { delay: 200 } }">
- <v-click>✅ Técnicas basadas en ML ofrecen **más vías** para obtener insights especiales sobre movimientos del mercado</v-click>
</div>

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0 }"
  :enter="{ scale: 1, opacity: 1, transition: { delay: 400 } }">
- <v-click>✅ Calibración de decisiones de trading **en tiempo real**</v-click>
</div>

### Práctica de la Industria

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 600 } }">
La mayoría de hedge funds e instituciones financieras **no revelan abiertamente** sus enfoques basados en ML (por buenas razones).
</div>

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

<!--
**Notas del Presentador:**

- Contexto: Gestión de portafolios tradicionalmente requiere asesores humanos costosos
- Robo-advisors democratizan el acceso a gestión profesional de inversiones
- Datos históricos: Las firmas tienen décadas de datos de mercado que pueden aprovechar
- Ejemplo: Vanguard, Fidelity ahora ofrecen servicios híbridos (humano + robo)
- Pregunta: "¿Alguien ha usado un robo-advisor o conoce alguno?"
- Transición: "Veamos cómo funcionan en detalle..."
-->

---
layout: default
class: text-left
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

<div
  v-motion
  :initial="{ x: -80, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }"
  class="border rounded-lg p-6">

## Aceptación del Mercado

Los robo-advisors han ganado **traction significativa** entre consumidores que:

- <v-click>No necesitan un asesor humano</v-click>
- <v-click>Se sienten cómodos invirtiendo de forma automatizada</v-click>

</div>

<div
  v-motion
  :initial="{ x: 80, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }"
  class="border rounded-lg p-6">

## Ventajas

- <v-click>✅ **Accesibilidad**: Servicios de inversión para más personas</v-click>
- <v-click>✅ **Bajo costo**: Comisiones reducidas vs. asesores tradicionales</v-click>
- <v-click>✅ **Automatización**: Rebalanceo continuo del portafolio</v-click>
- <v-click>✅ **Personalización**: Adaptado a objetivos y riesgo individual</v-click>

</div>

</div>

---
layout: default
class: text-left
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

<div
  v-motion
  :initial="{ y: 50, opacity: 0, rotateY: -15 }"
  :enter="{ y: 0, opacity: 1, rotateY: 0 }"
  class="border rounded-lg p-4">

## 📜 Regulación y Compliance

- <v-click>Explicabilidad de modelos</v-click>
- <v-click>Transparencia algorítmica</v-click>
- <v-click>Cumplimiento normativo</v-click>

</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0, rotateY: -15 }"
  :enter="{ y: 0, opacity: 1, rotateY: 0, transition: { delay: 200 } }"
  class="border rounded-lg p-4">

## ⚡ Riesgos Tecnológicos

- <v-click>Overfitting y validación</v-click>
- <v-click>Datos de baja calidad</v-click>
- <v-click>Sesgos en los modelos</v-click>

</div>

<div
  v-motion
  :initial="{ y: 50, opacity: 0, rotateY: -15 }"
  :enter="{ y: 0, opacity: 1, rotateY: 0, transition: { delay: 400 } }"
  class="border rounded-lg p-4">

## ⚖️ Ética y Responsabilidad

- <v-click>Uso responsable de datos</v-click>
- <v-click>Prevención de discriminación</v-click>
- <v-click>Privacidad del cliente</v-click>

</div>

</div>

---
layout: default
class: text-left
---

# Stack Tecnológico

## Herramientas Principales

<div class="text-left space-y-4">

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
**💻 Lenguajes:**
- <v-click>Python (principal)</v-click>
- <v-click>R (análisis estadístico)</v-click>
</div>

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 300 } }">
**📚 Librerías Clave:**
- <v-click>Pandas, NumPy (manipulación de datos)</v-click>
- <v-click>Scikit-learn (ML tradicional)</v-click>
- <v-click>TensorFlow, PyTorch (Deep Learning)</v-click>
- <v-click>QuantLib (finanzas cuantitativas)</v-click>
</div>

<div
  v-motion
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 600 } }">
**☁️ Infraestructura:**
- <v-click>Jupyter Notebooks</v-click>
- <v-click>Cloud platforms (AWS, GCP, Azure)</v-click>
- <v-click>Bases de datos (PostgreSQL, MongoDB)</v-click>
</div>

</div>

---
layout: default
---

# Casos de Estudio del Libro

<div class="grid grid-cols-3 gap-4 mt-6">

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0, rotateZ: -10 }"
  :enter="{ scale: 1, opacity: 1, rotateZ: 0 }"
  class="border rounded-lg p-4">

## 📊 Estrategias de Trading

- <v-click>Desarrollo de algoritmos de trading</v-click>
- <v-click>Backtesting y optimización</v-click>

</div>

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0, rotateZ: -10 }"
  :enter="{ scale: 1, opacity: 1, rotateZ: 0, transition: { delay: 200 } }"
  class="border rounded-lg p-4">

## 🤖 Robo-Advisors

- <v-click>Construcción de asesores automatizados</v-click>
- <v-click>Optimización de portafolios</v-click>

</div>

<div
  v-motion
  :initial="{ scale: 0.8, opacity: 0, rotateZ: -10 }"
  :enter="{ scale: 1, opacity: 1, rotateZ: 0, transition: { delay: 400 } }"
  class="border rounded-lg p-4">

## 📉 Análisis de Riesgo

- <v-click>Modelos predictivos</v-click>
- <v-click>Scoring y clasificación</v-click>

</div>

</div>

---
layout: default
---

# Estructura del Curso

<div class="grid grid-cols-2 gap-6 mt-8">

<div
  v-motion
  :initial="{ rotateY: -90, opacity: 0 }"
  :enter="{ rotateY: 0, opacity: 1 }"
  class="border rounded-lg p-6">

## Fundamentos (Clases 1-3)

- <v-click>Introducción al ML en finanzas</v-click>
- <v-click>Conceptos fundamentales</v-click>
- <v-click>Herramientas y ecosistema</v-click>

</div>

<div
  v-motion
  :initial="{ rotateY: 90, opacity: 0 }"
  :enter="{ rotateY: 0, opacity: 1, transition: { delay: 300 } }"
  class="border rounded-lg p-6">

## Casos Prácticos (Clases 4+)

- <v-click>Implementación de estrategias</v-click>
- <v-click>Desarrollo de modelos</v-click>
- <v-click>Evaluación y optimización</v-click>

</div>

</div>

---
layout: default
class: text-left
---

# Resumen

## Puntos Clave

<div class="text-left space-y-3 text-lg">

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
✅ <v-click>ML y Data Science están transformando la industria financiera</v-click>
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
✅ <v-click>Tres pilares: Infraestructura, Herramientas, Algoritmos</v-click>
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 400 } }">
✅ <v-click>Múltiples tipos de ML aplicables a diferentes problemas</v-click>
</div>

<div
  v-motion
  :initial="{ x: -100, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 600 } }">
✅ <v-click>Oportunidades crecientes para expertos; ética y cumplimiento normativo son esenciales</v-click>
</div>

</div>

---
layout: default
---

# Próximos Pasos

<div class="grid grid-cols-2 gap-6 mt-8">

<div class="border rounded-lg p-6">

## Preparación para la Próxima Clase

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
1. <v-click>Revisar Python e instalar entorno (Jupyter, librerías)</v-click>
</div>

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }">
2. <v-click>Explorar datasets financieros y leer capítulos 2-3 del libro</v-click>
</div>

</div>

<div class="border rounded-lg p-6">

## Recursos Adicionales

<div
  v-motion
  :initial="{ x: 50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
- <v-click>Documentación: Pandas, NumPy, Scikit-learn</v-click>
</div>

<div
  v-motion
  :initial="{ x: 50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 400 } }">
- <v-click>Datasets: Yahoo Finance, Quandl, Alpha Vantage</v-click>
</div>

</div>

</div>

---
layout: default
class: text-left
---

# Preguntas y Discusión

## Temas para Reflexionar

<div class="text-left space-y-4 text-lg">

<div
  v-motion
  :initial="{ rotate: -5, opacity: 0 }"
  :enter="{ rotate: 0, opacity: 1 }">
- <v-click>💭 ¿Qué aplicaciones de ML en finanzas conoces?</v-click>
</div>

<div
  v-motion
  :initial="{ rotate: -5, opacity: 0 }"
  :enter="{ rotate: 0, opacity: 1, transition: { delay: 300 } }">
- <v-click>🤔 ¿Cuáles son los principales desafíos que ves?</v-click>
</div>

<div
  v-motion
  :initial="{ rotate: -5, opacity: 0 }"
  :enter="{ rotate: 0, opacity: 1, transition: { delay: 600 } }">
- <v-click>🎯 ¿Qué área de finanzas te interesa más?</v-click>
</div>

</div>

---
layout: default
class: text-left
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
layout: default
class: text-center
---

# Fin de la Clase 1

<div class="text-2xl mt-8">

**Próxima clase:** Fundamentos de Machine Learning aplicados a Finanzas

</div>

<div class="text-4xl mt-12">

# ¡Gracias por su atención!

</div>
