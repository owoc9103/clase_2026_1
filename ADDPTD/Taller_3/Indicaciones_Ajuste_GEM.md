# Indicaciones para el Ajuste de la Base de Datos GEM APS

**Taller 3 - Analítica de Datos para la Toma de Decisiones**  
**Dataset:** GEM Adult Population Survey (APS) - Individual Level Data

---

## Introducción

Este documento describe los ajustes que los estudiantes deben realizar sobre la base de datos GEM APS. Para cada variable o grupo de variables se indica: (1) el ajuste a realizar, (2) los valores y etiquetas, y (3) la solución equivalente en **KNIME** con el nodo correspondiente.

---

# PARTE 1: ELIMINACIÓN DE COLUMNAS

## 1.1 Eliminar columnas con muchos valores faltantes (NA >= 1203)

**Objetivo:** Eliminar variables que tienen 1203 o más valores NA (no aplicables o sin respuesta).

**Indicaciones:**
- Calcular el conteo de NA por cada columna.
- Identificar las columnas donde `Conteo_NA >= 1203`.
- Eliminar esas columnas del dataset.

**Solución en KNIME:**

| Nodo | Configuración |
|------|---------------|
| **Missing Value Column Filter** | *Ruta:* `Data Manipulation` → `Filter` → `Missing Value Column Filter` |
| | 1. Seleccionar **todas las columnas** para evaluar |
| | 2. Criterio: **"By number of missing values"** |
| | 3. Umbral: **1203** (o el valor que corresponda al umbral deseado) |
| | 4. Opción: **"Remove columns with at least X missing values"** |

**Alternativa:** Si necesita un umbral dinámico (porcentaje), use **"By percentage of missing values"** y calcule el porcentaje equivalente (ej: 1203/número_total_filas * 100).

---

## 1.2 Eliminar columnas específicas (lista predefinida)

**Objetivo:** Eliminar un conjunto de columnas que no se utilizarán en el análisis (variables técnicas, duplicadas, o de años específicos).

**Columnas a eliminar:** `ctryalp`, `setid`, `ID`, `REGION`, `WBINC`, `WBincREV`, `yrsurv`, `weight`, `WEIGHT_L`, `WEIGHT_A`, `GEMOCCU`, `GEMWORK`, `GEMWORK3`, `GEMHHINC`, `GEMEDUC`, `UNEDUC`, `UNEDUC97`, `COZONAROU`, `Bstart22`, `BJOBST22`, `OWNMGE22`, `OMJOBST22`, `BUSANG22`, `FUTSUP22`, `DISCEN22`, `KNOWEN22`, `OPPORT22`, `SUSKIL22`, `FRFAIL22`, `EASYST22`, `OPPISM22`, `PROACT22`, `CREATIV22`, `VISION22`, `EQUALI22`, `NBGOOD22`, `NBSTAT22`, `NBMEDI22`, `INDSUP22`, `CULSUP22`, `SUB`, `SUBA`, `SUBO`, `SUBOA`, `SUBOANW`, `OMBABYX`, `OMESTBX`, `BABYBUSM`, `BABYBUSO`, `ESTBBUSM`, `ESTBBUSO`, `SUBOANWC`, `SUBOANW1`, `BABYBUS1`, `ESTBBUS1`, `TEA22`, `ANYBUSOW`, `TEA22MAL`, `TEA22FEM`, `BUSANGVL`, `SU_HITEC`, `BB_HITEC`, `EB_HITEC`, `TEAHITEC`, `EXTHITEC`, `su_22TEC`, `bb_22TEC`, `SU_SIC4C`, `BB_SIC4C`, `EB_SIC4C`, `SU_ISIC4_1D`, `BB_ISIC4_1D`, `EB_ISIC4_1D`, `TEAISIC4_1D`, `TEASIC4C`, `TEA22S1C`, `TEA22S2C`, `TEA22S3C`, `TEA22S4C`, `BO_EXAGR`, `EXIT_CTD`, `EXIT_ENT`, `TEA22EMP`, `su_22emp`, `bb_22emp`, `EB_22EMP`, `TEA22HJG`, `su_22hjg`, `bb_22hjg`, `EB_22HJG`, `tea22kix`, `su_22kix`, `bb_22kix`, `eb_22kix`, `tea22hix`, `su_22hix`, `bb_22hix`, `eb_22hix`, `FUTSUPNO`, `SU_MKSC`, `BB_MKSC`, `EB_MKSC`, `BB_CSTLOC`, `BB_CSTNAT`, `BB_CSTEXP`, `BB_NEWPROD`, `BB_NEWPROC`, `EB_CSTLOC`, `EB_CSTNAT`, `EB_CSTEXP`, `EB_NEWPROD`, `TEAIMPACT1`, `TEAIMPACT2`, `OPPIS_1`, `OPPIS_2`, `OPPIS_3`, `PROAC_1`, `PROAC_2`, `PROAC_3`, `CREATI_1`, `CREATI_2`, `CREATI_3`, `VISIO_1`, `VISIO_2`, `VISIO_3`, `SOCEN_1`, `SOCEN_2`, `SOCEN_3`, `INDSP22A`, `INDSP22B`, `INDSP22C`, `INDSP22D`, `CULSP22A`, `CULSP22B`, `CULSP22C`, `CULSP22D`, `TEA22IND`, `TEA22SPON`, `SU_SPON`, `SU_IND`, `BB_SPON`, `BB_IND`, `EB_SPON`, `EB_IND`, `TEAactivityr`, `MSURV`

