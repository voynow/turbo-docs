import os
from turbo_docs.utils import openai_api


def readme(text):
    """
    Generate a README.md using openAI API 
    """
    readme = "README.md"
    prompt = f"You are an expert software developer. Create a well-formatted, user-firendly readme.md documenting the following repo:\n\n{text}"
    response = openai_api.gpt_completion_error_handler(prompt)
    if response is None:
        print("Unable to generate README.md, it seems like you have uploaded too many tokens.")
    else:
        with open(readme, "w") as readme_file:
            readme_file.write(response)
