from PIL import Image, ImageDraw
import os

def agregar_fondo_blanco(imagen, nuevo_tamano, dpi):
    img = Image.open(imagen)
    img = img.resize(nuevo_tamano, Image.ANTIALIAS)
    fondo = Image.new("RGB", nuevo_tamano, "white")
    posicion = ((nuevo_tamano[0] - img.width) // 2, (nuevo_tamano[1] - img.height) // 2)
    fondo.paste(img, posicion)
    fondo.info["dpi"] = (dpi, dpi)
    nombre, extension = os.path.splitext(imagen)
    fondo.save(nombre + extension, dpi=(dpi, dpi))

def agregar_fondo_blanco_lote(ruta_directorio, nuevo_tamano, dpi):
    for archivo in os.listdir(ruta_directorio):
        if archivo.endswith(('.jpg')):
            agregar_fondo_blanco(os.path.join(ruta_directorio, archivo), nuevo_tamano, dpi)
    print("Finalizado")

ruta_directorio = "C:/Users/Personal01/Desktop/pruebas4"
nuevo_tamano = (240, 288)
dpi = 300

agregar_fondo_blanco_lote(ruta_directorio, nuevo_tamano, dpi)
