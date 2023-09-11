# Turbo Docs

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI](https://img.shields.io/pypi/v/turbo_docs)

Turbo Docs is a powerful tool designed to automate the process of generating documentation for your Python projects. It leverages the power of OpenAI's GPT-4 model to generate comprehensive and accurate documentation for your codebase. 

## Why Use Turbo Docs?

Writing documentation can be a tedious process, especially for large codebases. Turbo Docs simplifies this process by automatically generating documentation for each function in your Python files. It also provides the option to generate a README.md file for your repository, making it easier for others to understand your project.

## Repo Structure

```
turbo_docs
├── .gitignore
├── setup.py
├── turbo_docs
│   ├── commands
│   │   ├── docs.py
│   │   ├── readme.py
│   │   └── __init__.py
│   ├── generate.py
│   ├── utils
│   │   ├── cli_options.py
│   │   ├── directory.py
│   │   ├── openai_api.py
│   │   └── __init__.py
│   └── __init__.py
```

## Example Usage

To generate documentation for your Python files, simply navigate to your project directory and run the following command:

```bash
turbo_docs --docs
```

To generate a README.md file for your repository, use the following command:

```bash
turbo_docs --readme
```

You can also copy the directory text to your clipboard with:

```bash
turbo_docs --copy
```


## Installation

Turbo Docs can be installed via pip:

```bash
pip install turbo_docs
```

## Dependencies

Turbo Docs requires the following Python packages:

- openai
- click
- pyperclip
- toml
- pathspec
- llm-blocks
- tiktoken

## Development Status

Turbo Docs is currently in alpha development stage. It supports Python 3.6 and above.

## License

Turbo Docs is licensed under the MIT License.

🚀 Happy coding!