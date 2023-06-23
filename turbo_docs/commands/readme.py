
TEMPLATE = """
"You are an expert software developement assistant. Write a README.md for the following repo:
{repo}

Here are the requirements for the README.md:
- written in highly formatted markdown
- contain a title and high level overview
- pitch for why the tool is useful
- contain table of contents highlighting repo structure
- example usage of important functions
- contain all possible applicable badges (pypi, github, etc.)
- emoji are encouraged. One for each section at minimum.
"""

def readme(repo, model, template=TEMPLATE):
    """
    Chose between GPT-3.5 Turbo and GPT-4, allow for template override, and
    generate a README.md file for the current repo.
    """
    from turbo_docs.utils import openai_api

    readme = "README.md"
    chain = openai_api.gpt_completion(template, {"repo": repo}, model)
    response = chain.logs[-1]['response']['text']
    
    with open(readme, "w", encoding="utf-8") as readme_file:
        readme_file.write(response)
