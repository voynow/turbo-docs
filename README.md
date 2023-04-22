# Turbo-Docs

Turbo-Docs is a Python package for automatically generating formatted and user-friendly READMEs, docstrings, and unit tests from your codebase. It utilizes OpenAI's language model to generate the documentation and can commit changes to your repository with a generated commit message.

## Requirements
* OpenAI
* Click
* Pyperclip
* RedBaron
* GitPython

## Usage
`pip install turbo_docs`

Turbo-Docs is designed to make it easy to generate documentation and tests using the following commands:
* `turbo_docs --copy`  Copies the directory to the clipboard, useful for working with chatGPT
* `turbo_docs --readme`  Creates a README.md
* `turbo_docs --readme_large_repo`  Generates README.md for large repos with more info
* `turbo_docs --docstring`  Generates docstring for files
* `turbo_docs --unit_teste`  (WORK IN PROGRESS) Generates unit tests for files
* `turbo_docs --commit`  (WORK IN PROGRESS) Utilizes OpenAI to generate commit message & commits changes
