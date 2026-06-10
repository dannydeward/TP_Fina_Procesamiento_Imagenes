"""Null Object: operación que se usa cuando el nombre pedido no existe.

Evita tener que escribir un ``if operacion is None`` en el CLI: el registro
devuelve esta operación por defecto y al aplicarla informa el error.
"""
from typing import List

from PIL import Image

from .base import Operacion


class OperacionDesconocida(Operacion):
    nombre = "desconocida"
    extension = "txt"

    def __init__(self, pedida: str, disponibles: List[str]) -> None:
        self.pedida = pedida
        self.disponibles = disponibles

    def aplicar(self, img: Image.Image) -> Image.Image:
        raise ValueError(
            f"Operación '{self.pedida}' no reconocida. "
            f"Opciones disponibles: {', '.join(self.disponibles)}"
        )
