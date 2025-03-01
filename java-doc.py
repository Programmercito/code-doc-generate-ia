# imprimo start script
import os
import requests
from dotenv import load_dotenv, find_dotenv
import fnmatch
import re
import time

# Verificar si el archivo .env existe y cargar las variables de entorno
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
    print(f"Archivo .env encontrado en: {dotenv_path}")
else:
    print("Archivo .env no encontrado")

print("start script")

# obtengo la ruta de el .env con el parametro ruta
ruta = os.getenv("ruta")
prompt = os.getenv("prompt")
url = os.getenv("url")
model = os.getenv("model")

print(f"ruta a documentar: {ruta}")


def obtener_archivos_java(ruta, prompt):
    archivos = []
    for root, dirs, files in os.walk(ruta):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                con = prompt + "\n''' java\n" + content + "\n'''"
                archivos.append({"ruta": file_path, "contenido": con})
    return archivos


archivos_java = obtener_archivos_java(ruta, prompt)


def send_ollama(url, archivo_java):
    enviar = {"model": model, "prompt": archivo_java,"stream": False}
    response = requests.post(url, json=enviar)
    return response


# Imprimir los resultados
for archivo in archivos_java:
    print(f"Ruta: {archivo['ruta']}")
    print(f"Contenido:\n{archivo['contenido']}\n")
    response = send_ollama(url, archivo["contenido"])
    print(f"Respuesta: {response.text}")
    time.sleep(15)
    