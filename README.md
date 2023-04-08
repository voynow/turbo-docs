

# README.md
This repository contains the code necessary to generate a README.md file from a given folder. It utilizes the OpenAI API to generate the content of the file.

The `driver()` function found in `generate.py` does the following:
1. Gathers the content of all files in the current folder and subfolders, excluding files from the `.gitignore` file.
2. Sends this content to the OpenAI API for completion.
3. Writes the response to the root directory with the name `README.md`.
4. Commits and pushes the changes to the repository.

This process assumes that the repository contains the necessary `requirements.txt` file, listing the packages that need to be installed, and a `utils` folder, containing both the `directory.py` and the `openai_api.py` scripts.

The `directory.py` script handles the gathering of the repository's content and the exclusion of ignored files. Its main function is `get_directory_text()`, which returns a string with all the content in the repository.

The `openai_api.py` script contains a wrapper function for the OpenAI API, called `gpt_completion_wrapper()`, which sends the prompt to the API and returns the completion.

Finally, the `requirements.tx` file contains the necessary packages for the project, such as `requests` and `GitPython`. The additional package `openai` is required for the API's functioning.

In order to use this project, the API key should be added manually to the `openai_api.py`file, prompting the user for input before calling the API.

This project is Open Source and anyone is free to use and modify it, as long as they adhere to the license agreement. Enjoy!