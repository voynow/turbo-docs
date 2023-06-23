## function: generate_docs
#### args: path, function, model='gpt-4', template=TEMPLATE, chain=None
This function generates and writes documentation for a given function using the specified model and template, and optionally continues an existing chain of GPT completions for cohesive documentation. The generated documentation is saved in a Markdown file within the 'docs' directory.

## function: docs
#### args: repo_dict, model, template=TEMPLATE
This function parses the code in a given repository dictionary, identifies functions within Python files, and generates documentation for each function using a specified model and template. It also removes any existing 'docs' folder before generating new documentation.

