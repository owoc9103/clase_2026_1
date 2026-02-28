####Integrantes####
###Oscar Orozco####
###################

#Punto 1.
library(readr)

ruta <- "C:/Users/owoc9/Documents/U Javeriana/2025-II/Analítica de Datos para la toma de Decisiones/Taller 2/Insumos/taller2-fusion_combinacion/BaseDatos"

options(warn = -1)

archivos <- list.files(path = ruta, pattern = "\\.csv$", full.names = TRUE)


lista_ocupados <- list()
lista_caracteristicas <- list()


for (archivo in archivos) {
  

  nombre_archivo <- basename(archivo)
  

  tamano_kb <- round(file.info(archivo)$size / 1024, 2)
  

  cat("Archivo:", nombre_archivo, "| Tamaño:", tamano_kb, "KB\n")
  

  df <- read_delim(archivo, delim = ";", locale = locale(encoding = "UTF-8"))
  

  if (grepl("ocupados", nombre_archivo, ignore.case = TRUE)) {
    lista_ocupados[[nombre_archivo]] <- df
  } else if (grepl("caracteristicas", nombre_archivo, ignore.case = TRUE)) {
    lista_caracteristicas[[nombre_archivo]] <- df
  }
}


names(lista_ocupados)
names(lista_caracteristicas)

ocupados<-do.call("rbind",lista_ocupados)
caracteristicas<-do.call("rbind",lista_caracteristicas)

#Punto 2.
colnames(ocupados)

colnames(caracteristicas)

##Modificando el nombre de algunas variables de la base de datos
##de características

colnames(caracteristicas)[6]<-"Num_ord_persona_pp_inf"
colnames(caracteristicas)[7]<-"Sexo"
colnames(caracteristicas)[8]<-"Mes"
colnames(caracteristicas)[9]<-"Year"
colnames(caracteristicas)[10]<-"Años_Cumplidos"
colnames(caracteristicas)[11]<-"Parent_Jef_Hog"
colnames(caracteristicas)[12]<-"Actualemte"
colnames(caracteristicas)[13]<-"Padre_reside_Hog"
colnames(caracteristicas)[14]<-"Num_Ord_person_v1"
colnames(caracteristicas)[15]<-"Afi_Cot_Ben_Salud"
colnames(caracteristicas)[16]<-"Afi_Cot_Ben_Salud"

