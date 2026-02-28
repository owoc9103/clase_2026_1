library(readxl)
library(dplyr)
library(writexl)
bd<-read_excel("C:/Users/owoc9/Documents/U Javeriana/Analítica de datos para la toma de decisiones/GEM_Base_Datos/GEM 2022 APS Colombia Individual Level Data_6Feb2023.xlsx")

# Contar cuántos NA hay por columna
nas_por_columna <- sapply(bd, function(col) sum(is.na(col)))

# Convertir el resultado en un data.frame
nas_df <- data.frame(
  Campo = names(nas_por_columna),
  Conteo_NA = as.integer(nas_por_columna),
  row.names = NULL
)

nas_df<- nas_df %>% arrange(desc(Conteo_NA)) %>% filter(Conteo_NA>=1203)
colum_delete<-nas_df$Campo

which(colnames(bd)%in%colum_delete)


bd<-bd[,-which(colnames(bd)%in%colum_delete)]

df_column<-data.frame("Columnas"=colnames(bd))

colnames(bd)

write.table(df_column,"C:/Users/owoc9/Documents/U Javeriana/Analítica de datos para la toma de decisiones/GEM_Base_Datos/colum.csv")

bd$age7c <- with(bd,
            ifelse(age < 18, 1,
            ifelse(age >= 18 & age <= 24, 2,
            ifelse(age >= 25 & age <= 34, 3,
            ifelse(age >= 35 & age <= 44, 4,
            ifelse(age >= 45 & age <= 54, 5,
            ifelse(age >= 55 & age<= 64, 6,
            ifelse(age >= 65 & age <= 99, 7,
            ifelse(is.na(age), -2, NA)))))))))

bd$age7c <- factor(bd$age7c,
                         levels = c(1, 2, 3, 4, 5, 6, 7, -2),
                         labels = c("Menos de 18",
                                    "18-24",
                                    "25-34",
                                    "35-44",
                                    "45-54",
                                    "55-64",
                                    "65-99",
                                    "Sin respuesta/Rechaza"))



table(bd$opportL)

# Requiere que tu data frame se llame 'bd' y que contenga la variable 'knowentR'
bd$knowentR<- factor(bd$knowentR,
                           levels = c(0, 1, 2, 3, -1, -2),
                           labels = c("Ninguno", "Uno", "De 2 a 4", "5 o más", "No lo sabe", "Rechaza"))


bd$opportL <- factor(bd$opportL,
                          levels = c(5, 4, 3, 2, 1, -1, -2),
                          labels = c("Completamente de acuerdo", 
                                     "Algo de acuerdo", 
                                     "Ni de acuerdo ni en desacuerdo", 
                                     "Poco de acuerdo", 
                                     "Nada de acuerdo", 
                                     "No lo sabe", 
                                     "Rechaza"))


bd$suskillL <- factor(bd$suskillL,
                     levels = c(5, 4, 3, 2, 1, -1, -2),
                     labels = c("Completamente de acuerdo", 
                                "Algo de acuerdo", 
                                "Ni de acuerdo ni en desacuerdo", 
                                "Poco de acuerdo", 
                                "Nada de acuerdo", 
                                "No lo sabe", 
                                "Rechaza"))


bd$fearfailL <- factor(bd$fearfailL,
                      levels = c(5, 4, 3, 2, 1, -1, -2),
                      labels = c("Completamente de acuerdo", 
                                 "Algo de acuerdo", 
                                 "Ni de acuerdo ni en desacuerdo", 
                                 "Poco de acuerdo", 
                                 "Nada de acuerdo", 
                                 "No lo sabe", 
                                 "Rechaza"))

bd$easystartL <- factor(bd$easystartL,
                       levels = c(5, 4, 3, 2, 1, -1, -2),
                       labels = c("Completamente de acuerdo", 
                                  "Algo de acuerdo", 
                                  "Ni de acuerdo ni en desacuerdo", 
                                  "Poco de acuerdo", 
                                  "Nada de acuerdo", 
                                  "No lo sabe", 
                                  "Rechaza"))


# Vector con los nombres de las variables a recodificar
vars_likert <- c("oppism", "proact", "creativ", "vision", 
                 "equalincL", "nbgoodcL", "nbstatusL", 
                 "nbmediaL", "nbsocentL")

# Etiquetas correspondientes
etiquetas_likert <- c("Completamente de acuerdo", 
                      "Algo de acuerdo", 
                      "Ni de acuerdo ni en desacuerdo", 
                      "Poco de acuerdo", 
                      "Nada de acuerdo", 
                      "No lo sabe", 
                      "Rechaza")