**Solución en KNIME:**

| Nodo | Configuración |
|------|---------------|
| **Column Filter** | *Ruta:* `Data Manipulation` → `Filter` → `Column Filter` |
| | 1. Modo: **"Exclude"** (excluir columnas) |
| | 2. Seleccionar o pegar la lista de columnas a excluir |
| | 3. Alternativa: Crear un archivo CSV/Excel con los nombres y usar **Table Reader** + **Column Filter** con referencia a esa tabla |

---

# PARTE 2: CREACIÓN DE NUEVAS VARIABLES

## 2.1 Variable `age7c` (Edad en categorías)

**Objetivo:** Crear una variable categórica a partir de `age` con 7 rangos de edad más categorías de no respuesta.

**Reglas de recodificación:**

| Rango de `age` | Valor | Etiqueta |
|----------------|-------|----------|
| age < 18 | 1 | Menos de 18 |
| 18 <= age <= 24 | 2 | 18-24 |
| 25 <= age <= 34 | 3 | 25-34 |
| 35 <= age <= 44 | 4 | 35-44 |
| 45 <= age <= 54 | 5 | 45-54 |
| 55 <= age <= 64 | 6 | 55-64 |
| 65 <= age <= 99 | 7 | 65-99 |
| NA (age) | -2 | Sin respuesta/Rechaza |

**Solución en KNIME:**

| Nodo | Configuración |
|------|---------------|
| **Rule Engine** | *Ruta:* `Data Manipulation` → `Transform` → `Rule Engine` |
| | 1. Columna de salida: `age7c` |
| | 2. Reglas (sintaxis): |
| | `$age$ < 18 => "Menos de 18"` |
| | `$age$ >= 18 AND $age$ <= 24 => "18-24"` |
| | `$age$ >= 25 AND $age$ <= 34 => "25-34"` |
| | `$age$ >= 35 AND $age$ <= 44 => "35-44"` |
| | `$age$ >= 45 AND $age$ <= 54 => "45-54"` |
| | `$age$ >= 55 AND $age$ <= 64 => "55-64"` |
| | `$age$ >= 65 AND $age$ <= 99 => "65-99"` |
| | `$age$ IS MISSING => "Sin respuesta/Rechaza"` |
| | 3. Default: `"Sin respuesta/Rechaza"` |

---

# PARTE 3: RECODIFICACIÓN CON ETIQUETAS (Value Lookup)

Para las siguientes variables se reemplazan valores numéricos por etiquetas descriptivas. En KNIME se usa el nodo **Value Lookup** con una tabla diccionario.

**Procedimiento general en KNIME:**
1. Crear un archivo Excel o CSV con dos columnas: **Valor_Original** y **Etiqueta**.
2. Nodo **Excel Reader** o **CSV Reader** para cargar el diccionario.
3. Nodo **Value Lookup**: conectar la tabla de datos (puerto 1) y el diccionario (puerto 2).
4. Configurar: columna a buscar = variable de interés; columna clave del diccionario = Valor_Original; columna de reemplazo = Etiqueta.
5. Opción **"Replace"** para sustituir la columna original.

---

## 3.1 Variable `knowentR` (¿Conoce emprendedores?)

| Valor | Etiqueta |
|-------|----------|
| 0 | Ninguno |
| 1 | Uno |
| 2 | De 2 a 4 |
| 3 | 5 o más |
| -1 | No lo sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup (con diccionario)

---

