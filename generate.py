import click
from git import Repo
import pyperclip
from utils import directory, openai_api, cli_options


@click.command()
@cli_options.output_text
@cli_options.git_operations
@cli_options.create_readme
def driver(to_clipboard: bool, git_operations: bool, create_readme: bool):
    """
    Generate a README.md file for the current repository, commit, and push the changes (if specified).
    """
    dir_text = directory.get_directory_text()

    # copy directory to clipboard
    if to_clipboard:
        pyperclip.copy(dir_text)
        print("Directory text copied to clipboard")

    # create readme file
    if create_readme:
        prompt = f"Create a readme.md for the following repository:\n\n{dir_text}"
        response = openai_api.gpt_completion_wrapper(prompt)
        with open("README.md", "w") as readme_file:
            readme_file.write(response['text'])
        print("Generated README.md")
                
        # Perform Git operations
        if git_operations:
            repo = Repo(".")
            repo.git.add("README.md")
            repo.git.commit("-m", "Automatically generated README.md using GPT")
            repo.git.push()
            print("Performed Git operations add, commit, and push")

if __name__ == '__main__':
    driver()
