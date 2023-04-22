import os
from turbo_docs.utils import openai_api


def readme(text):
	"""
    Generate a formatted & user-friendly README.md file utilizing OpenAI API.
    """
	readme = "README.md"
	prompt = f"Create a formatted & user-friendly readme.md from the following:\n\n{text}"
	response = openai_api.gpt_completion_wrapper(prompt)
	try:
		with open(readme, "w") as readme_file:
			readme_file.write(response)
	except PermissionError as e:
		raise PermissionError(
			f"{e}\nYour device is blocking the above operation. Please remove {readme} and try again.")
	print(f"(--readme) Generated README.md")


def readme_large_repo(files):
	"""
    Read and create README from large repo files
    """
	responses = {}
	for file_path, file_content in files.items():
		if os.stat(file_path).st_size and file_path.split(".")[1]:
			print(f"(--readme_plus) Summarizing {file_path}")
			prompt = f"Create a README summarizing the following code, especially maintaining key logic:\n{file_content}"
			responses[file_path] = openai_api.gpt_completion_wrapper(prompt)

	flatmap = "\n\n\n".join(
		[f"{file_path}:\n{summary}" for file_path, summary in responses.items()])
	readme(flatmap)
	print(f"(--readme_plus) Generated README.md")
