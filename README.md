# Turbo Docs 🚀

Welcome to Turbo Docs - an innovative tool designed to streamline the documentation process for your projects. This tool is your one-stop destination for extracting text from your repository and generating an up-to-date `README.md` or copying its content, ready for interaction with services like ChatGPT.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contribution](#contribution)
- [License](#license)

## Features

✨ **Automatic README Generation**: Run `turbo_docs --readme` to generate a `README.md` that reflects the entire repository content while excluding patterns listed in `.gitignore` and `pyproject.toml`.

✂️ **Clipboard Ready**: Use `turbo_docs --copy` for copying all the relevant repository text into your clipboard, perfect for pasting into any AI or text manipulation service.

🔍 **Token Counter**: Count the number of tokens in a directory's text, giving you insights into how concise or detailed your documentation might be.

## Installation and Usage

Before you can use Turbo Docs, make sure you have Python installed on your system. Also, you will need to install some dependencies.

Install the turbo_docs package using pip:
    ```bash
    pip install turbo_docs
    ```

To get started with Turbo Docs, navigate to your desired project directory and execute the commands:

**Generate README:**
```bash
turbo_docs --readme
```
_This will create or overwrite the existing `README.md` in the project directory._

**Copy Text To Clipboard:**
```bash
turbo_docs --copy
```
_This will copy the combined text content of the project directory (excluding ignored files and directories) onto your system's clipboard._

## Configuration

To adjust which files are ignored when generating documentation or copying text, Turbo Docs reads the `pyproject.toml`. If no configuration exists, Turbo Docs will create a default one with common patterns like `__pycache__`, `venv`, etc.

You may edit the `pyproject.toml` under `tool.turbo_docs.ignore` to suit your needs.

## Contribution

💡 Your contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make Turbo Docs better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

🎉 **Enjoy documenting your projects with Turbo Docs!**