---
marp: true
theme: default
paginate: true
style: |
  section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
  section::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    opacity: 0.1;
  }
  h1, h2 {
    color: #fff;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
  }
  img {
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
  }
---

<!-- _class: lead -->
<!-- _paginate: false -->

![bg right:40%](../../imagenes/portada_ml_finanzas.jpg)

# Machine Learning en Finanzas: El Panorama
## Clase 1 - Introducción

**Basado en:** Machine Learning and Data Science Blueprints for Finance
*Hariom Tatsat, Sahil Puri, Brad Lookabaugh*

---

## Objetivos de la Clase

![bg right:35% w:400](../../imagenes/objetivos_ml.gif)

- Comprender el estado actual del Machine Learning en finanzas
- Identificar los tres pilares fundamentales para el éxito de ML en finanzas
- Conocer los diferentes tipos de Machine Learning aplicables
- Entender el panorama futuro de la industria

---

## El Panorama Actual

![bg right:40% w:450](../../imagenes/industria_financiera.jpg)

### Adopción Rápida en la Industria Financiera

- **Hedge Funds**: Inversión masiva en tecnologías de ML
- **Bancos de Inversión**: Implementación de sistemas inteligentes
- **Bancos Minoristas**: Automatización y personalización
- **Firmas FinTech**: Innovación disruptiva

---

## Factores de Crecimiento

### ¿Por qué ahora?

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

1. **Disponibilidad de Datos**
   - Volúmenes masivos de información financiera
   - Datos estructurados y no estructurados
   - Acceso a datos en tiempo real

2. **Poder Computacional Asequible**
   - Cloud computing
   - Procesamiento distribuido
   - GPUs y TPUs

</div>

<div style="flex: 1;">

![w:100%](../../imagenes/big_data_finanzas.jpg)
![w:100%](../../imagenes/cloud_computing.gif)

</div>

</div>

---

## Los Tres Pilares Fundamentales

![bg right:35% w:400](../../imagenes/tres_pilares_ml.jpg)

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

---

## Tipos de Machine Learning

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

### 📊 Aprendizaje Supervisado
![w:200](../../imagenes/supervised_learning.jpg)
- **Clasificación**: Detección de fraude, scoring crediticio
- **Regresión**: Predicción de precios, valoración de activos

### 🔍 Aprendizaje No Supervisado
![w:200](../../imagenes/unsupervised_learning.jpg)
- **Clustering**: Segmentación de clientes
- **Detección de anomalías**: Identificación de transacciones sospechosas

</div>

<div>

### 🎯 Aprendizaje por Refuerzo
![w:200](../../imagenes/reinforcement_learning.gif)
- **Trading algorítmico**: Optimización de estrategias
- **Robo-advisors**: Gestión automatizada de portafolios

</div>

</div>

---

## Aplicaciones en Finanzas

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">

<div>

### 📈 Trading y Mercados
![w:100%](../../imagenes/trading_algoritmico.jpg)
- Estrategias de trading algorítmico
- Predicción de movimientos de precios
- Arbitraje y market making

</div>

<div>

### ⚠️ Gestión de Riesgos
![w:100%](../../imagenes/gestion_riesgos.jpg)
- Modelos de riesgo crediticio
- Value at Risk (VaR)
- Stress testing

</div>

<div>

### 🤖 Servicios Financieros
![w:100%](../../imagenes/robo_advisor.gif)
- Robo-advisors
- Chatbots y atención al cliente
- Personalización de productos

</div>

</div>

---

## El Panorama Futuro

![bg right:40% w:450](../../imagenes/futuro_finanzas.jpg)

### Transformación de la Industria

- **Próximas Décadas**: La industria financiera será transformada por ML y Data Science
- **Demanda de Expertos**: Crecimiento exponencial en la necesidad de profesionales especializados
- **Nuevas Oportunidades**: Aplicaciones emergentes en áreas como:
  - 💰 Criptomonedas y DeFi
  - 🌱 Finanzas sostenibles (ESG)
  - 📋 RegTech y Compliance automatizado

