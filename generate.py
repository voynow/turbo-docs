import click
from git import Repo
from utils import directory, openai_api


@click.command()
@click.option('--output_text', default=False, is_flag=True, help='Display the directory text before generating the README.md file.')
@click.option('--git_operations', default=False, is_flag=True, help='Perform Git operations (add, commit, and push) for the generated README.md file.')
def driver(output_text, git_operations):
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
