"""Operaciones sobre el fondo usando rembg.

``rembg`` se importa de forma diferida (dentro de cada método) para que el
resto de las operaciones funcionen aunque esa dependencia no esté instalada.
"""
from PIL import Image, ImageFilter

from ..registro import registrar
from .base import Operacion


@registrar
class FondoBorroso(Operacion):
    """Mantiene a la persona nítida y desenfoca el fondo."""

    nombre = "fondo"
    extension = "png"

    def aplicar(self, img: Image.Image) -> Image.Image:
        from rembg import remove

        fondo = img.filter(ImageFilter.GaussianBlur(10)).convert("RGBA")
        persona = remove(img)
        fondo.paste(persona, (0, 0), persona)
        return fondo


@registrar
class QuitarFondo(Operacion):
    """Elimina el fondo y devuelve un PNG con transparencia."""

    nombre = "sin_fondo"
    extension = "png"

    def aplicar(self, img: Image.Image) -> Image.Image:
        from rembg import remove

        return remove(img).convert("RGBA")
