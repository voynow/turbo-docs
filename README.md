
# turbo_docs

[![Development Status](https://img.shields.io/badge/Development-3%20--%20Alpha-yellowgreen)](https://shields.io/)
[![License](https://img.shields.io/badge/License-MIT-blue)](https://shields.io/)
[![Python Versions](https://img.shields.io/badge/Python-3.6%20--%203.9-blue)](https://shields.io/)

turbo_docs is a python package for generating documentation for a repositoory.

## Installation

For users that just want to install, use the following command:

```bash
pip install turbo_docs
```

For developers that want to install in "editable" mode, use the following commands:

```bash
pip install -e .[dev]
```

## Requirements

To use Turbo Docs, you are required to have the following installed: 

- setuptools
- wheel
- twine

Activate your OpenAI API key by running the following code:

```bash
export OPENAI_API_KEY=<your_api_key>
```

## Usage

Using Turbo Docs is simple:

```bash
turbo_docs --create_readme --create_readme_plus --copy
```

This will generate a well-formatted README.md, while also summarizing the code and copying the text to the clipboard.

## Development

Install the development dependencies by running the command provided earlier.

Use the entry point `turbo_docs` to run the code.

To customise the options availabe, goto `turbo_docs/utils/cli_options.py`

## Contributing

Feel free to contribute to this project by forking this repo and submit Pull Requests for patches, fixes, new features etc.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.