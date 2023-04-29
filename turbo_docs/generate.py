import click
import pyperclip
from turbo_docs.commands import docstring as docstring_module
from turbo_docs.commands import readme as readme_module
from turbo_docs.utils import directory, cli_options


@click.command()
@cli_options.copy
@cli_options.readme
@cli_options.readme_large_repo
@cli_options.docstring
def driver(
        copy: bool,
        readme: bool,
        readme_large_repo: bool,
        docstring: bool,
) -> None:
    """
    Generate a README or docs.md for the current directory.
    """
    files = directory.get_files()
    dir_text = "\n\n".join(
        [f"{name}:\n\n{content}" for name, content in files.items()])

    # Copy directory text to clipboard if specified
    if copy:
        pyperclip.copy(dir_text)
        print("(--copy) Directory text copied to clipboard")

    # Generate docstring for each function if specified
    if docstring:
        docstring_module.docstring(files)

    # Generate README.md file if specified
    if readme:
        readme_module.readme(dir_text)

    # Generate docs.md file if specified
    if readme_large_repo:
        readme_module.readme_large_repo(files)



if __name__ == '__main__':
    driver()