# Recodificación sobrescribiendo en el mismo data frame
for (var in vars_likert) {
  bd[[var]] <- factor(bd[[var]],
                      levels = c(5, 4, 3, 2, 1, -1, -2),
                      labels = etiquetas_likert)
}

# Vector con los nombres de las variables a recodificar
vars_si_no <- c("bstart", "bjobst")

# Etiquetas correspondientes
etiquetas_si_no <- c("Sí", "No", "No sabe", "Rechaza","Otro")

# Recodificación sobrescribiendo directamente en el data frame
for (var in vars_si_no) {
  bd[[var]] <- factor(bd[[var]],
                      levels = c(1, 2, -1, -2,0),
                      labels = etiquetas_si_no)
}


# Vector con las variables a recodificar
vars_si_no_2 <- c("ownmge", "omjobst","OWNMGE22","OMJOBST22")

# Etiquetas correspondientes
etiquetas_si_no <- c("Sí", "No", "No sabe", "Rechaza","Otro")

# Recodificación sobrescribiendo directamente
for (var in vars_si_no_2) {
  bd[[var]] <- factor(bd[[var]],
                      levels = c(1, 2, -1, -2,0),
                      labels = etiquetas_si_no)
}


# Etiquetas para la variable gender
etiquetas_genero <- c("Hombre", "Mujer", "No sabe", "Rechaza")

# Recodificación directa en el data frame
bd$gender <- factor(bd$gender,
                    levels = c(1, 2, -1, -2),
                    labels = etiquetas_genero)



bd$hhsize <- ifelse(bd$hhsize == -1, "No sabe",
                          ifelse(bd$hhsize == -2, "Rechaza",
                                 as.character(bd$hhsize)))




# Variables a recodificar
vars_futsup_discent <- c("futsup", "discent","busang","doublecount")

# Etiquetas
etiquetas_si_no <- c("Sí", "No", "No sabe", "Rechaza","Otro")

# Recodificación
for (var in vars_futsup_discent) {
  bd[[var]] <- factor(bd[[var]],
                      levels = c(1, 2, -1, -2,0),
                      labels = etiquetas_si_no)
}

# Etiquetas para occup
etiquetas_occup <- c(
  "Empleado por cuenta ajena a tiempo completo",    # 1
  "Empleado por cuenta ajena a tiempo parcial",     # 2
  "Autoempleado",                                   # 3
  "Desempleado",                                    # 4
  "Jubilado",                                       # 5
  "Estudiante",                                     # 6
  "Labores del hogar",                              # 7
  "No está buscando empleo",                        # 8
  "Otro caso (Especificar) OCCUP_OTH (NO LEER)",    # 9
  "Cuidador de un miembro de su familia",           # 10
  "No sabe (NO LEER)",                              # -1
  "No contesta (NO LEER)"                           # -2
)

# Valores correspondientes (ordenados como en etiquetas_occup)
valores_occup <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2)

# Recodificación
bd$occup <- factor(bd$occup,
                   levels = valores_occup,
                   labels = etiquetas_occup)



# Etiquetas para COhhinc
etiquetas_ingresos <- c(
  "Menos de 1 SMMLV", 
  "Entre 1 y 2 SMMLV", 
  "Más de 2 SMMLV y menos de 3 SMMLV", 
  "Más de 3 SMMLV y menos de 4 SMMLV", 
  "Más de 4 SMMLV y menos de 5 SMMLV", 
  "Más de 5 SMMLV y menos de 6 SMMLV", 
  "Más de 6 SMMLV", 
  "No sabe", 
  "Rechaza"
)

# Valores correspondientes
valores_ingresos <- c(1, 2, 3, 4, 5, 6, 7, -1, -2)

# Recodificación
bd$COhhinc <- factor(bd$COhhinc,
                     levels = valores_ingresos,
                     labels = etiquetas_ingresos)


# Etiquetas para COREduc
etiquetas_educacion <- c(
  "Sin estudios", 
  "Primaria incompleta", 
  "Primaria Completa", 
  "Secundaria incompleta", 
  "Secundaria completa", 
  "Técnico incompleto", 
  "Técnico completo", 
  "Tecnológico incompleto", 
  "Tecnológico completo", 
  "Universitario incompleto", 
  "Universitario completo", 
  "Posgrado (especialización, maestría, doctorado)", 
  "No sabe", 
  "Rechaza"
)

# Valores correspondientes
valores_educacion <- c(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, -1, -2)

# Recodificación
bd$COREduc <- factor(bd$COREduc,
                     levels = valores_educacion,
                     labels = etiquetas_educacion)



