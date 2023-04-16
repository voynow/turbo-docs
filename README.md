
# Turbo Docs

Turbo Docs is a set of command-line utilities made for automating document creation and data entry tasks. Its utilities make it easy to create, package, and distribute Python packages for use by others. The code utilizes Python libraries like requests, openai, click, pyperclip, and redbaron in order to automate data entry tasks, formatting docstrings and wrapping text to 80 characters. The CLI application can generate a README summarizing the code, unit tests and docstrings for Python functions.

## Requirements

- Setuptools library
- Wheel library
- Twine
- Requests
- OpenAI
- Click
- pyperclip
- Redbaron

## Features

- Automate data entry tasks via copy to clipboard
- Generate a README summarizing the code
- Generate unit tests
- Generate concise docstrings for functions

## Usage

Generate a README.md summarizing your code: 

```
python generate.py --create_readme
```

Generate a README.md for larger repositories:

```
python generate.py --create_readme_plus
```

Generate unit tests for the code files (work in progress):

```
python generate.py --create_tests
```

Generate and insert docstrings for each Python function:

```
python generate.py --create_docstring
```

Copy all code files in the directory to the clipboard:

``` 
python generate.py --copy
```