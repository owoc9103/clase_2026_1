# =============================================================================
# EXPORTAR Indicaciones_Ajuste_GEM.Rmd A HTML
# =============================================================================
# Ejecutar este script en R o RStudio para generar el archivo HTML
# Requiere: install.packages("rmarkdown")
# =============================================================================

# Opción 1: Si está en RStudio, abra Indicaciones_Ajuste_GEM.Rmd y pulse
#           el botón "Knit" (tejer) o Ctrl+Shift+K

# Opción 2: Ejecutar desde consola R:
if (requireNamespace("rmarkdown", quietly = TRUE)) {
  rmarkdown::render(
    input = "Indicaciones_Ajuste_GEM.Rmd",
    output_format = "html_document",
    output_file = "Indicaciones_Ajuste_GEM.html",
    encoding = "UTF-8"
  )
  message("HTML generado: Indicaciones_Ajuste_GEM.html")
} else {
  message("Instale rmarkdown: install.packages('rmarkdown')")
}
