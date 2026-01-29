---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://images.squarespace-cdn.com/content/v1/59d9b2749f8dce3ebe4e676d/1516589724361-VFYWDK9T32VHB1OO72Z9/ML-word-cloud.png
# some information about your slides (markdown enabled)
title: Bienvenido a Slidev
info: |
  ## Plantilla Inicial de Slidev
  Presentaciones para desarrolladores.

  Aprende más en [Sli.dev](https://sli.dev)
# apply UnoCSS classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: false
# duration of the presentation
duration: 35min
---

---
layout: cover
background: linear-gradient(135deg, rgb(42, 67, 176) 0%, rgb(128, 1, 255) 100%)
class: text-center
---

<div class="text-blue-900 font-bold- text-6xl">
Machine Learning en Finanzas: 
El Panorama
</div>

<div class="pt-12">
  <span class="text-lg text-blue-900 font-bold- ">Clase 1 - Introducción</span>
</div>



<div class="abs-bl m-6 text-sm text-blue-900 ">
By: OWOC<br>

</div>



---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-4">Historia del Machine Learning</div>

<div class="max-w-lg mx-auto mt-6">
  <img 
    src="https://pbs.twimg.com/media/E51K5HwUYAgggrr.jpg" 
    alt="Historia del Machine Learning"
    class="w-full rounded-lg shadow-lg" />
</div>

<!-- Descripciones en la parte inferior -->
<div class="mt-4 relative min-h-[40px] max-w-sm mx-auto">
  <div
    v-click="1"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">1950:</strong> Test de Turing - Propuesta para evaluar la inteligencia de máquinas.
  </div>
  
  <div
    v-click="2"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">1956:</strong> Conferencia de Dartmouth - Nacimiento oficial del término "Inteligencia Artificial".
  </div>
  
  <div
    v-click="3"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">1986:</strong> Backpropagation popularizado - Avance clave en entrenamiento de redes neuronales.
  </div>
  
  <div
    v-click="4"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">1997:</strong> Deep Blue vence a Kasparov - Primer campeón mundial de ajedrez derrotado por IA.
  </div>
  
  <div
    v-click="5"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">2006:</strong> Renacimiento del Deep Learning - Geoffrey Hinton populariza el aprendizaje profundo.
  </div>
  
  <div
    v-click="6"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">2012:</strong> AlexNet - Breakthrough en reconocimiento de imágenes con deep learning.
  </div>
  
  <div
    v-click="7"
    class="absolute inset-0 text-[10px] px-2 py-1 rounded border-l-2 bg-blue-50 dark:bg-blue-50 text-black dark:text-black border-blue-500 dark:border-blue-400">
    <strong class="text-blue-700">2016:</strong> AlphaGo vence a Lee Sedol - IA supera al mejor jugador de Go del mundo.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1950 - Test de Turing</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Período:</strong> Post Segunda Guerra Mundial</li>
    <li><strong>Contexto:</strong> Inicio de la computación moderna</li>
    <li><strong>Figura clave:</strong> Alan Turing</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Propuesta del <strong>Test de Turing</strong> como criterio para evaluar la inteligencia de máquinas</li>
    <li>Publicado en el artículo "Computing Machinery and Intelligence" (1950)</li>
    <li>Establece la base filosófica para la IA</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Fundamento teórico para el desarrollo de la IA</li>
    <li>Inspiró décadas de investigación en inteligencia artificial</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1950 - Test de Turing</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Propongo considerar la pregunta: '¿Pueden pensar las máquinas?' Esto debe comenzar con definiciones del significado de los términos 'máquina' y 'pensar'."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Alan Turing, 1950</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> Si una máquina puede engañar a un humano haciéndole creer que es otro humano, entonces puede considerarse "inteligente".
  </div>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: 0, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
  <div class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
    <a href="https://www.youtube.com/watch?v=iaXLDz_UeYY" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:underline text-sm font-medium">
      📺 Ver video: Test de Turing (YouTube)
    </a>
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1956 - Conferencia de Dartmouth</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Evento:</strong> Conferencia de Dartmouth</li>
    <li><strong>Organizadores:</strong> John McCarthy, Marvin Minsky, Claude Shannon, Nathaniel Rochester</li>
    <li><strong>Duración:</strong> 6-8 semanas en verano de 1956</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Nacimiento oficial del término "Inteligencia Artificial"</strong></li>
    <li>Propuesta de crear máquinas que puedan simular la inteligencia humana</li>
    <li>Establecimiento de objetivos ambiciosos para la IA</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Fundación del campo de la IA como disciplina académica</li>
    <li>Creación de los primeros programas de investigación en IA</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1956 - Conferencia de Dartmouth (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Cada aspecto del aprendizaje o cualquier otra característica de la inteligencia puede en principio describirse con tal precisión que una máquina pueda simularla."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Propuesta de Dartmouth, 1956</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> La inteligencia puede ser descrita formalmente y replicada en máquinas mediante algoritmos.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1986 - Renacimiento del Backpropagation</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Período:</strong> Fin del "Invierno de la IA"</li>
    <li><strong>Contexto:</strong> Avances en computación y disponibilidad de datos</li>
    <li><strong>Figura clave:</strong> Geoffrey Hinton, David Rumelhart, Ronald Williams</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Popularización del algoritmo de Backpropagation</strong></li>
    <li>Publicación del artículo "Learning representations by back-propagating errors" (Nature, 1986)</li>
    <li>Demostración práctica de entrenamiento de redes neuronales multicapa</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Revitalización del interés en redes neuronales</li>
    <li>Base para el desarrollo del Deep Learning moderno</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1986 - Renacimiento del Backpropagation (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Describimos un nuevo procedimiento de aprendizaje, la retropropagación, para redes de unidades similares a neuronas. El procedimiento ajusta repetidamente los pesos de las conexiones de la red para minimizar una medida de la diferencia entre el vector de salida real y el deseado."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Rumelhart, Hinton & Williams, 1986</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> El backpropagation permite entrenar redes neuronales profundas ajustando los pesos de manera sistemática.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1997 - Deep Blue vs Kasparov</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1, transition: { delay: 100 } }"
  class="mt-6 flex justify-center">
  <img
    src="https://94fa3c88.delivery.rocketcdn.me/es/files/2024/11/Deep-Blue-DataScientest.webp"
    alt="Deep Blue vs Kasparov"
    class="max-w-md w-full rounded-lg shadow-lg" />
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1997 - Deep Blue vs Kasparov</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Evento:</strong> Partida de ajedrez histórico</li>
    <li><strong>Contendientes:</strong> Deep Blue (IBM) vs Garry Kasparov</li>
    <li><strong>Resultado:</strong> Victoria de Deep Blue</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Primera derrota de un campeón mundial de ajedrez por una máquina</strong></li>
    <li>Demostración del poder de la búsqueda exhaustiva y evaluación posicional</li>
    <li>Uso de hardware especializado (procesadores paralelos)</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Cambio de percepción pública sobre las capacidades de la IA</li>
    <li>Inspiración para futuros sistemas de IA en juegos (AlphaGo, AlphaZero)</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">1997 - Deep Blue vs Kasparov (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Podía sentir — podía percibir — una nueva clase de inteligencia al otro lado de la mesa."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Garry Kasparov, 1997</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> La combinación de poder computacional masivo y algoritmos sofisticados puede superar la intuición humana en dominios específicos.
  </div>

<div
  v-motion
  v-click="4"
  :initial="{ x: 0, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 200 } }">
  <div class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
    <a href="https://www.youtube.com/watch?v=hS7GnYUKs8k" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-blue-600 dark:text-blue-400 hover:underline text-sm font-medium">
      📺 Ver video: Deep Blue vs Kasparov (YouTube)
    </a>
  </div>
</div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2006 - Renacimiento del Deep Learning</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Período:</strong> Inicio de la era del Big Data</li>
    <li><strong>Contexto:</strong> Mayor disponibilidad de datos y poder computacional</li>
    <li><strong>Figura clave:</strong> Geoffrey Hinton, Yann LeCun, Yoshua Bengio</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Popularización del término "Deep Learning"</strong></li>
    <li>Desarrollo de técnicas para entrenar redes neuronales profundas</li>
    <li>Aprendizaje no supervisado de representaciones</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Fundación de la revolución del Deep Learning</li>
    <li>Aplicaciones exitosas en visión computacional y reconocimiento de voz</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2006 - Renacimiento del Deep Learning (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Nuestro objetivo es descubrir algoritmos de aprendizaje que puedan descubrir buenas representaciones internas de los datos en múltiples niveles de abstracción."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Geoffrey Hinton, 2006</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> Las redes profundas pueden aprender representaciones jerárquicas de los datos, desde características simples hasta conceptos complejos.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2012 - AlexNet y el Breakthrough</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Evento:</strong> ImageNet Challenge 2012</li>
    <li><strong>Equipo:</strong> Alex Krizhevsky, Ilya Sutskever, Geoffrey Hinton</li>
    <li><strong>Resultado:</strong> Reducción del error del 26% al 15.3%</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>AlexNet:</strong> Primera red neuronal profunda ganadora de ImageNet</li>
    <li>Uso de GPUs para entrenamiento acelerado</li>
    <li>Técnicas de regularización (Dropout, Data Augmentation)</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Inicio de la era moderna del Deep Learning</li>
    <li>Revolución en visión computacional</li>
    <li>Adopción masiva de CNNs en la industria</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2012 - AlexNet y el Breakthrough (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "Entrenamos una gran red neuronal convolucional profunda para clasificar los 1,2 millones de imágenes de alta resolución del concurso ImageNet LSVRC-2010 en las 1000 clases diferentes."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— Krizhevsky, Sutskever & Hinton, 2012</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> Las redes convolucionales profundas pueden aprender representaciones visuales jerárquicas de manera end-to-end.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2016 - AlphaGo y el Go</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contexto Histórico</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Evento:</strong> Partida AlphaGo vs Lee Sedol</li>
    <li><strong>Organización:</strong> DeepMind (Google)</li>
    <li><strong>Resultado:</strong> Victoria de AlphaGo 4-1</li>
  </ul>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Contribución Principal</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li><strong>Primera derrota de un campeón mundial de Go por IA</strong></li>
    <li>Combinación de Deep Learning y Monte Carlo Tree Search</li>
    <li>Aprendizaje por refuerzo y redes de valor/política</li>
  </ul>
</div>

<div
  v-motion
  v-click="4"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Impacto</h3>
  <ul class="list-disc list-inside text-sm space-y-1">
    <li>Demostración de IA que supera a humanos en juegos complejos</li>
    <li>Inspiración para AlphaZero (aprendizaje sin conocimiento previo)</li>
    <li>Aplicaciones en optimización y toma de decisiones</li>
  </ul>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  v-click="1"
  :initial="{ y: -20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }">
  <h2 class="text-2xl font-semibold text-blue-700 dark:text-blue-400">2016 - AlphaGo y el Go (continuación)</h2>
</div>

<div
  v-motion
  v-click="2"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1 }">
  <h3 class="text-lg font-semibold mt-4 mb-2">Cita Relevante</h3>
  <div class="bg-gray-100 dark:bg-gray-800 text-black dark:text-white p-4 rounded-lg border-l-4 border-blue-500 dark:border-blue-400 italic text-sm">
    "El juego del Go ha sido considerado durante mucho tiempo el más desafiante de los juegos clásicos para la inteligencia artificial."
  </div>
  <div class="text-xs text-gray-600 dark:text-gray-400 mt-2 text-right">— DeepMind Team, 2016</div>
</div>

<div
  v-motion
  v-click="3"
  :initial="{ x: -50, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { delay: 100 } }">
  <div class="mt-6 bg-blue-50 dark:bg-blue-900/90 text-black dark:text-gray-100 p-4 rounded-lg text-sm">
    <strong>Concepto clave:</strong> La combinación de aprendizaje profundo y búsqueda puede resolver problemas que se consideraban intratables para las máquinas.
  </div>
</div>

---
layout: default
class: text-left
---

<div class="text-3xl font-bold mb-6">Historia del Machine Learning</div>

<div
  v-motion
  :initial="{ y: 30, opacity: 0 }"
  :enter="{ y: 0, opacity: 1 }"
  class="text-center mb-8 p-6 bg-gray-800 rounded-lg border-l-4 border-blue-500">

<div class="text-2xl italic text-gray-300 mb-4">
  "El aprendizaje automático promete transformar amplios segmentos del sector financiero."
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
Actualmente, la mayoría de firmas financieras, incluyendo <v-click>fondos de cobertura</v-click>, <v-click>bancos de inversión y minoristas</v-click>, y <v-click>firmas fintech</v-click>, están adoptando e invirtiendo fuertemente en machine learning.
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

<div class="text-3xl font-bold mb-4">¿Por qué ahora?</div>

<p class="text-base text-gray-700 dark:text-gray-300 mb-5">Machine learning en finanzas se ha vuelto más prominente recientemente debido a:</p>

<div class="grid grid-cols-3 gap-4">

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }"
  class="p-4 rounded-xl border-l-4 border-blue-500 bg-blue-50 dark:bg-blue-900/30 dark:border-blue-400">
  <h3 class="text-base font-semibold mb-2 text-blue-800 dark:text-blue-200">📊 Grandes Volúmenes de Datos</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">El acceso a datos financieros estructurados y no estructurados ha crecido exponencialmente.</p>
</div>

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 350 } }"
  class="p-4 rounded-xl border-l-4 border-purple-500 bg-purple-50 dark:bg-purple-900/30 dark:border-purple-400">
  <h3 class="text-base font-semibold mb-2 text-purple-800 dark:text-purple-200">💻 Poder Computacional Asequible</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">Cloud computing y GPUs han hecho el procesamiento de ML accesible para más organizaciones.</p>
</div>

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 500 } }"
  class="p-4 rounded-xl border-l-4 border-green-500 bg-green-50 dark:bg-green-900/30 dark:border-green-400">
  <h3 class="text-base font-semibold mb-2 text-green-800 dark:text-green-200">📈 Crecimiento Exponencial</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">El uso de data science y ML crece exponencialmente en todas las áreas de finanzas.</p>
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

