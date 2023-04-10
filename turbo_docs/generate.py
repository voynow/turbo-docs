import click
import os
import pyperclip
from turbo_docs.utils import directory, openai_api, cli_options


def run_create_readme(text):
    """ Generates a README.md
    """
    prompt = f"Create a formatted & user-friendly readme.md from the following:\n\n{text}"
    response = openai_api.gpt_completion_wrapper(prompt)
    with open("README.md", "w") as readme_file:
        readme_file.write(response)
    print(f"(--create_readme) Generated README.md")


def run_create_readme_plus(files):
    """ Extends the run_create_readme function to handle larger repos
    """
    responses = {}
    for file_path, file_content in files.items():
        if os.stat(file_path).st_size and file_path.split(".")[1]:
            print(f"(--create_readme_plus) Summarizing from {file_path}")
            prompt = f"Summarize the following code, especially maintaining key logic:\n{file_content}"
            responses[file_path] = openai_api.gpt_completion_wrapper(prompt)
    psuedocode = "\n\n\n".join([f"{file_path}:\n{summary}" for file_path, summary in responses.items()])
    run_create_readme(psuedocode)
    print(f"(--create_readme_plus) Generated README.md")


@click.command()
@cli_options.copy
@cli_options.create_readme
@cli_options.create_readme_plus
def driver(copy: bool, create_readme: bool, create_readme_plus: bool) -> None:
    """ Main driver function that generates a README.md file for the current repository.
    """
    files = directory.get_files()
    dir_text = "\n\n".join([f"{name}:\n\n{content}" for name, content in files.items()])

    # Copy directory text to clipboard if specified
    if copy:
        pyperclip.copy(dir_text)
        print("(--copy) Directory text copied to clipboard")

    # Generate README.md file if specified
    if create_readme:
        run_create_readme(dir_text)

    # Generate docs.md file if specified
    if create_readme_plus:
        run_create_readme_plus(files)


if __name__ == '__main__':
    driver()
