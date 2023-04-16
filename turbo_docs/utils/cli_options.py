import click
from typing import Callable

def copy(func: Callable) -> Callable:
	"""
    Create a click option to support copying directory text to the clipboard.
    """
	return click.option(
		'--copy',
		default=False,
		is_flag=True,
		help='Copy the directory text to clipboard'
	)(func)

def create_readme(func: Callable) -> Callable:
	"""
    Add a --create_readme flag for a function, which when set to true, will generate
    a README.md file
    """
	return click.option(
		'--create_readme',
		default=False,
		is_flag=True,
		help='Generate README.md file'
	)(func)

def create_readme_plus(func: Callable) -> Callable:
	"""
    Wrap a function to provide flag to generate readme for larger repositories.
    """
	return click.option(
		'--create_readme_plus',
		default=False,
		is_flag=True,
		help='Generate readme for larger repositories'
	)(func)

def create_tests(func: Callable) -> Callable:
	"""
    Create a command line flag to generate unit tests for each code file.
    """
	return click.option(
		'--create_tests',
		default=False,
		is_flag=True,
		help='Generate unit tests for each code file'
	)(func)

def create_docstring(func: Callable) -> Callable:
	"""
    Generate and insert docstrings for each function using GPT.
    """
	return click.option(
		'--create_docstring',
		default=False,
		is_flag=True,
		help='Generate and insert docstrings for each function using GPT'
	)(func)