<div class="text-3xl font-bold mb-4">Los Pilares del Éxito</div>

<p class="text-base text-gray-700 dark:text-gray-300 mb-5">El éxito de machine learning en finanzas depende de:</p>

<div class="grid grid-cols-3 gap-4">

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 200 } }"
  class="p-4 rounded-xl border-l-4 border-blue-500 bg-blue-50 dark:bg-blue-900/30 dark:border-blue-400">
  <h3 class="text-base font-semibold mb-2 text-blue-800 dark:text-blue-200">🏗️ Infraestructura Eficiente</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">Arquitectura escalable y robusta para grandes volúmenes de datos y procesamiento en tiempo real.</p>
</div>

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 350 } }"
  class="p-4 rounded-xl border-l-4 border-purple-500 bg-purple-50 dark:bg-purple-900/30 dark:border-purple-400">
  <h3 class="text-base font-semibold mb-2 text-purple-800 dark:text-purple-200">🛠️ Toolkit Correcto</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">Herramientas, librerías y frameworks apropiados para cada tarea.</p>
</div>

<div
  v-motion
  :initial="{ y: 20, opacity: 0 }"
  :enter="{ y: 0, opacity: 1, transition: { delay: 500 } }"
  class="p-4 rounded-xl border-l-4 border-green-500 bg-green-50 dark:bg-green-900/30 dark:border-green-400">
  <h3 class="text-base font-semibold mb-2 text-green-800 dark:text-green-200">🧠 Algoritmos Correctos</h3>
  <p class="text-sm text-gray-700 dark:text-gray-200">Modelos de ML adecuados para cada problema de negocio.</p>
</div>

</div>

<div
  v-motion
  :initial="{ opacity: 0 }"
  :enter="{ opacity: 1, transition: { delay: 650 } }"
  class="mt-5 py-3 px-4 rounded-lg bg-amber-100 dark:bg-amber-900/40 border border-amber-400/50 dark:border-amber-500/50 text-center">
  <p class="text-sm font-semibold text-amber-900 dark:text-amber-100">Estos conceptos se demuestran y utilizan a lo largo de este curso.</p>
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
layout: cover
background: linear-gradient(135deg, rgb(42, 67, 176) 0%, rgb(128, 1, 255) 100%)
class: text-center
---

<div class="text-blue-900 font-bold- text-6xl">
Machine Learning en Finanzas: 
El Panorama
</div>

<div class="pt-12">
  <span class="text-lg text-blue-900 font-bold- ">Gracias por su atención</span>
</div>


<div class="abs-bl m-6 text-sm text-blue-900 ">
By: OWOC<br>

</div>
