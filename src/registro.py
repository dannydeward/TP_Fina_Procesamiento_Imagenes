"""Registro de operaciones (patrón Registry).

Mantiene un diccionario ``nombre -> operacion`` que permite invocar cualquier
operación por su nombre, sin necesidad de cadenas de ``if/elif``.
"""
from typing import List, Optional


class RegistroOperaciones:
    def __init__(self) -> None:
        self._operaciones: dict = {}

    def registrar(self, operacion) -> object:
        self._operaciones[operacion.nombre] = operacion
        return operacion

    def obtener(self, nombre: str) -> Optional[object]:
        """Devuelve la operación o ``None`` si no existe (sin lanzar error)."""
        return self._operaciones.get(nombre)

    def nombres(self) -> List[str]:
        return sorted(self._operaciones)


# Registro global único compartido por toda la aplicación.
registro = RegistroOperaciones()


def registrar(cls):
    """Decorador de clase: instancia la operación y la agrega al registro.

    Permite sumar operaciones nuevas con solo crear la clase y decorarla,
    sin modificar el registro ni el CLI (SOLID: Open/Closed).
    """
    registro.registrar(cls())
    return cls
