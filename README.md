# Turbo Docs 🚀

[![PyPI version](https://badge.fury.io/py/turbo_docs.svg)](https://badge.fury.io/py/turbo_docs)
[![GitHub stars](https://img.shields.io/github/stars/voynow/turbo_docs.svg)](https://github.com/voynow/turbo_docs/stargazers)

Turbo Docs is a powerful Python tool that helps developers automatically generate high-quality README.md files for their repositories. It leverages the power of OpenAI's GPT-3.5 Turbo and GPT-4 models to create well-structured, informative, and engaging documentation.

## Why Turbo Docs? 🤔

Writing good documentation is essential for any software project, but it can be time-consuming and tedious. Turbo Docs simplifies this process by generating a README.md file that meets all your requirements, allowing you to focus on writing great code.

## Table of Contents 📚

- [Installation](#installation)
- [Usage](#usage)
- [Repo Structure](#repo-structure)
- [Example Usage](#example-usage)
- [Badges](#badges)

## Installation 💻

To install Turbo Docs, simply run:

```bash
pip install turbo_docs
```

## Usage 🛠️

To use Turbo Docs, navigate to your project's root directory and run:

```bash
turbo_docs --readme
```

This will generate a README.md file for your project. You can also use the `--gpt3` flag to use the GPT-3.5 Turbo model:

```bash
turbo_docs --readme --gpt3
```

Additionally, you can copy the directory text to the clipboard by using the `--copy` flag:

```bash
turbo_docs --copy
```

## Repo Structure 🏗️

```
turbo_docs/
│
├── commands/
│   ├── __init__.py
│   └── readme.py
│
├── utils/
│   ├── __init__.py
│   ├── cli_options.py
│   ├── directory.py
│   └── openai_api.py
│
├── __init__.py
├── generate.py
├── setup.py
└── turbo_docs.toml
```

## Example Usage 📖

Here's an example of how to use Turbo Docs to generate a README.md file:

```python
from turbo_docs.commands import readme

# Define your repo structure as a string
repo = """
{'repo': 'example_repo',
 'files': {
     'main.py': 'print("Hello, World!")',
     'README.md': ''
 }
}
"""

# Generate the README.md file
readme(repo)
```

## License 📄

Turbo Docs is released under the [MIT License](https://opensource.org/licenses/MIT).