# Java Documentation Script with AI

## Overview

This repository contains a Python script designed to automatically document Java files using AI. The script reads Java files from a specified directory, sends their content to an AI model for documentation, and then writes the documented code back to the original files. The script uses the Ollama API for processing the Java files.

## Files

- java-doc.py: The main script that handles the documentation process.
- .env: Environment file containing configuration variables.

## How It Works

1. **Load Environment Variables**: The script loads configuration variables from a .env file, including the directory path (`ruta`), the prompt (`prompt`), the AI model URL (`url`), and the model name (`model`).

2. **Fetch Java Files**: The script traverses the specified directory to find all Java files.

3. **Send Content to AI**: The content of each Java file is sent to the Ollama API along with a user-defined prompt.

4. **Write Documented Code**: The AI's response, which includes the documented code, is written back to the original Java files.

## Usage

1. **Setup Environment Variables**: Create a .env file in the root directory with the following variables:
    ```ini
    ruta=path/to/java/files
    prompt=Your documentation prompt
    url=Ollama_API_endpoint
    model=Ollama_model_name
    ```

2. **Run the Script**: Execute the script using Python:
    ```sh
    python java-doc.py
    ```

## Important Notes

- **Prompt Quality**: The quality of the documentation depends heavily on the prompt provided. A poorly constructed prompt may result in incorrect or incomplete documentation.
- **Review Changes**: Always review the changes made by the AI before committing them. The AI might inadvertently remove or add code, so it's crucial to ensure the integrity of your codebase.

## Example

Here is an example of how to set up your .env file:
```ini
ruta=C:/Users/yourusername/projects/java
prompt=Please document the following Java code:
url=https://api.ollama.com/document
model=ollama-model
```

## Happy Coding!

We hope this script helps you streamline your Java documentation process. Happy coding!