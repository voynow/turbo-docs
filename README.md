# README.md

This repository is a tool for generating a README.md file for any given repository. It uses an OpenAI GPT-3 API to generate a custom README file based on the directory structure of the repository. It can also optionally copy the directory text to the clipboard, and perform standard Git operations (add, commit, and push) for the generated README.md file.

## Installation

Clone the repository using the following commands:

```
git clone https://github.com/<repo-name>
```

Ensure that you have Python 3.6 or later installed, and then install the required packages with:

```
pip install -r requirements.txt
```

You will also need to export your OpenAI API key as an environment variable before running the program:

```
export OPENAI_API_KEY={Your API Key Here}
```

## Usage

To generate a README.md file for your repository, run the following command from the top-level of your repository:

```
python generate.py
```

This will generate a README.md file for your repository. You can also specify the following optional flags:

- `--to_clipboard`: Copy the directory text to clipboard. This can be used in the ChatGPT webapp.
- `--git_operations`: Perform Git operations (add, commit, and push) for the generated README.md file.
- `--create_readme`: Generate README.md file.

## License

This project is licensed under the [MIT License](https://github.com/<repo-name>/LICENSE).