# Turbo Docs 🚀

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI](https://img.shields.io/pypi/v/turbo_docs)

Turbo Docs is a powerful Python package that automates the generation of documentation for your Python projects. It utilizes OpenAI's GPT models to create concise and informative documentation, making it easier for you and your users to understand your code.

## 📚 Table of Contents

- [Why Use Turbo Docs?](#why-use-turbo-docs)
- [Repo Structure](#repo-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Why Use Turbo Docs?

- **Save time**: Turbo Docs automatically generates documentation for your Python functions, so you can focus on writing code.
- **Stay up-to-date**: Turbo Docs can be easily integrated into your development workflow, ensuring your documentation is always current.
- **High-quality documentation**: Turbo Docs leverages the power of OpenAI's GPT models to generate concise and informative documentation.
- **Customizable**: You can choose between GPT-3.5 Turbo and GPT-4 models, and even provide your own templates for generating documentation.

## 🌳 Repo Structure

```
turbo_docs/
├── commands/
│   ├── docs.py
│   ├── readme.py
│   └── __init__.py
├── utils/
│   ├── cli_options.py
│   ├── directory.py
│   ├── openai_api.py
│   └── __init__.py
├── generate.py
├── __init__.py
├── setup.py
├── requirements.txt
└── turbo_docs.toml
```

## 📦 Installation

To install Turbo Docs, simply run:

```bash
pip install turbo_docs
```

## 🛠 Usage

To generate documentation for your Python project, navigate to your project's root directory and run:

```bash
turbo_docs --docs
```

To generate a README.md file for your project, run:

```bash
turbo_docs --readme
```

For more options, run:

```bash
turbo_docs --help
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any improvements or suggestions.

## 📄 License

Turbo Docs is released under the [MIT License](https://opensource.org/licenses/MIT).