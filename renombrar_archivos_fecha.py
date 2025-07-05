import os
from datetime import datetime

# Obtener la fecha actual en formato YYYYMMDD
fecha = datetime.now().strftime("%Y%m%d")

# Ruta de la carpeta donde están los archivos (ajusta según tu caso)
carpeta = "C:/archivos"

# Recorrer todos los archivos en la carpeta
for nombre in os.listdir(carpeta):
    origen = os.path.join(carpeta, nombre)
    destino = os.path.join(carpeta, f"{fecha}_{nombre}")
    os.rename(origen, destino)

print("Archivos renombrados correctamente.")
