import json
import os
from pathlib import Path


def ignored_files_init():
    """
    """
    ignored_files = []
    for file in os.listdir():
        if file[0] == ".":
            ignored_files.append(file)
    ignored_files.append("README.md")
    return ignored_files

def read_gitignore():
    """
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
    """
    for part in Path(filepath).parts:
        if part in ignore_files:
            return True
    return False


def read_file(file):
    file_open = file.read()
    for r in [(" " * 4, "\t"), ("\n\n", "\n")]:
        file_open = file_open.replace(*r)
    return file_open


def get_directory_text():
    """
    """
    dir_text = ""
    ignore_files = read_gitignore()

    for root, _, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root.replace(".\\", ""), file)

            # if not in ignore collect file text
            if not ignore_filepath(filepath, ignore_files):
                with open(filepath, "r") as f:
                    content = read_file(f)
                dir_text += f"{filepath}:\n\n{content}\n\n"
    
    return dir_text
