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


def create_default_config(toml_path):
    """Create a turbo_docs.toml with default ignore patterns"""
    print("No turbo_docs.toml configuration file found. Creating a default one.")
    default_config = {
        "ignore": [
            "turbo_docs.toml",
            "__pycache__",
            "venv",
            "build",
            "dist",
            "*.egg-info",
            ".git",
        ]
    }
    with open(toml_path, "w") as toml_file:
        toml.dump(default_config, toml_file)    


def get_repo_text_dict():
    """Return a dictionary of all text in the current repo"""
    toml_path = Path("turbo_docs.toml")

    # create default and load config
    if not toml_path.exists():
        create_default_config(toml_path)
    config = toml.load(toml_path)

    # create default if ignore not in config and reload
    if "ignore" not in config:
        create_default_config(toml_path)
        config = toml.load(toml_path)

    ignored_patterns = config.get("ignore", [])
    print(f"Ignoring the following patterns: {ignored_patterns}")
    pathspec = PathSpec.from_lines(GitWildMatchPattern, ignored_patterns)
    return collect_text_from_files(Path("."), pathspec)


def convert_dict_to_string(file_dict: dict):
    text = ""
    for path, content in file_dict.items():
        text += f"{path}:\n\n{content}\n\n"
    return text
