
# User-Friendly Readme.md

# Welcome!

This repository contains code that can be used to generate a user-friendly plain text readme.md file. It uses the Open AI GPT-3 API to automatically generate the readme.md by analyzing the file structure of a given code repository. 

## Requirements

In order to use the generate.py script, the following packages must be installed:
* requests 
* GitPython 
* openai 

## Usage

To generate a readme.md, simply run the `generate.py` script, which will use the Open AI GPT-3 API to analyze the file structure of the code repository and generate a user-friendly readme.md file. The generated README.md will be saved to the repository root directory and automatically committed and pushed.