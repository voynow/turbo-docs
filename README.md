# Turbo-Docs 🚀

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI](https://img.shields.io/pypi/v/turbo_docs)

Turbo Docs is a Python package designed to automate the process of generating documentation for your codebase. It uses the OpenAI API to generate documentation and README files, making it easier to maintain up-to-date and comprehensive documentation for your projects.

## Why Use Turbo-Docs? 🤔

Keeping documentation up-to-date can be a tedious task, especially for large codebases. Turbo Docs automates this process, ensuring that your documentation is always in sync with your code. It uses advanced AI models to generate human-like text, providing high-quality documentation that is easy to understand. 

## Repo Structure 🌳

```
.
├── .gitignore
├── setup.py
├── turbo_docs
│   ├── __init__.py
│   ├── commands
│   │   ├── __init__.py
│   │   ├── docs.py
│   │   └── readme.py
│   ├── generate.py
│   └── utils
│       ├── __init__.py
│       ├── cli_options.py
│       ├── directory.py
│       └── openai_api.py
└── docs
    ├── turbo_docs
    │   ├── commands
    │   │   ├── docs.md
    │   │   └── readme.md
    │   ├── generate.md
    │   └── utils
    │       ├── cli_options.md
    │       ├── directory.md
    │       └── openai_api.md
```

## Example Usage 📖

Generate a README.md file for the current repo:
```bash
turbo_docs --readme
```

Generate documentation for all code files:
```bash
turbo_docs --docs
```

Use the GPT-3.5 Turbo model:
```bash
turbo_docs --gpt3
```

Copy the directory text to clipboard:
```bash
turbo_docs --copy
```

Provide a narrative to guide the tone and content of the README:
```bash
turbo_docs --narrative "Your narrative here"
```

## Installation 📥

You can install Turbo Docs via pip:

```bash
pip install turbo_docs
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or feedback, please feel free to contact us.

Happy coding! :computer: :rocket: