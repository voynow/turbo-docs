import json
import os


def openai_init():
	"""
    Initializes the OpenAI library by setting the API key, and checking if it is set. Raises ValueError if API key is not found.
    """
	import openai
	openai.api_key = os.environ.get('OPENAI_API_KEY')

	if not openai.api_key:
		raise ValueError("Cannot find API key. Run the following command: export OPENAI_API_KEY=<your_api_key>")
	return openai


def gpt_completion_wrapper(prompt):
	"""
    This function wraps an OpenAI package to provide text completion from a given prompt using GPT-3. It uses the "text-davinci-003" engine and returns one completion with up to 2048 tokens.
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