## 3.2 Variables escala Likert (5 puntos + No sabe/Rechaza)

**Variables:** `opportL`, `suskillL`, `fearfailL`, `easystartL`

| Valor | Etiqueta |
|-------|----------|
| 5 | Completamente de acuerdo |
| 4 | Algo de acuerdo |
| 3 | Ni de acuerdo ni en desacuerdo |
| 2 | Poco de acuerdo |
| 1 | Nada de acuerdo |
| -1 | No lo sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup. Crear un diccionario y aplicarlo a cada variable (puede usar un **Column Loop** o varios nodos Value Lookup en paralelo).

---

## 3.3 Variables Likert adicionales

**Variables:** `oppism`, `proact`, `creativ`, `vision`, `equalincL`, `nbgoodcL`, `nbstatusL`, `nbmediaL`, `nbsocentL`

**Mismo mapeo que 3.2** (escala 5, 4, 3, 2, 1, -1, -2).

**Nodo KNIME:** Value Lookup con el mismo diccionario Likert. Puede usar **Loop** para aplicar a todas las columnas.

---

## 3.4 Variables Sí/No (bstart, bjobst)

**Variables:** `bstart`, `bjobst`

| Valor | Etiqueta |
|-------|----------|
| 1 | Sí |
| 2 | No |
| -1 | No sabe |
| -2 | Rechaza |
| 0 | Otro |

**Nodo KNIME:** Value Lookup

---

## 3.5 Variables Sí/No (ownmge, omjobst, OWNMGE22, OMJOBST22)

**Mismo mapeo que 3.4.**

**Nodo KNIME:** Value Lookup (reutilizar diccionario Sí/No)

---

## 3.6 Variable `gender` (Género)

| Valor | Etiqueta |
|-------|----------|
| 1 | Hombre |
| 2 | Mujer |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.7 Variable `hhsize` (Tamaño del hogar)

**Objetivo:** Reemplazar -1 y -2 por texto; el resto se mantiene como número o carácter.

| Valor | Reemplazo |
|-------|-----------|
| -1 | No sabe |
| -2 | Rechaza |
| Otros | Mantener valor original |

**Solución en KNIME:**

| Nodo | Configuración |
|------|---------------|
| **Rule Engine** o **String Replacer** | Reglas: `$hhsize$ = -1 => "No sabe"`, `$hhsize$ = -2 => "Rechaza"` |
| | O usar **String Replacer** en columna convertida a String: reemplazar "-1" por "No sabe", "-2" por "Rechaza" |

---

## 3.8 Variables futsup, discent, busang, doublecount

**Mismo mapeo que 3.4** (Sí, No, No sabe, Rechaza, Otro).

**Nodo KNIME:** Value Lookup

---

## 3.9 Variable `occup` (Ocupación)

| Valor | Etiqueta |
|-------|----------|
| 1 | Empleado por cuenta ajena a tiempo completo |
| 2 | Empleado por cuenta ajena a tiempo parcial |
| 3 | Autoempleado |
| 4 | Desempleado |
| 5 | Jubilado |
| 6 | Estudiante |
| 7 | Labores del hogar |
| 8 | No está buscando empleo |
| 9 | Otro caso (Especificar) |
| 10 | Cuidador de un miembro de su familia |
| -1 | No sabe |
| -2 | No contesta |

**Nodo KNIME:** Value Lookup

---

## 3.10 Variable `COhhinc` (Ingresos del hogar - Colombia)

| Valor | Etiqueta |
|-------|----------|
| 1 | Menos de 1 SMMLV |
| 2 | Entre 1 y 2 SMMLV |
| 3 | Más de 2 SMMLV y menos de 3 SMMLV |
| 4 | Más de 3 SMMLV y menos de 4 SMMLV |
| 5 | Más de 4 SMMLV y menos de 5 SMMLV |
| 6 | Más de 5 SMMLV y menos de 6 SMMLV |
| 7 | Más de 6 SMMLV |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.11 Variable `COREduc` (Nivel educativo - Colombia)

| Valor | Etiqueta |
|-------|----------|
| 0 | Sin estudios |
| 1 | Primaria incompleta |
| 2 | Primaria completa |
| 3 | Secundaria incompleta |
| 4 | Secundaria completa |
| 5 | Técnico incompleto |
| 6 | Técnico completo |
| 7 | Tecnológico incompleto |
| 8 | Tecnológico completo |
| 9 | Universitario incompleto |
| 10 | Universitario completo |
| 11 | Posgrado (especialización, maestría, doctorado) |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.12 Variable `COpost` (Postestrato - Colombia)

