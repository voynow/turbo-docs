
TEMPLATE = """
"You are an expert software developement assistant. Write a README.md for the following repo:
{repo}

Here are the requirements for the README.md:
- written in highly formatted markdown
- badeges for github stars and pypi if applicable
- an utline written assuming the user knows nothing about the repo
- a section on why use this repo, pitching the repo to the user
- repo structure formatted as a tree
- example usage of important functions, especially functions exposed to the user, in code blocks
- emoji are encouraged. One for each section at minimum.
"""

def readme(repo, model, template=TEMPLATE, narrative=""):
    """
    Chose between GPT-3.5 Turbo and GPT-4, allow for template override, and
    generate a README.md file for the current repo.
    """
    from turbo_docs.utils import openai_api

    if narrative:
        template = f"Narritive for your task:\n{narrative}\n\n{template}"

    readme = "README.md"
    response, _ = openai_api.gpt_completion(template, model, repo=repo)
    
    with open(readme, "w", encoding="utf-8") as readme_file:
        readme_file.write(response)
