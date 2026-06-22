# 

# Clase base de errores del editor
class EditorError(Exception):
    def __init__(self, message="Ocurrió un error en el editor de imágenes."):
        super().__init__(message)


# Error cuando el usuario pasa un parámetro inválido
class InvalidParameterError(EditorError):
    def __init__(self, message="Parámetro inválido."):
        super().__init__(message)


# Error cuando se intenta trabajar sin haber cargado imagen
class NoImageLoadedError(EditorError):
    def __init__(self, message="No hay ninguna imagen cargada."):
        super().__init__(message)