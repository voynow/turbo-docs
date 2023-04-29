import click
from typing import Callable

def copy(func: Callable) -> Callable:
    """
    Copy the directory text to clipboard.
    """
    return click.option(
        '--copy',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard'
    )(func)

def readme(func: Callable) -> Callable:
    """
    Add --readme option to a click command to generate a README.md file.
    """
    return click.option(
        '--readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)

def readme_large_repo(func: Callable) -> Callable:
    """
    Decorate a given callable to add an option to generate readme for larger
    repositories.
    """
    return click.option(
        '--readme_large_repo',
        default=False,
        is_flag=True,
        help='Generate readme for larger repositories'
    )(func)

def docstring(func: Callable) -> Callable:
    """
    Generate and insert docstrings for each function.
    """
    return click.option(
        '--docstring',
        default=False,
        is_flag=True,
        help='Generate and insert docstrings for each function'
    )(func)
