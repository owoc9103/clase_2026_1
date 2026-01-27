---
theme: seriph
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Fundamentos de Programación en Python
  Presentación completa del curso teórico
drawings:
  persist: false
transition: slide-left
mdc: true
title: Fundamentos de Programación en Python
---

# Fundamentos de Programación en Python 🐍

<div class="pt-12">
  <span class="text-6xl opacity-50">Curso Completo</span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://docs.python.org/es/3/tutorial/" target="_blank" alt="Python" title="Python Tutorial">
    <carbon-logo-github />
  </a>
</div>

<div class="abs-bl m-6 text-sm opacity-50">
  Basado en el Tutorial Oficial de Python
</div>

---
layout: default
---

# 📚 Contenido del Curso

<div class="grid grid-cols-2 gap-4 mt-8">

<div v-click="1">

## Clase 1
**Introducción a Python**
- 🐍 ¿Qué es Python?
- 💻 Intérprete de Python
- 🔢 Números y operaciones
- 📝 Strings (texto)
- 📋 Listas básicas

</div>

<div v-click="2">

## Clase 2
**Control de Flujo y Funciones**
- 🔀 Condicionales (if/else)
- 🔄 Bucles (for/while)
- ⚙️ Funciones
- 🎯 Lambda y más

</div>

<div v-click="3">

## Clase 3
**Estructuras de Datos**
- 📊 Listas avanzadas
- 🔗 Tuplas y secuencias
- 🎲 Conjuntos (sets)
- 📖 Diccionarios
- ✨ Comprensiones

</div>

<div v-click="4">

## Clase 4
**Módulos y E/S**
- 📦 Módulos
- 📁 Archivos
- 📄 JSON
- 🎨 Decoradores
- ⚡ Generadores

</div>

<div v-click="5" class="col-span-2">

## Clase 5
**Errores, Clases y Biblioteca Estándar**
- ⚠️ Manejo de errores
- 🏛️ Programación orientada a objetos
- 📚 Biblioteca estándar

</div>

</div>

---
layout: section
class: text-center
---

# Clase 1: Introducción a Python 🐍

<div class="text-4xl mt-8">
  <span v-click="1">¡</span><span v-click="2">Bienvenido</span><span v-click="3"> a Python!</span>
</div>

---
layout: two-cols
---

# ¿Qué es Python? 🐍

<div v-click="1" class="text-xl mb-4">

## Definición Simple

**Python** es un lenguaje de programación que permite escribir instrucciones para que la computadora las ejecute. Es como dar órdenes claras y sencillas a una máquina.

</div>

<div v-click="2" class="mt-4">

**Características principales:**

</div>

<ul class="text-lg mt-2">
  <li v-click="3">✨ <strong>Fácil de leer</strong> - Se parece al lenguaje humano</li>
  <li v-click="4">📊 <strong>Versátil</strong> - Sirve para muchas tareas</li>
  <li v-click="5">🎯 <strong>Poderoso</strong> - Puede hacer cosas complejas</li>
  <li v-click="6">⚡ <strong>Rápido de aprender</strong> - Ideal para principiantes</li>
</ul>

::right::

<div v-click="7" class="mt-8">

<img 
  src="https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" 
  alt="Python Logo"
  class="w-full rounded-lg shadow-lg"
/>

</div>

<div v-click="8" class="mt-4 text-center">

```python
# Python es simple y legible
print("¡Hola, Python!")
# Esto imprime: ¡Hola, Python!
```

</div>

---
layout: center
class: text-center
---

# Usando el Intérprete de Python 💻

<div v-click="1" class="text-xl mb-6">

## ¿Qué es el Intérprete?

El **intérprete de Python** es un programa que lee tu código y lo ejecuta línea por línea. Es como un traductor que convierte tus instrucciones en acciones que la computadora entiende.

</div>

<div v-click="2" class="mt-8">

```python
# Verificar la versión de Python
import sys
print(f"Versión: {sys.version}")
print(f"Info: {sys.version_info}")
```

</div>

<div v-click="3" class="mt-6">

<img 
  src="https://media.giphy.com/media/l46CyJmS9KUbokzs4/giphy.gif" 
  alt="Coding"
  class="w-64 mx-auto rounded-lg"
/>

</div>

<div v-click="4" class="mt-4 text-xl">

En Jupyter Notebook, cada celda ejecuta código Python directamente 🚀

</div>

---
layout: default
---

# Números y Operaciones 🔢

<div v-click="1" class="text-xl mb-4">

## ¿Qué son los Números en Python?

Los **números** son valores que representan cantidades. Python puede trabajar con números enteros (1, 2, 3) y números decimales (3.14, 2.5). Es como usar una calculadora, pero programable.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Operaciones Aritméticas Básicas

```python
# Suma
print(2 + 3)        # 5

# Resta
print(5 - 2)        # 3

# Multiplicación
print(4 * 7)        # 28

# División
print(15 / 3)       # 5.0 (siempre decimal)

# División entera
print(15 // 3)      # 5 (solo parte entera)

# Módulo (resto)
print(17 % 5)       # 2 (resto de la división)

# Potencia
print(2 ** 8)       # 256 (2 elevado a 8)
```

</div>

<div v-click="3">

## Tipos de Números

```python
# Números enteros (int)
entero = 5
print(type(entero))  # <class 'int'>

# Números decimales (float)
decimal = 3.14
print(type(decimal))  # <class 'float'>

# Operaciones mixtas
resultado = entero + decimal
print(resultado)  # 8.14 (siempre float)
```

</div>

</div>

---
layout: default
---

# Variables 🔄

<div v-click="1" class="text-xl mb-4">

## ¿Qué es una Variable?

Una **variable** es como una caja con un nombre donde guardas información. Puedes ponerle cualquier nombre y guardar valores dentro. Es como etiquetar cajas para saber qué contienen.

</div>

<div v-click="2" class="mt-6">

```python
# Crear variables
ancho = 20
alto = 5 * 9
area = ancho * alto

print(f"Ancho: {ancho}")
print(f"Alto: {alto}")
print(f"Área: {area}")

# Las variables pueden cambiar
ancho = 30
print(f"Nuevo ancho: {ancho}")
```

</div>

<div v-click="3" class="mt-6">

## Reglas para Nombres de Variables

```python
# ✅ Correcto
nombre = "Juan"
edad_estudiante = 20
precio_total = 99.99

# ❌ Incorrecto
# 2nombre = "Juan"      # No puede empezar con número
# nombre-estudiante = 20 # No puede tener guiones
# class = "A"           # No puede ser palabra reservada
```

</div>

---
layout: default
---

# Strings (Texto) 📝

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un String?

Un **string** (cadena de texto) es una secuencia de caracteres como letras, números y símbolos. Es como escribir en un papel, pero en Python. Puedes guardar palabras, frases o cualquier texto.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Crear Strings

```python
# Comillas simples
texto1 = 'Hola'

# Comillas dobles
texto2 = "Mundo"

# Comillas triples (múltiples líneas)
texto3 = '''Este es un
texto de múltiples
líneas'''

print(texto1)
print(texto2)
print(texto3)
```

