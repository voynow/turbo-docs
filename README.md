# Turbo Docs

Turbo Docs is a Python package that helps you generate a professional README.md file for your repository using GPT-3.5 Turbo or GPT-4. It can also copy the text from all files in the current directory to the clipboard, which is useful when working with ChatGPT.

## Installation

To install Turbo Docs, you need to have Python 3.6 or higher. You can install the package using pip:

```bash
pip install turbo_docs
```

## Setup

Before using Turbo Docs, you need to set up your OpenAI API key. If you don't have an API key, create an OpenAI account at https://platform.openai.com/overview. Then, set the API key as an environment variable:

```bash
export OPENAI_API_KEY=<your_api_key>
```

## Usage

To use Turbo Docs, navigate to your project directory and run the following command:

```bash
turbo_docs
```

### Options

- `--copy`: Copy the directory text to the clipboard. Useful for working with ChatGPT.
- `--readme`: Generate a README.md file. Useful for keeping documentation up to date.
- `--gpt3`: Use the GPT-3.5 Turbo model instead of GPT-4.

## Configuration

You can configure Turbo Docs to ignore specific files and folders by creating a `turbo_docs.toml` file in your project directory. Add the files and folders you want to ignore in the `ignore` list:

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

## Dependencies

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

These dependencies will be installed automatically when you install Turbo Docs using pip.

## License

Turbo Docs is released under the MIT License.