import os
from git import Repo
from utils import api, directory

def main():

    # Prepare a list of files to send to the ChatGPT API
    file_list = directory.prepare_files_list()

    # Send the request to the ChatGPT API
    response = api.gpt_gen(file_list)

    # Write the received README.md and documentation.md to the root directory
    with open("README.md", "w") as readme_file:
        readme_file.write(response["readme"])
    with open("documentation.md", "w") as documentation_file:
        documentation_file.write(response["documentation"])

    # Commit and push the changes to the repository
    repo = Repo(".")
    repo.git.add("README.md")
    repo.git.add("documentation.md")
    repo.git.commit("-m", "Automatically generated README and documentation.")
    # repo.git.push()

if __name__ == "__main__":
    main()
