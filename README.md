# 🐍 Script Python: Renombrar Archivos con Fecha

Este pequeño script en Python automatiza la tarea de renombrar archivos dentro de una carpeta, agregando la fecha actual al inicio del nombre.

## 🧩 ¿Qué hace este script?

Toma todos los archivos ubicados en una carpeta especificada y les antepone la fecha en formato `YYYYMMDD`.

### 📁 Ejemplo:

Archivos originales:
```
informe.docx
imagen.png
datos.csv
```

Después de ejecutar el script:
```
20250704_informe.docx
20250704_imagen.png
20250704_datos.csv
```

## 🧪 Requisitos

- Python 3.x
- Permisos de lectura y escritura en la carpeta objetivo

## ▶️ Cómo usarlo

1. Cambia la ruta `carpeta = "C:/archivos"` por la ruta real en tu equipo.
2. Ejecuta el script desde la terminal o tu editor de código.

```bash
python renombrar_archivos_fecha.py
```

## ⚠️ Advertencia

Asegúrate de que la carpeta solo contenga archivos (no carpetas) y que tengas una copia de seguridad, ya que el renombrado es irreversible si no se controla.

## 🔗 Archivo principal

Puedes ver el archivo .py completo aquí, ya esta alojada una nueva versión del script:  
👉 [Archivos_Fecha](./Archivos_Fecha.py)


## 📄 Licencia

Este script se distribuye con fines educativos y está bajo licencia MIT. ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

##
@ srg-info | Proyecto personal para automatización de tareas con Python.
