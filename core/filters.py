#aqui estan todas oas funciones que vamos a usar definidas, si queremos usar otras debemos definirlas aqui 
# y luego importala a editore incorporarla a la clase editor 

from PIL import Image, ImageEnhance, ImageFilter, ImageStat


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


# Fondo difuminado persona nitida 

def fondo_borroso(img):
    
    from rembg import remove

    fondo_blur = img.filter(ImageFilter.GaussianBlur(10)).convert("RGBA")

    persona = remove(img)
    fondo_blur.paste(persona, (0, 0), persona)
    return fondo_blur


  # ── Imagen sin fondo (PNG) ──────────────────────────────────────────────────────
def quitar_fondo(img):
    from rembg import remove
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


