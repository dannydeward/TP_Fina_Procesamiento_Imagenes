"""Mejora automática basada en brillo y contraste medidos."""
from typing import List, Tuple

from PIL import Image, ImageEnhance, ImageFilter, ImageStat

from ..registro import registrar
from .base import Operacion

# Cada rango es (minimo, maximo, factor). Reemplaza las cadenas de if/elif:
# se elige el primer rango que contiene al valor medido.
RANGOS_BRILLO: List[Tuple[float, float, float]] = [
    (0, 60, 1.4),       # imagen muy oscura -> subir brillo
    (60, 100, 1.2),     # algo oscura -> subir un poco
    (190, 256, 0.8),    # muy clara -> bajar brillo
]
RANGOS_CONTRASTE: List[Tuple[float, float, float]] = [
    (0, 30, 1.4),       # plana -> aumentar contraste
    (30, 50, 1.2),      # poco contraste -> aumentar un poco
    (90, 1e9, 0.9),     # demasiado contraste -> reducir
]


@registrar
class MejoraAutomatica(Operacion):
    nombre = "mejora"
    extension = "jpg"

    def aplicar(self, img: Image.Image) -> Image.Image:
        resultado = self._ajustar_brillo(img)
        resultado = self._ajustar_contraste(resultado)
        resultado = resultado.filter(ImageFilter.MedianFilter(size=3))
        return resultado.filter(ImageFilter.SHARPEN)

    def _ajustar_brillo(self, img: Image.Image) -> Image.Image:
        promedio = self._promedio(ImageStat.Stat(img).mean)
        factor = self._factor(promedio, RANGOS_BRILLO)
        return ImageEnhance.Brightness(img).enhance(factor)

    def _ajustar_contraste(self, img: Image.Image) -> Image.Image:
        desviacion = self._promedio(ImageStat.Stat(img).stddev)
        factor = self._factor(desviacion, RANGOS_CONTRASTE)
        return ImageEnhance.Contrast(img).enhance(factor)

    @staticmethod
    def _promedio(valores) -> float:
        return sum(valores) / len(valores)

    @staticmethod
    def _factor(valor: float, rangos, defecto: float = 1.0) -> float:
        """Devuelve el factor del primer rango que contiene al valor."""
        return next(
            (factor for minimo, maximo, factor in rangos
             if minimo <= valor < maximo),
            defecto,
        )
