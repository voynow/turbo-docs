import json
import os
from pathlib import Path
from typing import List, Dict


def ignored_files_init() -> List[str]:
    """
    Create a list of files to be ignored when searching a directory.
    """
    ignored_files = ["README.md", "tests", "setup.py"]
    for file in os.listdir():
        if file[0] == ".":
            ignored_files.append(file)
    return ignored_files


def read_gitignore() -> List[str]:
    """
    Reads and returns contents of .gitignore file into a list of strings.
    """
    ignore_files = ignored_files_init()
    try:
        with open(".gitignore", "r") as gitignore:
            for line in gitignore:
                ignore_files.append(line.strip())
    except FileNotFoundError:
        raise ValueError(
            ".gitignore file required for excluding files from documentation generation")
    return ignore_files


def ignore_filepath(filepath: str, ignore_files: List[str]) -> bool:
    """
    Return True if a given filepath contains any part specified in a list of
    strings, else return False.
    """
    for part in Path(filepath).parts:
        if part in ignore_files:
            return True
    return False


def get_files() -> Dict:
    """
    Retrieve the contents of all files in the current directory, excluding those
    specified in the ignore file.
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
                if content:
                    files_dict[filepath] = content.replace(
                        " " * 4, "\t").strip()
    return files_dict
