import click
import os
from pathlib import Path
import pyperclip
from turbo_docs.utils import directory, openai_api, cli_options


def run_create_readme(text):
    """ Generate a formatted and user-friendly README.md file using the provided text.
    """
    readme = "README.md"
    prompt = f"Create a formatted & user-friendly readme.md from the following:\n\n{text}"
    response = openai_api.gpt_completion_wrapper(prompt)
    try:
        with open(readme, "w") as readme_file:
            readme_file.write(response)
    except PermissionError:
        os.remove(readme)
        with open(readme, "w") as readme_file:
            readme_file.write(response)
    print(f"(--create_readme) Generated README.md")




def run_create_readme_plus(files):
    """ Generate a README.md file with summarized code content from the provided files.
    """
    responses = {}
    for file_path, file_content in files.items():
        if os.stat(file_path).st_size and file_path.split(".")[1]:
            print(f"(--create_readme_plus) Summarizing {file_path}")
            prompt = f"Create a README summarizing the following code, especially maintaining key logic:\n{file_content}"
            responses[file_path] = openai_api.gpt_completion_wrapper(prompt)

    flatmap = "\n\n\n".join([f"{file_path}:\n{summary}" for file_path, summary in responses.items()])
    run_create_readme(flatmap)
    print(f"(--create_readme_plus) Generated README.md")


def run_create_tests(test_file_path, file_content):
    """ Generate unit tests for the provided code file content and save them in a test file.
    """
    print(f"(--create_tests) Generating unit tests for {test_file_path}")
    prompt = f"Generate unit tests for the following code:\n{file_content}"
    test_content = openai_api.gpt_completion_wrapper(prompt)
    with open(test_file_path, "w") as test_file:
        test_file.write(test_content)


def run_create_tests_helper(files):
    """ Create unit tests for the provided code files and save them in a 'tests' directory.
    """
    tests_dir = "tests"
    Path(tests_dir).mkdir(exist_ok=True)

    for file_path, file_content in files.items():
        if os.stat(file_path).st_size and file_path.split(".")[1]:
            test_file_name = f"test_{os.path.basename(file_path)}"
            test_file_path = os.path.join(tests_dir, test_file_name)
    
            resp = input(f"Would you like to create unit tests for {test_file_name} (Y/n):")
            if resp != "n" and resp != "N":
                run_create_tests(test_file_path, file_content)


@click.command()
@cli_options.copy
@cli_options.create_readme
@cli_options.create_readme_plus
@cli_options.create_tests
def driver(copy: bool, create_readme: bool, create_readme_plus: bool, create_tests: bool) -> None:
    """ The main driver function that handles various command-line options for generating documentation and tests.
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

    # Generate unit tests for each code file if specified
    if create_tests:
        run_create_tests_helper(files)


if __name__ == '__main__':
    driver()
