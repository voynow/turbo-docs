import click
import os
from pathlib import Path
import pyperclip
from redbaron import RedBaron
import textwrap
from turbo_docs.utils import directory, openai_api, cli_options


def run_create_readme(text):
	"""
    Generates a README.md file based on a provided text using the OpenAI API and
    raises a PermissionError if the file is blocked by the device.
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
    Creates a README for provided files by computing summaries of the code, and then
    running create_readme to generate a README.md file.
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
    Run create tests to generate unit tests for a specified file path.
    """
	print(f"(--create_tests) Generating unit tests for {test_file_path}")
	prompt = f"Generate unit tests for the following code:\n{file_content}"
	test_content = openai_api.gpt_completion_wrapper(prompt)
	with open(test_file_path, "w") as test_file:
		test_file.write(test_content)


def run_create_tests_helper(files):
	"""
    Create test for each file in the "files" dictionary, prompting the user if
    they would like to create unit tests for the file.
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


def wrap_text(text):
	"""
    Wrap the given text to 80 characters.
    """
	line_length = 80

	# wrap text to 80 chars
	text = " ".join(text.split("\n"))
	wrapped_text = '\n'.join(textwrap.wrap(text, line_length, break_long_words=False))

	return wrapped_text


def format_docstring(s):
	"""
    Format a docstring to fit standard rules.
    """
	if s.startswith('"') or s.startswith('\n'):
		return format_docstring(s[1:])

	if s.endswith('"') or s.endswith('\n'):
		return format_docstring(s[:-1])

	if "\n\n" in s:
		return format_docstring(s.replace("\n\n", "\n"))

	if '"""' in s:
		return format_docstring(s.replace('"""', '\\"\\"\\"'))

	wrapped_text = wrap_text(s.strip())
	return  f'"""\n{wrapped_text}\n"""'



def run_create_docstring(files):
	"""
    Generate a docstring for a function in a Python file.
    """
	for file_path, content in files.items():
		if file_path.split(".")[1]:

			red = RedBaron(content)
			functions = red.find_all("def")
			if functions:
				for func in functions:
					func_name = func.name
					print(f"(--create_docstring) Generating docstring for {file_path}.{func_name}")

					# Remove existing docstring before creating the prompt
					if func.value[0].type == "string":
						func.value.pop(0)

					prompt = f'Generate a concise docstring for the following Python function. Do not include argurments and returns.\n\n{func.dumps()}'
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
    Processes the specified command line arguments and calls functions 
	accordingly, such as copying directory text to the clipboard, 
	generating README.md files, generating tests, or generating docstring.
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
