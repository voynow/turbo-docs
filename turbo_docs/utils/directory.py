from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from pathlib import Path
import toml


def read_text(path: Path) -> str:
    """Assuming all non-textual files are in the turbo_docs.toml ignore list"""
    try:
        with open(path, "r") as file:
            return file.read()
        
    except UnicodeDecodeError:
        print(f"File {path} contains non-textual content. Add to 'turbo_docs.toml' if this file should be ignored.")
        with open(path, 'r', encoding='utf-8', errors='replace') as file:
            return file.read()
        
    except Exception as e:
        raise e


def collect_text_from_files(dir_path: Path, pathspec: PathSpec) -> dict:
    """recursively collect text from all files in a directory"""
    result = {}
    for path in dir_path.iterdir():
        if path.is_file():
            if not pathspec.match_file(str(path)):
                result[path] = read_text(path)
        elif path.is_dir():
            result.update(collect_text_from_files(path, pathspec))

    return result


def get_repo_text_dict():
    """Return a dictionary of all text in the current repo"""
    if not Path("turbo_docs.toml").exists():
        ignored_patterns = []
        print("Warning: 'turbo_docs.toml' not found. All files will be included.")
    else:
        config = toml.load("turbo_docs.toml")
        ignored_patterns = config.get("ignore", [])

    pathspec = PathSpec.from_lines(GitWildMatchPattern, ignored_patterns)
    return collect_text_from_files(Path("."), pathspec)


def convert_dict_to_string(file_dict: dict):
    text = ""
    for path, content in file_dict.items():
        text += f"{path}:\n\n{content}\n\n"
    return text
