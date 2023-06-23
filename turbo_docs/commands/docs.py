
import ast
from pathlib import Path
from turbo_docs.utils import openai_api

TEMPLATE = """
You are an expert software developement assistant. Write documentation for the following function:
{function}

Here are the requirements for the function documentation:
- Brief description of the function
- Detailed description of the parameters
- Explanation of the return values
- Sample invocation of the function
"""


def split_into_functions(code):
    """ parse file for functions """
    module = ast.parse(code)
    functions = [node for node in module.body if isinstance(node, ast.FunctionDef)]
    return [ast.unparse(f) for f in functions]


def write_to_file(path, function_name, doc):
    """ append each function doc to file doc """
    doc_path = Path('docs') / path
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(doc_path, 'a') as f:
        f.write(f'## {function_name}\n\n{doc}\n\n')


def generate_docs(repo_dict, gpt3=False, template=TEMPLATE):

    if gpt3:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4"

    for path, content in repo_dict.items():
        if path.suffix == '.py':

            for function in split_into_functions(content):
                doc = openai_api.gpt_completion(template, {"function": function}, model)
                write_to_file(path, function, doc)