</div>

<div v-click="3">

## Operaciones Básicas con Strings

```python
nombre = "Python"

# Concatenación (unir textos)
print(nombre + " es genial")
# Resultado: Python es genial

# Repetición
print(nombre * 3)
# Resultado: PythonPythonPython

# Longitud
print(len(nombre))
# Resultado: 6
```

</div>

</div>

---
layout: default
---

# Métodos de Strings 📝

<div v-click="1" class="text-xl mb-4">

## ¿Qué son los Métodos?

Los **métodos** son acciones que puedes hacer con un string. Es como tener herramientas especiales para trabajar con texto. Cada método hace algo específico.

</div>

<div v-click="2" class="mt-6">

```python
texto = "  Python es Genial  "

# Convertir a mayúsculas
print(texto.upper())
# Resultado: "  PYTHON ES GENIAL  "

# Convertir a minúsculas
print(texto.lower())
# Resultado: "  python es genial  "

# Capitalizar (primera letra mayúscula)
print(texto.capitalize())
# Resultado: "  python es genial  "

# Título (cada palabra con mayúscula)
print(texto.title())
# Resultado: "  Python Es Genial  "

# Eliminar espacios al inicio y final
print(texto.strip())
# Resultado: "Python es Genial"

# Reemplazar texto
print(texto.replace("Genial", "Increíble"))
# Resultado: "  Python es Increíble  "

# Dividir en lista
print(texto.split())
# Resultado: ['Python', 'es', 'Genial']

# Buscar texto
print(texto.find("Python"))
# Resultado: 2 (posición donde empieza)
```

</div>

---
layout: default
---

# Indexación y Slicing de Strings 🔍

<div v-click="1" class="text-xl mb-4">

## ¿Qué es Indexación?

La **indexación** es acceder a caracteres individuales de un string usando su posición. Es como contar letras desde el inicio. Python cuenta desde 0, no desde 1.

</div>

<div v-click="2" class="mt-6">

```python
texto = "Python"

# Indexación positiva (desde el inicio)
print(texto[0])   # P (primera letra)
print(texto[1])   # y (segunda letra)
print(texto[2])   # t (tercera letra)
print(texto[5])   # n (última letra)

# Indexación negativa (desde el final)
print(texto[-1])  # n (última letra)
print(texto[-2])  # o (penúltima letra)
print(texto[-6])  # P (primera letra)
```

</div>

<div v-click="3" class="mt-6">

## Slicing (Cortar Strings)

```python
texto = "Python"

# Slicing básico [inicio:fin]
print(texto[0:3])    # Pyt (del 0 al 2)
print(texto[2:5])    # tho (del 2 al 4)
print(texto[2:])     # thon (del 2 hasta el final)
print(texto[:3])     # Pyt (del inicio al 2)

# Con pasos [inicio:fin:paso]
print(texto[::2])    # Pto (cada 2 caracteres)
print(texto[::-1])   # nohtyP (invertido)
```

</div>

---
layout: default
---

# Listas 📋

<div v-click="1" class="text-xl mb-4">

## ¿Qué es una Lista?

Una **lista** es un contenedor que guarda múltiples elementos en orden. Es como una caja con compartimentos numerados donde puedes guardar diferentes cosas. Puedes agregar, quitar o cambiar elementos.

</div>

<div v-click="2" class="mt-6">

```python
# Crear listas
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "naranja"]
mixta = [1, "texto", 3.14, True]

# Lista vacía
lista_vacia = []

# Acceder a elementos
print(numeros[0])      # 1 (primer elemento)
print(numeros[-1])     # 5 (último elemento)
print(frutas[1])       # banana
```

</div>

<div v-click="3" class="mt-6">

## Operaciones Básicas con Listas

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenación
print(lista1 + lista2)
# Resultado: [1, 2, 3, 4, 5, 6]

# Repetición
print(lista1 * 2)
# Resultado: [1, 2, 3, 1, 2, 3]

# Longitud
print(len(lista1))
# Resultado: 3

# Verificar si contiene elemento
print(2 in lista1)
# Resultado: True
```

</div>

---
layout: default
---

# Métodos de Listas (Parte 1) 📋

<div v-click="1" class="text-xl mb-4">

## Métodos para Agregar Elementos

</div>

<div v-click="2" class="mt-6">

```python
lista = [1, 2, 3]

# append() - Agregar al final
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# insert() - Insertar en posición específica
lista.insert(0, 0)
print(lista)  # [0, 1, 2, 3, 4]

# extend() - Agregar múltiples elementos
lista.extend([5, 6])
print(lista)  # [0, 1, 2, 3, 4, 5, 6]

# + (operador) - Concatenar listas
lista = lista + [7, 8]
print(lista)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
```

</div>

---
layout: default
---

# Métodos de Listas (Parte 2) 📋

<div v-click="1" class="text-xl mb-4">

## Métodos para Eliminar y Modificar Elementos

</div>

<div v-click="2" class="mt-6">

```python
lista = [1, 2, 3, 4, 5, 3]

# remove() - Eliminar primera ocurrencia
lista.remove(3)
print(lista)  # [1, 2, 4, 5, 3]

# pop() - Eliminar por índice (retorna el valor)
elemento = lista.pop(0)
print(elemento)  # 1
print(lista)     # [2, 4, 5, 3]

# pop() sin índice - Elimina el último
ultimo = lista.pop()
print(ultimo)  # 3
print(lista)   # [2, 4, 5]

# del - Eliminar por índice
del lista[0]
print(lista)  # [4, 5]

# clear() - Vaciar toda la lista
lista.clear()
print(lista)  # []
```

</div>

---
layout: default
---

# Métodos de Listas (Parte 3) 📋

<div v-click="1" class="text-xl mb-4">

## Métodos para Buscar y Ordenar

</div>

<div v-click="2" class="mt-6">

```python
lista = [3, 1, 4, 1, 5, 9, 2, 6]

# index() - Encontrar posición de elemento
posicion = lista.index(4)
print(posicion)  # 2

# count() - Contar ocurrencias
cantidad = lista.count(1)
print(cantidad)  # 2

# sort() - Ordenar la lista (modifica la lista)
lista.sort()
print(lista)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sort() descendente
lista.sort(reverse=True)
print(lista)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() - Ordenar sin modificar (retorna nueva lista)
lista_original = [3, 1, 4]
lista_ordenada = sorted(lista_original)
print(lista_original)  # [3, 1, 4] (sin cambios)
print(lista_ordenada)  # [1, 3, 4]

# reverse() - Invertir orden
lista.reverse()
print(lista)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

</div>

---
layout: section
class: text-center
---

# Clase 2: Control de Flujo y Funciones ⚙️

<div class="text-4xl mt-8">
  <span v-click="1">Toma</span><span v-click="2"> decisiones</span><span v-click="3"> y repite</span>
</div>

---
layout: default
---

# Sentencias Condicionales 🔀

<div v-click="1" class="text-xl mb-4">

## ¿Qué son las Condicionales?

