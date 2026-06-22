import os
from core.editor import ImageEditor


def test_load_and_save():
    editor = ImageEditor("input.jpg")
    editor.save("output/test_original.png")
    print("test_load_and_save OK")


def test_grayscale():
    editor = ImageEditor("input.jpg")
    editor.apply_grayscale()
    editor.save("output/test_grayscale.png")
    print("test_grayscale OK")


def test_rotate():
    editor = ImageEditor("input.jpg")
    editor.apply_rotate(90)
    editor.save("output/test_rotate.png")
    print("test_rotate OK")


def test_blur():
    editor = ImageEditor("input.jpg")
    editor.apply_blur(5)
    editor.save("output/test_blur.png")
    print("test_blur OK")


def test_brightness_contrast():
    editor = ImageEditor("input.jpg")
    editor.apply_brightness(1.5)
    editor.apply_contrast(1.5)
    editor.save("output/test_brightness_contrast.png")
    print("test_brightness_contrast OK")


def test_remove_background():
    editor = ImageEditor("input.jpg")
    editor.apply_remove_background()
    editor.save("output/test_remove_background.png")
    print("test_remove_background OK")


def test_blurred_background():
    editor = ImageEditor("input.jpg")
    editor.apply_blurred_background()
    editor.save("output/test_blurred_background.png")
    print("test_blurred_background OK")


def main():
    if not os.path.exists("output"):
        os.makedirs("output")

    print("INICIANDO TESTS")

    test_load_and_save()
    test_grayscale()
    test_rotate()
    test_blur()
    test_brightness_contrast()
    test_remove_background()
    test_blurred_background()

    print("TODOS LOS TESTS FINALIZADOS")


if __name__ == "__main__":
    main()