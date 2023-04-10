
# README.md

turbo_docs is a package for generating a detailed and formatted README.md for a given code repository. It does this by using [OpenAI's GPT-3](https://openai.com/blog/openai-api/) technology to generate detailed descriptions of the given code based on the code structure and files.

## Prerequisites
- Python 3.6+
- Run `pip install -r requirements.dev.txt` to install necessary development dependencies.
  - setuptools
  - wheel
  - twine
- Run `pip install -r requirements.txt` to install necessary application dependencies.
  - requests
  - openai
  - click
  - pyperclip

## Installation
1. Clone this repository.
2. `python setup.py install`

## Usage

The main entry point is the `turbo_docs` command.

```
$ turbo_docs --help
Usage: turbo_docs [OPTIONS]

Main driver function that generates a README.md file for the current repository.

Options:
  --copy                 Copy the directory text to clipboard. This can be used
                         in the ChatGPT webapp.
  --create_readme        Generate README.md file
  --help                 Show this message and exit.
```