Las **condicionales** permiten que el programa tome decisiones. Es como decir "si esto es cierto, haz esto; si no, haz otra cosa". Es la forma de hacer que el programa "piense" y reaccione según las circunstancias.

</div>

<div v-click="2" class="mt-6">

## if - La Condición Básica

```python
# Estructura básica
x = 10
if x > 5:
    print(f"{x} es mayor que 5")
# Resultado: 10 es mayor que 5

# if-else
edad = 18
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
# Resultado: Es mayor de edad
```

</div>

---
layout: default
---

# if-elif-else 🔀

<div v-click="1" class="text-xl mb-4">

## Múltiples Condiciones

Cuando necesitas verificar varias condiciones en orden, usas **elif** (abreviatura de "else if"). Es como una escalera de decisiones: si la primera no se cumple, prueba la segunda, y así sucesivamente.

</div>

<div v-click="2" class="mt-6">

```python
nota = 85

if nota >= 90:
    calificacion = "A"
    print("Excelente")
elif nota >= 80:
    calificacion = "B"
    print("Muy bien")
elif nota >= 70:
    calificacion = "C"
    print("Bien")
elif nota >= 60:
    calificacion = "D"
    print("Aprobado")
else:
    calificacion = "F"
    print("Reprobado")

print(f"Nota: {nota}, Calificación: {calificacion}")
# Resultado: Nota: 85, Calificación: B
```

</div>

---
layout: default
---

# Operadores de Comparación 🔍

<div v-click="1" class="text-xl mb-4">

## ¿Qué son los Operadores de Comparación?

Los **operadores de comparación** son símbolos que comparan dos valores y devuelven True (verdadero) o False (falso). Es como hacer preguntas: "¿es mayor?", "¿es igual?", etc.

</div>

<div v-click="2" class="mt-6">

```python
a, b = 5, 10

# Igual a
print(a == b)  # False (5 no es igual a 10)

# Diferente de
print(a != b)  # True (5 es diferente de 10)

# Menor que
print(a < b)   # True (5 es menor que 10)

# Mayor que
print(a > b)   # False (5 no es mayor que 10)

# Menor o igual que
print(a <= b)  # True (5 es menor o igual a 10)

# Mayor o igual que
print(a >= b)  # False (5 no es mayor o igual a 10)
```

</div>

---
layout: default
---

# Operadores Lógicos 🧩

<div v-click="1" class="text-xl mb-4">

## ¿Qué son los Operadores Lógicos?

Los **operadores lógicos** combinan condiciones. Es como usar las palabras "y", "o", "no" en español. Te permiten hacer preguntas más complejas.

</div>

<div v-click="2" class="mt-6">

```python
edad = 25
tiene_licencia = True
es_estudiante = True
es_profesor = False

# and (y) - Ambas condiciones deben ser True
if edad >= 18 and tiene_licencia:
    print("Puede conducir")
# Resultado: Puede conducir

# or (o) - Al menos una condición debe ser True
if es_estudiante or es_profesor:
    print("Tiene acceso al campus")
# Resultado: Tiene acceso al campus

# not (no) - Invierte el resultado
if not es_profesor:
    print("No es profesor")
# Resultado: No es profesor

# Combinaciones
if (edad >= 18 and tiene_licencia) or es_profesor:
    print("Puede usar el vehículo")
```

</div>

---
layout: default
---

# Bucles for 🔄

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Bucle for?

Un **bucle for** repite un bloque de código para cada elemento de una secuencia. Es como decir "para cada cosa en esta lista, haz esto". Te ahorra escribir el mismo código muchas veces.

</div>

<div v-click="2" class="mt-6">

```python
# Iterar sobre una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Resultado:
# Me gusta la manzana
# Me gusta la banana
# Me gusta la naranja

# Iterar sobre una cadena
palabra = "Python"
for letra in palabra:
    print(letra, end=" ")
# Resultado: P y t h o n
```

</div>

---
layout: default
---

# enumerate() y range() 🔢

<div v-click="1" class="text-xl mb-4">

## enumerate() - Índice y Valor

**enumerate()** te da tanto el índice (posición) como el valor de cada elemento. Es útil cuando necesitas saber en qué posición estás mientras recorres una lista.

</div>

<div v-click="2" class="mt-6">

```python
# enumerate() - Obtener índice y valor
meses = ["Enero", "Febrero", "Marzo", "Abril"]
for indice, mes in enumerate(meses, start=1):
    print(f"Mes {indice}: {mes}")

# Resultado:
# Mes 1: Enero
# Mes 2: Febrero
# Mes 3: Marzo
# Mes 4: Abril
```

</div>

<div v-click="3" class="mt-6">

## range() - Generar Secuencias de Números

```python
# range(stop) - Del 0 hasta stop-1
for i in range(5):
    print(i, end=" ")
# Resultado: 0 1 2 3 4

# range(start, stop) - Del start hasta stop-1
for i in range(2, 8):
    print(i, end=" ")
# Resultado: 2 3 4 5 6 7

# range(start, stop, step) - Con paso
for i in range(0, 10, 2):
    print(i, end=" ")
# Resultado: 0 2 4 6 8

# range() descendente
for i in range(10, 0, -1):
    print(i, end=" ")
# Resultado: 10 9 8 7 6 5 4 3 2 1
```

</div>

---
layout: default
---

# break y continue 🛑

<div v-click="1" class="text-xl mb-4">

## ¿Qué son break y continue?

**break** detiene completamente el bucle, como decir "ya no sigas". **continue** salta a la siguiente iteración, como decir "omite esto y sigue con el siguiente". Son formas de controlar mejor el flujo del bucle.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## break - Salir del Bucle

```python
# break: salir del bucle
for numero in range(1, 11):
    if numero == 5:
        break  # Sale del bucle
    print(numero, end=" ")
print("\nBucle terminado")

# Resultado:
# 1 2 3 4
# Bucle terminado
```

</div>

<div v-click="3">

## continue - Saltar Iteración

```python
# continue: saltar a la siguiente iteración
for numero in range(1, 11):
    if numero % 2 == 0:  # Si es par
        continue  # Salta números pares
    print(numero, end=" ")
print()

# Resultado: 1 3 5 7 9
# (Solo muestra números impares)
```

</div>

</div>

---
layout: default
---

# Bucle while 🔄

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Bucle while?

Un **bucle while** repite código mientras una condición sea verdadera. Es como decir "mientras esto sea cierto, sigue haciendo esto". Se detiene cuando la condición se vuelve falsa.

</div>

<div v-click="2" class="mt-6">

```python
# Ejemplo: Contador
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar contador

# Resultado:
# Contador: 0
# Contador: 1
# Contador: 2
# Contador: 3
# Contador: 4

# Ejemplo: Secuencia de Fibonacci
a, b = 0, 1
while a < 10:
    print(a, end=' ')
    a, b = b, a + b
print()
# Resultado: 0 1 1 2 3 5 8
```

</div>

---
layout: default
---

# Funciones ⚙️

<div v-click="1" class="text-xl mb-4">

## ¿Qué es una Función?

