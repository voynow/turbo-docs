
# README.md
This repository contains the source code and files used to automatically generate a README.md using the openAI GPT-3 API.

## Requirements
This code uses the following packages:

 - Requests
 - GitPython
 - OpenAI

## How it works
The generate.py script is the main driver for the code, it reads the content of the current directory and sends it to the openAI API to generate the content of the README.md. The API is invoked through the OpenAI library, which also reads the OpenAI API key from the user.

The content of the directory is determined from the utils/directory.py file, which reads the .gitignore file to determine which files should be ignored, and which files should be included in the directory listing.

## Usage
To use this code, you need to have an OpenAI API key and the required packages installed, run the generate.py script, and the README.md will be generated and committed to the repository.