# Descargador de Imágenes para Presentaciones

Script de Python para descargar imágenes de internet para las presentaciones de Machine Learning en Finanzas.

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements_imagenes.txt
```

## Uso Básico

### Opción 1: Ver lista de imágenes necesarias

```bash
python descargar_imagenes.py
```

Esto mostrará todas las imágenes necesarias con sus términos de búsqueda sugeridos.

### Opción 2: Descargar desde URL específica

```bash
python descargar_imagenes.py --url "https://ejemplo.com/imagen.jpg,nombre_archivo.jpg"
```

### Opción 3: Usar Unsplash (requiere API key)

1. Regístrate en [Unsplash Developers](https://unsplash.com/developers)
2. Crea una aplicación y obtén tu Access Key
3. Configura la variable de entorno:
   ```bash
   # Windows PowerShell
   $env:UNSPLASH_ACCESS_KEY="tu_clave_aqui"
   
   # Windows CMD
   set UNSPLASH_ACCESS_KEY=tu_clave_aqui
   
   # Linux/Mac
   export UNSPLASH_ACCESS_KEY="tu_clave_aqui"
   ```
4. Ejecuta:
   ```bash
   python descargar_imagenes.py --unsplash
   ```

## Uso Programático

```python
from descargar_imagenes import DescargadorImagenes
from pathlib import Path

# Crear descargador
descargador = DescargadorImagenes(
    directorio_destino=Path("imagenes"),
    unsplash_key="tu_clave_opcional"
)

# Descargar desde URL
descargador.descargar_desde_url(
    "https://ejemplo.com/imagen.jpg",
    "mi_imagen.jpg"
)

# Descargar múltiples imágenes
urls = {
    "imagen1.jpg": "https://ejemplo.com/img1.jpg",
    "imagen2.jpg": "https://ejemplo.com/img2.jpg"
}
descargador.descargar_lote_desde_urls(urls)
```

## Imágenes Necesarias

El script incluye una lista predefinida de 24 imágenes necesarias para las presentaciones:

- `portada_ml_finanzas.jpg` - Portada principal
- `objetivos_ml.gif` - Objetivos de ML
- `industria_financiera.jpg` - Industria financiera
- `big_data_finanzas.jpg` - Big Data
- `cloud_computing.gif` - Cloud computing
- `tres_pilares_ml.jpg` - Tres pilares
- `supervised_learning.jpg` - Aprendizaje supervisado
- `unsupervised_learning.jpg` - Aprendizaje no supervisado
- `reinforcement_learning.gif` - Aprendizaje por refuerzo
- `trading_algoritmico.jpg` - Trading algorítmico
- `gestion_riesgos.jpg` - Gestión de riesgos
- `robo_advisor.gif` - Robo-advisor
- `futuro_finanzas.jpg` - Futuro de finanzas
- `regulacion.jpg` - Regulación
- `riesgos_tecnicos.gif` - Riesgos técnicos
- `etica_ia.jpg` - Ética en IA
- `stack_tecnologico.jpg` - Stack tecnológico
- `trading_strategies.jpg` - Estrategias de trading
- `robo_advisor_caso.jpg` - Caso robo-advisor
- `analisis_riesgo.gif` - Análisis de riesgo
- `resumen_ml.gif` - Resumen ML
- `discusion.jpg` - Discusión
- `referencias.jpg` - Referencias
- `cierre_clase.jpg` - Cierre de clase

## Fuentes Recomendadas de Imágenes

- **Unsplash**: https://unsplash.com (gratis, requiere API key para búsqueda automática)
- **Pexels**: https://www.pexels.com (gratis)
- **Pixabay**: https://pixabay.com (gratis)
- **Freepik**: https://www.freepik.com (algunas gratuitas)

## Notas

- Las imágenes se guardan en la carpeta `imagenes/` dentro de `ML_Finanzas/`
- El script respeta los rate limits con delays entre descargas
- Si una imagen ya existe, se omite automáticamente
- Para GIFs animados, busca específicamente archivos .gif o convierte videos a GIF