Una **función** es un bloque de código reutilizable con un nombre. Es como una receta: defines los pasos una vez y luego puedes usarla cuantas veces quieras. Te ahorra repetir código.

</div>

<div v-click="2" class="mt-6">

```python
# Función simple (sin parámetros)
def saludar():
    print("¡Hola, Python!")

# Llamar la función
saludar()
# Resultado: ¡Hola, Python!

# Función con parámetros
def saludar_persona(nombre):
    print(f"¡Hola, {nombre}!")

saludar_persona("María")
# Resultado: ¡Hola, María!

# Función con múltiples parámetros
def calcular_area(ancho, alto):
    area = ancho * alto
    return area

resultado = calcular_area(5, 10)
print(f"Área: {resultado}")
# Resultado: Área: 50
```

</div>

---
layout: default
---

# Parámetros y Valores por Defecto 🎯

<div v-click="1" class="text-xl mb-4">

## Valores por Defecto

Los **valores por defecto** permiten que algunos parámetros sean opcionales. Si no los proporcionas, Python usa el valor predeterminado. Es como tener opciones preestablecidas.

</div>

<div v-click="2" class="mt-6">

```python
# Función con valor por defecto
def potencia(base, exponente=2):
    """
    Calcula la potencia de un número.
    Si no se especifica exponente, usa 2 (cuadrado).
    """
    return base ** exponente

# Usar con ambos parámetros
print(potencia(2, 3))  # 8 (2^3)

# Usar solo con base (usa exponente=2 por defecto)
print(potencia(5))     # 25 (5^2)

# También puedes especificar por nombre
print(potencia(base=3, exponente=4))  # 81
```

</div>

---
layout: default
---

# *args y **kwargs 🌟

<div v-click="1" class="text-xl mb-4">

## Argumentos Arbitrarios

**\*args** permite pasar cualquier cantidad de argumentos posicionales. **\*\*kwargs** permite pasar cualquier cantidad de argumentos con nombre. Es como tener una función flexible que acepta cualquier cantidad de datos.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## *args - Argumentos Posicionales

```python
# *args: argumentos posicionales arbitrarios
def sumar(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar(1, 2, 3))        # 6
print(sumar(1, 2, 3, 4, 5))  # 15
print(sumar(10))              # 10
```

</div>

<div v-click="3">

## **kwargs - Argumentos con Nombre

```python
# **kwargs: argumentos de palabra clave
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Pedro", edad=28, ciudad="Cali")
# Resultado:
# nombre: Pedro
# edad: 28
# ciudad: Cali
```

</div>

</div>

---
layout: default
---

# Expresiones Lambda ⚡

<div v-click="1" class="text-xl mb-4">

## ¿Qué es Lambda?

**Lambda** es una forma de crear funciones pequeñas y anónimas (sin nombre) en una sola línea. Es como una función mini que defines y usas inmediatamente. Útil para operaciones simples.

</div>

<div v-click="2" class="mt-6">

```python
# Función lambda simple
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # 25

# Lambda con múltiples parámetros
sumar = lambda a, b: a + b
print(sumar(3, 4))  # 7

# Lambda con condicional
mayor = lambda x, y: x if x > y else y
print(mayor(5, 3))  # 5
```

</div>

<div v-click="3" class="mt-6">

## Lambda con map() y filter()

```python
numeros = [1, 2, 3, 4, 5]

# map() - Aplicar función a cada elemento
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]

# filter() - Filtrar elementos
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# Combinar
cuadrados_pares = list(map(lambda x: x**2, 
                          filter(lambda x: x % 2 == 0, numeros)))
print(cuadrados_pares)  # [4, 16]
```

</div>

---
layout: section
class: text-center
---

# Clase 3: Estructuras de Datos 📊

<div class="text-4xl mt-8">
  <span v-click="1">Organiza</span><span v-click="2"> tus datos</span>
</div>

---
layout: default
---

# Comprensión de Listas ✨

<div v-click="1" class="text-xl mb-4">

## ¿Qué es la Comprensión de Listas?

La **comprensión de listas** es una forma elegante y corta de crear listas. En lugar de escribir varias líneas con un bucle, puedes crear la lista en una sola línea. Es como una receta compacta para hacer listas.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Forma Tradicional vs Comprensión

```python
# Forma tradicional (3 líneas)
cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

# Con comprensión de listas (1 línea)
cuadrados = [x**2 for x in range(10)]

# Ambas producen: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

</div>

<div v-click="3">

## Comprensión con Condición

```python
# Números pares del 0 al 19
pares = [x for x in range(20) if x % 2 == 0]
# Resultado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Cuadrados de números pares
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
# Resultado: [0, 4, 16, 36, 64]
```

</div>

</div>

---
layout: default
---

# Comprensión Anidada 🔄

<div v-click="1" class="text-xl mb-4">

## Comprensiones dentro de Comprensiones

Puedes poner una comprensión dentro de otra para crear estructuras más complejas, como matrices o listas de listas. Es como hacer listas dentro de listas de forma compacta.

</div>

<div v-click="2" class="mt-6">

```python
# Matriz usando comprensión anidada
matriz = [[i*j for j in range(1, 4)] 
          for i in range(1, 4)]

# Resultado:
# [[1, 2, 3],   # 1*1, 1*2, 1*3
#  [2, 4, 6],   # 2*1, 2*2, 2*3
#  [3, 6, 9]]   # 3*1, 3*2, 3*3

# Tabla de multiplicar
tabla = [[f"{i}x{j}={i*j}" for j in range(1, 6)] 
         for i in range(1, 6)]
```

</div>

---
layout: default
---

# Tuplas 🔗

<div v-click="1" class="text-xl mb-4">

## ¿Qué es una Tupla?

Una **tupla** es como una lista, pero **inmutable** (no se puede cambiar después de crearla). Es como una lista congelada. Útil cuando quieres asegurarte de que los datos no cambien accidentalmente.

</div>

<div v-click="2" class="mt-6">

```python
# Crear tuplas
tupla = (1, 2, 3)
print("Tupla:", tupla)  # (1, 2, 3)
print("Tipo:", type(tupla))  # <class 'tuple'>

# Tupla con un elemento (necesita coma)
tupla_simple = (42,)
print(tupla_simple)  # (42,)

# Desempaquetado (asignar a variables)
x, y, z = tupla
print(f"x={x}, y={y}, z={z}")  # x=1, y=2, z=3

# Acceder a elementos (igual que listas)
print(tupla[0])   # 1
print(tupla[-1])  # 3
```

</div>

<div v-click="3" class="mt-6">

## Tuplas como Claves en Diccionarios

```python
# Las tuplas pueden ser claves (porque son inmutables)
coordenadas = {
    (0, 0): "Origen",
    (1, 2): "Punto A",
    (3, 4): "Punto B"
}

print(coordenadas[(1, 2)])  # Punto A
```

</div>

---
layout: default
---

# Conjuntos (Sets) 🎲

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Conjunto?

Un **conjunto** es una colección de elementos **únicos** y **desordenados**. No puede tener duplicados. Es como una bolsa donde cada cosa solo puede estar una vez. Útil para eliminar duplicados o verificar pertenencia rápidamente.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Crear y Usar Conjuntos

```python
# Crear conjuntos
frutas = {"manzana", "banana", "naranja"}
print(frutas)  # {'manzana', 'banana', 'naranja'}

