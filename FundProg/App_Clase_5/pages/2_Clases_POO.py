# -*- coding: utf-8 -*-
"""
Página: Clases y Programación Orientada a Objetos
Clase 5 - Fundamentos de Programación
"""

import streamlit as st
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.code_executor import ejecutar_codigo
from utils.preguntas import pregunta_con_ampliar
from utils.theme import inject_theme_styles

st.set_page_config(page_title="Clases y POO", page_icon="🏛️", layout="wide")
inject_theme_styles()

st.title("🏛️ Clases y Programación Orientada a Objetos")
st.markdown("---")

tab_teoria, tab_preguntas, tab_ejercicio_ia, tab_codigo = st.tabs([
    "📖 Teoría", "❓ Preguntas", "🤖 Ejercicio con IA", "💻 Editor de Código"
])

with tab_teoria:
    st.header("9.1 ¿Qué es la POO?")
    st.markdown("""
    La **Programación Orientada a Objetos (POO)** es un paradigma que organiza el código en "objetos" 
    que representan entidades del mundo real. Cada objeto tiene:
    - **Atributos**: características o datos que describen el objeto
    - **Métodos**: acciones o comportamientos que el objeto puede realizar
    """)
    
    st.subheader("Conceptos clave (definiciones ampliadas)")
    
    with st.expander("**Clase**", expanded=True):
        st.markdown("""
        Una **clase** es la plantilla o molde a partir del cual se crean los objetos. Define qué atributos 
        tendrán los objetos y qué métodos podrán ejecutar. Pensemos en una clase como el plano de una casa: 
        el plano no es la casa, pero describe cómo será cada casa construida a partir de él. En Python, 
        `class CuentaBancaria:` define la estructura; `cuenta = CuentaBancaria("Juan", 1000)` crea un objeto 
        concreto siguiendo esa estructura.
        """)
    
    with st.expander("**Objeto / Instancia**"):
        st.markdown("""
        Un **objeto** (o **instancia**) es un ejemplar específico creado a partir de una clase. Si la clase 
        es el plano, el objeto es la casa construida. Cada objeto tiene su propia copia de los atributos: 
        `cuenta1` y `cuenta2` pueden tener saldos diferentes aunque ambas sean de tipo `CuentaBancaria`. 
        Los objetos son las entidades con las que interactuamos en el programa.
        """)
    
    with st.expander("**Encapsulación**"):
        st.markdown("""
        La **encapsulación** consiste en agrupar datos (atributos) y las operaciones que los manipulan 
        (métodos) dentro de una misma unidad (la clase). Además, permite ocultar detalles internos 
        mediante atributos privados o protegidos, exponiendo solo una interfaz pública. Por ejemplo, 
        el saldo de una cuenta puede ser `_saldo` (protegido) y solo modificarse mediante `depositar()` 
        y `retirar()`, no directamente. Esto evita errores y facilita el mantenimiento.
        """)
    
    with st.expander("**Herencia**"):
        st.markdown("""
        La **herencia** permite crear una nueva clase basada en una clase existente. La clase hija 
        hereda atributos y métodos de la clase padre, y puede añadir nuevos o sobrescribir los heredados. 
        Por ejemplo, `CuentaAhorros` hereda de `CuentaBancaria` la lógica de depositar y retirar, 
        pero añade `aplicar_interes()`. Esto evita duplicar código y organiza el diseño en jerarquías 
        con sentido (una cuenta de ahorros *es* una cuenta bancaria, con algo más).
        """)
    
    with st.expander("**Polimorfismo**"):
        st.markdown("""
        El **polimorfismo** significa que diferentes clases pueden responder al mismo mensaje (llamada 
        a método) de manera distinta. Por ejemplo, `CuentaAhorros` y `CuentaCorriente` pueden tener 
        implementaciones distintas de `retirar()`: la primera no permite sobregiro; la segunda sí. 
        Cuando llamas `cuenta.retirar(100)`, Python ejecuta la versión correcta según el tipo real 
        del objeto. Esto permite escribir código genérico que trabaja con diferentes tipos sin 
        conocer los detalles de cada uno.
        """)
    
    st.header("9.2 Definir una clase")
    st.code("""
class NombreClase:
    def __init__(self, parametros):
        self.atributo = valor  # Constructor
    
    def metodo(self, parametros):
        return resultado  # Método de instancia
""", language="python")
    
    st.markdown("""
    - **`self`**: referencia al objeto actual; permite acceder a sus atributos y métodos desde dentro de la clase
    - **`__init__`**: constructor; se ejecuta automáticamente al crear el objeto
    - **Atributos de instancia**: variables específicas de cada objeto (ej: `self.saldo`)
    - **Atributos de clase**: variables compartidas por todos los objetos (ej: `banco = "Banco Python"`)
    """)
    
    st.header("9.3 Métodos especiales (magic methods)")
    st.markdown("""
    Los métodos especiales (también llamados *dunder* por *double underscore*) permiten que tus objetos 
    se integren con operadores y funciones de Python. Por ejemplo, definir `__str__` hace que `print(objeto)` 
    muestre lo que tú quieras; `__add__` permite usar `objeto1 + objeto2`.
    """)
    st.markdown("""
    | Método | Uso | Ejemplo |
    |--------|-----|---------|
    | `__init__` | Constructor | Se ejecuta al crear el objeto |
    | `__str__` | Representación legible | `print(obj)` usa esto |
    | `__repr__` | Representación para desarrolladores | Idealmente `eval(repr(obj))` recrea el objeto |
    | `__len__` | Define `len(objeto)` | Útil para colecciones |
    | `__eq__` | Define `==` | Comparación de igualdad |
    | `__add__` | Define `+` | Suma personalizada |
    """)
    
    st.header("9.4 Herencia")
    st.code("""
class ClaseHija(ClasePadre):
    def __init__(self, ...):
        super().__init__(...)  # Llamar constructor padre
        # código adicional
""", language="python")
    
    st.header("9.5 Encapsulación")
    st.markdown("""
    Python usa convenciones de nombres para indicar el nivel de acceso:
    - **Sin prefijo** (ej: `titular`): público; accesible desde cualquier parte
    - **Un guion bajo `_`** (ej: `_saldo`): protegido por convención; "no uses fuera de la clase"
    - **Dos guiones bajos `__`** (ej: `__pin`): privado mediante *name mangling*; Python cambia el nombre internamente
    """)
    
    st.header("9.6 Tipos de métodos")
    st.markdown("""
    - **Método de instancia**: recibe `self`, opera sobre el objeto (ej: `depositar`, `retirar`)
    - **Método de clase** (`@classmethod`): recibe `cls`, opera sobre la clase; útil para constructores alternativos
    - **Método estático** (`@staticmethod`): no recibe `self` ni `cls`; función de utilidad relacionada con la clase
    """)
    
    with st.expander("💡 Explicación ampliada (estilo tutor)"):
        st.markdown("""
        **¿Por qué POO?** En lugar de tener funciones sueltas que reciben muchos parámetros, 
        agrupas datos (atributos) y acciones (métodos) en objetos. Una `CuentaBancaria` tiene 
        `saldo` y `depositar()`; todo está junto y tiene sentido.
        
        **Herencia en la vida real:** Una `CuentaAhorros` y una `CuentaCorriente` son tipos de 
        cuenta bancaria. Comparten lo básico (depositar, retirar) pero cada una añade su propio 
        comportamiento (interés vs sobregiro). La herencia evita repetir código.
        
        **Tip:** Usa ChatGPT o similar para pedir un ejercicio paso a paso sobre clases. 
        Ver la pestaña **Ejercicio con IA** para un prompt listo.
        """)

