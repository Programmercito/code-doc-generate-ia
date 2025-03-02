# imprimo start script
import os
import requests
from dotenv import load_dotenv, find_dotenv
import re
import time
import json
import base64
import os
from google import genai
from google.genai import types



def generate(prompt):
    client = genai.Client(
        api_key=os.environ.get("key"),
    )

    model = "gemini-2.0-flash-thinking-exp-01-21"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=prompt
                ),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1.7,
        top_p=0.95,
        top_k=64,
        max_output_tokens=8192,
        response_mime_type="text/plain",
    )
    response_text = ""  # Variable para acumular el texto de la respuesta

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text+= chunk.text
    return response_text


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
                con = prompt + "\n" + content + ""
                archivos.append({"ruta": file_path, "contenido": con})
    return archivos


archivos_java = obtener_archivos_java(ruta, prompt)
# Imprimir los resultados
for archivo in archivos_java:
    print(f"Ruta: {archivo['ruta']}")
    response = generate(archivo["contenido"])
    response_text = response
    extraido = re.search(r'```java(.*?)```', response_text, re.DOTALL)
    codigofinal=extraido.group(1)
    with open(archivo["ruta"] , "w", encoding="utf-8") as f:
        f.write(codigofinal.encode('utf-8').decode('utf-8'))
    print(f"archivo comentado con exito!")
    time.sleep(20)


