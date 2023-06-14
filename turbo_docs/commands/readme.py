
TEMPLATE = """
"You are an expert software developement assistant.

Create a formatted professional README.md documenting setup and usage of the following repo:
{repo}
"""

def readme(repo, gpt3=False, template=TEMPLATE):
    """
    Chose between GPT-3.5 Turbo and GPT-4, allow for template override, and
    generate a README.md file for the current repo.
    """
    from turbo_docs.utils import openai_api

    readme = "README.md"
    if gpt3:
        model = "gpt-3.5-turbo-16k"
    else:
        model = "gpt-4"

    response = openai_api.gpt_completion(template, {"repo": repo}, model)
    if response is None:
        print("Unable to generate README.md, it seems like you have uploaded too many tokens.")
    else:
        with open(readme, "w") as readme_file:
            readme_file.write(response)
