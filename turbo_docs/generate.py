import click
import pyperclip
from turbo_docs.commands import readme as readme_module
from turbo_docs.utils import directory, cli_options


@click.command()
@cli_options.copy
@cli_options.readme
def driver(
        copy: bool,
        readme: bool,
) -> None:
    """
    Pull text from all files in the current directory and apply the following commands:

    'turbo_docs --copy' copies the text to clipboard
        Useful for wokring with ChatGPT

    'turbo_docs --readme' generates a README.md file
        Useful for keeping documentation up to date
    """
    dir_text = directory.get_repo_text()

    if copy:
        pyperclip.copy(dir_text)
        print("(--copy) Directory text copied to clipboard")

    if readme:
        readme_module.readme(dir_text)
        print("(--readme) README.md file generated")


if __name__ == '__main__':
    driver()