with tab_preguntas:
    st.header("Preguntas de comprensión")
    st.caption("Selecciona tu respuesta y haz clic en **Enviar respuesta**. Luego podrás ampliar con ejemplos para copiar al notebook.")
    
    pregunta_con_ampliar(
        key_prefix="poo_q1",
        pregunta="1. ¿Qué es `self` en un método de instancia?",
        opciones=[
            "La clase misma",
            "Referencia al objeto actual",
            "Un parámetro opcional"
        ],
        correcta="Referencia al objeto actual",
        explicacion_correcta="Exacto. `self` es la referencia al objeto sobre el que se ejecuta el método.",
        explicacion_incorrecta="`self` es la referencia al objeto actual (la instancia).",
        ejemplos_notebook=[
            {"titulo": "Uso de self en métodos",
             "explicacion": "self permite que cada objeto tenga sus propios valores de titular y saldo.",
             "codigo": "class Cuenta:\n    def __init__(self, titular, saldo):\n        self.titular = titular  # self = este objeto\n        self.saldo = saldo\n    \n    def depositar(self, monto):\n        self.saldo += monto  # self.saldo = saldo de ESTE objeto\n\nc = Cuenta('Juan', 100)\nc.depositar(50)\nprint(c.saldo)"},
            {"titulo": "self vs parámetros",
             "explicacion": "self identifica el objeto; los demás parámetros son datos que recibe el método.",
             "codigo": "class Producto:\n    def __init__(self, nombre, precio):\n        self.nombre = nombre\n        self.precio = precio\n    \n    def aplicar_descuento(self, porcentaje):\n        self.precio *= (1 - porcentaje/100)\n\np = Producto('Laptop', 1000)\np.aplicar_descuento(10)\nprint(p.precio)"},
            {"titulo": "Múltiples instancias, cada una con su self",
             "explicacion": "c1 y c2 son objetos distintos; modificar c1 no afecta a c2.",
             "codigo": "c1 = Cuenta('Ana', 500)\nc2 = Cuenta('Pedro', 1000)\nprint(c1.saldo, c2.saldo)\nc1.depositar(100)\nprint(c1.saldo, c2.saldo)"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="poo_q2",
        pregunta="2. ¿Para qué sirve `super().__init__()`?",
        opciones=[
            "Para crear un objeto",
            "Para llamar al constructor de la clase padre",
            "Para heredar atributos sin inicializar"
        ],
        correcta="Para llamar al constructor de la clase padre",
        explicacion_correcta="Correcto. `super().__init__()` invoca el constructor de la clase padre para inicializar lo heredado.",
        explicacion_incorrecta="`super().__init__()` llama al constructor de la clase padre.",
        ejemplos_notebook=[
            {"titulo": "Herencia con super",
             "explicacion": "Sin super().__init__(x), self.x no existiría en la clase Hija.",
             "codigo": "class Padre:\n    def __init__(self, x):\n        self.x = x\n\nclass Hija(Padre):\n    def __init__(self, x, y):\n        super().__init__(x)\n        self.y = y\n\nh = Hija(1, 2)\nprint(h.x, h.y)"},
            {"titulo": "CuentaAhorros heredando de CuentaBancaria",
             "explicacion": "CuentaAhorros reutiliza titular y saldo del padre y añade tasa de interés.",
             "codigo": "class CuentaBancaria:\n    def __init__(self, titular, saldo=0):\n        self.titular = titular\n        self.saldo = saldo\n\nclass CuentaAhorros(CuentaBancaria):\n    def __init__(self, titular, saldo=0, tasa=0.02):\n        super().__init__(titular, saldo)\n        self.tasa = tasa\n\nc = CuentaAhorros('Maria', 1000, 0.03)\nprint(c.titular, c.saldo, c.tasa)"},
            {"titulo": "Orden de llamadas en herencia",
             "explicacion": "super() invoca al padre; el orden de ejecución es importante para depuración.",
             "codigo": "class A:\n    def __init__(self):\n        print('A.__init__')\n\nclass B(A):\n    def __init__(self):\n        print('B.__init__ (antes super)')\n        super().__init__()\n        print('B.__init__ (después super)')\n\nb = B()"},
        ]
    )
    
    st.divider()
    
    pregunta_con_ampliar(
        key_prefix="poo_q3",
        pregunta="3. ¿Qué diferencia hay entre `__str__` y `__repr__`?",
        opciones=[
            "Son iguales",
            "`__str__` es para usuarios; `__repr__` para desarrolladores",
            "`__repr__` es más corto"
        ],
        correcta="`__str__` es para usuarios; `__repr__` para desarrolladores",
        explicacion_correcta="Correcto. `__str__` es legible para usuarios; `__repr__` para depuración y desarrollo.",
        explicacion_incorrecta="`__str__` es para usuarios; `__repr__` para desarrolladores (idealmente, eval(repr(obj)) recrea el objeto).",
        ejemplos_notebook=[
            {"titulo": "__str__ vs __repr__",
             "explicacion": "str() usa __str__; repr() usa __repr__. print() usa __str__ por defecto.",
             "codigo": "class Punto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n    def __repr__(self):\n        return f'Punto({self.x}, {self.y})'\n\np = Punto(3, 4)\nprint(str(p))\nprint(repr(p))"},
            {"titulo": "print usa __str__, lista usa __repr__",
             "explicacion": "Al imprimir una lista de objetos, Python usa __repr__ para cada elemento.",
             "codigo": "p = Punto(3, 4)\nprint(p)\nlista = [p]\nprint(lista)"},
            {"titulo": "Ejemplo con CuentaBancaria",
             "explicacion": "__str__ para mensajes amigables; __repr__ para depuración (idealmente recreable).",
             "codigo": "class CuentaBancaria:\n    def __init__(self, titular, saldo):\n        self.titular = titular\n        self.saldo = saldo\n    def __str__(self):\n        return f'Cuenta de {self.titular}: ${self.saldo:,.2f}'\n    def __repr__(self):\n        return f'CuentaBancaria(titular={self.titular!r}, saldo={self.saldo})'\n\nc = CuentaBancaria('Juan', 1500.50)\nprint(c)\nprint(repr(c))"},
        ]
    )

with tab_ejercicio_ia:
    st.header("🤖 Usa la IA para desarrollar un ejercicio sobre clases")
    st.markdown("""
    Te recomendamos usar **ChatGPT**, **Claude**, **Cursor** o cualquier asistente de IA para que te guíe 
    en un ejercicio pequeño pero completo sobre clases. La IA puede darte **paso a paso** con **explicación 
    en cada uno**, adaptado a tu nivel.
    """)
    
    st.subheader("📋 Prompt sugerido (copia y pega en tu IA favorita)")
    
    prompt_ia = '''Soy estudiante de programación en Python aprendiendo sobre clases y POO. Necesito un ejercicio pequeño pero claro que cumpla lo siguiente:

1. **Tema**: Una clase sencilla (por ejemplo: Producto, Libro, Estudiante o similar, no CuentaBancaria que ya vi).

2. **Formato paso a paso**: Dame el ejercicio dividido en pasos numerados (Paso 1, Paso 2, etc.).

3. **Explicación en cada paso**: Después de cada paso, incluye una breve explicación de qué hace ese código y por qué.

4. **Código listo para copiar**: Que cada bloque de código pueda copiarse y ejecutarse en un notebook de Python.

5. **Incluir**: constructor (__init__), al menos 2 métodos de instancia, y opcionalmente __str__ o herencia si aplica.

6. **Extensión**: Máximo 5-6 pasos para que sea manejable.

Por favor, empieza con el Paso 1 y su explicación.'''
    
    st.code(prompt_ia, language="text")
    st.caption("Usa el botón **Copy** del bloque de código o selecciona y copia (Ctrl+C) el texto.")
    
    st.divider()
    
    st.subheader("💡 Cómo usar este ejercicio")
    st.markdown("""
    1. **Copia el prompt** de arriba y pégalo en ChatGPT, Claude o Cursor.
    2. La IA te dará el **Paso 1** con código y explicación.
    3. **Copia el código** en una celda de tu notebook y ejecútalo.
    4. Pide **"Siguiente paso"** o **"Paso 2"** para continuar.
    5. Repite hasta completar el ejercicio.
    6. **Practica**: intenta modificar el ejercicio (añadir un método, cambiar un atributo) y pide a la IA que te explique.
    """)
    
    st.info("""
    **Ventaja de usar IA:** La explicación se adapta a tus dudas. Si algo no queda claro, pregunta 
    "¿Por qué usamos self aquí?" o "¿Qué pasa si no llamo a super().__init__?" y la IA te lo explicará.
    """)

with tab_codigo:
    st.header("Editor de código")
    st.markdown("Practica definiendo clases y usando herencia.")
    
    codigo_default = '''# Ejemplo: clase CuentaBancaria simple
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.saldo:,.2f}"

# Crear y usar
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)
print(cuenta)
'''
    
    codigo = st.text_area("Código Python", value=codigo_default, height=280)
    
    if st.button("▶️ Ejecutar"):
        stdout, stderr, success = ejecutar_codigo(codigo)
        if success:
            if stdout:
                st.text("Salida:")
                st.code(stdout)
            else:
                st.success("Código ejecutado correctamente.")
        else:
            st.error(stderr)
    
    st.subheader("Ejercicio sugerido")
    st.markdown("""
    Crea una clase `CuentaAhorros` que herede de `CuentaBancaria` y añada:
    - Atributo `tasa_interes` en el constructor
    - Método `aplicar_interes()` que sume al saldo el interés (saldo * tasa_interes)
    - Sobrescribe `__str__` para mostrar la tasa de interés
    """)
    
    st.caption("💡 **Tip:** Para un ejercicio guiado paso a paso con explicaciones, usa la pestaña **Ejercicio con IA**.")
