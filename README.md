# Code Documentation Script with AI

## Overview

This repository contains Python scripts designed to automatically document code files using AI. The scripts read code files from a specified directory, send their content to an AI model for documentation, and then write the documented code back to the original files. The scripts use the Ollama API and Google Gemini API for processing the code files.

## Files

- `code-doc.py`: The main script that handles the documentation process using the Ollama API.
- `code-doc-gemini.py`: An alternative script that handles the documentation process using the Google Gemini API.
- `ts-doc-gemini.py`: A script specifically for documenting TypeScript files using the Google Gemini API.
- `.env`: Environment file containing configuration variables.

## How It Works

1. **Load Environment Variables**: The scripts load configuration variables from a `.env` file, including the directory path (`ruta`), the prompt (`prompt`), the AI model URL (`url`), and the model name (`model`).

2. **Fetch Code Files**: The scripts traverse the specified directory to find all code files with the specified extension.

3. **Send Content to AI**: The content of each code file is sent to the respective AI API along with a user-defined prompt.

4. **Write Documented Code**: The AI's response, which includes the documented code, is written back to the original code files.

## Usage

1. **Setup Environment Variables**: Create a `.env` file in the root directory with the following variables:
    ```ini
    ruta=path/to/code/files
    prompt=Your documentation prompt
    url=Ollama_API_endpoint
    model=Ollama_model_name
    key=Your_Google_Gemini_API_key
    hecho=|hecho|
    extension=ts
    prefijo=typescript
    ```

2. **Run the Scripts**: Execute the desired script using Python:
    ```sh
    python code-doc.py
    ```
    or
    ```sh
    python code-doc-gemini.py
    ```
    or
    ```sh
    python ts-doc-gemini.py
    ```

## Important Notes

- **Prompt Quality**: The quality of the documentation depends heavily on the prompt provided. A poorly constructed prompt may result in incorrect or incomplete documentation.
- **Review Changes**: Always review the changes made by the AI before committing them. The AI might inadvertently remove or add code, so it's crucial to ensure the integrity of your codebase.

## Example

Here is an example of how to set up your [.env](http://_vscodecontentref_/1) file:
```ini
ruta=C:\Users\hered\codes\personal\metroprincipal
#prompt=You are a programmer who generates Javadocs for your Spring Boot project. You will only return source code.I want you to generate Javadoc for my Java files. The comments must include the following elements:For classes (this should be prior to or before the class definition line, NOT above the package):Comment on what the current class is for (in Spanish).Author comment: @author must be present, but left empty. @version: 1.0. For methods:Input parameters: list and describe each one (in Spanish).Output: write the return value (in Spanish).Follow the format known by Oracle. Do not add any other comments. It is not necessary to comment every line, only the comments required for Javadoc. You must respond with the complete source code plus its Javadoc as I indicated, you cannot remove a single line of code.
prompt=Eres un experto en Typescript y vas a documentar tu app angular Agrega las siguientes anotaciones JSDoc a mi archivo de TypeScript, asegurándote de no agregar ni quitar código existente, solo añade los comentarios JSDoc. Aquí están las anotaciones a agregar: 1. @class: Describe una clase. 2. @param: Describe los parámetros de una función o método.3. @returns: Describe el valor de retorno de una función o método.4. Descripción: Proporciona una descripción clara de lo que hace cada DEFINICION de un método, clase o interfaz.Reglas: No agregar ni quitar código fuente, solo añadir los comentarios JSDoc.
url=http://localhost:11434/api/generate
model=llava
key=Your_Google_Gemini_API_key
hecho=|hecho|
extension=ts
prefijo=typescript