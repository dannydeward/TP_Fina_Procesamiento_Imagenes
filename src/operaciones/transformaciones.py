"""Operaciones geométricas: rotación y espejado."""
from PIL import Image

from ..registro import registrar
from .base import Operacion


@registrar
class Rotar(Operacion):
    nombre = "rotar"
    extension = "jpg"

    def __init__(self, angulo: int = 90) -> None:
        self.angulo = angulo

    def aplicar(self, img: Image.Image) -> Image.Image:
        return img.rotate(self.angulo, expand=True)


@registrar
class FlipHorizontal(Operacion):
    nombre = "flip"
    extension = "jpg"

    def aplicar(self, img: Image.Image) -> Image.Image:
        return img.transpose(Image.FLIP_LEFT_RIGHT)
