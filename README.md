# Turbo Docs

Turbo Docs is a Python package that helps you generate a well-formatted, user-friendly README.md file for your repository using GPT-3.5-turbo or GPT-4 (default). It also provides a command to copy the text from all files in the current directory to the clipboard, which is useful when working with ChatGPT.

## Installation

To install Turbo Docs, run the following command:

```bash
pip install turbo_docs
```

## Requirements

Turbo Docs requires the following packages:

- requests
- openai
- llm-blocks
- click
- pyperclip
- redbaron
- gitpython
- toml
- pathspec

These packages will be installed automatically when you install Turbo Docs.

## Usage

To use Turbo Docs, run the following command in your terminal:

```bash
turbo_docs [OPTIONS]
```

### Options

- `--copy`: Copy the directory text to the clipboard. Useful for working with ChatGPT.
- `--readme`: Generate a README.md file. Useful for keeping documentation up to date.
- `--gpt3`: Use the GPT-3.5 Turbo model instead of GPT-4.

### Example

To generate a README.md file using GPT-3.5-turbo, run the following command:

```bash
turbo_docs --readme --gpt3
```

## Configuration

You can configure Turbo Docs by creating a `turbo_docs.toml` file in your repository. This file allows you to specify files and folders to ignore when generating the README.md file or copying the directory text to the clipboard.

Example `turbo_docs.toml`:

```toml
ignore = [
    "__pycache__",
    "venv",
    "build",
    "dist",
    "*.egg-info",
    ".git",
    "README.md",  # This is recommended so that --readme doesn't include the readme file itself
]
```

## License

Turbo Docs is released under the MIT License.