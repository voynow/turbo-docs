import click
from typing import Callable

def copy(func: Callable) -> Callable:
	return click.option(
		'--copy',
		default=False,
		is_flag=True,
		help='Copy the directory text to clipboard'
	)(func)

def create_readme(func: Callable) -> Callable:
	return click.option(
		'--create_readme',
		default=False,
		is_flag=True,
		help='Generate README.md file'
	)(func)

def create_readme_plus(func: Callable) -> Callable:
	return click.option(
		'--create_readme_plus',
		default=False,
		is_flag=True,
		help='Generate readme for larger repositories'
	)(func)

def create_tests(func: Callable) -> Callable:
	return click.option(
		'--create_tests',
		default=False,
		is_flag=True,
		help='Generate unit tests for each code file'
	)(func)
