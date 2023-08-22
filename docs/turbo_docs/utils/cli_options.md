## function: copy
#### args: func
The `copy` function is a decorator that adds a command line option `--copy` to the function it decorates. When this option is used, it copies the directory text to the clipboard. This function is useful when you want to quickly copy the output of a command line tool without having to manually select and copy the text.

## function: readme
#### args: func
The readme function is a decorator that adds a command line option '--readme' to the function it decorates. When the '--readme' option is used, it triggers the generation of a README.md file. This function is useful for automating the creation of README files in your projects.

## function: narrative
#### args: func
The `narrative` function is a decorator that adds a command line option to the function it decorates. This option allows the user to provide a narrative that can guide the tone and content of the README file. This is particularly useful when you want to customize the README generation process based on specific requirements or guidelines.

## function: gpt3
#### args: func
The gpt3 function is a decorator that adds a command line option to the function it decorates. This option allows the user to specify whether to use the GPT-3.5 Turbo model or not. It's a convenient way to switch between different models without changing the code.

## function: docs
#### args: func
The `docs` function is a decorator that adds a command line option `--docs` to the function it decorates. When the `--docs` flag is set to True, it triggers the generation of documentation for all code files. This function is particularly useful for automating the documentation process in a codebase.

