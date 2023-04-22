# README

Welcome to Turbo Docs, an automated project documentation generator!

This project provides a set of libraries and utilities to generate user-friendly project documentation. With Turbo Docs you can quickly generate project README files, docstrings and unit tests which saved you lots of time and effort.

## Requirements

The following packages are required to use Turbo Docs:
- setuptools
- wheel
- twine
- requests
- openai
- click
- pyperclip
- redbaron
- gitpython

## Installation

To install Turbo Docs, please run the following command:

```
pip install turbo_docs
```

## Usage

To generate project documentation with Turbo Docs, use the `driver` script to call the various subcommands.

```
python turbo_docs\generate.py --copy --readme --readme_large_repo --unit_tests --docstring --commit
```

The `driver` command allows you to pass multiple flags to generate the desired project documentation. The flags for each command are as follows: 
- `--copy`: Copy the dir text to clipboard
- `--readme`: Generate a README.md file
- `--readme_large_repo`: Generate readme for larger repos
- `--unit_tests`: Generate unit tests for each code file
- `--docstring`: Generate and insert docstrings for each function
- `--commit`: Generate a commit message and execute the commit

## Contributing

If you would like to contribute to Turbo Docs, please feel free to open a pull request

Or each out to me at voynow99@gmail.com, https://www.linkedin.com/in/voynow/, or https://twitter.com/JamesVoynow!