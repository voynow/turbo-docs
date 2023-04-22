import click
from typing import Callable

def copy(func: Callable) -> Callable:
    """
    Create a click option to enable the user to copy directory text to clipboard
    """
    return click.option(
        '--copy',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard'
    )(func)

def readme(func: Callable) -> Callable:
    """
    Decorate a function with the `--readme` option to generate a README.md file.
    """
    return click.option(
        '--readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)

def readme_large_repo(func: Callable) -> Callable:
    """
    Run function to generate README for larger repositories.
    """
    return click.option(
        '--readme_large_repo',
        default=False,
        is_flag=True,
        help='Generate readme for larger repositories'
    )(func)

def unit_tests(func: Callable) -> Callable:
    """
    Enable generation of unit tests for each code file.
    """
    return click.option(
        '--unit_tests',
        default=False,
        is_flag=True,
        help='Generate unit tests for each code file'
    )(func)

def docstring(func: Callable) -> Callable:
    """
    Autogenerate docstrings for functions.
    """
    return click.option(
        '--docstring',
        default=False,
        is_flag=True,
        help='Generate and insert docstrings for each function'
    )(func)

def commit(func: Callable) -> Callable:
    """
    Decorate a function to generate a commit message and execute a commit.
    """
    return click.option(
        '--commit',
        default=False,
        is_flag=True,
        help='Generate a commit message and execute the commit'
    )(func)
