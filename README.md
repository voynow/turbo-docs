

## Turbo-Docs
Turbo-Docs is a package for Python creating formatted, user-friendly README.md files and unit tests. 

### Installation
Using pip:
```bash
pip install turbo_docs
```

Using setup.py
```bash
python setup.py install
```

### Usage
Using the command line: 
```bash
turbo_docs [OPTION]
```

- Create a Formatted and User-Friendly Readme.md file:

```bash
turbo_docs --create_readme
```

- Create a Formatted and User-Friendly Readme.md file for large repos:

```bash
turbo_docs --create_readme_plus
```

- Create Unit Tests for each code file: 

```bash
turbo_docs --create_tests
```

### Requirements
- Python 3.8+
- Setuptools
- Wheel
- Twine
- OpenAI
- Requests
- Click
- Pyperclip

### Developed by

This code is developed by [Jamie Voynow](https://github.com/voynow), a software developer with an aim to make the process of creating and managing documentation easier. For more information, visit the [GitHub repository](https://github.com/voynow/turbo-docs).