# Taller 3: Depuración y Transformación de Datos de Emprendimiento

## Objetivo
Realizar un proceso completo de limpieza y transformación de datos sobre **microestablecimientos comerciales (tenderos)** en Colombia, aplicando buenas prácticas de depuración. La base incluye **~482 variables** con información **sociodemográfica**, del negocio, actitudes emprendedoras e informalidad.

---

## Fuente de Información

**Base de datos:** Emprendimiento e informalidad: Microestablecimientos comerciales (Línea Base)  
**Fuente:** Universidad del Rosario - Alianza EFI (Economía Formal e Inclusiva)  
**Dataset:** [doi.org/10.34848/FK2/RD5NIK](https://doi.org/10.34848/FK2/RD5NIK)  
**Observaciones:** 1.654 | **Variables:** ~482  
**Temática:** Emprendimiento, informalidad, características sociodemográficas de tenderos

---

## Documentación de Referencia (PDF)

| Documento | Descripción | Enlace |
|-----------|-------------|--------|
| **Cuestionario línea base** | Formulario completo de la encuesta con todas las preguntas/variables | [Encuesta Emprendimiento V2.pdf](https://research-data.urosario.edu.co/file.xhtml?persistentId=doi:10.34848/FK2/RD5NIK/3ENESL) |
| **Informe Estudio Nacional** | Informe metodológico y resultados del estudio a tenderos | [WP1-2020-001.pdf](https://research-data.urosario.edu.co/file.xhtml?persistentId=doi:10.34848/FK2/RD5NIK/4FCEWZ) |
| **Informe completo (Alianza EFI)** | Descarga del informe extendido | [alianzaefi.com](https://alianzaefi.com/download/informe-estudio-nacional-de-emprendimiento-a-tenderos-primera-ronda/) |
| **Consentimiento y formularios** | Documentos de consentimiento informado | [EFI Proyecto 1 CI y Fisicas Tenderos.docx](https://research-data.urosario.edu.co/file.xhtml?persistentId=doi:10.34848/FK2/RD5NIK/DDU0HT) |

---

## Estructura de la Base de Datos

La encuesta incluye bloques temáticos. **Consulte el PDF del cuestionario** para el listado completo de variables. A continuación se presentan los tipos de variables y las indicaciones generales por categoría.

### Bloques temáticos (referencia)

1. **Identificación y ubicación** – Códigos, municipio, zona
2. **Sociodemográficas** – Edad, sexo, educación, etnia, estrato, hogar
3. **Características del negocio** – Antigüedad, ingresos, empleados, formalidad
4. **Actitudes y percepciones** – Escalas sobre emprendimiento, informalidad
5. **Financiamiento y capital** – Acceso a crédito, ahorros
6. **Prácticas comerciales** – Proveedores, precios, competencia

---

## Indicaciones por Tipo de Variable

### Variables sociodemográficas

**Ejemplos:** edad, sexo, nivel educativo, estrato socioeconómico, etnia, jefe del hogar, número de personas en el hogar, etc.

**Indicaciones para el estudiante:**
- [ ] Identificar variables de edad y verificar rangos válidos (ej: 18-100)
- [ ] Estandarizar variables categóricas (sexo, educación) a factor
- [ ] Detectar valores fuera de rango o códigos especiales (99, 999 = no sabe/no responde)
- [ ] Crear categorías agrupadas si hay muchas modalidades (ej: nivel educativo)
- [ ] Verificar consistencia entre variables relacionadas (ej: edad vs año de nacimiento)
- [ ] Tratar valores "No aplica", "No responde" según criterio del análisis

**Código de ejemplo:**
```r
# Ejemplo para variable de edad
datos <- datos %>%
  mutate(edad = as.numeric(edad),
         edad = ifelse(edad < 15 | edad > 100, NA, edad))

# Ejemplo para variable categórica
datos <- datos %>%
  mutate(sexo = factor(sexo, levels = c(1, 2), labels = c("Hombre", "Mujer")))
```

---

### Variables del negocio / microestablecimiento

**Ejemplos:** antigüedad del negocio, ingresos mensuales, número de empleados, registro ante Cámara de Comercio, tipo de establecimiento, etc.

**Indicaciones para el estudiante:**
- [ ] Verificar unidades de medida (ingresos en pesos, porcentajes, etc.)
- [ ] Identificar y tratar valores extremos (outliers) en variables numéricas
- [ ] Crear variable binaria de formalidad (registrado vs no registrado)
- [ ] Depurar fechas y calcular antigüedad si aplica
- [ ] Recodificar variables de ingresos en rangos si hay muchos missing
- [ ] Cruzar consistencia (ej: empleados >= 0)

**Código de ejemplo:**
```r
# Ejemplo para ingresos con outliers
datos <- datos %>%
  mutate(ingresos = as.numeric(ingresos),
         ingresos = ifelse(ingresos < 0 | ingresos > 1e9, NA, ingresos))

# Variable de formalidad
datos <- datos %>%
  mutate(formal = as.integer(registro_camara == 1))
```

---

### Variables de escalas / actitudes (Likert)

**Ejemplos:** preguntas de actitud hacia el emprendimiento, percepción de riesgo, intención emprendedora, etc.

**Indicaciones para el estudiante:**
- [ ] Identificar la escala (ej: 1-5, 1-7) y valores válidos
- [ ] Recodificar ítems invertidos si aplica
- [ ] Calcular puntajes compuestos o promedios por constructo
- [ ] Tratar valores "No sabe/No responde" como NA o categoría según análisis
- [ ] Verificar consistencia interna si se construyen escalas
- [ ] Documentar la recodificación realizada

**Código de ejemplo:**
```r
# Ejemplo para escala 1-5
datos <- datos %>%
  mutate(actitud_1 = ifelse(actitud_1 %in% 1:5, actitud_1, NA))

# Promedio de ítems de un constructo
datos <- datos %>%
  mutate(actitud_prom = rowMeans(select(., starts_with("actitud_")), na.rm = TRUE))
```

---

### Variables de ubicación geográfica

**Ejemplos:** departamento, municipio, zona (urbana/rural), código DANE, etc.

**Indicaciones para el estudiante:**
- [ ] Estandarizar nombres de departamentos/municipios (mayúsculas, acentos)
- [ ] Verificar códigos DANE si se usan (5 dígitos para municipio)
- [ ] Crear variable de región si se requiere agregación
- [ ] Identificar códigos faltantes o inconsistentes
- [ ] Cruzar con diccionario de códigos DANE si está disponible

---

### Variables de identificación

**Indiques:** ID de encuesta, folio, etc.

**Indicaciones para el estudiante:**
- [ ] Verificar unicidad del identificador
- [ ] Preservar como character si tiene ceros a la izquierda
- [ ] No usar para análisis estadístico
- [ ] Usar para detectar duplicados

---

## Proceso General de Depuración

### Paso 1: Exploración inicial
```r
# Estructura
str(datos)
names(datos)

# Resumen por tipo de variable
summary(datos)
sapply(datos, class)

# Valores faltantes
colSums(is.na(datos))
```

### Paso 2: Selección de variables
Con 482 variables, se recomienda:
- [ ] Seleccionar un subconjunto de ~50-100 variables según objetivos del taller
- [ ] Priorizar: sociodemográficas + variables clave del negocio + algunas escalas
- [ ] Documentar el criterio de selección

```r
# Ejemplo de selección
vars_interes <- c("id", "edad", "sexo", "educacion", "ingresos", 
                  "antiguedad_negocio", "empleados", "formal", ...)
datos_sel <- datos %>% select(all_of(vars_interes))
```

### Paso 3: Depuración por bloques
- [ ] Aplicar las indicaciones por tipo de variable
- [ ] Generar reporte de cambios (registros eliminados, recodificaciones)
- [ ] Guardar versiones intermedias si el proceso es extenso

### Paso 4: Validación final
- [ ] Verificar que no queden valores imposibles
- [ ] Revisar distribuciones de variables clave
- [ ] Documentar decisiones y exclusiones

---

## Tareas Obligatorias del Taller

1. **Exploración:** Generar un resumen de las primeras 50 variables (tipo, valores únicos, NAs)
2. **Selección:** Definir y justificar un subconjunto de variables para trabajar
3. **Depuración:** Aplicar al menos 3 tipos de transformaciones (ej: fechas, factores, outliers)
4. **Reporte:** Documento breve (1-2 páginas) con:
   - Descripción del proceso
   - Decisiones de depuración
   - Estadísticas antes/después
   - Limitaciones identificadas

---

## Entregables

- [ ] Script R completo con exploración, selección y depuración
- [ ] Archivo CSV con datos depurados (puede ser subconjunto de variables)
- [ ] Reporte en PDF o Word según indicaciones anteriores

---

## Referencias Adicionales

- **Alianza EFI:** https://alianzaefi.com/
- **Universidad del Rosario - Repositorio:** https://research-data.urosario.edu.co/