---

## Desafíos y Consideraciones

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 15px;">

<div>

### 📜 Regulación y Compliance
![w:100%](../../imagenes/regulacion.jpg)
- Explicabilidad de modelos
- Transparencia algorítmica
- Cumplimiento normativo

</div>

<div>

### ⚡ Riesgos Tecnológicos
![w:100%](../../imagenes/riesgos_tecnicos.gif)
- Overfitting y validación
- Datos de baja calidad
- Sesgos en los modelos

</div>

<div>

### ⚖️ Ética y Responsabilidad
![w:100%](../../imagenes/etica_ia.jpg)
- Uso responsable de datos
- Prevención de discriminación
- Privacidad del cliente

</div>

</div>

---

## Stack Tecnológico

![bg right:35% w:400](../../imagenes/stack_tecnologico.jpg)

### Herramientas Principales

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

---

## Casos de Estudio del Libro

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;">

<div>

### 📊 Estrategias de Trading
![w:100%](../../imagenes/trading_strategies.jpg)
- Desarrollo de algoritmos de trading
- Backtesting y optimización

</div>

<div>

### 🤖 Robo-Advisors
![w:100%](../../imagenes/robo_advisor_caso.jpg)
- Construcción de asesores automatizados
- Optimización de portafolios

</div>

<div>

### 📉 Análisis de Riesgo
![w:100%](../../imagenes/analisis_riesgo.gif)
- Modelos predictivos
- Scoring y clasificación

</div>

</div>

---

## Estructura del Curso

### Fundamentos (Clases 1-3)
- Introducción al ML en finanzas
- Conceptos fundamentales
- Herramientas y ecosistema

### Casos Prácticos (Clases 4+)
- Implementación de estrategias
- Desarrollo de modelos
- Evaluación y optimización

---

## Resumen

![bg right:35% w:400](../../imagenes/resumen_ml.gif)

### Puntos Clave

✅ ML y Data Science están transformando la industria financiera

✅ Tres pilares: Infraestructura, Herramientas, Algoritmos

✅ Múltiples tipos de ML aplicables a diferentes problemas

✅ Oportunidades crecientes para profesionales especializados

✅ Importancia de la ética y el cumplimiento normativo

---

## Próximos Pasos

### Preparación para la Próxima Clase

1. Revisar conceptos básicos de Python
2. Instalar entorno de desarrollo (Jupyter, librerías)
3. Explorar datasets financieros públicos
4. Leer capítulos 2-3 del libro (fundamentos)

### Recursos Adicionales
- Documentación de Pandas y NumPy
- Tutoriales de Scikit-learn
- Datasets: Yahoo Finance, Quandl, Alpha Vantage

---

## Preguntas y Discusión

![bg right:40% w:450](../../imagenes/discusion.jpg)

### Temas para Reflexionar

- 💭 ¿Qué aplicaciones de ML en finanzas conoces?
- 🤔 ¿Cuáles son los principales desafíos que ves?
- 🎯 ¿Qué área de finanzas te interesa más?

---

## Referencias

![bg right:35% w:400](../../imagenes/referencias.jpg)

**Libro Principal:**
- Tatsat, H., Puri, S., & Lookabaugh, B. (2020). *Machine Learning and Data Science Blueprints for Finance*. O'Reilly Media.

**Recursos Adicionales:**
- O'Reilly Learning Platform
- GitHub: Repositorios de finanzas cuantitativas
- Papers académicos sobre ML en finanzas

---

<!-- _class: lead -->
<!-- _paginate: false -->

![bg](../../imagenes/cierre_clase.jpg)

## Fin de la Clase 1

**Próxima clase:** Fundamentos de Machine Learning aplicados a Finanzas

# ¡Gracias por su atención!