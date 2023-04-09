import click
import pyperclip
from utils import directory, openai_api, cli_options

@click.command()
@cli_options.copy
@cli_options.create_readme
def driver(copy: bool, create_readme: bool) -> None:
    """
    Main driver function that generates a README.md file for the current repository.
    
    :param copy: bool, If True, copies the directory text to the clipboard.
    :param create_readme: bool, If True, generates a README.md file for the current repository.
    """
    dir_text = directory.get_directory_text()

    # Copy directory text to clipboard if specified
    if copy:
        pyperclip.copy(dir_text)
        print("(--copy) Directory text copied to clipboard")

    # Generate README.md file if specified
    if create_readme:
        prompt = f"Create a detailed/formatted readme.md for the following code:\n\n{dir_text}"
        response = openai_api.gpt_completion_wrapper(prompt)
        with open("README.md", "w") as readme_file:
            readme_file.write(response['text'])
        print("(--create_readme) Generated README.md")

if __name__ == '__main__':
    driver()
