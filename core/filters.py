#aqui estan todas oas funciones que vamos a usar definidas, si queremos usar otras debemos definirlas aqui 
# y luego importala a editore incorporarla a la clase editor 

from PIL import Image, ImageEnhance, ImageFilter, ImageStat
from rembg import remove 

#rotar
def rotar(img, angulo):
    return img.rotate(angulo, expand=True)

#espejo 
def flip_horizontal(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)


# escala de grises  
def blanco_negro(img):
    return img.convert("L").convert("RGB")

#brillo 
def brillo(img, factor):
    return ImageEnhance.Brightness(img).enhance(factor)

#contraste 
def contraste(img, factor):
    return ImageEnhance.Contrast(img).enhance(factor)

#difuminado  
def blur(img, radio=5):
    return img.filter(ImageFilter.GaussianBlur(radio))


# Fondo difuminado perosna nitida 
def fondo_borroso(img):
    fondo_blur = img.filter(ImageFilter.GaussianBlur(10))
    persona = remove(img) #se exgtrae la persona
    fondo_blur.paste(persona, (0, 0), persona) # se pega sobre el fondo 
    return fondo_blur

# ── Imagen sin fondo (PNG) ──────────────────────────────────────────────────────
def quitar_fondo(img):
    resultado = remove(img).convert("RGBA")
    return resultado

#autoedicion
def autoedicion(image):  

    img = image

    # Brillo leve
    img = ImageEnhance.Brightness(img).enhance(1.1)

    # Contraste leve
    img = ImageEnhance.Contrast(img).enhance(1.2)

    # Saturación (Color)
    img = ImageEnhance.Color(img).enhance(1.3)

    # Definición / nitidez
    img = img.filter(ImageFilter.SHARPEN)

    return img



"""


# ----------------------------------------
# ESCALA DE GRISES
# ----------------------------------------
def escala_grises(image):
    gray = image.convert("L")
    return gray.convert("RGB")


# ----------------------------------------
# ROTAR
# ----------------------------------------
def rotar(image, angulo):
    return image.rotate(angulo, expand=True)


# ----------------------------------------
# DESENFOQUE (BLUR)
# ----------------------------------------
def desenfocar(image, radius=5):
    return image.filter(ImageFilter.GaussianBlur(radius))


# ----------------------------------------
# BRILLO
# ----------------------------------------
def brillo(image, factor):
    return ImageEnhance.Brightness(image).enhance(factor)


# ----------------------------------------
# CONTRASTE
# ----------------------------------------
def contraste(image, factor):
    return ImageEnhance.Contrast(image).enhance(factor)


# ----------------------------------------
# ESPEJO (FLIP HORIZONTAL)
# ----------------------------------------
def espejo(image):
    return image.transpose(Image.FLIP_LEFT_RIGHT)


# ----------------------------------------
# QUITAR FONDO (rembg)
# Devuelve imagen con transparencia (RGBA)
# ----------------------------------------
def quitar_fondo(image):
    resultado = remove(image).convert("RGBA")
    return resultado


# ----------------------------------------
# FONDO BORROSO + PERSONA NÍTIDA
# ----------------------------------------
def fondo_borroso(image):
    # Aseguramos que la imagen esté en RGBA
    image_rgba = image.convert("RGBA")

    # Creamos el fondo difuminado
    fondo_blur = image_rgba.filter(ImageFilter.GaussianBlur(10))

    # Extraemos persona sin fondo (con transparencia)
    persona = remove(image_rgba).convert("RGBA")

    # Pegamos la persona encima del fondo borroso usando su alpha como máscara
    fondo_blur.paste(persona, (0, 0), persona)

    return fondo_blur


def autoedicion(image):  

    img = image

    # Brillo leve
    img = ImageEnhance.Brightness(img).enhance(1.1)

    # Contraste leve
    img = ImageEnhance.Contrast(img).enhance(1.2)

    # Saturación (Color)
    img = ImageEnhance.Color(img).enhance(1.3)

    # Definición / nitidez
    img = img.filter(ImageFilter.SHARPEN)

    return img
"""