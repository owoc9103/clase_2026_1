# =============================================================================
# TALLER 3 - BASE DE DATOS DE EMPRENDIMIENTO
# Depuración y Transformación de Datos
# =============================================================================
# Fuente: Universidad del Rosario - Alianza EFI
# Dataset: Emprendimiento e informalidad: Microestablecimientos comerciales
# 482 variables | 1.654 observaciones | Información sociodemográfica
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CONFIGURACIÓN Y PAQUETES
# -----------------------------------------------------------------------------

# Instalar paquetes si no están instalados (descomentar si es necesario)
# install.packages(c("dataverse", "dplyr", "readr", "httr", "lubridate", "stringr", "tidyr"))

library(dplyr)
library(readr)
library(lubridate)
library(stringr)
library(tidyr)

# Directorio de trabajo - ajustar según ubicación del proyecto
if (requireNamespace("rstudioapi", quietly = TRUE) && rstudioapi::isAvailable()) {
  setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
} else {
  setwd(".")  # Usar directorio actual o especificar: setwd("ruta/a/Taller_3")
}

# -----------------------------------------------------------------------------
# 2. DESCARGA DE LA BASE DE DATOS
# -----------------------------------------------------------------------------

dir_salida <- "datos"
if (!dir.exists(dir_salida)) dir.create(dir_salida)

archivo_tab <- file.path(dir_salida, "Tenderos03_Publica.tab")
archivo_csv <- file.path(dir_salida, "tenderos_crudos.csv")

# Opción A: Descarga automática
descarga_ok <- FALSE

# A1. Intentar con paquete dataverse
if (requireNamespace("dataverse", quietly = TRUE)) {
  cat("Intentando descarga con paquete dataverse...\n")
  tryCatch({
    datos_crudos <- dataverse::get_dataframe_by_name(
      filename = "Tenderos03_Publica.tab",
      dataset = "10.34848/FK2/RD5NIK",
      server = "research-data.urosario.edu.co"
    )
    descarga_ok <- TRUE
    cat("Descarga exitosa.\n")
  }, error = function(e) {
    cat("Dataverse falló:", conditionMessage(e), "\n")
  })
}

# A2. Intentar descarga directa por URL (si A1 falló)
if (!descarga_ok && requireNamespace("httr", quietly = TRUE)) {
  cat("Intentando descarga directa por URL...\n")
  url_file <- "https://research-data.urosario.edu.co/api/access/datafile/368"
  tryCatch({
    resp <- httr::GET(url_file, httr::write_disk(archivo_tab, overwrite = TRUE))
    if (httr::status_code(resp) == 200 && file.exists(archivo_tab)) {
      datos_crudos <- read_delim(archivo_tab, delim = "\t", show_col_types = FALSE)
      descarga_ok <- TRUE
      cat("Descarga exitosa.\n")
    }
  }, error = function(e) {
    if (file.exists(archivo_tab)) file.remove(archivo_tab)
    cat("Descarga URL falló:", conditionMessage(e), "\n")
  })
}

# Opción B: Leer archivo local si ya fue descargado manualmente
if (!descarga_ok && file.exists(archivo_tab)) {
  cat("Leyendo archivo local:", archivo_tab, "\n")
  datos_crudos <- read_delim(archivo_tab, delim = "\t", show_col_types = FALSE)
  descarga_ok <- TRUE
}

# Opción C: Instrucciones para descarga manual
if (!descarga_ok) {
  stop(
    "\n========================================\n",
    "DESCARGA MANUAL REQUERIDA\n",
    "========================================\n",
    "1. Visite: https://doi.org/10.34848/FK2/RD5NIK\n",
    "2. Descargue el archivo 'Tenderos03_Publica.tab'\n",
    "3. Colóquelo en la carpeta: ", normalizePath(dir_salida), "\n",
    "4. Vuelva a ejecutar este script.\n",
    "========================================\n"
  )
}

# Verificar que se cargaron datos
if (is.null(datos_crudos) || nrow(datos_crudos) == 0) {
  stop("No se pudieron cargar los datos.")
}

cat("Registros cargados:", nrow(datos_crudos), "\n")
cat("Variables:", ncol(datos_crudos), "\n")

# -----------------------------------------------------------------------------
# 3. GUARDAR COPIA CRUDA (antes de depuración)
# -----------------------------------------------------------------------------

write_csv(datos_crudos, archivo_csv)
cat("Copia cruda guardada en:", archivo_csv, "\n")

# -----------------------------------------------------------------------------
# 4. ESTRUCTURA INICIAL - EXPLORACIÓN
# -----------------------------------------------------------------------------

cat("\n--- ESTRUCTURA DE LA BASE DE DATOS ---\n")
str(datos_crudos, list.len = 20)
cat("\n--- NOMBRES DE VARIABLES (primeras 50) ---\n")
print(head(names(datos_crudos), 50))
cat("\n--- RESUMEN ---\n")
summary(datos_crudos[, 1:min(10, ncol(datos_crudos))])

# -----------------------------------------------------------------------------
# 5. PLANTILLA PARA DEPURACIÓN Y TRANSFORMACIÓN
# -----------------------------------------------------------------------------
# Los estudiantes deben completar las tareas indicadas en Indicaciones_Taller_3.md
# Con ~482 variables, se recomienda trabajar por bloques temáticos:
# - Variables sociodemográficas (edad, sexo, educación, etc.)
# - Variables del negocio (ingresos, empleados, formalidad, etc.)
# - Variables de actitudes emprendedoras

datos_limpios <- datos_crudos %>%
  # TODO: Los estudiantes aplicarán las transformaciones según las indicaciones
  # Seleccionar subconjunto de variables para el taller si 482 es excesivo:
  # select(...) %>%
  identity()  # Placeholder - reemplazar con transformaciones reales

# -----------------------------------------------------------------------------
# 6. GUARDAR DATOS PROCESADOS (después de completar el taller)
# -----------------------------------------------------------------------------

# Descomentar al finalizar el taller:
# archivo_limpio <- file.path(dir_salida, "tenderos_limpos.csv")
# write_csv(datos_limpios, archivo_limpio)
# cat("Datos depurados guardados en:", archivo_limpio, "\n")

# -----------------------------------------------------------------------------
# REFERENCIAS Y DOCUMENTACIÓN
# -----------------------------------------------------------------------------
# - Dataset: https://doi.org/10.34848/FK2/RD5NIK
# - Cuestionario (PDF): https://research-data.urosario.edu.co/file.xhtml?persistentId=doi:10.34848/FK2/RD5NIK/3ENESL
# - Informe estudio (PDF): https://research-data.urosario.edu.co/file.xhtml?persistentId=doi:10.34848/FK2/RD5NIK/4FCEWZ
# - Informe completo: https://alianzaefi.com/download/informe-estudio-nacional-de-emprendimiento-a-tenderos-primera-ronda/
