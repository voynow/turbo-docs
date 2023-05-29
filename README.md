# Repo: Turbo Docs

Turbo Docs is a Python CLI application that automatically generates documentation for a repository, such as README.md and Python function docstrings, using OpenAI GPT-3 or GPT-4.

## Dependencies

### requirements.dev.txt

- setuptools
- wheel
- twine

### requirements.txt

- requests
- openai
- click
- pyperclip
- redbaron
- gitpython

## Modules

### turbo_docs/generate.py

`generate.py` is the main entry point of the Turbo Docs CLI application. It sets up the Click CLI and executes the specified commands.

This script takes `--copy`, `--readme`, and `--docstring` options to copy the output text, generate README.md, and generate docstrings for Python functions respectively.

### turbo_docs/commands/docstring.py

`docstring.py` is responsible for generating docstrings for Python functions using a GPT-3 or GPT-4 text completion model.

- `wrap_text` Wrap text to 80 characters and break long words.

- `format_docstring` Formats a docstring to adhere to PEP 8.

- `docstring` Generate a docstring for Python functions using a GPT-3 text completion model.

### turbo_docs/commands/readme.py

`readme.py` is responsible for generating a README.md file using the OpenAI API.

- `readme` Generate a README.md using OpenAI API.

### turbo_docs/utils/cli_options.py

`cli_options.py` provides decorators for common command-line options in the Turbo Docs CLI including:

- `copy` Copy the directory text to clipboard
- `readme` Generate README.md file
- `docstring` Generate and insert docstrings for each function

### turbo_docs/utils/directory.py

`directory.py` provides helper functions for working with directories.

- `ignored_files_init` Initialize a list of files to be ignored in the directory.
- `read_gitignore` Read .gitignore file and return a list of ignored files.
- `ignore_filepath` Check if the given filepath contains any of the given ignored files.
- `get_files` Retrieve all text from files, excluding filepaths specified by .gitignore.

### turbo_docs/utils/openai_api.py

`openai_api.py` provides functions for interacting with the OpenAI API.

- `openai_init` Initialize the OpenAI API and prompt the user for their API key if it is not stored as an environment variable.
- `gpt_completion_wrapper` Provide GPT-3 or GPT-4 completions for a given prompt and optional OpenAI package.
- `gpt_completion_error_handler` Handle errors raised by OpenAI GPT completion API.

## Usage

To use Turbo Docs, make sure you have installed the dependencies listed in `requirements.txt`. Run the `generate.py` script with the desired options to generate documentation:

```
python turbo_docs/generate.py --readme --docstring
```

This command will generate a README.md file and docstrings for Python functions in the repository.