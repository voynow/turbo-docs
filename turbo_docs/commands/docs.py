
import ast
from pathlib import Path
from turbo_docs.utils import openai_api

TEMPLATE = """
You are an expert software developement assistant tasked with writing documentation for a repository. 

Write documentation for the following function:
{function}

Your documentation should include the following and nothing more:
## function: function_name
#### args: arg1, arg2, ...
Description of function in english as concisely as possible in less than 4 sentences. 
Do not mlist arguments. Do not give code examples. Minimize tokens at all costs.
"""

def generate_docs(model, template, function, path):
    """ Generate and write documentation for a function """
    documentation = openai_api.gpt_completion(template, {"function": function}, model)
    doc_path = Path('docs') / path.with_suffix('.md')
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(doc_path, 'a') as f:
        f.write(f'{documentation}\n\n')


def docs(repo_dict, gpt3=False, template=TEMPLATE):
    """ Parse code for functions and generate documentation for each """
    if gpt3:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4"

    for path, content in repo_dict.items():
        if path.suffix == '.py':
            module = ast.parse(content)
            functions = [ast.unparse(node) for node in module.body if isinstance(node, ast.FunctionDef)]
            for function in functions:
                generate_docs(model, template, function, path)
