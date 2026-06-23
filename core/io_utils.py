from PIL import Image, ImageOps

def load_image(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)#aplicamos exif_transpose para siempre tenerla foto en 90° y evitarq ue se rote en alguna transformacion
    print(img.size)
    return img



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
