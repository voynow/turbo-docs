import click
from typing import Callable

def copy(func: Callable) -> Callable:
    """
    Make it possible to copy directory text to clipboard.
    """
    return click.option(
        '--copy',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard'
    )(func)

def readme(func: Callable) -> Callable:
    """
    Decorate a function to add an option for generating a README.md file.
    """
    return click.option(
        '--readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)

def readme_large_repo(func: Callable) -> Callable:
    """
    Adds an optional flag to generate readme for larger repositories.
    """
    return click.option(
        '--readme_large_repo',
        default=False,
        is_flag=True,
        help='Generate readme for larger repositories'
    )(func)

def unit_tests(func: Callable) -> Callable:
    """
    Add the '--unit_tests' option for a given function that, when true, generates
    unit tests for each code file.
    """
    return click.option(
        '--unit_tests',
        default=False,
        is_flag=True,
        help='Generate unit tests for each code file'
    )(func)

def docstring(func: Callable) -> Callable:
    """
    Decorate function to generate and insert docstrings for each function.
    """
    return click.option(
        '--docstring',
        default=False,
        is_flag=True,
        help='Generate and insert docstrings for each function'
    )(func)

def commit(func: Callable) -> Callable:
    """
    Decorator to add a command line option to a function to generate a commit
    message and execute the commit.
    """
    return click.option(
        '--commit',
        default=False,
        is_flag=True,
        help='Generate a commit message and execute the commit'
    )(func)
