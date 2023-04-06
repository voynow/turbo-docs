import requests
import json

def gpt_gen(data):
    import openai
    openai.api_key = "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"
    # openai.api_key = input("Please enter your openAI API key: ")

    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following Python files and generate a README.md and a user-friendly documentation.md:\n{data}",
        max_tokens=2048,
        n=1,
        stop=None,
    )

    print(completions.choices[0])