import json
import os


def openai_init():
    """
    Initialize the OpenAI API and prompt the user for their API key if it is not
    stored as an environment variable.
    """
    import openai
    openai.api_key = os.environ.get('OPENAI_API_KEY')

    if not openai.api_key:
        print("OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below.")
        print("If you have not done so already, create an OpenAI account at https://platform.openai.com/overview.")
        openai.api_key = input("Secret key:")
    return openai


def gpt_completion_wrapper(prompt, openai_package=None):
    """
    Provide GPT-3 completions for a given prompt and optional OpenAI package.
    """
    if not openai_package:
        openai_package = openai_init()

    completions = openai_package.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
    )
    return completions.choices[0]['text'].strip()


def gpt_completion_error_handler(prompt):
    """
    Handle errors raised by OpenAI GPT completion API.
    """
    text = None
    openai_package = openai_init()

    try:
        text = gpt_completion_wrapper(prompt, openai_package=openai_package)
    except openai_package.error.InvalidRequestError as e:
        print(f"Caught OpenAI API error: {e}")
    return text
