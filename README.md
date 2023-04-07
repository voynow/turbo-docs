
# Readme

This repository contains a python script that generates a user friendly readme file based on the contents of the code repository. 

The script uses the OpenAI ChatGPT API to generate the readme and the `utils` folder contains the functions used to interact with the API.

## Usage

To generate a readme for your code repository, you will need an OpenAI API key. It can be obtained for free here: https://openai.com/

Once you have an API key, follow the steps below:

1. Make sure the repo is cloned on your local machine.
2. Create a `.gitignore` file to exclude any files from the readme generation.
3. Open `main.py` and enter your OpenAI API key on line 8.
4. Run `python main.py` to generate the README.md.
5. The generated README will be committed to the repo and pushed to the remote repository.

## Requirements

This script requires the following libraries to be installed on your system:
- Requests
- GitPython
- OpenAI