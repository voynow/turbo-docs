import json
import os
from pathlib import Path

def ignored_files_init():
    """
    Initialize a list of ignored files and including README.md, dir_text.txt, etc.
    :return: list, The list of ignored files.
    """
    ignored_files = ["README.md", "dir_text.txt"]
    for file in os.listdir():
        if file[0] == ".":
            ignored_files.append(file)
    return ignored_files

def read_gitignore():
    """
    Read .gitignore file and return the list of ignored files.
    :return: list, The list of ignored files.
    """
    ignore_files = ignored_files_init()
    try:
        with open(".gitignore", "r") as gitignore:
            for line in gitignore:
                ignore_files.append(line.strip())
    except FileNotFoundError:
        raise ValueError(".gitignore file required for excluding files from documentation generation")
    return ignore_files

def ignore_filepath(filepath, ignore_files):
    """
    Check if a filepath should be ignored based on the ignore_files list.
    :param filepath: str, The filepath to check.
    :param ignore_files: list, The list of ignored files.
    :return: bool, True if the filepath should be ignored, False otherwise.
    """
    for part in Path(filepath).parts:
        if part in ignore_files:
            return True
    return False

def read_file(file):
    """
    Read a file and replace multiple spaces with tabs and consecutive newlines with a single newline.
    :param file: file object, The file to read.
    :return: str, The formatted content of the file.
    """
    file_open = file.read()
    for r in [(" " * 4, "\t"), ("\n\n", "\n")]:
        file_open = file_open.replace(*r)
    return file_open

def get_directory_text():
    """
    Get the text representation of the current directory, excluding ignored files.
    :return: str, The text representation of the directory.
    """
    dir_text = ""
    ignore_files = read_gitignore()

    # iterate over files
    for root, _, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root.replace(".\\", ""), file)

            # if not in ignore collect file text
            if not ignore_filepath(filepath, ignore_files):
                with open(filepath, "r") as f:
                    content = read_file(f)
                dir_text += f"{filepath}:\n\n{content}\n\n"
    
    return dir_text
