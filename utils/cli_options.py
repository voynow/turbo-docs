import click

def output_text(func):
    return click.option(
        '--to_clipboard',
        default=False,
        is_flag=True,
        help='Copy the directory text to clipboard. This can be used in the ChatGPT webapp.'
    )(func)

def git_operations(func):
    return click.option(
        '--git_operations',
        default=False,
        is_flag=True,
        help='Perform Git operations (add, commit, and push) for the generated README.md file.'
    )(func)

def create_readme(func):
    return click.option(
        '--create_readme',
        default=False,
        is_flag=True,
        help='Generate README.md file'
    )(func)
