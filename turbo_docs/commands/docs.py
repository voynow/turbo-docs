import ast
from pathlib import Path
import shutil

TEMPLATE = """
You are an expert software developement assistant tasked with writing documentation for a repository.

The documentation must following the following format:
## function: function_name
#### args: arg1, arg2, ...
Insert description of the function here
<end>

In your description, describe the function in english in at least one sentence but less than four sentences. Subtly describe the usefule/counterintuitive aspects of the function. Do not list arguments. Do not give code examples.

Here is the function:
{function}

Now, write the documentation following the format above.
"""

def generate_docs(path, function, model="gpt-4", template=TEMPLATE, chain=None):
    """
    Generate and write documentation for a function. Use existing chain for
    a cohesive chain of gpt completions.
    """
    from turbo_docs.utils import openai_api

    documentation, chain = openai_api.gpt_completion(
        model=model, chain=chain, template=template, function=function
    )
    doc_path = Path("docs") / path.with_suffix(".md")
    doc_path.parent.mkdir(parents=True, exist_ok=True)
    with open(doc_path, "a") as f:
        f.write(f"{documentation}\n\n")
    return chain


def docs(repo_dict, model, template=TEMPLATE):
    """Parse code for functions and generate documentation for each"""
    chain = None

    # remove old docs since we are appending
    if Path("docs").exists():
        shutil.rmtree("docs")

    for path, content in repo_dict.items():
        if path.suffix == ".py":
            module = ast.parse(content)
            functions = [
                (node, ast.unparse(node))
                for node in module.body
                if isinstance(node, ast.FunctionDef)
            ]
            for node, function in functions:
                print(f"Generating docs for {path.stem}.{node.name}")
                chain = generate_docs(
                    path, function, model=model, template=template, chain=chain
                )
