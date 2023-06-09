# Turbo Docs

Turbo Docs is a Python script that utilizes OpenAI's GPT API to generate README.md files and docstrings for your Python projects automatically.

## Requirements

To use Turbo Docs, you will need to have the following Python packages installed:

- setuptools
- wheel
- twine
- requests
- openai
- click
- pyperclip
- redbaron
- gitpython
- toml

You can install them using the requirements.txt and requirements.dev.txt files in the repository.

## Usage

To generate a README.md or docstrings for the current directory, you can run the `generate.py` script in the `turbo_docs` folder:

```bash
# install tubro_docs
pip install turbo_docs

# command line interface
turbo_docs [--copy] [--readme] [--docstring]
```

You can use the optional flags:
- `--copy`: Copy the directory text to clipboard.
- `--readme`: Generate README.md file.
- `--docstring`: Generate and insert docstrings for each function.

## Customization

You can modify the files and directories that are excluded from the documentation generation by editing the `exclude.toml` file in the root of the repository. 

Example syntax to exclude requirements files:

```toml
exclude = [
  "requirements.*"
]
```

## Modules

Turbo Docs consists of three main modules:

1. `turbo_docs.commands.docstring`: Contains functions to generate docstrings for Python functions using GPT-3 text completion model.
2. `turbo_docs.commands.readme`: Contains a function to generate a README.md file using the OpenAI API.
3. `turbo_docs.utils`: Contains utility functions and decorators for working with CLI options, directories, and the OpenAI API.

## Contributing

Contributions are always welcome! If you have ideas for improvements or bug fixes, please open an issue or submit a pull request.