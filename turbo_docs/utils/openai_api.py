import os
import openai

if not os.environ.get("OPENAI_API_KEY"):
	print("OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below.")
	print("If you have not done so already, create an OpenAI account at https://platform.openai.com/overview.")
	os.environ['OPENAI_API_KEY'] = input("Secret key:")

from llm_blocks import chat_utils


def gpt_completion(template, inputs, model="gpt-4"):
	"""Genneric chat wrapper over the OpenAI API"""

	print(f"Using model: {model}")
	if model == "gpt-4":
		print("Warning: This model is under limited beta access and is not available to all users.")
		print("Warning: GPT-4 api calls tend to be slower than other models.")
	resp = None

	try:
		chain = chat_utils.GenericChain(
			template=template, 
			model_name=model
		)
		resp = chain(inputs)['text']
	except openai.error.InvalidRequestError as e:
		print(f"Caught OpenAI API error: {e}")

	return resp
