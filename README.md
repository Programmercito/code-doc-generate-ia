# Java Documentation Script with AI

## Overview

This repository contains Python scripts designed to automatically document Java files using AI. The scripts read Java files from a specified directory, send their content to an AI model for documentation, and then write the documented code back to the original files. The scripts use the Ollama API and Google Gemini API for processing the Java files.

## Files

- `java-doc.py`: The main script that handles the documentation process using the Ollama API.
- `java-doc-gemini.py`: An alternative script that handles the documentation process using the Google Gemini API.
- `.env`: Environment file containing configuration variables.

## How It Works

1. **Load Environment Variables**: The scripts load configuration variables from a `.env` file, including the directory path (`ruta`), the prompt (`prompt`), the AI model URL (`url`), and the model name (`model`).

2. **Fetch Java Files**: The scripts traverse the specified directory to find all Java files.

3. **Send Content to AI**: The content of each Java file is sent to the respective AI API along with a user-defined prompt.

4. **Write Documented Code**: The AI's response, which includes the documented code, is written back to the original Java files.

## Usage

1. **Setup Environment Variables**: Create a `.env` file in the root directory with the following variables:
    ```ini
    ruta=path/to/java/files
    prompt=Your documentation prompt
    url=Ollama_API_endpoint
    model=Ollama_model_name
    key=Your_Google_Gemini_API_key
    hecho=|hecho|
    ```

2. **Run the Scripts**: Execute the desired script using Python:
    ```sh
    python java-doc.py
    ```
    or
    ```sh
    python java-doc-gemini.py
    ```

## Important Notes

- **Prompt Quality**: The quality of the documentation depends heavily on the prompt provided. A poorly constructed prompt may result in incorrect or incomplete documentation.
- **Review Changes**: Always review the changes made by the AI before committing them. The AI might inadvertently remove or add code, so it's crucial to ensure the integrity of your codebase.

## Example

Here is an example of how to set up your [.env](http://_vscodecontentref_/1) file:
```ini
ruta=xxxxx
prompt=Deseo que generes comentarios Javadoc para mis archivos Java. Los comentarios deben incluir los siguientes elementos: Para las clases(esto debe ser previo o antes de la linea de la definicion de la clase NO encima el paquete):1. comentario de para que sirve la clase actual 2. Comentario de autor: debe estar presente @author, pero dejarse vacío.3.  @version: 1.0,  Para los metodos1. Parámetros de entrada: listar y describir cada uno.2. Salida: escribir el valor de retorno.Sigue el formato conocido por oracle.No añadas ningún otro comentario. No es ecesario comentar cada línea, sólo los comentarios requeridos para Javadoc.Debes responderme el codigo fuente completo mas su javadoc como indique , no puedes quitar ni una linea de codigo 
url=http://localhost:11434/api/generate
model=deepseek-coder-v2
key=Your_Google_Gemini_API_key
hecho=|hecho|