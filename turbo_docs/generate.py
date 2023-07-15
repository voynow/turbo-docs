import click
from pathlib import Path
import pyperclip
import tiktoken
from turbo_docs.commands import readme as readme_module
from turbo_docs.commands import docs as docs_module
from turbo_docs.utils import directory, cli_options

def resolve_model(gpt3):
    if gpt3:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4"
        print(
            "Warning: This model is under limited beta access and is not available to all users."
        )
        print("Warning: GPT-4 api calls tend to be slower than other models.")

    print(f"Using model: {model}")
    return model

def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string, allowed_special="all"))
    return num_tokens

@click.command()
@cli_options.copy
@cli_options.readme
@cli_options.gpt3
@cli_options.docs
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

    if readme:
        if Path("README.md") in dir_text_dict:
            del dir_text_dict[Path("README.md")]
        dir_text_str = directory.convert_dict_to_string(dir_text_dict)
        model = resolve_model(gpt3)
        readme_module.readme(dir_text_str, model)
        print("Generated README.md")

    if docs:
        model = resolve_model(gpt3)
        docs_module.docs(dir_text_dict, model)
        print("Generated documentation")

    if copy:
        dir_text_str = directory.convert_dict_to_string(dir_text_dict)
        num_tokens = num_tokens_from_string(dir_text_str)
        pyperclip.copy(dir_text_str)
        print(f"Directory text copied to clipboard containing {num_tokens} tokens")
