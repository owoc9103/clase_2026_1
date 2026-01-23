"""
Script para descargar imágenes de internet para las presentaciones de ML en Finanzas.

Este script permite:
1. Descargar imágenes desde URLs directas
2. Buscar y descargar imágenes usando la API de Unsplash (gratuita)
3. Descargar múltiples imágenes en lote

Requisitos:
    Las dependencias están especificadas en ../requirements.txt
    Instalar con: pip install -r ../requirements.txt
    
    Dependencias principales para este script:
    - requests>=2.31.0
    - Pillow>=10.0.0

Para usar la API de Unsplash (opcional):
    1. Regístrate en https://unsplash.com/developers
    2. Crea una aplicación
    3. Obtén tu Access Key
    4. Agrégala al script o como variable de entorno UNSPLASH_ACCESS_KEY
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Optional
import time
from urllib.parse import urlparse

# Validar dependencias
try:
    import requests
except ImportError:
    print("[ERROR] La librería 'requests' no está instalada.")
    print("   Instala las dependencias con: pip install -r ../requirements.txt")
    sys.exit(1)

try:
    from PIL import Image
    PILOW_AVAILABLE = True
except ImportError:
    PILOW_AVAILABLE = False
    print("[ADVERTENCIA] Pillow no está disponible. La validación de imágenes estará deshabilitada.")

# Configuración
# El script está en la carpeta imagenes, así que guardamos las imágenes en la misma carpeta
IMAGENES_DIR = Path(__file__).parent
IMAGENES_DIR.mkdir(exist_ok=True)

# Lista de imágenes necesarias para las presentaciones
IMAGENES_NECESARIAS = {
    "portada_ml_finanzas.jpg": {
        "busqueda": "machine learning finance",
        "descripcion": "Portada principal de ML en Finanzas"
    },
    "objetivos_ml.gif": {
        "busqueda": "machine learning goals objectives",
        "descripcion": "Objetivos de Machine Learning"
    },
    "industria_financiera.jpg": {
        "busqueda": "financial industry banking",
        "descripcion": "Industria financiera"
    },
    "big_data_finanzas.jpg": {
        "busqueda": "big data finance analytics",
        "descripcion": "Big Data en finanzas"
    },
    "cloud_computing.gif": {
        "busqueda": "cloud computing technology",
        "descripcion": "Cloud computing"
    },
    "tres_pilares_ml.jpg": {
        "busqueda": "machine learning infrastructure tools",
        "descripcion": "Tres pilares de ML"
    },
    "supervised_learning.jpg": {
        "busqueda": "supervised learning classification",
        "descripcion": "Aprendizaje supervisado"
    },
    "unsupervised_learning.jpg": {
        "busqueda": "unsupervised learning clustering",
        "descripcion": "Aprendizaje no supervisado"
    },
    "reinforcement_learning.gif": {
        "busqueda": "reinforcement learning AI",
        "descripcion": "Aprendizaje por refuerzo"
    },
    "trading_algoritmico.jpg": {
        "busqueda": "algorithmic trading stock market",
        "descripcion": "Trading algorítmico"
    },
    "gestion_riesgos.jpg": {
        "busqueda": "risk management finance",
        "descripcion": "Gestión de riesgos"
    },
    "robo_advisor.gif": {
        "busqueda": "robo advisor fintech",
        "descripcion": "Robo-advisor"
    },
    "futuro_finanzas.jpg": {
        "busqueda": "future finance technology",
        "descripcion": "Futuro de las finanzas"
    },
    "regulacion.jpg": {
        "busqueda": "financial regulation compliance",
        "descripcion": "Regulación financiera"
    },
    "riesgos_tecnicos.gif": {
        "busqueda": "technology risks cybersecurity",
        "descripcion": "Riesgos tecnológicos"
    },
    "etica_ia.jpg": {
        "busqueda": "AI ethics responsible technology",
        "descripcion": "Ética en IA"
    },
    "stack_tecnologico.jpg": {
        "busqueda": "technology stack programming",
        "descripcion": "Stack tecnológico"
    },
    "trading_strategies.jpg": {
        "busqueda": "trading strategies investment",
        "descripcion": "Estrategias de trading"
    },
    "robo_advisor_caso.jpg": {
        "busqueda": "automated investment advisor",
        "descripcion": "Caso de estudio robo-advisor"
    },
    "analisis_riesgo.gif": {
        "busqueda": "risk analysis financial",
        "descripcion": "Análisis de riesgo"
    },
    "resumen_ml.gif": {
        "busqueda": "machine learning summary overview",
        "descripcion": "Resumen de ML"
    },
    "discusion.jpg": {
        "busqueda": "discussion meeting collaboration",
        "descripcion": "Discusión y debate"
    },
    "referencias.jpg": {
        "busqueda": "books references library",
        "descripcion": "Referencias bibliográficas"
    },
    "cierre_clase.jpg": {
        "busqueda": "education graduation success",
        "descripcion": "Cierre de clase"
    }
}


class DescargadorImagenes:
    """Clase para descargar imágenes desde internet."""
    
    def __init__(self, directorio_destino: Path = IMAGENES_DIR, unsplash_key: Optional[str] = None):
        """
        Inicializa el descargador de imágenes.
        
        Args:
            directorio_destino: Directorio donde se guardarán las imágenes
            unsplash_key: Clave de acceso de Unsplash (opcional)
        """
        self.directorio_destino = Path(directorio_destino)
        self.directorio_destino.mkdir(exist_ok=True)
        self.unsplash_key = unsplash_key or os.getenv("UNSPLASH_ACCESS_KEY")
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
    
    def _validar_imagen(self, ruta_archivo: Path) -> bool:
        """
        Valida que el archivo descargado sea una imagen válida.
        
        Args:
            ruta_archivo: Ruta al archivo a validar
            
        Returns:
            True si es una imagen válida, False en caso contrario
        """
        if not PILOW_AVAILABLE:
            return True  # Si Pillow no está disponible, asumimos que es válido
        
        try:
            # verify() cierra el archivo, así que necesitamos abrirlo dos veces
            with Image.open(ruta_archivo) as img:
                img.verify()
            # Reabrir para asegurar que el archivo esté en un estado válido
            with Image.open(ruta_archivo) as img:
                img.load()
            return True
        except Exception:
            return False
    
    def descargar_desde_url(self, url: str, nombre_archivo: str) -> bool:
        """
        Descarga una imagen desde una URL directa.
        
        Args:
            url: URL de la imagen
            nombre_archivo: Nombre del archivo de destino
            
        Returns:
            True si la descarga fue exitosa, False en caso contrario
        """
        try:
            print(f"Descargando {nombre_archivo} desde {url}...")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            ruta_destino = self.directorio_destino / nombre_archivo
            
            with open(ruta_destino, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            # Validar que sea una imagen válida
            if not self._validar_imagen(ruta_destino):
                print(f"[ADVERTENCIA] El archivo descargado podría no ser una imagen válida: {nombre_archivo}")
                # No eliminamos el archivo, por si acaso es útil
            
            print(f"[OK] Descargado: {nombre_archivo}")
            return True
            
        except Exception as e:
            print(f"[ERROR] Error al descargar {nombre_archivo}: {e}")
            return False
    
    def buscar_unsplash(self, query: str, cantidad: int = 1) -> List[str]:
        """
        Busca imágenes en Unsplash.
        
        Args:
            query: Término de búsqueda
            cantidad: Número de imágenes a buscar
            
        Returns:
            Lista de URLs de imágenes
        """
        if not self.unsplash_key:
            print("[ADVERTENCIA] No se proporcionó clave de Unsplash. Usa URLs directas o configura UNSPLASH_ACCESS_KEY")
            return []
        
        try:
            url = "https://api.unsplash.com/search/photos"
            params = {
                "query": query,
                "per_page": cantidad,
                "client_id": self.unsplash_key
            }
            
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            urls = [photo["urls"]["regular"] for photo in data.get("results", [])]
            
            return urls
            
        except Exception as e:
            print(f"[ERROR] Error al buscar en Unsplash: {e}")
            return []
    
    def _obtener_imagen_placeholder(self, ancho: int = 800, alto: int = 600) -> str:
        """
        Obtiene una URL de imagen placeholder usando Lorem Picsum.
        
        Args:
            ancho: Ancho de la imagen
            alto: Alto de la imagen
            
        Returns:
            URL de la imagen placeholder
        """
        import random
        # Usar un ID aleatorio para obtener diferentes imágenes
        imagen_id = random.randint(1, 1000)
        return f"https://picsum.photos/{ancho}/{alto}?random={imagen_id}"
    
    def descargar_imagen_placeholder(self, nombre_archivo: str, ancho: int = 800, alto: int = 600) -> bool:
        """
        Descarga una imagen placeholder (sin API key requerida).
        
        Args:
            nombre_archivo: Nombre del archivo de destino
            ancho: Ancho de la imagen (default: 800)
            alto: Alto de la imagen (default: 600)
            
        Returns:
            True si la descarga fue exitosa, False en caso contrario
        """
        url = self._obtener_imagen_placeholder(ancho, alto)
        return self.descargar_desde_url(url, nombre_archivo)
    
    def descargar_imagen_por_busqueda(self, nombre_archivo: str, termino_busqueda: str) -> bool:
        """
        Busca y descarga una imagen usando Unsplash.
        
        Args:
            nombre_archivo: Nombre del archivo de destino
            termino_busqueda: Término de búsqueda
            
        Returns:
            True si la descarga fue exitosa, False en caso contrario
        """
        urls = self.buscar_unsplash(termino_busqueda, cantidad=1)
        
        if not urls:
            return False
        
        return self.descargar_desde_url(urls[0], nombre_archivo)
    
    def descargar_lote_desde_urls(self, urls_dict: Dict[str, str], delay: float = 1.0) -> Dict[str, bool]:
        """
        Descarga múltiples imágenes desde URLs.
        
        Args:
            urls_dict: Diccionario con {nombre_archivo: url}
            delay: Tiempo de espera entre descargas (segundos)
            
        Returns:
            Diccionario con el resultado de cada descarga
        """
        resultados = {}
        
        for nombre, url in urls_dict.items():
            resultados[nombre] = self.descargar_desde_url(url, nombre)
            time.sleep(delay)  # Respetar rate limits
        
        return resultados
    
    def descargar_imagenes_necesarias(self, usar_unsplash: bool = False, usar_placeholder: bool = False) -> None:
        """
        Descarga todas las imágenes necesarias para las presentaciones.
        
        Args:
            usar_unsplash: Si True, intenta buscar en Unsplash. Si False, solo muestra las URLs necesarias.
            usar_placeholder: Si True, descarga imágenes placeholder cuando no hay API key disponible.
        """
        print(f"\n[DIRECTORIO] Directorio de destino: {self.directorio_destino}")
        print(f"[INFO] Total de imágenes necesarias: {len(IMAGENES_NECESARIAS)}\n")
        
        if usar_unsplash and not self.unsplash_key:
            if usar_placeholder:
                print("[INFO] No hay clave de Unsplash. Usando imágenes placeholder...\n")
            else:
                print("[ADVERTENCIA] No se puede usar Unsplash sin una clave de acceso.")
                print("   Opciones:")
                print("   1. Obtén una clave en https://unsplash.com/developers")
                print("   2. Configura la variable de entorno UNSPLASH_ACCESS_KEY")
                print("   3. Usa --placeholder para descargar imágenes placeholder")
                print("   4. Usa el método descargar_lote_desde_urls() con URLs directas\n")
                return
        
        exitosas = 0
        fallidas = 0
        
        for nombre_archivo, info in IMAGENES_NECESARIAS.items():
            ruta_destino = self.directorio_destino / nombre_archivo
            
            # Verificar si ya existe
            if ruta_destino.exists():
                print(f"[SKIP] Ya existe: {nombre_archivo}")
                continue
            
            if usar_unsplash and self.unsplash_key:
                if self.descargar_imagen_por_busqueda(nombre_archivo, info["busqueda"]):
                    exitosas += 1
                else:
                    fallidas += 1
                    print(f"   Búsqueda sugerida: {info['busqueda']}")
            elif usar_placeholder or (usar_unsplash and not self.unsplash_key):
                # Usar placeholder si se solicita o si no hay API key
                if self.descargar_imagen_placeholder(nombre_archivo):
                    exitosas += 1
                    print(f"   [PLACEHOLDER] Imagen de ejemplo descargada")
                else:
                    fallidas += 1
            else:
                print(f"[IMAGEN] {nombre_archivo}")
                print(f"   Descripción: {info['descripcion']}")
                print(f"   Búsqueda sugerida: {info['busqueda']}")
                print(f"   -> Necesitas proporcionar una URL para esta imagen\n")
            
            time.sleep(0.5)  # Rate limiting
        
        if usar_unsplash or usar_placeholder:
            print(f"\n[OK] Descargas exitosas: {exitosas}")
            print(f"[ERROR] Descargas fallidas: {fallidas}")


def main():
    """Función principal del script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Descargar imágenes para presentaciones de ML en Finanzas"
    )
    parser.add_argument(
        "--unsplash",
        action="store_true",
        help="Usar API de Unsplash para buscar imágenes (requiere UNSPLASH_ACCESS_KEY)"
    )
    parser.add_argument(
        "--placeholder",
        action="store_true",
        help="Descargar imágenes placeholder (no requiere API key)"
    )
    parser.add_argument(
        "--url",
        type=str,
        help="Descargar una imagen desde una URL específica (formato: url,nombre_archivo)"
    )
    parser.add_argument(
        "--directorio",
        type=str,
        default=str(IMAGENES_DIR),
        help=f"Directorio de destino (default: {IMAGENES_DIR})"
    )
    
    args = parser.parse_args()
    
    descargador = DescargadorImagenes(
        directorio_destino=Path(args.directorio),
        unsplash_key=os.getenv("UNSPLASH_ACCESS_KEY")
    )
    
    if args.url:
        # Descargar desde URL específica
        partes = args.url.split(",", 1)
        if len(partes) == 2:
            url, nombre = partes
            descargador.descargar_desde_url(url.strip(), nombre.strip())
        else:
            print("Error: Formato incorrecto. Usa: --url 'https://ejemplo.com/imagen.jpg,nombre_archivo.jpg'")
    else:
        # Descargar imágenes necesarias
        descargador.descargar_imagenes_necesarias(
            usar_unsplash=args.unsplash,
            usar_placeholder=args.placeholder
        )


if __name__ == "__main__":
    main()
