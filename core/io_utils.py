from PIL import Image

def load_image(path):
    return Image.open(path)

def save_image(image, output_path, format=None):
    if format is None:
        image.save(output_path)
    else:
        image.save(output_path, format=format)

        

def convertimos_formato(entrada, salida):
    img = Image.open(entrada)

    if salida.lower().endswith((".jpg", ".jpeg")):
        img = img.convert("RGB")

    img.save(salida)
    print("Convertido:", entrada, "->", salida)
