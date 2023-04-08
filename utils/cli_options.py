import click

output_text = click.option(
    '--output_text',
    default=False,
    is_flag=True,
    help='Display the directory text before generating the README.md file.'
)

git_operations = click.option(
    '--git_operations',
    default=False,
    is_flag=True,
    help='Perform Git operations (add, commit, and push) for the generated README.md file.'
)
