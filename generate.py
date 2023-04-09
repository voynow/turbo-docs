import click
from git import Repo
import pyperclip
from utils import directory, openai_api, cli_options
from typing import Callable

@click.command()
@cli_options.to_clipboard
@cli_options.git_operations
@cli_options.create_readme
def driver(to_clipboard: bool, git_operations: bool, create_readme: bool) -> None:
    """
    Generates a README.md file for the current repository, commits, and pushes the changes (if specified).
    
    :param to_clipboard: bool, If True, copies the directory text to the clipboard.
    :param git_operations: bool, If True, performs Git operations (add, commit, and push) for the generated README.md file.
    :param create_readme: bool, If True, generates a README.md file for the current repository.
    """
    dir_text = directory.get_directory_text()

    # Copy directory text to clipboard if specified
    if to_clipboard:
        pyperclip.copy(dir_text)
        print("Directory text copied to clipboard")

    # Generate README.md file if specified
    if create_readme:
        prompt = f"Create a readme.md for the following repository:\n\n{dir_text}"
        response = openai_api.gpt_completion_wrapper(prompt)
        with open("README.md", "w") as readme_file:
            readme_file.write(response['text'])
        print("Generated README.md")

    # Perform Git operations if specified
    if git_operations:
        repo = Repo(".")
        repo.git.add("README.md")
        repo.git.commit("-m", "Automatically generated README.md using GPT")
        repo.git.push()
        print("Performed Git operations add, commit, and push")

if __name__ == '__main__':
    driver()
