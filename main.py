import os
from git import Repo
from api_interaction import send_request_to_chatgpt, get_chatgpt_api_key
from directory_processing import read_gitignore, prepare_files_list

def main():
    api_key = get_chatgpt_api_key()

    # Read .gitignore file and prepare the list of ignored files and directories
    ignored_files = read_gitignore()

    # Prepare a list of files to send to the ChatGPT API
    file_list = prepare_files_list(ignored_files)

    # Send the request to the ChatGPT API
    response = send_request_to_chatgpt(api_key, file_list)

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
    repo.git.push()

if __name__ == "__main__":
    main()