# Agregar elementos
frutas.add("uva")
print(frutas)  # {'manzana', 'banana', 'naranja', 'uva'}

# Eliminar elementos
frutas.remove("banana")
print(frutas)  # {'manzana', 'naranja', 'uva'}

# Los duplicados se eliminan automáticamente
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3}
```

</div>

<div v-click="3">

## Operaciones con Conjuntos

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# Unión (todos los elementos)
print(a | b)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección (elementos comunes)
print(a & b)  # {4, 5}

# Diferencia (solo en a, no en b)
print(a - b)  # {1, 2, 3}

# Diferencia simétrica (en uno u otro, no en ambos)
print(a ^ b)  # {1, 2, 3, 6, 7, 8}
```

</div>

</div>

---
layout: default
---

# Métodos de Conjuntos 🎲

<div v-click="1" class="text-xl mb-4">

## Métodos Disponibles para Conjuntos

</div>

<div v-click="2" class="mt-6">

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Agregar elementos
a.add(4)           # Agregar un elemento
a.update([5, 6])   # Agregar múltiples elementos

# Eliminar elementos
a.remove(1)        # Eliminar (error si no existe)
a.discard(2)       # Eliminar (sin error si no existe)
a.pop()           # Eliminar y retornar elemento aleatorio
a.clear()         # Vaciar el conjunto

# Verificar pertenencia
print(3 in a)     # True
print(10 in a)    # False

# Operaciones de conjunto
a.union(b)        # Equivalente a a | b
a.intersection(b) # Equivalente a a & b
a.difference(b)   # Equivalente a a - b
a.symmetric_difference(b)  # Equivalente a a ^ b

# Verificar relaciones
a.issubset(b)     # ¿a es subconjunto de b?
a.issuperset(b)   # ¿a es superconjunto de b?
a.isdisjoint(b)   # ¿a y b no tienen elementos comunes?
```

</div>

---
layout: default
---

# Diccionarios 📖

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Diccionario?

Un **diccionario** almacena pares de **clave-valor**. Es como un diccionario real: buscas una palabra (clave) y encuentras su significado (valor). Cada clave es única y te permite acceder rápidamente a su valor asociado.

</div>

<div v-click="2" class="mt-6">

```python
# Crear diccionarios
telefonos = {
    "Juan": "123-4567",
    "María": "234-5678",
    "Pedro": "345-6789"
}

# Acceder a valores
print(telefonos["Juan"])  # 123-4567

# Agregar/modificar
telefonos["Ana"] = "456-7890"
telefonos["Juan"] = "999-9999"  # Modificar

# Eliminar
del telefonos["Pedro"]

print(telefonos)
# Resultado: {'Juan': '999-9999', 'María': '234-5678', 'Ana': '456-7890'}
```

</div>

---
layout: default
---

# Métodos de Diccionarios (Parte 1) 📖

<div v-click="1" class="text-xl mb-4">

## Métodos para Acceder y Modificar

</div>

<div v-click="2" class="mt-6">

```python
persona = {"nombre": "Carlos", "edad": 30, "ciudad": "Bogotá"}

# Obtener claves
claves = list(persona.keys())
print(claves)  # ['nombre', 'edad', 'ciudad']

# Obtener valores
valores = list(persona.values())
print(valores)  # ['Carlos', 30, 'Bogotá']

# Obtener pares clave-valor
items = list(persona.items())
print(items)  # [('nombre', 'Carlos'), ('edad', 30), ('ciudad', 'Bogotá')]

# get() - Obtener valor con valor por defecto
edad = persona.get("edad", "No especificada")
email = persona.get("email", "No especificado")
print(edad)   # 30
print(email)  # No especificado
```

</div>

---
layout: default
---

# Métodos de Diccionarios (Parte 2) 📖

<div v-click="1" class="text-xl mb-4">

## Métodos para Modificar y Actualizar

</div>

<div v-click="2" class="mt-6">

```python
persona = {"nombre": "Carlos", "edad": 30}

# update() - Actualizar con otro diccionario
persona.update({"ciudad": "Bogotá", "edad": 31})
print(persona)  # {'nombre': 'Carlos', 'edad': 31, 'ciudad': 'Bogotá'}

# pop() - Eliminar y retornar valor
edad = persona.pop("edad")
print(edad)     # 31
print(persona)  # {'nombre': 'Carlos', 'ciudad': 'Bogotá'}

# popitem() - Eliminar y retornar último par
ultimo = persona.popitem()
print(ultimo)   # ('ciudad', 'Bogotá')
print(persona)  # {'nombre': 'Carlos'}

# setdefault() - Obtener valor o establecer si no existe
ciudad = persona.setdefault("ciudad", "Desconocida")
print(ciudad)   # Desconocida
print(persona)  # {'nombre': 'Carlos', 'ciudad': 'Desconocida'}

# clear() - Vaciar diccionario
persona.clear()
print(persona)  # {}
```

</div>

---
layout: default
---

# Comprensión de Diccionarios ✨

<div v-click="1" class="text-xl mb-4">

## Crear Diccionarios de Forma Compacta

La **comprensión de diccionarios** es como la comprensión de listas, pero para diccionarios. Te permite crear diccionarios de forma elegante en una sola línea.

</div>

<div v-click="2" class="mt-6">

```python
# Diccionario de cuadrados
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(cuadrados_dict)
# Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condición
pares_dict = {x: x*2 for x in range(1, 11) if x % 2 == 0}
print(pares_dict)
# Resultado: {2: 4, 4: 8, 6: 12, 8: 16, 10: 20}

# Invertir clave-valor
original = {"a": 1, "b": 2, "c": 3}
invertido = {valor: clave for clave, valor in original.items()}
print(invertido)
# Resultado: {1: 'a', 2: 'b', 3: 'c'}
```

</div>

---
layout: default
---

# Técnicas de Iteración 🔄

<div v-click="1" class="text-xl mb-4">

## zip() - Iterar Múltiples Secuencias

**zip()** combina múltiples listas en pares. Es como abrochar una cremallera: une elementos de la misma posición de diferentes listas. Útil cuando tienes datos relacionados en listas separadas.

</div>

<div v-click="2" class="mt-6">

```python
# zip() - Iterar sobre múltiples secuencias
nombres = ["Ana", "Luis", "Carmen"]
edades = [25, 30, 28]
ciudades = ["Bogotá", "Medellín", "Cali"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre}, {edad} años, de {ciudad}")

# Resultado:
# Ana, 25 años, de Bogotá
# Luis, 30 años, de Medellín
# Carmen, 28 años, de Cali

# Convertir a lista de tuplas
combinado = list(zip(nombres, edades, ciudades))
print(combinado)
# [('Ana', 25, 'Bogotá'), ('Luis', 30, 'Medellín'), ('Carmen', 28, 'Cali')]
```

</div>

---
layout: default
---

# enumerate() y sorted() 🔍

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="1">

## enumerate() - Índice y Valor

```python
meses = ["Enero", "Febrero", "Marzo"]