# Etiquetas para COpost
etiquetas_copost <- c(
  "No es aplicable",  # -3
  "No sabe",          # -1
  "Rechaza"           # -2
)

# Valores correspondientes
valores_copost <- c(-3, -1, -2)

# Recodificación
bd$COpost <- factor(bd$COpost,
                    levels = valores_copost,
                    labels = etiquetas_copost)


# Etiquetas para la variable contact
etiquetas_contact <- c(
  "Presencial (cara a cara)",     # 1
  "Linear telefónica fija",       # 2
  "Línea telefónica móvil",       # 3
  "Otro caso"                     # 4
)

# Valores correspondientes
valores_contact <- c(1, 2, 3, 4)

# Recodificación
bd$contact <- factor(bd$contact,
                     levels = valores_contact,
                     labels = etiquetas_contact)

# Etiquetas para la variable cphhinc
etiquetas_cphhinc <- c(
  "Han disminuido considerablemente",   # 1
  "Han disminuido un poco",             # 2
  "No han mostrado cambios sustanciales", # 3
  "Han aumentado un poco",              # 4
  "Han aumentado considerablement",     # 5
  "No sabe",                            # -1
  "Rechaza"                             # -2
)

# Valores correspondientes
valores_cphhinc <- c(1, 2, 3, 4, 5, -1, -2)

# Recodificación
bd$cphhinc <- factor(bd$cphhinc,
                     levels = valores_cphhinc,
                     labels = etiquetas_cphhinc)


which(colnames(bd)=="COXXNIVSE")

# Etiquetas para la variable COXXNIVSE
etiquetas_COXXNIVSE <- c(
  "Estrato 1",   # 1
  "Estrato 2",   # 2
  "Estrato 3",   # 3
  "Estrato 4",   # 4
  "Estrato 5",   # 5
  "Estrato 6",   # 6
  "No sabe",     # -1
  "Rechaza"      # -2
)

# Valores correspondientes
valores_COXXNIVSE <- c(1, 2, 3, 4, 5, 6, -1, -2)

# Recodificación
bd$COXXNIVSE <- factor(bd$COXXNIVSE,
                       levels = valores_COXXNIVSE,
                       labels = etiquetas_COXXNIVSE)


# Etiquetas para la variable COxxetn
etiquetas_COxxetn <- c(
  "Afrodescendiente",                         # 1
  "Asiático",                                 # 2
  "Blanco",                                   # 3
  "Indígena",                                 # 4
  "Mulato",                                   # 5
  "Mestizo",                                  # 6
  "Raizal",                                   # 7
  "Otro (ESPECIFICAR) XXETN_OTH (NO LEER)",   # 8
  "No sabe",                                  # -1
  "Rechaza"                                   # -2
)

# Valores correspondientes
valores_COxxetn <- c(1, 2, 3, 4, 5, 6, 7, 8, -1, -2)

# Recodificación
bd$COxxetn <- factor(bd$COxxetn,
                     levels = valores_COxxetn,
                     labels = etiquetas_COxxetn)

# Etiquetas para la variable COnacio
etiquetas_CONACIO <- c(
  "Colombiana",  # 1
  "Otra"         # 2
)

# Valores correspondientes
valores_CONACIO <- c(1, 2)

# Recodificación
bd$CONACIO <- factor(bd$CONACIO,
                     levels = valores_CONACIO,
                     labels = etiquetas_CONACIO)

# Etiquetas para las variables Bstart22 y BJOBST22
etiquetas_binarias <- c(
  "Sí",       # 1
  "No",       # 2
  "No sabe",  # -1
  "Rechaza"   # -2
)

# Valores correspondientes
valores_binarios <- c(1, 2, -1, -2)

# Recodificación
bd$Bstart22 <- factor(bd$Bstart22,
                      levels = valores_binarios,
                      labels = etiquetas_binarias)

bd$BJOBST22 <- factor(bd$BJOBST22,
                      levels = valores_binarios,
                      labels = etiquetas_binarias)


# Lista de las columnas a recategorizar
columnas <- c("SU_CSTLOC", "SU_CSTNAT", "SU_CSTEXP")

# Recategorizando las columnas especificadas
for (col in columnas) {
  bd[[col]] <- ifelse(bd[[col]] == 1, "Sí",
                      ifelse(bd[[col]] == 2, "No",
                             ifelse(bd[[col]] == -1, "No lo sabe",
                                    ifelse(bd[[col]] == -2, "Rechaza", NA))))
}



