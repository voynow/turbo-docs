from pathlib import Path

import click
import pyperclip
import tiktoken

from turbo_docs.commands import docs as docs_module
from turbo_docs.commands import readme as readme_module
from turbo_docs.utils import cli_options, directory


def resolve_model(gpt3):
    if gpt3:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4-1106-preview"
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


def generate_readme(dir_text_dict: dict, gpt3: bool, narrative: str) -> None:
    if Path("README.md") in dir_text_dict:
        del dir_text_dict[Path("README.md")]
    dir_text_str = directory.convert_dict_to_string(dir_text_dict)
    model = resolve_model(gpt3)
    num_tokens = num_tokens_from_string(dir_text_str)
    print(f"Generating README.md. Using {num_tokens} tokens.")
    readme_module.readme(dir_text_str, model, narrative=narrative)
    print("Generated README.md")


def generate_docs(dir_text_dict: dict, gpt3: bool) -> None:
    model = resolve_model(gpt3)
    docs_module.docs(dir_text_dict, model)
    print("Generated documentation")


def copy_text_to_clipboard(dir_text_dict: dict) -> None:
    dir_text_str = directory.convert_dict_to_string(dir_text_dict)
    num_tokens = num_tokens_from_string(dir_text_str)
    print(f"Copying directory to clipboard. Using {num_tokens} tokens.")
    pyperclip.copy(dir_text_str)
    print("Copied directory text to clipboard")


@click.command()
@cli_options.copy
@cli_options.readme
@cli_options.gpt3
@cli_options.docs
@cli_options.narrative
def driver(
    copy: bool,
    readme: bool,
    gpt3: bool,
    docs: bool,
    narrative: str,
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
        generate_readme(dir_text_dict, gpt3, narrative)

    if docs:
        generate_docs(dir_text_dict, gpt3)

    if copy:
        copy_text_to_clipboard(dir_text_dict)
