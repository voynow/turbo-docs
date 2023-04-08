import click
from git import Repo
from utils import directory, openai_api, cli_options


@click.command()
@cli_options.output_text
@cli_options.git_operations
def driver(output_text: bool, git_operations: bool):
    """
    Generate a README.md file for the current repository, commit, and push the changes (if specified).
    """
    # Prepare a list of files to send to GPT
    dir_text = directory.get_directory_text()

    # Send the request to the API
    prompt = f"Create a readme.md from the following repository:\n\n{dir_text}"
    response = openai_api.gpt_completion_wrapper(prompt)

    # Write the received README.md to the root directory
    with open("README.md", "w") as readme_file:
        readme_file.write(response['text'])

    if output_text:
        print(dir_text)
    
    # Perform Git operations if the flag is set
    if git_operations:
        repo = Repo(".")
        repo.git.add("README.md")
        repo.git.commit("-m", "Automatically generated README.md using GPT")
        repo.git.push()

if __name__ == '__main__':
    driver()
