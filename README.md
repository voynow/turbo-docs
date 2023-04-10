

# turbo_docs

A command line tool to quickly generate formatted & user-friendly README.md files for small & large repositories.

## Requirements

* `setuptools`
* `wheel`
* `twine`
* `requests`
* `openai`
* `click`
* `pyperclip`

## Running

Install the requirements with `pip install -r requirements.txt` and then run `python setup.py install`.

The main driver function for `turbo_docs` is invoked with the `turbo_docs` command from the terminal.

## Usage

`turbo_docs` takes the following options and generate README.md files accordingly:
* `--copy`: Copy the directory text to clipboard
* `--create_readme`: Generate README.md file
* `--create_readme_plus`: Generate readme for larger repositories