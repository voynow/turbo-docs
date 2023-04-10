
# README

turbo_docs is a python package that provides an automated way to generate a detailed/formatted `README.md` file for a repository.

## Requirements

### Development

* setuptools
* wheel
* twine

### Production 

* requests
* openai
* click 
* pyperclip

## Installation

To install turbo_docs, use the following command:

```
pip install turbo_docs 
```

## Usage

To generate a `README.md` file for the repository, run the following command:

```
turbo_docs --create_readme
```

To copy the directory text to the clipboard, run the following command:

```
turbo_docs --copy
```

## License

turbo_docs is licensed under the [MIT License](LICENSE).