for indice, mes in enumerate(meses, start=1):
    print(f"Mes {indice}: {mes}")

# Resultado:
# Mes 1: Enero
# Mes 2: Febrero
# Mes 3: Marzo
```

</div>

<div v-click="2">

## sorted() - Ordenar

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Ordenar ascendente
print(sorted(numeros))
# [1, 1, 2, 3, 4, 5, 6, 9]

# Ordenar descendente
print(sorted(numeros, reverse=True))
# [9, 6, 5, 4, 3, 2, 1, 1]

# Ordenar diccionario por valor
ventas = {"A": 150, "B": 200, "C": 120}
ventas_ordenadas = sorted(ventas.items(), 
                         key=lambda x: x[1], 
                         reverse=True)
print(ventas_ordenadas)
# [('B', 200), ('A', 150), ('C', 120)]
```

</div>

</div>

---
layout: section
class: text-center
---

# Clase 4: Módulos y Entrada/Salida 📦

<div class="text-4xl mt-8">
  <span v-click="1">Organiza</span><span v-click="2"> tu código</span>
</div>

---
layout: default
---

# Módulos 📦

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Módulo?

Un **módulo** es un archivo que contiene código Python que puedes reutilizar. Es como tener una caja de herramientas: guardas funciones útiles en un archivo y las usas cuando las necesitas. Te permite organizar y reutilizar código.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Importar Módulos

```python
# Importar módulo completo
import math
print(f"Pi: {math.pi}")
print(f"Raíz: {math.sqrt(16)}")

# Importar funciones específicas
from math import sqrt, pow, pi
print(f"Pi: {pi}")
print(f"Raíz: {sqrt(25)}")

# Importar con alias
import datetime as dt
fecha = dt.datetime.now()
print(fecha)
```

</div>

<div v-click="3">

## Crear Módulos Propios

```python
# Guardar en: finanzas.py
def calcular_interes_simple(principal, tasa, tiempo):
    """Calcula interés simple."""
    return principal * tasa * tiempo

def calcular_interes_compuesto(principal, tasa, tiempo):
    """Calcula interés compuesto."""
    return principal * (1 + tasa) ** tiempo - principal

# Para usar en otro archivo:
# import finanzas
# resultado = finanzas.calcular_interes_simple(1000, 0.05, 2)
```

</div>

</div>

---
layout: default
---

# Módulos Estándar Útiles 🛠️

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="1">

## datetime - Trabajar con Fechas

```python
from datetime import datetime, timedelta

hoy = datetime.now()
print(f"Hoy: {hoy}")
print(f"Formato: {hoy.strftime('%Y-%m-%d %H:%M:%S')}")

mañana = hoy + timedelta(days=1)
print(f"Mañana: {mañana.date()}")

# Crear fecha específica
fecha = datetime(2024, 1, 15)
print(f"Fecha: {fecha}")
```

</div>

<div v-click="2">

## collections - Estructuras Avanzadas

```python
from collections import defaultdict, Counter

# defaultdict - diccionario con valor por defecto
gastos = defaultdict(list)
gastos["Alimentación"].append(350)
gastos["Transporte"].append(120)
print(dict(gastos))

# Counter - contar elementos
transacciones = ["Ingreso", "Egreso", "Ingreso", "Ingreso"]
contador = Counter(transacciones)
print(contador)
# Counter({'Ingreso': 3, 'Egreso': 1})
```

</div>

</div>

---
layout: default
---

# Formateo de Salida 📝

<div v-click="1" class="text-xl mb-4">

## ¿Qué es el Formateo?

El **formateo** es dar formato a los datos cuando los muestras. Es como decorar un pastel: tomas los datos y los presentas de forma bonita y legible. Python tiene varias formas de hacerlo.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## f-strings (Python 3.6+)

```python
nombre = "María"
edad = 30
saldo = 5000.50

# f-string básico
mensaje = f"{nombre} tiene {edad} años"
print(mensaje)

# Con formato de números
mensaje = f"Saldo: ${saldo:,.2f}"
print(mensaje)  # Saldo: $5,000.50

# Con expresiones
print(f"En 10 años tendrá {edad + 10} años")
```

</div>

<div v-click="3">

## format() Method

```python
# Con nombres
texto = "El precio es {precio:.2f} y la cantidad es {cantidad}"
print(texto.format(precio=99.99, cantidad=5))

# Con índices
print("Coordenadas: ({0}, {1})".format(10, 20))

# Con formato
print("{:>10}".format("derecha"))   # Alineado a la derecha
print("{:<10}".format("izquierda")) # Alineado a la izquierda
print("{:^10}".format("centro"))    # Centrado
```

</div>

</div>

---
layout: default
---

# Archivos 📁

<div v-click="1" class="text-xl mb-4">

## ¿Qué es Trabajar con Archivos?

Trabajar con **archivos** significa leer y escribir datos en archivos de texto. Es como leer y escribir en un cuaderno: puedes guardar información para usarla después o leer información que guardaste antes.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Escribir Archivos

```python
# Escribir archivo
contenido = """Línea 1
Línea 2
Línea 3"""

with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write(contenido)

print("Archivo escrito exitosamente")

# Modos de apertura:
# "r" - leer (read)
# "w" - escribir (write, sobrescribe)
# "a" - agregar (append, añade al final)
# "x" - crear (solo si no existe)
```

</div>

<div v-click="3">

## Leer Archivos

```python
# Leer archivo completo
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo, 1):
        print(f"{i}: {linea.strip()}")

# Leer todas las líneas en lista
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print(f"Total: {len(lineas)} líneas")
```

</div>

</div>

---
layout: default
---

# JSON 📄

<div v-click="1" class="text-xl mb-4">

## ¿Qué es JSON?

**JSON** (JavaScript Object Notation) es un formato para guardar datos estructurados. Es como un diccionario de Python pero en formato de texto que cualquier programa puede leer. Muy útil para guardar configuraciones o datos.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Guardar JSON

```python
import json

datos_financieros = {
    "cliente": "Juan Pérez",
    "saldo": 5000.50,
    "transacciones": [
        {"fecha": "2024-01-15", "tipo": "Ingreso", "monto": 1000},
        {"fecha": "2024-01-20", "tipo": "Egreso", "monto": -500}
    ]
}

# Escribir JSON
with open("datos.json", "w", encoding="utf-8") as archivo:
    json.dump(datos_financieros, archivo, indent=2, ensure_ascii=False)

print("JSON guardado exitosamente")
```

</div>

<div v-click="3">

## Leer JSON

```python
import json

# Leer JSON
with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    print("Datos cargados:")
    print(json.dumps(datos, indent=2, ensure_ascii=False))

# Acceder a datos
print(f"Cliente: {datos['cliente']}")
print(f"Saldo: ${datos['saldo']:,.2f}")
print(f"Transacciones: {len(datos['transacciones'])}")
```

</div>

</div>

---
layout: default
---

# Decoradores 🎨

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Decorador?

