# Turbo Docs

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI](https://img.shields.io/pypi/v/turbo_docs)

Turbo Docs is a powerful command-line interface (CLI) tool designed to automate the generation of documentation for your Python projects. It leverages the capabilities of OpenAI's GPT-4 model to generate comprehensive and accurate documentation for your codebase. 

## Why Use Turbo Docs? 🚀

Turbo Docs is not just another documentation tool. It's your personal documentation assistant that understands your code and generates meaningful and concise documentation. It's perfect for developers who want to focus more on coding and less on writing documentation. 

## Repo Structure 📂

```
turbo_docs
├── commands
│   ├── docs.py
│   ├── readme.py
│   └── __init__.py
├── utils
│   ├── cli_options.py
│   ├── directory.py
│   ├── openai_api.py
│   └── __init__.py
├── generate.py
├── __init__.py
├── setup.py
└── requirements.txt
```

## Example Usage 💻

```bash
# Generate a README.md file for your current repository
turbo_docs --readme

# Generate documentation for all Python files in your current repository
turbo_docs --docs

# Copy the text from all files in your current directory to clipboard
turbo_docs --copy
```

## Installation 📦

Turbo Docs can be installed via pip:

```bash
pip install turbo_docs
```

## Requirements 📄

Turbo Docs requires the following Python packages:

- openai
- llm-blocks
- click
- pyperclip
- toml
- pathspec
- tiktoken

These can be installed from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📝

Turbo Docs is licensed under the MIT License. See `LICENSE` for more information.

## Contact 📧

For any questions or concerns, please open an issue on GitHub.

## Final Words 🎉

Turbo Docs is here to make your life as a developer easier. Give it a try and let it handle the tedious task of documentation for you. Happy coding!