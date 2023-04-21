import json
import os


def openai_init():
    """
    Initialize the OpenAI API with API Key stored in environment variable.
    """
    import openai
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    if not openai.api_key:
        raise ValueError("Cannot find API key. Run the following command: export OPENAI_API_KEY=<your_api_key>")
    return openai


def gpt_completion_wrapper(prompt):
    """
    GPT-3 completion wrapper that fetches a completion from OpenAI package and
    returns it, with specified parameters.
    """
    openai_package = openai_init()
    completions = openai_package.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
    )
    return completions.choices[0]['text'].strip()
