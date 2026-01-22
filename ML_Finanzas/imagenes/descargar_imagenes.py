"""
Script para descargar imágenes de internet para las presentaciones de ML en Finanzas.

Este script permite:
1. Descargar imágenes desde URLs directas
2. Buscar y descargar imágenes usando la API de Unsplash (gratuita)
3. Descargar múltiples imágenes en lote

Requisitos:
    pip install requests pillow

Para usar la API de Unsplash (opcional):
    1. Regístrate en https://unsplash.com/developers
    2. Crea una aplicación
    3. Obtén tu Access Key
    4. Agrégala al script o como variable de entorno UNSPLASH_ACCESS_KEY
"""

import os
import requests
from pathlib import Path
from typing import List, Dict, Optional
import time
from urllib.parse import urlparse

# Configuración
IMAGENES_DIR = Path(__file__).parent / "imagenes"
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
            
            print(f"✓ Descargado: {nombre_archivo}")
            return True
            
        except Exception as e:
            print(f"✗ Error al descargar {nombre_archivo}: {e}")
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
            print("⚠ Advertencia: No se proporcionó clave de Unsplash. Usa URLs directas o configura UNSPLASH_ACCESS_KEY")
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
            print(f"✗ Error al buscar en Unsplash: {e}")
            return []
    
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
    
    def descargar_imagenes_necesarias(self, usar_unsplash: bool = False) -> None:
        """
        Descarga todas las imágenes necesarias para las presentaciones.
        
        Args:
            usar_unsplash: Si True, intenta buscar en Unsplash. Si False, solo muestra las URLs necesarias.
        """
        print(f"\n📁 Directorio de destino: {self.directorio_destino}")
        print(f"📊 Total de imágenes necesarias: {len(IMAGENES_NECESARIAS)}\n")
        
        if usar_unsplash and not self.unsplash_key:
            print("⚠ No se puede usar Unsplash sin una clave de acceso.")
            print("   Opciones:")
            print("   1. Obtén una clave en https://unsplash.com/developers")
            print("   2. Configura la variable de entorno UNSPLASH_ACCESS_KEY")
            print("   3. Usa el método descargar_lote_desde_urls() con URLs directas\n")
            return
        
        exitosas = 0
        fallidas = 0
        
        for nombre_archivo, info in IMAGENES_NECESARIAS.items():
            ruta_destino = self.directorio_destino / nombre_archivo
            
            # Verificar si ya existe
            if ruta_destino.exists():
                print(f"⏭  Ya existe: {nombre_archivo}")
                continue
            
            if usar_unsplash:
                if self.descargar_imagen_por_busqueda(nombre_archivo, info["busqueda"]):
                    exitosas += 1
                else:
                    fallidas += 1
                    print(f"   Búsqueda sugerida: {info['busqueda']}")
            else:
                print(f"📝 {nombre_archivo}")
                print(f"   Descripción: {info['descripcion']}")
                print(f"   Búsqueda sugerida: {info['busqueda']}")
                print(f"   → Necesitas proporcionar una URL para esta imagen\n")
            
            time.sleep(0.5)  # Rate limiting
        
        if usar_unsplash:
            print(f"\n✅ Descargas exitosas: {exitosas}")
            print(f"❌ Descargas fallidas: {fallidas}")


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
        descargador.descargar_imagenes_necesarias(usar_unsplash=args.unsplash)


if __name__ == "__main__":
    main()
