import click
from typing import Callable

def copy(func: Callable) -> Callable:
    return click.option(
        '--copy',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard. This can be used in the ChatGPT webapp.'
    )(func)

def create_readme(func: Callable) -> Callable:
    return click.option(
        '--create_readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)
