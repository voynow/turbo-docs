import requests
import json
import openai

# openai.api_key = input("Please enter your openAI API key: ")
from utils import secrets_manager
openai.api_key = secrets_manager.get_secrets()['openai_secret_key']


def gpt_gen(data):

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following code repository and generate a user-friendly readme.md:\n{data}",
        max_tokens=2048,
        n=1,
        stop=None,
    )

    return completions.choices[0]