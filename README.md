# Turbo Docs

Turbo Docs is a command line utility designed to efficiently generate and process files for Python projects. It provides a suite of commands that allow users to generate README.md files, generate tests, generate docstrings, copy the directory text to the clipboard, generate a commit message, and execute commits. 

## Requirements

Turbo Docs requires the following libraries to function properly:
- [setuptools](https://pypi.org/project/setuptools/): Used to create Python packages
- [wheel](https://pypi.org/project/wheel/): Used to build packages in the wheel format (supports both Python 2 and Python 3)
- [twine](https://pypi.org/project/twine/): Used to safely upload packages to the Python Package Index
- [Requests](https://pypi.org/project/requests/): Used to make HTTP requests
- [OpenAI](https://pypi.org/project/openai/): Used to build intelligent products using machine learning
- [Click](https://pypi.org/project/click/): Used to create command line interfaces 
- [Pyperclip](https://pypi.org/project/pyperclip/): Used to copy text from and to the clipboard 
- [RedBaron](https://pypi.org/project/redbaron/): Used to programmatically manipulate Python source code
- [GitPython](https://pypi.org/project/gitpython/): Used to interact with git repositories from Python

## Usage

Using Turbo Docs is as simple as running the `turbo-docs` command from the terminal.

The command accepts the following options:

- `--readme`: Generates a `README.md` file 
- `--copy`: Copies the directory text to the clipboard
- `--readme-large-repo`: Generates a `README.md` file for a large repository
- `--unit-tests`: Generates unit tests for code files 
- `--docstring`: Generates and inserts docstrings for each function 
- `--commit`: Generates a commit message and executes the commit 

Example:  
`turbo-docs --docstring`

If you have any issues when running the command, please open an [issue](https://github.com/turbo-docs/issues).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)