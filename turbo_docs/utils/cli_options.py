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

def docstring(func: Callable) -> Callable:
    return click.option(
        '--docstring',
        default=False,
        is_flag=True,
        help='Generate and insert docstrings for each function'
    )(func)
