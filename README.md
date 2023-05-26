# Turbo_Docs
A library for creating **formatted & user-friendly** readmes from existing files.

## Features 
- Generates **README.md** for the current directory from files
- Copies directory text to clipboard using **Pyperclip**, useful for working with chatGPT
- Generates **docstrings** for all functions in your codebase

## Usage
To generate a README or docs.md, use the following command:

`turbo_docs --{command}`

For more options, use the following flags:
- `--copy`
- `--readme`
- `--docstring`

## Requirements

### Development Requirements
- setuptools
- wheel
- twine

### Package Requirements
- requests
- openai
- click
- pyperclip
- redbaron
- gitpython

## Installation
To install the required packages, execute the following commands:

For development requirements:
```
pip install -r requirements.dev.txt
```

For package requirements:
```
pip install -r requirements.txt
```

## Directory Structure
- `turbo_docs/generate.py`: Main script for running the command-line tool, includes the driving function and option handling
- `turbo_docs/commands/docstring.py`: Handles the generation of docstring for functions using GPT-3 completion
- `turbo_docs/commands/readme.py`: Generates README.md and docs.md using openAI API
- `turbo_docs/utils/cli_options.py`: Contains decorators for CLI options
- `turbo_docs/utils/directory.py`: Manages directory and file manipulation, including ignoring files
- `turbo_docs/utils/openai_api.py`: Includes methods for calling the OpenAI API and handling errors

## License
Turbo_Docs is licensed under the MIT License.