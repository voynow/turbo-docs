
# README

This repository contains a python script to generate a README.md file from the contents of a repository and optionally commit and push the changes.

### Requirements

- requests
- GitPython
- openai
- click

### Usage

To generate a README.md file, run `python generate.py`. If the `--output_text` flag is set, the script will print the text for the current repository before generating the README.md file. If the `--git_operations` flag is set, the script will add, commit and push the changes for the generated README.md file.  
The OpenAI API key should be provided when prompted.

### Files

- **generate.py**: The python script to generate a README.md file.
- **requirements.txt**: The list of the Python dependencies.
- **utils/cli_options.py**: Command-line options for the generate.py script.
- **utils/directory.py**: Functions to navigate through the directory structure.
- **utils/openai_api.py**: Functions to access the OpenAI API.