import click
import pyperclip
from turbo_docs.commands import commit as commit_module
from turbo_docs.commands import docstring as docstring_module
from turbo_docs.commands import readme as readme_module
from turbo_docs.commands import unit_tests as unit_tests_module
from turbo_docs.utils import directory, cli_options


@click.command()
@cli_options.copy
@cli_options.readme
@cli_options.readme_large_repo
@cli_options.unit_tests
@cli_options.docstring
@cli_options.commit
def driver(
        copy: bool,
        readme: bool,
        readme_large_repo: bool,
        unit_tests: bool,
        docstring: bool,
        commit: bool
) -> None:
    """
    Generates files, such as README, Docstring and Unit Tests, based on the code in 
    your local directory
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

    # Generate unit tests for each code file if specified
    if unit_tests:
        print("Warning: This feature is still in development. GPT4 will likely solve this problem waiting on API access. -voynow")
        unit_tests_module.unit_tests(files)

    # Generate docstring for each function if specified
    if commit:
        print("Warning: This feature is still in development. GPT4 will likely solve this problem waiting on API access. -voynow")
        commit_module.commit(files)




if __name__ == '__main__':
    driver()
