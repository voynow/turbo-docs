import json
import os


def openai_init():
    """
    Initializes OpenAI API and sets API key.
    """
    import openai
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    if not openai.api_key:
        print("OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below.")
        print("If you have not done so already, create an OpenAI account at https://platform.openai.com/overview.")
        openai.api_key = input("Secret key:")
    return openai


def gpt_completion_wrapper(prompt):
    """
    Wraps OpenAI's text completion model to generate a result for the given prompt.
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
