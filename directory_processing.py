import os
from pathlib import Path

def read_gitignore():
    """
    """
    ignored_files = set([file for file in os.listdir() if file[0] == "."])
    try:
        with open(".gitignore", "r") as gitignore:
            for line in gitignore:
                ignored_files.add(line.strip())
    except FileNotFoundError:
        raise ValueError(".gitignore file required for excluding files from documentation generation")
    return ignored_files

def ignore_filepath(filepath, ignored_files):
    """
    """
    for part in Path(filepath).parts:
        if part in ignored_files:
            return True
    return False

def prepare_files_list(ignored_files):
    """
    """
    file_list = []
    for root, _, files in os.walk("."):
        for file in files:
            filepath = os.path.join(root.replace(".\\", ""), file)
            if not ignore_filepath(filepath, ignored_files):
                with open(filepath, "r") as f:
                    content = f.read()
                file_list.append({"name": filepath, "content": content})
    return file_list
