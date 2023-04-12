

# turbo_docs

turbo_docs is a speech-to-text generator for Python 3.6 - 3.9. This package enables users to generate a formatted and user-friendly README.md file, generte code summaries, and create unit tests using command-line options. 

## Requirements
The following libraries must be installed: 
- setuptools
- wheel 
- twine 
- requests 
- openai 
- click 
- pyperclip 

## Usage 
The package contains the following command-line options for running specified processes: 
- --copy (true/false): Copy directory text to clipboard
- --create_readme (true/false): Generate readme file
- --create_readme_plus (true/false): Generate formatted and user-friendly readme file
- --create_tests (true/false): Generate unit tests 


The script `generate.driver` serves as the entry point for the package. It uses the OpenAI GPT-3 API to send a user prompt and receive completions with up to 2048 tokens. 

A `.gitignore` file is used to create a list of ignored files, including README.md, tests, and any file in the current directory that starts with a period. The `directory.py` script retrieves the content of unmasked files and stores them in a dictionary. 

## Development Status

alpha