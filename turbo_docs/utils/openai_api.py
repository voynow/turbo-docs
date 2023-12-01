import os

# import openai

if not os.environ.get("OPENAI_API_KEY"):
    print(
        "OpenAI API key is not set. Please set it as an environment variable (export OPENAI_API_KEY=<your_api_key>) or enter it below."
    )
    print(
        "If you have not done so already, create an OpenAI account at https://platform.openai.com/overview."
    )
    os.environ["OPENAI_API_KEY"] = input("Secret key: ")

# from llm_blocks import block_factory


# def gpt_completion(template, model="gpt-4", chain=None, **inputs):
# 	"""Generic chat wrapper over the OpenAI API"""

# 	if chain is None:
# 		template_block = block_factory.get(
# 			type="template",
# 			template=template,
# 			model_name=model
# 		)
# 	try:
# 		resp = template_block(inputs)
# 	except openai.error.InvalidRequestError as e:
# 		raise ValueError(f"Caught OpenAI API error: {e}")
# 	return resp, chain


from openai import OpenAI

client = OpenAI()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)
