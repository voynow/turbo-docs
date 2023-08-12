import click
from typing import Callable

def copy(func: Callable) -> Callable:
    return click.option(
        '--copy',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard'
    )(func)

def readme(func: Callable) -> Callable:
    return click.option(
        '--readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)

def narrative(func: Callable) -> Callable:
    return click.option(
        '--narrative',
        default="",
        type=str,
        help='Provide a narrative to guide the tone and content of the README'
    )(func)

def gpt3(func: Callable) -> Callable:
    return click.option(
        '--gpt3',
        default=False,
        is_flag=True,
        help='Use the GPT-3.5 Turbo model'
    )(func)

def docs(func: Callable) -> Callable:
    return click.option(
        '--docs',
        default=False,
        is_flag=True,
        help='Generate documentation for all code files'
    )(func)
