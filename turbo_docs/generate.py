import click
import os
from pathlib import Path
import pyperclip
from redbaron import RedBaron
from turbo_docs.utils import directory, openai_api, cli_options


def run_create_readme(text):
	"""
    Runs a create_readme operation with the given input string, writes the formatted and user-friendly output to README.md. Obstacles are handled by graceful error raising.
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
    Runs the create_readme_plus function which generates a README file from source code which summarizes the key logic of the code. Calls the openai_api to generate completion and then calls run_create_readme() to generate the README file.
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
    Runs a create_tests task for a given code file. This task calls the openai API to generate unit tests for the given code and writes the results to a test file.
    """
	print(f"(--create_tests) Generating unit tests for {test_file_path}")
	prompt = f"Generate unit tests for the following code:\n{file_content}"
	test_content = openai_api.gpt_completion_wrapper(prompt)
	with open(test_file_path, "w") as test_file:
		test_file.write(test_content)


def run_create_tests_helper(files):
	"""
    Create unit tests for a specified list of files.
    The tests will be created in the "tests" directory if it does not already exist.
    The file name for the test is in the format test_<filename>. The user will be prompted to create the test files if size and extension are valid. 
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


def clean_up_triple_quotes(s):
	"""
    Validate the given docstring so that the output inside the docstring is valid syntax.
    """
	if not s.startswith('"""'):
		while s.startswith('"'):
			s = s[1:]
		return clean_up_triple_quotes('"""' + s[1:])
	if not s.endswith('"""'):
		while s.endswith('"'):
			s = s[:-1]
		return clean_up_triple_quotes(s[:-1] + '"""')
	if '"""' in s[3:-3]:
		s_edit = s[3:-3].replace('"""', '\\"\\"\\"')
		return clean_up_triple_quotes(f'"""{s_edit}"""')
	return s

def format_docstring(s):
	"""
    Formats a provided docstring string to make it compliant to PEP 8 standards by adding '\"\"\"' to the beginning and end of the string and eliminating additional line breaks.
    """
	if not s.startswith('"""\n'):
		s = f'"""\n{s[3:]}'

	if not s.endswith('\n"""'):
		s = f'{s[:-3]}\n"""'
	
	while "\n\n" in s:
		s = s.replace("\n\n", "\n")
	return s


def run_create_docstring(files):
	"""
    Run create docstring to create proper docstrings for functions in a files dict.
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
				docstring_formatted = format_docstring(clean_up_triple_quotes(docstring))
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
    Generates various necessary assets for a project.
    The assets generated depend on the flags chosen when calling this function. 
    The assets generated include documents such as pyperclip, README.md, and tests; as 
    well as docstrings for each function in the project. 
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
