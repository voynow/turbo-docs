from turbo_docs.utils import openai_api

TEMPLATE = """
"You are an expert software developement assistant.

Create a well-formatted, user-firendly readme.md documenting the following repo:
{repo}
"""

def readme(repo, template=TEMPLATE):
    """
    Generate a README.md using openAI API
    """
    readme = "README.md"
    response = openai_api.gpt_completion(template, {"repo": repo})
    if response is None:
        print("Unable to generate README.md, it seems like you have uploaded too many tokens.")
    else:
        with open(readme, "w") as readme_file:
            readme_file.write(response)
