#en este archivo van la aplicaicon de todas las funciones que vamos ausar  definidas una a una 

from core.io_utils import load_image, save_image
from core.filters import (brillo,contraste,autoedicion,rotar,flip_horizontal,blanco_negro,blur,fondo_borroso,quitar_fondo)
from core.exceptions import NoImageLoadedError, InvalidParameterError


class ImageEditor:# aqui inci ala clase editor , donde recibe la imagen original y aplica la formula segun lo planteado 
    def __init__(self, path=None):
        self.original_image = None
        self.image = None

        if path is not None:
            self.load(path)

    def load(self, path):
        self.original_image = load_image(path)
        self.image = self.original_image.copy()
        return self

    def reset(self):
        if self.original_image is None:
            raise NoImageLoadedError()

        self.image = self.original_image.copy()
        return self

    def  apply_grayscale(self):
        if self.image is None:
            raise NoImageLoadedError()

        self.image = blanco_negro(self.image)
        return self

    def apply_rotate(self, angle):
        if self.image is None:
            raise NoImageLoadedError()

        if not isinstance(angle, (int, float)):
            raise InvalidParameterError("El ángulo debe ser un número.")

        self.image = rotar(self.image, angle)
        return self

    def apply_blur(self, radius=5):
        if self.image is None:
            raise NoImageLoadedError()

        if radius < 0:
            raise InvalidParameterError("El radio del blur no puede ser negativo.")

        self.image = blur(self.image, radius)
        return self

    def apply_brightness(self, factor):
        if self.image is None:
            raise NoImageLoadedError()

        if factor <= 0:
            raise InvalidParameterError("El brillo debe ser mayor que 0.")

        self.image = brillo(self.image, factor)
        return self

    def apply_contrast(self, factor):
        if self.image is None:
            raise NoImageLoadedError()

        if factor <= 0:
            raise InvalidParameterError("El contraste debe ser mayor que 0.")

        self.image = contraste(self.image, factor)
        return self

    def apply_mirror(self):
        if self.image is None:
            raise NoImageLoadedError()

        self.image = flip_horizontal(self.image)
        return self

    def apply_remove_background(self):
        if self.image is None:
            raise NoImageLoadedError()

        self.image = quitar_fondo(self.image)
        return self

    def apply_blurred_background(self):
        if self.image is None:
            raise NoImageLoadedError()

        self.image = fondo_borroso(self.image)
        return self

    def save(self, output_path, format=None):
        if self.image is None:
            raise NoImageLoadedError()

        save_image(self.image, output_path, format)
        return self

    def apply_autoedicion(self):
        if self.image is None:
            raise NoImageLoadedError()

        self.image = autoedicion(self.image)
        return self