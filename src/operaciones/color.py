"""Operaciones de color: blanco y negro, brillo y contraste."""
from PIL import Image, ImageEnhance

from ..registro import registrar
from .base import Operacion


@registrar
class BlancoNegro(Operacion):
    nombre = "byn"
    extension = "jpg"

    def aplicar(self, img: Image.Image) -> Image.Image:
        return img.convert("L").convert("RGB")

@registrar
class Brillo(Operacion):
    nombre = "brillo"
    extension = "jpg"

    def __init__(self, factor: float = 1.5) -> None:
        self.factor = factor

    def aplicar(self, img: Image.Image) -> Image.Image:
        return ImageEnhance.Brightness(img).enhance(self.factor)


@registrar
class Contraste(Operacion):
    nombre = "contraste"
    extension = "jpg"

    def __init__(self, factor: float = 2.0) -> None:
        self.factor = factor

    def aplicar(self, img: Image.Image) -> Image.Image:
        return ImageEnhance.Contrast(img).enhance(self.factor)
