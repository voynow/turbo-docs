import click
from typing import Callable

def to_clipboard(func: Callable) -> Callable:
    return click.option(
        '--to_clipboard',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard. This can be used in the ChatGPT webapp.'
    )(func)

def git_operations(func: Callable) -> Callable:
    return click.option(
        '--git_operations',
        default=False,
        is_flag=True,
        help='Perform Git operations (add, commit, and push) for the generated README.md file.'
    )(func)

def create_readme(func: Callable) -> Callable:
    return click.option(
        '--create_readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)
