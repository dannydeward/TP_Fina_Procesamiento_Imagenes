"""Contrato común para todas las operaciones de imagen."""
from abc import ABC, abstractmethod

from PIL import Image


class Operacion(ABC):
    """Interfaz que toda operación debe cumplir.

    - ``nombre``: clave con la que se la invoca desde el registro.
    - ``extension``: formato de salida del archivo resultante.
    - ``aplicar``: recibe una imagen y devuelve la imagen procesada.
    """

    nombre: str = ""
    extension: str = "jpg"

    @abstractmethod
    def aplicar(self, img: Image.Image) -> Image.Image:
        raise NotImplementedError
