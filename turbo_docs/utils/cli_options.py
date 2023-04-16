import click
from typing import Callable

def copy(func: Callable) -> Callable:
	"""
    Copy a given Callable object to the clipboard. Provides flag --copy to enable/disable the copy.
    """
	return click.option(
		'--copy',
		default=False,
		is_flag=True,
		help='Copy the directory text to clipboard'
	)(func)

def create_readme(func: Callable) -> Callable:
	"""
    Add support for a --create_readme flag to a given Callable. When this flag is included, a README.md file will be generated.
    """
	return click.option(
		'--create_readme',
		default=False,
		is_flag=True,
		help='Generate README.md file'
	)(func)

def create_readme_plus(func: Callable) -> Callable:
	"""
    Wraps a given function with an '--create_readme_plus' option for generating a readme for larger repositories.
    """
	return click.option(
		'--create_readme_plus',
		default=False,
		is_flag=True,
		help='Generate readme for larger repositories'
	)(func)

def create_tests(func: Callable) -> Callable:
	"""
    A decorator that adds an argument to a command line function enabling a flag for generating unit tests for each code file.
    """
	return click.option(
		'--create_tests',
		default=False,
		is_flag=True,
		help='Generate unit tests for each code file'
	)(func)

def create_docstring(func: Callable) -> Callable:
	"""
    Create docstrings for each function using GPT.
    """
	return click.option(
		'--create_docstring',
		default=False,
		is_flag=True,
		help='Generate and insert docstrings for each function using GPT'
	)(func)
