# Turbo Docs

Turbo Docs is a Python tool designed to help developers generate a well-formatted README.md file for their repository and perform other tasks related to gathering information from their codebase.

## Installation

You can install Turbo Docs using pip:

```bash
pip install turbo_docs
```

## Usage

Turbo Docs provides command line options for various tasks, such as generating a README.md file, or copying the formatted directory text to the clipboard. To use Turbo Docs, run the following command in your terminal:

```bash
turbo_docs [options]
```

### Available Options

- `--copy`: Copy the formatted text of the entire directory to clipboard. This can be useful when working with GPT. Example:

  ```
  turbo_docs --copy
  ```

- `--readme`: Generate a well-formatted README.md file for the repository. Example:

  ```
  turbo_docs --readme
  ```

## Configuration

To configure Turbo Docs, create a `turbo_docs.toml` file in the root of your project and specify the files and directories to ignore. The following example shows how to exclude different types of files and directories:

```toml
ignore = 
    "__pycache__",
    "venv",
    "build",
    "dist",
    "*.egg-info",
    ".git",
    "README.md",  # This is recommended so that --readme doesn't include the readme file itself
]
```

## Files and Folders Overview

Here's an overview of the files and folders in the Turbo Docs repository:

- `turbo_docs\commands\readme.py`: Contains the `readme` function that generates a README.md file using the OpenAI API.
- `turbo_docs\commands\__init__.py`: The init file for the `turbo_docs.commands` package.
- `turbo_docs\generate.py`: The main module containing the `driver` function which is the entry point for the script.
- `turbo_docs\utils\cli_options.py`: Contains the functions for adding command-line options, such as `copy` and `readme`.
- `turbo_docs\utils\directory.py`: Contains utility functions for working with directories and reading text from files.
- `turbo_docs\utils\openai_api.py`: Contains utility functions for interacting with the OpenAI API.
- `turbo_docs\__init__.py`: The init file for the `turbo_docs` package.
- `.gitignore`: A list of files and directories to be ignored by GIT.
- `exclude.toml`: Example toml configuration file for specifying files or directories to exclude.
- `requirements.txt`: Lists all the required Python packages for Turbo Docs.
- `setup.py`: Sets up the Turbo Docs Python package.
- `turbo_docs.toml`: The Turbo Docs configuration file.

## Dependencies

Turbo Docs uses the following Python packages:

- `requests`
- `openai`
- `click`
- `pyperclip`
- `redbaron`
- `gitpython`
- `toml`
- `pathspec`

Please make sure these packages are installed before running Turbo Docs.

## License

Turbo Docs is released under the MIT License. See the LICENSE file for more details.