
from git import Repo
import json
import os

from utils import directory, openai_api


def driver(output_text=True):

    # Prepare a list of files to send to GPT
    dir_text = directory.get_directory_text()
    if output_text:
        print(dir_text)

    # Send the request to the API
    prompt = f"Analyze the following code repository and generate a user-friendly readme.md:\n\n{dir_text}"
    response = openai_api.gpt_completion_wrapper(prompt)

    # Write the received README.md to the root directory
    with open("README.md", "w") as readme_file:
        readme_file.write(response['text'])

    # Commit and push the changes to the repository
    repo = Repo(".")
    repo.git.add("README.md")
    repo.git.commit("-m", "Automatically generated README.md using GPT")
    repo.git.push()


if __name__ == "__main__":
    driver()
