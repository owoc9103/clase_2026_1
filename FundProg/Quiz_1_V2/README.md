# Quiz 1 - Versiones V1, V2, V3

Tres versiones del mismo Quiz 1 con 8 preguntas en diferente orden y respuestas de opción múltiple en diferentes posiciones.

## Archivos

| Archivo | Descripción |
|---------|-------------|
| Quiz1_V1_Preguntas.Rmd / Quiz1_V1_Respuestas.Rmd | Versión 1 |
| Quiz1_V2_Preguntas.Rmd / Quiz1_V2_Respuestas.Rmd | Versión 2 |
| Quiz1_V3_Preguntas.Rmd / Quiz1_V3_Respuestas.Rmd | Versión 3 |

## Preguntas incluidas (8)

1. **MC** - Ciclo `for`: ¿Qué valores produce `range(...)`? / ¿Qué imprime `for i in range(...)`?
2. **MC** - Ciclo `while`: ¿Cuándo usarlo? / ¿Por qué modificar la condición? / Diferencia for vs while
3. **MC** - Estructura inmutable para claves (Tupla)
4. **MC** - Método que inserta en última posición (`append()`)
5. **VF** - La función `map()` aplica una función a cada elemento...
6. **VF** - `is` vs `==` (Falso: es al revés)
7. **Error** - Indentación en bloque `if` (única pregunta de detección de errores)
8. **Código** - Función `promedio` (3 formulaciones distintas en cada versión)

## Compilar a PDF

En RStudio, abrir cada .Rmd y hacer clic en **Knit**. O desde R:

```r
setwd("FundProg/Quiz_1_V2")
for (v in 1:3) {
  rmarkdown::render(paste0("Quiz1_V", v, "_Preguntas.Rmd"))
  rmarkdown::render(paste0("Quiz1_V", v, "_Respuestas.Rmd"))
}
```
