

# README Generator

Welcome to the README Generator! This repository provides a quick and easy way to generate a user-friendly README.md for any code repository.

## Features

- Automatically generate a README.md file and documentation.md file from any code repository.
- Uses OpenAI's GPT-3 model to generate text based on the content of the code repository.
- Exclude files that are specified in the `.gitignore` file.

## Requirements

- Requests library
- GitPython library
- OpenAI library

## Usage

1. Clone this repository and install the necessary requirements.
2. Provide your OpenAI API key in the `utils/secrets_manager.py` file.
3. Run `python main.py` to generate the README.md and documentation.md and commit them to the repository.

## Contribute

We welcome all contributions! Please open up a pull request or an issue if you want to suggest any changes.