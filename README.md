# Turbo-Docs 🚀

![GitHub stars](https://img.shields.io/github/stars/voynow/turbo-docs?style=social)
![PyPI](https://img.shields.io/pypi/v/turbo-docs)

Turbo-Docs is a powerful tool for developers that automates the process of generating documentation for your Python projects. It leverages the power of OpenAI's GPT-3.5 Turbo and GPT-4 models to create concise, accurate, and cohesive documentation for your functions and classes. 

## Why Use Turbo-Docs? 🤔

Writing documentation can be a tedious and time-consuming task. Turbo-Docs simplifies this process by automatically generating documentation for your Python code. It uses advanced AI models to understand your code and generate human-like text that accurately describes what your functions and classes do. This not only saves you time but also ensures that your documentation is always up-to-date with your code.

## Repo Structure 🌳

```
turbo-docs/
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
├── setup.py
└── __init__.py
```

## Example Usage 📖

- `--readme`: This is the main feature of Turbo-Docs. It generates a README.md file for your project using the provided template and saves the result in a new README.md file.

- `--docs`: This feature generates documentation for all code files in your project, providing a convenient way to keep your documentation up-to-date.

- `--gpt3`: This feature enables the use of the GPT-3.5 Turbo model for generating documentation. It's a great option if you don't have access to the GPT-4 model.

- `--copy`: This feature copies the directory text to the clipboard, making it easy to share your project's structure and contents.

- `--narrative`: This feature allows you to provide a narrative to guide the tone and content of the README. It's a great way to personalize your documentation and make it more engaging for your users.

## Installation 📥

You can install Turbo-Docs using pip:

```bash
pip install turbo-docs
```

Please note that you'll need to have Python 3.6 or later installed on your machine to use Turbo-Docs.

## Conclusion 🎉

Turbo-Docs is a powerful tool that can save you a lot of time and effort when it comes to documenting your Python projects. Give it a try and see how it can improve your workflow!

## License 📄

This project is licensed under the MIT License.