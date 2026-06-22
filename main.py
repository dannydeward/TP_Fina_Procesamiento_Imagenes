import os
from core.editor import ImageEditor
import sys


def mostrar_menu():
    print("\n--- MENU DE OPCIONES ---")
    print("1 - Escala de grises")
    print("2 - Rotar")
    print("3 - Blur")
    print("4 - Brillo")
    print("5 - Contraste")
    print("6 - Espejo")
    print("7 - Quitar fondo")
    print("8 - Fondo borroso")
    print("9 - Autoedición (IA)")
    print("10 - Reset")
    print("0 - Salir")


def guardar_resultado(editor, contador):
    nombre = f"output/resultado_{contador}.png"
    editor.save(nombre)
    editor.reset()
    print(f"Imagen guardada en: {nombre}")
    return contador + 1


def pedir_ruta_imagen():

    while True:

        ruta = input("\nIngrese la ruta completa de la imagen: ")

        ruta = ruta.strip().strip("\"'")
        ruta = os.path.normpath(ruta)

        print("RUTA RECIBIDA:", repr(ruta))
        print("EXISTE:", os.path.isfile(ruta))

        if os.path.isfile(ruta):
            return ruta

        print("❌ No se encontró la imagen. Verifique la ruta.")


def main():

    # Pedir imagen al usuario
    ruta = pedir_ruta_imagen()

    # Crear carpeta de salida
    if not os.path.exists("output"):
        os.makedirs("output")

    # Crear editor
    editor = ImageEditor(ruta)
    contador = 1

    print("\nImagen cargada correctamente.")

    print("\n¿Modo de edición?")
    print("1 - Manual")
    print("2 - Autoedición (IA)")

    modo = input("Selecciona una opción: ")

    if modo == "2":
        editor.apply_autoedicion()
        contador = guardar_resultado(editor, contador)


    while True:

        mostrar_menu()

        opcion = input("Elige una opción: ")


        if opcion == "1":

            editor.apply_grayscale()
            contador = guardar_resultado(editor, contador)
            print("Escala de grises aplicada.")


        elif opcion == "2":

            angulo = float(input("Ingrese ángulo (ej 90): "))
            editor.apply_rotate(angulo)
            contador = guardar_resultado(editor, contador)
            print("Rotación aplicada.")


        elif opcion == "3":

            radio = float(input("Ingrese radio blur (ej 5): "))
            editor.apply_blur(radio)
            contador = guardar_resultado(editor, contador)
            print("Blur aplicado.")


        elif opcion == "4":

            factor = float(input("Ingrese factor brillo (ej 1.2): "))
            editor.apply_brightness(factor)
            contador = guardar_resultado(editor, contador)
            print("Brillo aplicado.")


        elif opcion == "5":

            factor = float(input("Ingrese factor contraste (ej 1.3): "))
            editor.apply_contrast(factor)
            contador = guardar_resultado(editor, contador)
            print("Contraste aplicado.")


        elif opcion == "6":

            editor.apply_mirror()
            contador = guardar_resultado(editor, contador)
            print("Espejo aplicado.")


        elif opcion == "7":

            editor.apply_remove_background()
            contador = guardar_resultado(editor, contador)
            print("Fondo removido.")


        elif opcion == "8":

            editor.apply_blurred_background()
            contador = guardar_resultado(editor, contador)
            print("Fondo borroso aplicado.")


        elif opcion == "9":

            editor.apply_autoedicion()
            contador = guardar_resultado(editor, contador)
            print("Autoedición aplicada.")


        elif opcion == "10":

            editor.reset()
            print("Imagen reseteada.")


        elif opcion == "0":

            print("Saliendo...")
            break


        else:

            print("Opción inválida.")



if __name__ == "__main__":
    main()







