# =============================================================================
# LEER ARCHIVO .SAV (SPSS) - GEM Adult Population Survey
# Dataset: GEM 2021 APS Global Individual Level Data
# Fuente: Global Entrepreneurship Monitor (GEM)
# =============================================================================

# -----------------------------------------------------------------------------
# 1. PAQUETES
# -----------------------------------------------------------------------------

# install.packages("haven")  # Descomentar si no está instalado

library(haven)
library(dplyr)

# -----------------------------------------------------------------------------
# 2. CONFIGURACIÓN - Ruta del archivo
# -----------------------------------------------------------------------------

# Directorio de trabajo
if (requireNamespace("rstudioapi", quietly = TRUE) && rstudioapi::isAvailable()) {
  setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
}

# Archivo: GEM Adult Population Survey (APS) - Global Individual Level Data
archivo_sav <- "C:/Users/owoc9/Downloads_Unal/datos/GEM 2021 APS Global Individual Level Data_8Dec2025.sav"

# -----------------------------------------------------------------------------
# 3. LEER ARCHIVO .SAV
# -----------------------------------------------------------------------------

if (!file.exists(archivo_sav)) {
  stop(
    "No se encontró el archivo .sav\n",
    "Coloque su archivo en la carpeta 'datos/' o edite la variable 'archivo_sav'\n",
    "Ruta buscada: ", archivo_sav
  )
}

cat("Leyendo archivo:", archivo_sav, "\n")

datos <- read_sav(archivo_sav)

# -----------------------------------------------------------------------------
# 4. EXPLORACIÓN
# -----------------------------------------------------------------------------

cat("\nRegistros:", nrow(datos), "\n")
cat("Variables:", ncol(datos), "\n")
cat("\n--- Primeras variables ---\n")
print(head(names(datos), 20))
cat("\n--- Estructura ---\n")
str(datos, list.len = 15)
cat("\n--- Primeras filas ---\n")
print(head(datos, 3))

# -----------------------------------------------------------------------------
# 5. OPCIONAL: Convertir a data frame estándar y guardar en CSV
# -----------------------------------------------------------------------------

# Convertir etiquetas de valor a factor (opcional)
datos_df <- as.data.frame(datos)

# Guardar copia en CSV
archivo_csv <- sub("\\.sav$", "_exportado.csv", archivo_sav)
write.csv(datos_df, archivo_csv, row.names = FALSE)
cat("\nCopia guardada en:", archivo_csv, "\n")
