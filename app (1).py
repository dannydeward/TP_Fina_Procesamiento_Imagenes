from PIL import Image, ImageFilter, ImageEnhance, ImageStat
from rembg import remove

# ── Cargar imagen  ─────────────────────────────────────────────────────────────
def load_image(path):
    path=r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\6db25a58-dd6b-4065-8a28-c107c10ade16.jpg"
    img = Image.open(path)
    return img

# ── Funciones base ─────────────────────────────────────────────────────────────

def rotar(img, angulo):
    return img.rotate(angulo, expand=True)

def flip_horizontal(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def blanco_negro(img):
    return img.convert("L").convert("RGB")

def brillo(img, factor):
    return ImageEnhance.Brightness(img).enhance(factor)

def contraste(img, factor):
    return ImageEnhance.Contrast(img).enhance(factor)

def blur(img, radio=5):
    return img.filter(ImageFilter.GaussianBlur(radio))

# ── Fondo difuminado ───────────────────────────────────────────────────────────
def fondo_borroso(img):
    fondo_blur = img.filter(ImageFilter.GaussianBlur(10))
    persona = remove(img)
    fondo_blur.paste(persona, (0, 0), persona)
    return fondo_blur

# ── Imagen sin fondo (PNG) ──────────────────────────────────────────────────────
def quitar_fondo(img):
    resultado = remove(img).convert("RGBA")
    return resultado

# ── Auto-mejora ────────────────────────────────────────────────────────────────
def mejora_automatica(img):
    resultado = img.copy()
    stat = ImageStat.Stat(img)
    brillo_promedio = sum(stat.mean) / len(stat.mean)
    if brillo_promedio < 60: 
        resultado = ImageEnhance.Brightness(resultado).enhance(1.4) 
    elif brillo_promedio < 100: 
        resultado = ImageEnhance.Brightness(resultado).enhance(1.2) 
    elif brillo_promedio > 190: 
        resultado = ImageEnhance.Brightness(resultado).enhance(0.8) 
    else:
        pass
    stat = ImageStat.Stat(img)
    contraste = sum(stat.stddev) / len(stat.stddev)
    if contraste < 30:
        resultado = ImageEnhance.Contrast(resultado).enhance(1.4)
    elif contraste < 50:
        resultado = ImageEnhance.Contrast(resultado).enhance(1.2)
    elif contraste > 90:
        resultado = ImageEnhance.Contrast(resultado).enhance(0.9)
    else:
        pass
    resultado = resultado.filter(ImageFilter.MedianFilter(size=3))
    resultado = resultado.filter(ImageFilter.SHARPEN)
    return resultado

# ── Probando las funciones ──────────────────────────────────────────────────────
opcion = input("Funcion")

if opcion == "rotar":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = rotar(img, 90)
    resultado.save("resultado_rotado.jpg")

elif opcion == "flip":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = flip_horizontal(img)
    resultado.save("resultado_flip.jpg")

elif opcion == "byn":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = blanco_negro(img)
    resultado.save("resultado_bn.jpg")

elif opcion == "brillo":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = brillo(img, 1.5)
    resultado.save("resultado_brillo.jpg")

elif opcion == "contraste":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = contraste(img, 2)
    resultado.save("resultado_contraste.jpg")

elif opcion == "blur":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = blur(img, 8)
    resultado.save("resultado_blur.jpg")

elif opcion == "fondo":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = fondo_borroso(img)
    resultado.save("resultado_fondo.png")

elif opcion == "sin_fondo":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\2024-12-28 (2).jpg"
    img = load_image(path)
    resultado = quitar_fondo(img)
    resultado.save("resultado_sin_fondo.png")

elif opcion == "mejora":
    path = r"C:\Users\Sabri\Desktop\Fotos Fondo de Pantalla\6db25a58-dd6b-4065-8a28-c107c10ade16.jpg"
    img = load_image(path)
    resultado = mejora_automatica(img)
    resultado.save("mejorada.jpg")
