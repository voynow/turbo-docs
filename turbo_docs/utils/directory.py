import json
import os
from pathlib import Path
from typing import List, Dict


def ignored_files_init() -> List[str]:
    """
    Initialize the list of files to be ignored
    """
    ignored_files = ["README.md", "tests", "setup.py"]
    for file in os.listdir():
        if file[0] == ".":
            ignored_files.append(file)
    return ignored_files


def read_gitignore() -> List[str]:
    """
    Read .gitignore file and return a list of ignored files.
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
    Checks if a filepath includes a particular file or folder to ignore.
    """
    for part in Path(filepath).parts:
        if part in ignore_files:
            return True
    return False


def get_files() -> Dict:
    """
    Retrieve files from directory ignoring items from .gitignore and formatting tab
    indentation.
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
