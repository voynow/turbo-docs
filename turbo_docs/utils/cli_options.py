from typing import Callable

import click


def copy(func: Callable) -> Callable:
    return click.option(
        "--copy",
        default=False,
        is_flag=True,
        help="Copy the directory text to clipboard",
    )(func)


def readme(func: Callable) -> Callable:
    return click.option(
        "--readme", default=False, is_flag=True, help="Generate README.md file"
    )(func)


def gpt3(func: Callable) -> Callable:
    return click.option(
        "--gpt3", default=False, is_flag=True, help="Use the GPT-3.5 Turbo model"
    )(func)