| Valor | Etiqueta |
|-------|----------|
| -3 | No es aplicable |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.13 Variable `contact` (Modalidad de contacto)

| Valor | Etiqueta |
|-------|----------|
| 1 | Presencial (cara a cara) |
| 2 | Línea telefónica fija |
| 3 | Línea telefónica móvil |
| 4 | Otro caso |

**Nodo KNIME:** Value Lookup

---

## 3.14 Variable `cphhinc` (Cambio en ingresos del hogar)

| Valor | Etiqueta |
|-------|----------|
| 1 | Han disminuido considerablemente |
| 2 | Han disminuido un poco |
| 3 | No han mostrado cambios sustanciales |
| 4 | Han aumentado un poco |
| 5 | Han aumentado considerablemente |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.15 Variable `COXXNIVSE` (Estrato socioeconómico)

| Valor | Etiqueta |
|-------|----------|
| 1 | Estrato 1 |
| 2 | Estrato 2 |
| 3 | Estrato 3 |
| 4 | Estrato 4 |
| 5 | Estrato 5 |
| 6 | Estrato 6 |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.16 Variable `COxxetn` (Etnia)

| Valor | Etiqueta |
|-------|----------|
| 1 | Afrodescendiente |
| 2 | Asiático |
| 3 | Blanco |
| 4 | Indígena |
| 5 | Mulato |
| 6 | Mestizo |
| 7 | Raizal |
| 8 | Otro (Especificar) |
| -1 | No sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

## 3.17 Variable `CONACIO` (Nacionalidad)

| Valor | Etiqueta |
|-------|----------|
| 1 | Colombiana |
| 2 | Otra |

**Nodo KNIME:** Value Lookup

---

## 3.18 Variables Bstart22, BJOBST22

**Mismo mapeo:** 1=Sí, 2=No, -1=No sabe, -2=Rechaza.

**Nodo KNIME:** Value Lookup

---

## 3.19 Variables SU_CSTLOC, SU_CSTNAT, SU_CSTEXP

| Valor | Etiqueta |
|-------|----------|
| 1 | Sí |
| 2 | No |
| -1 | No lo sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup o Rule Engine

---

## 3.20 Variables SU_NEWPROD, SU_NEWPROC

| Valor | Etiqueta |
|-------|----------|
| 1 | No, no ofrezco ningún producto o servicio que sea nuevo |
| 2 | Nuevo para la gente de la zona en la que vive |
| 3 | Nuevo para la gente de su país |
| 4 | Nuevo en el mundo |
| -1 | No lo sabe |
| -2 | Rechaza |

**Nodo KNIME:** Value Lookup

---

# PARTE 4: ESTRUCTURA SUGERIDA DEL WORKFLOW EN KNIME

```
[Excel/SPSS Reader] 
       |
       v
[Missing Value Column Filter]  --> Eliminar columnas con NA >= 1203
       |
       v
[Column Filter]  --> Excluir lista de columnas predefinidas (opcional, puede ir al final)
       |
       v
[Rule Engine]  --> Crear age7c
       |
       v
[Value Lookup] x N  --> Aplicar diccionarios a cada variable (o usar Loop)
       |
       v
[Column Filter]  --> Excluir columnas de la lista delete_colum
       |
       v
[Excel Writer]  --> Guardar GEM_Data_Final.xlsx
```

**Recomendación:** Crear **tablas diccionario** en Excel (una hoja por tipo de mapeo: Likert, Sí/No, occup, COhhinc, etc.) y conectarlas a múltiples nodos Value Lookup para evitar repetir configuraciones.

---

# ANEXO: Creación de tablas diccionario para Value Lookup

**Ejemplo - Diccionario Likert (archivo Excel "Diccionarios_GEM.xlsx", hoja "Likert"):**

| Valor | Etiqueta |
|-------|----------|
| 5 | Completamente de acuerdo |
| 4 | Algo de acuerdo |
| 3 | Ni de acuerdo ni en desacuerdo |
| 2 | Poco de acuerdo |
| 1 | Nada de acuerdo |
| -1 | No lo sabe |
| -2 | Rechaza |

**Ejemplo - Diccionario Sí/No:**

| Valor | Etiqueta |
|-------|----------|
| 1 | Sí |
| 2 | No |
| -1 | No sabe |
| -2 | Rechaza |
| 0 | Otro |

---

*Documento generado para el Taller 3 - Ajuste Base de Datos GEM APS*
