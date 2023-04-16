import json
import os
from pathlib import Path
from typing import List, Dict

def ignored_files_init() -> List[str]:
	"""
    Initialize a list with files that have to be ignored. Files starting with "." will automaticly be included to the list.
    """
	ignored_files = ["README.md", "tests"]
	for file in os.listdir():
		if file[0] == ".":
			ignored_files.append(file)
	return ignored_files

def read_gitignore() -> List[str]:
	"""
    Reads the .gitignore file and returns a list of the excluded files for documentation generation. Raises a ValueError if the .gitignore file is not found.
    """
	ignore_files = ignored_files_init()
	try:
		with open(".gitignore", "r") as gitignore:
			for line in gitignore:
				ignore_files.append(line.strip())
	except FileNotFoundError:
		raise ValueError(".gitignore file required for excluding files from documentation generation")
	return ignore_files

def ignore_filepath(filepath: str, ignore_files: List[str]) -> bool:
	"""
    Checks if any parts of a filepath are contained in a list of items to ignore.
    """
	for part in Path(filepath).parts:
		if part in ignore_files:
			return True
	return False

def get_files() -> Dict:
	"""
    Retrieve the text content from all files in the current directory and its subdirectories and return them in a dictionary.
    """
	files_dict = {}
	ignore_files = read_gitignore()

	# Iterate over files
	for root, _, files in os.walk("."):
		for file in files:
			filepath = os.path.join(root, file).replace(".\\", "")

			# If not in ignore, collect file text
			if not ignore_filepath(filepath, ignore_files):
				with open(filepath, "r") as f:
					content = f.read()
				files_dict[filepath] = content.replace(" " * 4, "\t").strip()
	return files_dict
