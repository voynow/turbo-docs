import os

if not os.environ.get("OPENAI_API_KEY"):
    print(
        "OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below."
    )
    print(
        "If you have not done so already, create an OpenAI account at https://platform.openai.com/overview."
    )
    os.environ["OPENAI_API_KEY"] = input("Secret key: ")

from openai import OpenAI


def gpt_completion(prompt, model="gpt-4-1106-preview"):
    client = OpenAI()
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )
    return chat_completion.choices[0].message.content
