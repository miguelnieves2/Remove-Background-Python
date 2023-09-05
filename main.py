import os
from PIL import Image
from rembg import remove

# ruta raiz del proyecto
ruta_raiz = os.getcwd()

# indicar la imagen
ruta_imagen = 'image.jpg'

# Construir la ruta de la raiz del proyecto
ruta_archivo = os.path.join(ruta_raiz, ruta_imagen)

def es_imagen(ruta_archivo):
    try:
        # intenta abrir la imagen
        Image.open(ruta_archivo)
        return True
    except:
        return False

# Verificar si existe la imagen
if os.path.exists(ruta_archivo):
    print("Se ha encontrado el archivo.")
    # Verificar si es una imagen
    if es_imagen(ruta_archivo):
        print("Se verifico que es una imagen.")

        # Eliminación del fondo de la imagen
        with open(ruta_imagen, 'rb') as i:
            output = remove(i.read())
            ruta_salida = os.path.splitext(ruta_imagen)[0] + "_output.png"
            with open(ruta_salida, 'wb') as o:
                o.write(output)
            print(f"Imagen con fondo eliminado guardada en: \n")
            print({ruta_salida})
    else:
        print("No es una imagen.")
else:
    print("No se ha encontrado el archivo.")
