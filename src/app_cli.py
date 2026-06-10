"""Orquestador del programa: pide la operación, la busca en el registro y la aplica.

No usa cadenas de ``if/elif``: la operación se resuelve por nombre desde el
registro (patrón Registry) y, si no existe, se usa un Null Object.
"""
from pathlib import Path

from . import operaciones  # noqa: F401  (importar registra todas las operaciones)
from .cargador import CargadorImagenes
from .operaciones.desconocida import OperacionDesconocida
from .registro import registro


def ejecutar(nombre_operacion: str, nombre_imagen: str,
             cargador: CargadorImagenes = None) -> Path:
    cargador = cargador or CargadorImagenes()
    operacion = registro.obtener(nombre_operacion) or OperacionDesconocida(
        nombre_operacion, registro.nombres()
    )
    imagen = cargador.cargar(nombre_imagen)
    resultado = operacion.aplicar(imagen)
    salida = f"resultado_{nombre_operacion}.{operacion.extension}"
    return cargador.guardar(resultado, salida)


def main() -> None:
    print(f"Operaciones disponibles: {', '.join(registro.nombres())}")
    nombre_operacion = input("Función: ").strip().lower()
    nombre_imagen = input("Imagen (dentro de la carpeta 'imagenes/'): ").strip()
    try:
        ruta = ejecutar(nombre_operacion, nombre_imagen)
        print(f"✅ Guardado en: {ruta}")
    except (ValueError, FileNotFoundError, OSError) as error:
        print(f"❌ {error}")
