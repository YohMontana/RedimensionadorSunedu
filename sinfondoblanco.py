from PIL import Image
import os

def redimensionar_imagen(imagen, nuevo_tamano, dpi):
    img = Image.open(imagen)
    img = img.resize(nuevo_tamano, Image.ANTIALIAS)
    img.info["dpi"] = (dpi, dpi)
    nombre, extension = os.path.splitext(imagen)
    img.save(nombre + extension, dpi=(dpi, dpi))

def redimensionar_lote(ruta_directorio, nuevo_tamano, dpi):
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            redimensionar_imagen(os.path.join(ruta_directorio, archivo), nuevo_tamano, dpi)
    print("Accion terminada")

ruta_directorio = "C:/Users/Personal01/Desktop/prueba2"
nuevo_tamano = (240, 288)
dpi = 300

redimensionar_lote(ruta_directorio, nuevo_tamano, dpi)