Un **decorador** es una función que modifica o mejora otra función sin cambiar su código. Es como ponerle un adorno a algo: la cosa original sigue igual, pero ahora tiene algo extra. Útil para agregar funcionalidad como medir tiempo, validar datos, etc.

</div>

<div v-click="2" class="mt-6">

```python
# Decorador simple para medir tiempo
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        import time
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

# Usar decorador
@medir_tiempo
def calcular_cuadrados(n):
    return [x**2 for x in range(n)]

# Al llamar la función, automáticamente mide el tiempo
resultado = calcular_cuadrados(1000000)
```

</div>

---
layout: default
---

# Generadores ⚡

<div v-click="1" class="text-xl mb-4">

## ¿Qué es un Generador?

Un **generador** es una función que produce valores uno por uno en lugar de crear una lista completa. Es como una máquina expendedora: cada vez que pides algo, te da el siguiente, sin tener que preparar todo de antemano. Ahorra memoria.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## Generador con yield

```python
# Generador simple
def numeros_pares(n):
    for i in range(n):
        if i % 2 == 0:
            yield i  # Produce valor y pausa

# Usar generador
for num in numeros_pares(10):
    print(num, end=" ")
# Resultado: 0 2 4 6 8

# Convertir a lista
lista = list(numeros_pares(10))
print(lista)  # [0, 2, 4, 6, 8]
```

</div>

<div v-click="3">

## Expresión Generadora

```python
# Expresión generadora (similar a comprensión)
cuadrados = (x**2 for x in range(10))
print(cuadrados)  # <generator object>

# Convertir a lista
print(list(cuadrados))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Ventaja: usa menos memoria
# Útil para grandes cantidades de datos
```

</div>

</div>

---
layout: section
class: text-center
---

# Clase 5: Errores, Clases y Biblioteca Estándar ⚠️

<div class="text-4xl mt-8">
  <span v-click="1">Programa</span><span v-click="2"> robusto</span>
</div>

---
layout: default
---

# Manejo de Errores ⚠️

<div v-click="1" class="text-xl mb-4">

## ¿Qué es el Manejo de Errores?

El **manejo de errores** es preparar tu programa para cuando algo salga mal. Es como tener un plan B: si algo falla, el programa no se rompe, sino que maneja el error de forma elegante y continúa funcionando.

</div>

<div class="grid grid-cols-2 gap-4 mt-4">

<div v-click="2">

## try-except Básico

```python
# try-except básico
def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("No se puede dividir por cero")
        return None

print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # None (con mensaje)
```

</div>

<div v-click="3">

## Múltiples Excepciones

```python
def procesar_numero(texto):
    try:
        numero = float(texto)
        resultado = 100 / numero
        return resultado
    except ValueError:
        print("Error: No es un número válido")
        return None
    except ZeroDivisionError:
        print("Error: División por cero")
        return None

procesar_numero("10")   # 10.0
procesar_numero("abc")  # None (ValueError)
procesar_numero("0")    # None (ZeroDivisionError)
```

</div>

</div>

---
layout: default
---

# try-except-else-finally 🔄

<div v-click="1" class="text-xl mb-4">

## Estructura Completa de Manejo de Errores

</div>

<div v-click="2" class="mt-6">

```python
def leer_archivo(nombre):
    try:
        archivo = open(nombre, "r")
        contenido = archivo.read()
    except FileNotFoundError:
        print(f"Error: Archivo {nombre} no encontrado")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None
    else:
        # Se ejecuta si NO hay errores
        print("Archivo leído exitosamente")
        return contenido
    finally:
        # Siempre se ejecuta (con o sin errores)
        print("Operación finalizada")
        archivo.close()

# Nota: En la práctica, usa 'with' para archivos
# with open(nombre, "r") as archivo:
#     contenido = archivo.read()
```

</div>

---
layout: default
---

# Excepciones Personalizadas 🎯

<div v-click="1" class="text-xl mb-4">

## ¿Qué son las Excepciones Personalizadas?

Las **excepciones personalizadas** son errores que tú defines para situaciones específicas de tu programa. Es como crear tus propias señales de advertencia personalizadas para tu aplicación.

</div>

<div v-click="2" class="mt-6">

```python
# Crear excepción personalizada
class SaldoInsuficienteError(Exception):
    """Excepción para saldo insuficiente."""
    pass

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(
            f"Saldo insuficiente. Tienes ${saldo}, intentas retirar ${monto}"
        )
    return saldo - monto

# Usar excepción personalizada
try:
    nuevo_saldo = retirar(100, 150)
except SaldoInsuficienteError as e:
    print(f"Error: {e}")
# Resultado: Error: Saldo insuficiente. Tienes $100, intentas retirar $150
```

</div>

---
layout: default
---

# Clases y Objetos 🏛️

<div v-click="1" class="text-xl mb-4">

## ¿Qué es una Clase?

Una **clase** es un molde o plantilla para crear objetos. Es como un plano de una casa: defines cómo debe ser (atributos) y qué puede hacer (métodos), y luego puedes crear muchas casas (objetos) usando ese mismo plano.

</div>

<div v-click="2" class="mt-6">

```python
# Clase simple
class CuentaBancaria:
    """Clase que representa una cuenta bancaria."""
    
    def __init__(self, titular, saldo_inicial=0):
        """Inicializa la cuenta (constructor)."""
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        """Deposita dinero en la cuenta."""
        if monto > 0:
            self.saldo += monto
            return True
        return False
    
    def retirar(self, monto):
        """Retira dinero de la cuenta."""
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            return True
        return False
    
    def consultar_saldo(self):
        """Consulta el saldo actual."""
        return self.saldo
    
    def __str__(self):
        """Representación en string."""
        return f"Cuenta de {self.titular}: ${self.saldo:,.2f}"
```

</div>

---
layout: default
---

# Usar Clases 🏛️

<div v-click="1" class="text-xl mb-4">

## Crear y Usar Objetos

</div>

<div v-click="2" class="mt-6">

```python
# Crear instancia (objeto) de la clase
cuenta = CuentaBancaria("Juan Pérez", 1000)
print(cuenta)
# Resultado: Cuenta de Juan Pérez: $1,000.00

# Usar métodos
cuenta.depositar(500)
print(f"Saldo: ${cuenta.consultar_saldo():,.2f}")
# Resultado: Saldo: $1,500.00

cuenta.retirar(200)
print(f"Saldo: ${cuenta.consultar_saldo():,.2f}")
# Resultado: Saldo: $1,300.00

# Crear múltiples objetos
cuenta2 = CuentaBancaria("María González", 500)
print(cuenta2)
# Resultado: Cuenta de María González: $500.00

# Cada objeto es independiente
print(cuenta.saldo)   # 1300
print(cuenta2.saldo)  # 500
```

</div>

---
layout: default
---

# Herencia 🔄

<div v-click="1" class="text-xl mb-4">

## ¿Qué es la Herencia?

La **herencia** permite crear una nueva clase basada en una clase existente. Es como heredar características: la nueva clase tiene todo lo de la clase padre, pero puedes agregar o modificar cosas. Útil para evitar repetir código.

