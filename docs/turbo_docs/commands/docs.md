## function: generate_docs
#### args: path, function, model='gpt-4', template=TEMPLATE, chain=None
The `generate_docs` function is designed to generate and write documentation for a given function. It utilizes the OpenAI API to generate the documentation, which can be based on a specific model and template. The function also supports the use of an existing chain for a cohesive chain of gpt completions. The generated documentation is then written to a markdown file at the specified path.

## function: docs
#### args: repo_dict, model, template=TEMPLATE
The `docs` function parses code from a given repository dictionary, identifies all the functions within Python files, and generates documentation for each of these functions. It first checks if a 'docs' directory exists and removes it to ensure a fresh start. It then iterates over the repository dictionary, parsing Python files and identifying functions using the Abstract Syntax Trees (AST) module. For each function, it generates documentation using a specified model and template, and prints a message indicating the progress.

