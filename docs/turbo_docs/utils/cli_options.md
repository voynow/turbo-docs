## function: copy
#### args: func
A decorator function that adds a command line option to the decorated function. The added option is "--copy" which is a flag that defaults to False. When the option is used, it copies the directory text to the clipboard.

## function: readme
#### args: func
Generates a README.md file for a repository.

## function: gpt3
#### args: func
Wraps the provided function with a click option decorator that adds a command line option '--gpt3' with default value False and is_flag set to True. This option can be used to enable the use of the GPT-3.5 Turbo model.

## function: docs
#### args: func
Decorator function that takes in a function as an argument and returns a modified version of that function. The modified function includes a command line option '--docs' which, when used, generates documentation for all code files.

