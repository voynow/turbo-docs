# Turbo Docs 🚀

Turbo Docs is an expert software development assistant that helps you generate and maintain documentation for your Python projects. It automates the process of creating README.md files and function documentation, making it easy to keep your project documentation up-to-date and consistent.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features ✨

- Generate README.md files for your repositories using GPT-3.5 Turbo or GPT-4 models
- Automatically create function documentation for your Python code
- Copy directory text to clipboard for easy integration with ChatGPT
- Customize templates for generating documentation
- Easily maintain up-to-date documentation for your projects

## Installation 💾

To install Turbo Docs, simply run:

```bash
pip install turbo-docs
```

## Usage 🛠️

To use Turbo Docs, run the following command in your project directory:

```bash
turbo_docs [OPTIONS]
```

Available options:

- `--copy`: Copy the directory text to clipboard (useful for working with ChatGPT)
- `--readme`: Generate a README.md file (useful for keeping documentation up-to-date)
- `--gpt3`: Use the GPT-3.5 Turbo model (useful if you don't have GPT-4 access)
- `--docs`: Generate documentation for each code file (useful for keeping documentation up-to-date)

Example usage:

```bash
turbo_docs --readme --docs --gpt3
```

This command will generate a README.md file and create documentation for each code file in the project using gpt-3.5-turbo-16k.

## Requirements 📋

Turbo Docs requires the following Python packages:

- requests
- openai
- llm-blocks
- click
- pyperclip
- redbaron
- gitpython
- toml
- pathspec

## Contributing 🤝

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any improvements or suggestions.

## License 📄

Turbo Docs is released under the MIT License. See [LICENSE](LICENSE) for more information.