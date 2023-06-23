## function: copy
#### args: func
This function takes a callable as input and returns a new callable with an added `--copy` option. The `--copy` option, when set to True, enables copying the directory text to the clipboard. This is useful for quickly sharing directory contents without manually copying them.

## function: readme
#### args: func
The readme function takes a callable function as input and returns a new function wrapped with a click.option decorator. This decorator adds a command line option '--readme' to the input function, allowing users to generate a README.md file when the option is enabled.

## function: gpt3
#### args: func
The gpt3 function is a decorator that adds a command line option '--gpt3' to the given callable function, enabling the use of GPT-3.5 Turbo model when the flag is set. It simplifies the integration of GPT-3.5 Turbo into your application by handling the command line option for you. <end>

## function: docs
#### args: func
This function takes a callable function as input and returns a modified version of the function with an added command line option '--docs'. This option, when used, generates documentation for all code files in the project, providing a convenient way to keep documentation up-to-date.