</div>

<div v-click="2" class="mt-6">

```python
# Clase base (padre)
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

# Clase derivada (hija) - Hereda de CuentaBancaria
class CuentaAhorros(CuentaBancaria):
    """Cuenta de ahorros con interés."""
    
    def __init__(self, titular, saldo_inicial=0, tasa_interes=0.02):
        super().__init__(titular, saldo_inicial)  # Llamar al constructor padre
        self.tasa_interes = tasa_interes
    
    def aplicar_interes(self):
        """Aplica interés al saldo."""
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        return interes

# Usar clase heredada
cuenta_ahorros = CuentaAhorros("María González", 1000, 0.03)
print(cuenta_ahorros)  # Usa __str__ de la clase padre
interes = cuenta_ahorros.aplicar_interes()
print(f"Interés: ${interes:,.2f}")
print(f"Nuevo saldo: ${cuenta_ahorros.consultar_saldo():,.2f}")
```

</div>

---
layout: default
---

# Biblioteca Estándar - math 📐

<div v-click="1" class="text-xl mb-4">

## Módulo math - Funciones Matemáticas

El módulo **math** contiene funciones matemáticas útiles. Es como tener una calculadora científica dentro de Python.

</div>

<div v-click="2" class="mt-6">

```python
import math

# Constantes
print(f"Pi: {math.pi}")        # 3.141592653589793
print(f"e: {math.e}")          # 2.718281828459045

# Funciones básicas
print(f"Raíz cuadrada: {math.sqrt(16)}")      # 4.0
print(f"Potencia: {math.pow(2, 3)}")          # 8.0
print(f"Valor absoluto: {math.fabs(-5)}")     # 5.0

# Funciones trigonométricas
print(f"Seno: {math.sin(math.pi/2)}")         # 1.0
print(f"Coseno: {math.cos(0)}")               # 1.0
print(f"Tangente: {math.tan(math.pi/4)}")     # 1.0

# Logaritmos
print(f"Logaritmo natural: {math.log(10)}")   # 2.302585092994046
print(f"Logaritmo base 10: {math.log10(100)}") # 2.0

# Redondeo
print(f"Redondear arriba: {math.ceil(4.3)}")   # 5
print(f"Redondear abajo: {math.floor(4.7)}")  # 4
```

</div>

---
layout: default
---

# Biblioteca Estándar - datetime 📅

<div v-click="1" class="text-xl mb-4">

## Módulo datetime - Trabajar con Fechas

El módulo **datetime** permite trabajar con fechas y horas. Es como tener un calendario y reloj programable.

</div>

<div v-click="2" class="mt-6">

```python
from datetime import datetime, timedelta

# Fecha y hora actual
hoy = datetime.now()
print(f"Hoy: {hoy}")
print(f"Año: {hoy.year}, Mes: {hoy.month}, Día: {hoy.day}")

# Crear fecha específica
fecha = datetime(2024, 1, 15, 14, 30, 0)
print(f"Fecha: {fecha}")

# Operaciones con fechas
mañana = hoy + timedelta(days=1)
print(f"Mañana: {mañana.date()}")

semana_pasada = hoy - timedelta(weeks=1)
print(f"Semana pasada: {semana_pasada.date()}")

# Formatear fecha
print(f"Formato: {hoy.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Día de la semana: {hoy.strftime('%A')}")
print(f"Mes: {hoy.strftime('%B')}")
```

</div>

---
layout: default
---

# Biblioteca Estándar - time ⏱️

<div v-click="1" class="text-xl mb-4">

## Módulo time - Medición de Tiempo

El módulo **time** permite medir tiempo de ejecución y trabajar con tiempo. Útil para saber cuánto tarda tu código en ejecutarse.

</div>

<div v-click="2" class="mt-6">

```python
import time

# Medir tiempo de ejecución
inicio = time.time()

# Simular operación
suma = sum(range(1000000))

fin = time.time()
tiempo_transcurrido = fin - inicio

print(f"Tiempo: {tiempo_transcurrido:.4f} segundos")
print(f"Resultado: {suma}")

# Obtener tiempo actual
tiempo_actual = time.time()
print(f"Tiempo Unix: {tiempo_actual}")

# Convertir a formato legible
tiempo_legible = time.ctime(tiempo_actual)
print(f"Tiempo legible: {tiempo_legible}")

# Pausar ejecución
print("Esperando 2 segundos...")
time.sleep(2)
print("¡Listo!")
```

</div>

---
layout: center
class: text-center
---

# 🎉 ¡Felicidades! 🎉

<div class="text-6xl mt-8 mb-8">

Has completado el curso de

**Fundamentos de Programación en Python**

</div>

<div v-click="1" class="text-2xl mt-8">

## Lo que has aprendido:

</div>

<div v-click="2" class="grid grid-cols-3 gap-4 mt-6 text-xl">

<div>✅ Fundamentos de Python</div>
<div>✅ Estructuras de datos</div>
<div>✅ Control de flujo</div>
<div>✅ Funciones y módulos</div>
<div>✅ Archivos y JSON</div>
<div>✅ Programación orientada a objetos</div>
<div>✅ Manejo de errores</div>
<div>✅ Biblioteca estándar</div>
<div>✅ Aplicaciones financieras</div>

</div>

<div v-click="3" class="mt-8">

<img 
  src="https://media.giphy.com/media/3o7aD2saQq1sJ6L5xu/giphy.gif" 
  alt="Success"
  class="w-64 mx-auto rounded-lg"
/>

</div>

---
layout: center
class: text-center
---

# 📚 Próximos Pasos

<div v-click="1" class="text-3xl mt-8">

## Continúa aprendiendo:

</div>

<div v-click="2" class="grid grid-cols-2 gap-6 mt-8 text-xl">

<div>

- 📊 **Pandas** - Análisis de datos
- 🔢 **NumPy** - Computación numérica
- 📈 **Matplotlib** - Visualización
- 🤖 **Machine Learning** - Scikit-learn

</div>

<div>

- 💰 **Finanzas** - Aplicaciones avanzadas
- 🌐 **APIs** - Integración de datos
- 🗄️ **Bases de datos** - SQL y NoSQL
- 🚀 **Proyectos** - Practica con casos reales

</div>

</div>

<div v-click="3" class="mt-8 text-2xl">

**¡Sigue programando y explorando!** 🚀

</div>

<div v-click="4" class="mt-6">

<img 
  src="https://media.giphy.com/media/l46CyJmS9KUbokzs4/giphy.gif" 
  alt="Keep Learning"
  class="w-48 mx-auto rounded-lg"
/>

</div>

---
layout: end
class: text-center
---

# Gracias por tu atención 🙏

<div class="text-4xl mt-8">

**Fundamentos de Programación en Python**

</div>

<div class="text-2xl mt-6 opacity-70">

Basado en el Tutorial Oficial de Python

</div>

<div class="mt-8">

[📖 Documentación Python](https://docs.python.org/es/3/tutorial/) · 
[🐍 Python.org](https://www.python.org/)

</div>
