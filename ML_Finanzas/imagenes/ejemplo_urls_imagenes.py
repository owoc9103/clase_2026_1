"""
Ejemplo de uso del script descargar_imagenes.py

Este archivo muestra cómo usar el script para descargar imágenes.
Puedes editar este archivo con las URLs de las imágenes que quieras descargar.
"""

from descargar_imagenes import DescargadorImagenes
from pathlib import Path

# Directorio donde se guardarán las imágenes
DIRECTORIO_IMAGENES = Path(__file__).parent / "imagenes"

# Ejemplo 1: Descargar una imagen desde una URL específica
def ejemplo_descarga_simple():
    """Descarga una imagen desde una URL."""
    descargador = DescargadorImagenes(directorio_destino=DIRECTORIO_IMAGENES)
    
    url = "https://ejemplo.com/imagen.jpg"
    nombre = "mi_imagen.jpg"
    
    descargador.descargar_desde_url(url, nombre)


# Ejemplo 2: Descargar múltiples imágenes desde URLs
def ejemplo_descarga_multiple():
    """Descarga múltiples imágenes desde URLs."""
    descargador = DescargadorImagenes(directorio_destino=DIRECTORIO_IMAGENES)
    
    # Diccionario con {nombre_archivo: url}
    urls_imagenes = {
        "portada_ml_finanzas.jpg": "https://ejemplo.com/portada.jpg",
        "objetivos_ml.gif": "https://ejemplo.com/objetivos.gif",
        "industria_financiera.jpg": "https://ejemplo.com/industria.jpg",
        # Agrega más URLs aquí...
    }
    
    resultados = descargador.descargar_lote_desde_urls(urls_imagenes, delay=1.0)
    
    # Mostrar resultados
    for nombre, exito in resultados.items():
        if exito:
            print(f"✓ {nombre} descargado correctamente")
        else:
            print(f"✗ Error al descargar {nombre}")


# Ejemplo 3: Usar Unsplash para buscar imágenes
def ejemplo_buscar_unsplash():
    """Busca y descarga imágenes usando Unsplash."""
    # Necesitas configurar tu clave de Unsplash
    # Opción 1: Como variable de entorno
    # export UNSPLASH_ACCESS_KEY="tu_clave_aqui"
    
    # Opción 2: Pasarla directamente (no recomendado para producción)
    UNSPLASH_KEY = "tu_clave_aqui"  # Reemplaza con tu clave
    
    descargador = DescargadorImagenes(
        directorio_destino=DIRECTORIO_IMAGENES,
        unsplash_key=UNSPLASH_KEY
    )
    
    # Buscar y descargar una imagen
    descargador.descargar_imagen_por_busqueda(
        "portada_ml_finanzas.jpg",
        "machine learning finance"
    )


# Ejemplo 4: Ver lista de imágenes necesarias
def ejemplo_listar_imagenes():
    """Muestra la lista de imágenes necesarias para las presentaciones."""
    descargador = DescargadorImagenes(directorio_destino=DIRECTORIO_IMAGENES)
    
    # Esto mostrará todas las imágenes necesarias con sus términos de búsqueda
    descargador.descargar_imagenes_necesarias(usar_unsplash=False)


if __name__ == "__main__":
    print("Ejemplos de uso del descargador de imágenes\n")
    print("1. Ver lista de imágenes necesarias:")
    ejemplo_listar_imagenes()
    
    print("\n" + "="*50)
    print("\nPara usar estos ejemplos:")
    print("1. Edita este archivo con las URLs de tus imágenes")
    print("2. O configura UNSPLASH_ACCESS_KEY para usar búsqueda automática")
    print("3. Ejecuta: python ejemplo_urls_imagenes.py")