# Lista de las columnas a recategorizar
columnas <- c("SU_NEWPROD", "SU_NEWPROC")

# Recategorizando las columnas especificadas
for (col in columnas) {
  bd[[col]] <- ifelse(bd[[col]] == 1, "No, no ofrezco ningún producto o servicio que sea nuevo",
                      ifelse(bd[[col]] == 2, "Nuevo para la gente de la zona en la que vive",
                             ifelse(bd[[col]] == 3, "Nuevo para la gente de su país",
                                    ifelse(bd[[col]] == 4, "Nuevo en el mundo",
                                           ifelse(bd[[col]] == -1, "No lo sabe (NO LEER)",
                                                  ifelse(bd[[col]] == -2, "Rechaza (NO LEER)", NA))))))
}


delete_colum<-c('ctryalp',	'setid',	'ID',	'REGION',	'WBINC',	'WBincREV',	'yrsurv',	'weight',	'WEIGHT_L',	'WEIGHT_A',	'GEMOCCU',	'GEMWORK',	'GEMWORK3',	'GEMHHINC',	'GEMEDUC',	'UNEDUC',	'UNEDUC97',	'COZONAROU',	'Bstart22',	'BJOBST22',	'OWNMGE22',	'OMJOBST22',	'BUSANG22',	'FUTSUP22',	'DISCEN22',	'KNOWEN22',	'OPPORT22',	'SUSKIL22',	'FRFAIL22',	'EASYST22',	'OPPISM22',	'PROACT22',	'CREATIV22',	'VISION22',	'EQUALI22',	'NBGOOD22',	'NBSTAT22',	'NBMEDI22',	'INDSUP22',	'CULSUP22',	'SUB',	'SUBA',	'SUBO',	'SUBOA',	'SUBOANW',	'OMBABYX',	'OMESTBX',	'BABYBUSM',	'BABYBUSO',	'ESTBBUSM',	'ESTBBUSO',	'SUBOANWC',	'SUBOANW1',	'BABYBUS1',	'ESTBBUS1',	'TEA22',	'ANYBUSOW',	'TEA22MAL',	'TEA22FEM',	'BUSANGVL',	'SU_HITEC',	'BB_HITEC',	'EB_HITEC',	'TEAHITEC',	'EXTHITEC',	'su_22TEC',	'bb_22TEC',	'SU_SIC4C',	'BB_SIC4C',	'EB_SIC4C',	'SU_ISIC4_1D',	'BB_ISIC4_1D',	'EB_ISIC4_1D',	'TEAISIC4_1D',	'TEASIC4C',	'TEA22S1C',	'TEA22S2C',	'TEA22S3C',	'TEA22S4C',	'BO_EXAGR',	'EXIT_CTD',	'EXIT_ENT',	'TEA22EMP',	'su_22emp',	'bb_22emp',	'EB_22EMP',	'TEA22HJG',	'su_22hjg',	'bb_22hjg',	'EB_22HJG',	'tea22kix',	'su_22kix',	'bb_22kix',	'eb_22kix',	'tea22hix',	'su_22hix',	'bb_22hix',	'eb_22hix',	'FUTSUPNO',	'SU_MKSC',	'BB_MKSC',	'EB_MKSC',	'BB_CSTLOC',	'BB_CSTNAT',	'BB_CSTEXP',	'BB_NEWPROD',	'BB_NEWPROC',	'EB_CSTLOC',	'EB_CSTNAT',	'EB_CSTEXP',	'EB_NEWPROD',	'TEAIMPACT1',	'TEAIMPACT2',	'OPPIS_1',	'OPPIS_2',	'OPPIS_3',	'PROAC_1',	'PROAC_2',	'PROAC_3',	'CREATI_1',	'CREATI_2',	'CREATI_3',	'VISIO_1',	'VISIO_2',	'VISIO_3',	'SOCEN_1',	'SOCEN_2',	'SOCEN_3',	'INDSP22A',	'INDSP22B',	'INDSP22C',	'INDSP22D',	'CULSP22A',	'CULSP22B',	'CULSP22C',	'CULSP22D',	'TEA22IND',	'TEA22SPON',	'SU_SPON',	'SU_IND',	'BB_SPON',	'BB_IND',	'EB_SPON',	'EB_IND',	'TEAactivityr',	'MSURV')


bd2 <- bd[, !(names(bd) %in% delete_colum)]

write_xlsx(bd2,"C:/Users/owoc9/Documents/U Javeriana/2025-II/Analítica de Datos para la toma de Decisiones/Talle 3 GEM_Base_Datos/GEM_Data_Final.xlsx")
