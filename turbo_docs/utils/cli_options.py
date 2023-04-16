import click
from typing import Callable

def copy(func: Callable) -> Callable:
	"""
    Apply the click option for copying the directory to clipboard on any callable object.
    """
	return click.option(
		'--copy',
		default=False,
		is_flag=True,
		help='Copy the directory text to clipboard'
	)(func)

def create_readme(func: Callable) -> Callable:
	"""
    This function creates a README.md file with a flag parameter to set its generation. This can be used to easily generate a README.md file with a single command. 
    """
	return click.option(
		'--create_readme',
		default=False,
		is_flag=True,
		help='Generate README.md file'
	)(func)

def create_readme_plus(func: Callable) -> Callable:
	"""
    Returns a decorator for Click commands that adds an option to generate a readme for larger repositories. 
    """
	return click.option(
		'--create_readme_plus',
		default=False,
		is_flag=True,
		help='Generate readme for larger repositories'
	)(func)

def create_tests(func: Callable) -> Callable:
	"""
    Creates unit tests for code files. Enables a flag to generate the tests when the function is called.
    """
	return click.option(
		'--create_tests',
		default=False,
		is_flag=True,
		help='Generate unit tests for each code file'
	)(func)

def create_docstring(func: Callable) -> Callable:
	"""
    Add the ability to create GPT generated docstring for functions. This is useful for quickly generating basic docstrings for functions
    """
	return click.option(
		'--create_docstring',
		default=False,
		is_flag=True,
		help='Generate and insert docstrings for each function using GPT'
	)(func)
