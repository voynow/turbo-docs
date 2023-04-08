import click

def output_text(func):
    return click.option(
        '--output_text',
        default=False,
        is_flag=True,
        help='Display the directory text before generating the README.md file.'
    )(func)

def git_operations(func):
    return click.option(
        '--git_operations',
        default=False,
        is_flag=True,
        help='Perform Git operations (add, commit, and push) for the generated README.md file.'
    )(func)
