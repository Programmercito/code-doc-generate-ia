# imprimo start script
import os
from dotenv import load_dotenv, find_dotenv

# Verificar si el archivo .env existe y cargar las variables de entorno
dotenv_path = find_dotenv()
print(f"dotenv_path: {dotenv_path}")
if dotenv_path:
    load_dotenv(dotenv_path)
    print(f"Archivo .env encontrado en: {dotenv_path}")
else:
    print("Archivo .env no encontrado")

print("start script")

# Imprimir todas las variables de entorno cargadas
for key, value in os.environ.items():
    print(f'{key}: {value}')

# obtengo la ruta de el .env con el parametro ruta
ruta = os.getenv("ruta")

print(f'ruta: {ruta}')