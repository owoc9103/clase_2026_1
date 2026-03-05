# Quices - Fundamentos de Programación (Clases 1-3)

Este folder contiene 3 quices basados en los temas de las Clases 1, 2 y 3 de Fundamentos de Programación.

## Estructura

Cada quiz tiene dos versiones:

- **\*_Preguntas.Rmd**: Solo las preguntas (para entregar a los estudiantes)
- **\*_Respuestas.Rmd**: Preguntas con respuestas (para el profesor)

| Archivo | Descripción |
|---------|-------------|
| Quiz_1_Preguntas.Rmd / Quiz_1_Respuestas.Rmd | Quiz 1 - Versión A |
| Quiz_2_Preguntas.Rmd / Quiz_2_Respuestas.Rmd | Quiz 2 - Versión B |
| Quiz_3_Preguntas.Rmd / Quiz_3_Respuestas.Rmd | Quiz 3 - Versión C |

## Composición de cada quiz (6 preguntas)

- **2 opción múltiple** (una respuesta correcta)
- **2 verdadero o falso**
- **1 identificar el error** en código
- **1 escribir código** (nivel básico-intermedio)

Los tres quices cubren los mismos temas pero con preguntas en diferente orden y opciones de respuesta en posiciones distintas para evitar copias.

## Cómo generar los PDF

### Requisitos

- R (https://cran.r-project.org/)
- Paquetes: `rmarkdown`, `tinytex` (o LaTeX completo como MiKTeX)

### Instalación de paquetes (una vez)

```r
install.packages("rmarkdown")
install.packages("tinytex")
tinytex::install_tinytex()  # Si no tiene LaTeX instalado
```

### Compilar todos los PDF

Desde R o RStudio, en el directorio Quiz_1:

```r
setwd("FundProg/Quiz_1")
rmarkdown::render("Quiz_1_Preguntas.Rmd")
rmarkdown::render("Quiz_1_Respuestas.Rmd")
rmarkdown::render("Quiz_2_Preguntas.Rmd")
rmarkdown::render("Quiz_2_Respuestas.Rmd")
rmarkdown::render("Quiz_3_Preguntas.Rmd")
rmarkdown::render("Quiz_3_Respuestas.Rmd")
```

O desde RStudio: abrir cada archivo .Rmd y hacer clic en **Knit** (tejer).

### Compilar con pandoc (alternativa)

Si tiene R y pandoc instalados desde la terminal:

```bash
Rscript -e "rmarkdown::render('Quiz_1_Preguntas.Rmd')"
```

## Temas cubiertos

- **Clase 1**: Introducción a Python, tipos numéricos, strings, listas básicas
- **Clase 2**: Control de flujo (if/elif/else), bucles (for/while), funciones
- **Clase 3**: Estructuras de datos (listas avanzadas, tuplas, conjuntos, diccionarios), comprensiones
