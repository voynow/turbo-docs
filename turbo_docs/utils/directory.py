from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from pathlib import Path
import toml

def read_text(path: Path) -> str:
    """ 
    Read the text from a file and return it as a string. We are assuming that
    all non-textual files are in the ignore list in 'turbo_docs.toml'.
    """
    try:
        with open(path, 'r') as file:
            return f'filename: {path.name}\npath: {path}\n\n{file.read()}\n\n'
    except UnicodeDecodeError:
        raise ValueError(f"File {path} contains non-textual content. Please add it to the ignore list in 'turbo_docs.toml'.")
    except Exception as e:
        raise e

def collect_text_from_files(dir_path: Path, pathspec: PathSpec) -> str:
    """
    Traverse through all files in a directory (and its subdirectories), 
    collect the text from each file and return it as a single string.
    """
    result = ''
    
    for path in dir_path.iterdir():
        if path.is_file():
            if not pathspec.match_file(str(path)):
                result += read_text(path)
        elif path.is_dir():
            result += collect_text_from_files(path, pathspec)

    return result


def get_repo_text():
    """
    Recursively get all text from files in the current directory, ignoring files 
    specified in the exclude list in turbo_docs.toml

    Text returned in the following format for each document:
    filename: <filename>
    path: <path>
    <text>
    ...
    """
    if not Path('turbo_docs.toml').exists():
        ignored_patterns = []
        print("Warning: 'turbo_docs.toml' not found. All files will be included.")
    else:
        config = toml.load('turbo_docs.toml')
        ignored_patterns = config.get('ignore', [])
    print(f"Ignoring files and folders matching the following patterns: {ignored_patterns}")

    pathspec = PathSpec.from_lines(GitWildMatchPattern, ignored_patterns)
    text = collect_text_from_files(Path("."), pathspec)

    return text