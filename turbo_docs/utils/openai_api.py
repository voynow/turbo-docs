import os
import openai

if not os.environ.get("OPENAI_API_KEY"):
	print("OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below.")
	print("If you have not done so already, create an OpenAI account at https://platform.openai.com/overview.")
	os.environ['OPENAI_API_KEY'] = input("Secret key: ")

from llm_blocks import chat_utils


def gpt_completion(template, model="gpt-4", chain=None, **inputs):
	"""Generic chat wrapper over the OpenAI API"""

	if chain is None:
		chain = chat_utils.GenericChain(
			template=template, 
			model_name=model
		)
	try:
		resp = chain(inputs)
	except openai.error.InvalidRequestError as e:
		raise ValueError(f"Caught OpenAI API error: {e}")
	return resp, chain
