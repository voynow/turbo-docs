# README.md #

# Generate
This repository is being used to generate a README.md for the current repository. It contains the following files: 

- .\generate.py: The main driver function that generates a README.md file for the current repository.
- .\requirements.txt: Contains the package requirements used by generate.py.
- utils\cli_options.py: Contains the command line options used by generate.py.
- utils\directory.py: Contains functions for generating a text representation of the current directory.
- utils\openai_api.py: Contains a wrapper for OpenAI's GPT-3 API.

## Usage
To use the `generate.py` driver, run:

```terminal
python generate.py [options]
```

The available options are:

- `--copy`: If set, copies the directory text to the clipboard.
- `--create_readme`: If set, generates a README.md file for the current repository.

## Examples
To generate a README.md file for the current repository, run:

```terminal
python generate.py --create_readme
```

To generate a README.md file and copy the directory text to the clipboard, run:

```terminal
python generate.py --copy --create_readme
```