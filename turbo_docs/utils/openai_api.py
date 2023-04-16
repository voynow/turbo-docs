import json
import os


def openai_init():
	"""
    Inititalize OpenAI API environment.
    Checks for the existence of API key and requires the user to set if it has not been set already.
    """
	import openai
	openai.api_key = os.environ.get('OPENAI_API_KEY')

	if not openai.api_key:
		raise ValueError("Cannot find API key. Run the following command: export OPENAI_API_KEY=<your_api_key>")
	return openai


def gpt_completion_wrapper(prompt):
	"""
    ''This function wraps an OpenAI completion for input prompt and returns the text in the first completion item.''
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
