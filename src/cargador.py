"""Carga y guardado de imágenes (SOLID: Single Responsibility)."""
from pathlib import Path

from PIL import Image


class CargadorImagenes:
    def __init__(self, carpeta_entrada: str = "imagenes",
                 carpeta_salida: str = "resultados") -> None:
        self.carpeta_entrada = Path(carpeta_entrada)
        self.carpeta_salida = Path(carpeta_salida)
        self.carpeta_salida.mkdir(parents=True, exist_ok=True)

    def cargar(self, nombre_archivo: str) -> Image.Image:
        return Image.open(self.carpeta_entrada / nombre_archivo)

    def guardar(self, img: Image.Image, nombre_archivo: str) -> Path:
        ruta = self.carpeta_salida / nombre_archivo
        img.save(ruta)
        return ruta
