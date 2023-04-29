# Turbo_Docs
A library for creating **formatted & user-friendly** readmes from existing files.

## Features 
-   Generates **README.md** for the current directory from files
-   For larger repositories, uses the alternative command `turbo_docs --readme_large_repo`
-   Copies directory text to clipboard using **Pyperclip**, useful for working with chatGPT
-   Generates **docstrings** for all functions in your codebase


## Usage
To generate a README or docs.md, use the following command:

`turbo_docs --{command}`

For more options, use the following flags:
-   `--copy`
-   `--readme`
-   `--readme_large_repo`
-   `--docstring`


## Requirements
-   Requests
-   OpenAI
-   Pyperclip
-   RedBaron
-   GitPython