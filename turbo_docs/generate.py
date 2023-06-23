import click
import pyperclip
from turbo_docs.commands import readme as readme_module
from turbo_docs.commands import docs as docs_module
from turbo_docs.utils import directory, cli_options


@click.command()
@cli_options.copy
@cli_options.readme
@cli_options.gpt3
def driver(
    copy: bool,
    readme: bool,
    gpt3: bool,
    docs: bool,
) -> None:
    """
    Pull text from all files in the current directory and apply the following commands:

    'turbo_docs --copy' copies the text to clipboard
        Useful for wokring with ChatGPT

    'turbo_docs --readme' generates a README.md file
        Useful for keeping documentation up to date

    'turbo_docs --gpt3' uses GPT-3.5-turbo-16k
        Useful if you don't have GPT-4 access

    'turbo_docs --docs' generates a docs for each file
        Useful for keeping documentation up to date
    """
    dir_text_dict = directory.get_repo_text_dict()

    if copy:
        pyperclip.copy(directory.convert_dict_to_string(dir_text_dict))
        print("Directory copied to clipboard")

    if readme:
        readme_text_dict = directory.remove_readme(dir_text_dict)
        readme_text = directory.convert_dict_to_string(readme_text_dict)
        readme_module.readme(readme_text, gpt3)
        print("Generated README.md")


    if docs:
        docs_module.generate_docs(dir_text_dict, gpt3)
        print("Generated documentation")


if __name__ == "__main__":
    driver()