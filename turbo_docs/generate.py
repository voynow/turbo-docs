import click
import os
from pathlib import Path
import pyperclip
from redbaron import RedBaron
from turbo_docs.utils import directory, openai_api, cli_options


def run_create_readme(text):
	"""
    Create a formatted and user-friendly README.md file using OpenAI API.
    """
	readme = "README.md"
	prompt = f"Create a formatted & user-friendly readme.md from the following:\n\n{text}"
	response = openai_api.gpt_completion_wrapper(prompt)
	try:
		with open(readme, "w") as readme_file:
			readme_file.write(response)
	except PermissionError as e:
		raise PermissionError(f"{e}\nYour device is blocking the above operation. Please remove {readme} and try again.")
	print(f"(--create_readme) Generated README.md")




def run_create_readme_plus(files):
	"""
    Create and generate a README.md summarizing code snippets from various files. The README.md will contain each file's summary with the respective file's name at the start of the summary. It will also maintain key logic from the respective code snippets.
    """
	responses = {}
	for file_path, file_content in files.items():
		if os.stat(file_path).st_size and file_path.split(".")[1]:
			print(f"(--create_readme_plus) Summarizing {file_path}")
			prompt = f"Create a README summarizing the following code, especially maintaining key logic:\n{file_content}"
			responses[file_path] = openai_api.gpt_completion_wrapper(prompt)

	flatmap = "\n\n\n".join([f"{file_path}:\n{summary}" for file_path, summary in responses.items()])
	run_create_readme(flatmap)
	print(f"(--create_readme_plus) Generated README.md")


def run_create_tests(test_file_path, file_content):
	"""
    Create unit tests from a given file using OpenAI's GPT-3 API. 
    This function generates unit tests for the existing code in a given file, prompting the user for code content and writing the generated output to a specified path. 
    """
	print(f"(--create_tests) Generating unit tests for {test_file_path}")
	prompt = f"Generate unit tests for the following code:\n{file_content}"
	test_content = openai_api.gpt_completion_wrapper(prompt)
	with open(test_file_path, "w") as test_file:
		test_file.write(test_content)


def run_create_tests_helper(files):
	"""
    Helper function for creating uni tests for source files.
    Makes sure a valid size file and file format exist, and then prompts the user to confirm the creation of tests. If user confirms, runs run_create_tests function.
    """
	tests_dir = "tests"
	Path(tests_dir).mkdir(exist_ok=True)

	for file_path, file_content in files.items():
		if os.stat(file_path).st_size and file_path.split(".")[1]:
			test_file_name = f"test_{os.path.basename(file_path)}"
			test_file_path = os.path.join(tests_dir, test_file_name)
	
			resp = input(f"Would you like to create unit tests for {test_file_name} (Y/n):")
			if resp != "n" and resp != "N":
				run_create_tests(test_file_path, file_content)


def is_valid_docstring(s):
	"""
    Checks if a given string is a valid docstring
    """
	print(s)
	if not s.startswith('"""') or not s.endswith('"""'):
		return False
	return True

def format_docstring(s):
	"""
    Format the given docstring so it meets the PEP 8 guidelines and raise a ValueError if the string is not valid.
    """
	if not is_valid_docstring(s):
		raise ValueError("Invalid docstring format")
	
	if not s.startswith('"""\n'):
		s = f'"""\n{s[3:]}'

	if not s.endswith('\n"""'):
		s = f'{s[:-3]}\n"""'
	
	while "\n\n" in s:
		s = s.replace("\n\n", "\n")
	return s


def run_create_docstring(files):
	"""
    Create a professional docstring for a python function
    This function will generate a professional docstring for a python function from given arguments and then write it back into the file. 
    """
	for file_path, content in files.items():
		if os.stat(file_path).st_size and file_path.split(".")[1]:

			red = RedBaron(content)
			for func in red.find_all("def"):
				func_name = func.name
				print(f"(--create_docstring) Generating docstring for {file_path}.{func_name}")

				# Remove existing docstring before creating the prompt
				if func.value[0].type == "string":
					func.value.pop(0)

				prompt = f'Generate a professional docstring for the following Python function. Do not include argurments and returns.\n\n{func.dumps()}'
				docstring = openai_api.gpt_completion_wrapper(prompt)
				docstring_formatted = format_docstring(docstring)
				func.value.insert(0, docstring_formatted)

			# Write the modified code back to the file
			with open(file_path, "w") as f:
				f.write(red.dumps())


@click.command()
@cli_options.copy
@cli_options.create_readme
@cli_options.create_readme_plus
@cli_options.create_tests
@cli_options.create_docstring
def driver(copy: bool, create_readme: bool, create_readme_plus: bool, create_tests: bool, create_docstring: bool) -> None:
	"""
    A command line utility allowing for generation of README.md, tests.md, and docstrings for functions in a project directory
    """
	files = directory.get_files()
	dir_text = "\n\n".join([f"{name}:\n\n{content}" for name, content in files.items()])

	# Copy directory text to clipboard if specified
	if copy:
		pyperclip.copy(dir_text)
		print("(--copy) Directory text copied to clipboard")

	# Generate README.md file if specified
	if create_readme:
		run_create_readme(dir_text)

	# Generate docs.md file if specified
	if create_readme_plus:
		run_create_readme_plus(files)

	# Generate unit tests for each code file if specified
	if create_tests:
		run_create_tests_helper(files)

	# Generate docstring for each function if specified
	if create_docstring:
		run_create_docstring(files)











if __name__ == '__main__':
	driver()
