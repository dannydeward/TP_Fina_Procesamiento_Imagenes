"""Importar este paquete registra todas las operaciones disponibles.

Cada módulo usa el decorador ``@registrar``, así que basta con importarlos
para que queden cargados en el registro global.
"""
from . import color, filtros, fondo, mejora, transformaciones  # noqa: F401
