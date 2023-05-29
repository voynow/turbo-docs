import fnmatch
import os
from pathlib import Path
import toml
from typing import List, Dict


def read_exclude_config():
    """
    Reads the exclude.toml file and returns the exclude list.
    """
    try:
        with open("exclude.toml", "r") as config_file:
            config_data = toml.load(config_file)
    except FileNotFoundError:
        raise ValueError("exclude.toml file is missing.")

    exclude = config_data.get("exclude", [])

    return exclude


def ignored_files_init() -> List[str]:
    """
    Initialize a list of files to be ignored in directory.
    """
    ignore_files = ["README.md", "tests", "setup.py"]
    for file in os.listdir():
        if file[0] == ".":
            ignore_files.append(file)
    return ignore_files


def read_gitignore() -> List[str]:
    """
    Reads in a .gitignore file and returns a list of ignored files.
    """
    ignore_files = []
    try:
        with open(".gitignore", "r") as gitignore:
            for line in gitignore:
                ignore_files.append(line.strip())
    except FileNotFoundError:
        raise ValueError(
            ".gitignore file required for excluding files from documentation generation"
        )
    return ignore_files


def get_ignore_list() -> List[str]:
    """
    Returns a list of files to be ignored in directory.
    """
    ignore_files = ignored_files_init()
    ignore_files.extend(read_exclude_config())
    ignore_files.extend(read_gitignore())
    return ignore_files


def matches_ignore_pattern(filepath: str, ignore_patterns: List[str]) -> bool:
    """
    Check if the given file path matches any of the ignore patterns.
    """
    filepath_parts = filepath.split(os.sep)
    return any(
        fnmatch.fnmatch(filepath, pattern)
        or any(fnmatch.fnmatch(part, pattern) for part in filepath_parts)
        for pattern in ignore_patterns
    )

def read_file_content(filepath: str) -> str:
    """
    Read the content of the file at the given path.
    """
    with open(filepath, "r") as f:
        content = f.read()
    return content.replace(" " * 4, "\t").strip()


def get_files() -> Dict:
    """
    Retrieve all text from files, excluding filepaths specified by exclude.toml and .gitignore.
    """
    files_dict = {}
    ignore_patterns = get_ignore_list()

    # Iterate over files
    for root, _, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root, file)

            # If file path or its parent directories match any of the ignore patterns
            if matches_ignore_pattern(filepath, ignore_patterns):
                continue

            # If not in ignore, collect file text
            content = read_file_content(filepath)
            if content:
                files_dict[filepath] = content

    return files_dict
