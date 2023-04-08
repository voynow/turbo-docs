import requests
import json
import openai

openai.api_key = input("Please enter your openAI API key:")


def gpt_completion_wrapper(prompt):
    """
    """
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
    )

    return completions.choices[0]