"""Filtros de imagen: desenfoque."""
from PIL import Image, ImageFilter

from ..registro import registrar
from .base import Operacion


@registrar
class Blur(Operacion):
    nombre = "blur"
    extension = "jpg"

    def __init__(self, radio: int = 8) -> None:
        self.radio = radio

    def aplicar(self, img: Image.Image) -> Image.Image:
        return img.filter(ImageFilter.GaussianBlur(self.radio))
