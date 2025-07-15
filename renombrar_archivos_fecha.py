# ======================================================
#--  Proyecto: Archivos_Fecha
#--  Autor: [srg.info]
#--  Descripción: Srcript para renombrar archivo, en este caso con fecha.
#-- ======================================================



git tag v1.0
git push origin v1.0

import os
from datetime import datetime

# Obtener la fecha actual en formato YYYYMMDD
fecha = datetime.now().strftime("%Y%m%d")
#fecha = "20240710"  # <-- Cambia esto según la fecha que necesites

# Ruta de la carpeta donde están los archivos (ajusta según tu caso)
carpeta = r"C:/archivos"

# Recorrer todos los archivos en la carpeta
for nombre in os.listdir(carpeta):
    origen = os.path.join(carpeta, nombre)
    destino = os.path.join(carpeta, f"{fecha}_{nombre}")
    os.rename(origen, destino)

print("Archivos renombrados correctamente.")




git tag v1.1
git push origin v1.0

import os

# Pedir la fecha al usuario
fecha = input("Introduce la fecha en formato YYYYMMDD: ")

# Preguntar si quiere filtrar por extensión
filtrar = input("¿Deseas renombrar solo archivos con cierta extensión? (s/n): ").lower()

extensiones = []

if filtrar == "s":
    ext_input = input("Introduce las extensiones separadas por coma (ej: .txt,.docx,.pdf): ")
    extensiones = [ext.strip() for ext in ext_input.split(",")]

# Ruta de la carpeta
carpeta = r"C:\Users\dgmso\Desktop\Cuaderno de Práctica Profesional Desarrollo Web, SQL y Redes - Guía Paso a Paso\Cambiodefechas"

# Renombrar archivos según condiciones
archivos_renombrados = 0

for nombre in os.listdir(carpeta):
    origen = os.path.join(carpeta, nombre)

    if os.path.isfile(origen):
        if not extensiones or any(nombre.lower().endswith(ext) for ext in extensiones):
            destino = os.path.join(carpeta, f"{fecha}_{nombre}")
            os.rename(origen, destino)
            archivos_renombrados += 1

print(f"✅ {archivos_renombrados} archivo(s) renombrado(s) correctamente.")
