
import os
from pathlib import Path
from turbo_docs.utils import openai_api


def create_tests(test_file_path, file_content):
	"""
    Run create tests to generate unit tests for a specified file path.
    """
	print(f"(--tests) Generating unit tests for {test_file_path}")
	prompt = f"Generate unit tests for the following code:\n{file_content}"
	test_content = openai_api.gpt_completion_wrapper(prompt)
	with open(test_file_path, "w") as test_file:
		test_file.write(test_content)


def unit_tests(files):
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
				create_tests(test_file_path, file_content)