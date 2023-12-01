from pathlib import Path

import click
import pyperclip
import tiktoken

from turbo_docs.commands import readme as readme_module
from turbo_docs.utils import cli_options, directory


def num_tokens_from_string(string: str, encoding_name: str = "cl100k_base") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string, allowed_special="all"))
    return num_tokens


@click.command()
@cli_options.copy
@cli_options.readme
def driver(
    copy: bool,
    readme: bool,
) -> None:
    """
    Pull text from all files in the current directory and apply the following commands:

    'turbo_docs --copy' copies the text to clipboard - Useful for wokring with ChatGPT
    'turbo_docs --readme' generates a README.md file - Useful for keeping documentation up to date
    """
    dir_text_dict = directory.get_repo_text_dict()

    if readme:
        if Path("README.md") in dir_text_dict:
            del dir_text_dict[Path("README.md")]
        dir_text_str = directory.convert_dict_to_string(dir_text_dict)
        readme_module.readme(dir_text_str)
        print("Generated README.md")

    if copy:
        dir_text_str = directory.convert_dict_to_string(dir_text_dict)
        num_tokens = num_tokens_from_string(dir_text_str)
        pyperclip.copy(dir_text_str)
        print(f"Directory text copied to clipboard containing {num_tokens} tokens")
