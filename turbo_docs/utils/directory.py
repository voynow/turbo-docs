from pathlib import Path
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
import toml


def read_text(path: Path) -> str:
    """Assuming all non-textual files are in the pyproject.toml ignore list"""
    try:
        with open(path, "r") as file:
            return file.read()

    except UnicodeDecodeError:
        with open(path, "r", encoding="utf-8", errors="replace") as file:
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
    """Create a pyproject.toml with default ignore patterns"""
    print("Creating default pyproject.toml with entry for turbo_docs")
    configs = toml.load(toml_path) if toml_path.exists() else {}

    if "tool" not in configs:
        configs["tool"] = {}
    configs["tool"]["turbo_docs"] = {
        "ignore": [
            "pyproject.toml",
            "__pycache__",
            "venv",
            "build",
            "dist",
            "*.egg-info",
            ".git",
            ".env",
        ]
    }

    with open(toml_path, "w") as toml_file:
        toml.dump(configs, toml_file)


def get_repo_text_dict():
    toml_path = Path("pyproject.toml")

    if (
        not toml_path.exists()
        or "tool" not in toml.load(toml_path)
        or "turbo_docs" not in toml.load(toml_path)["tool"]
    ):
        create_default_config(toml_path)

    config = toml.load(toml_path)["tool"]["turbo_docs"]

    ignored_patterns = config.get("ignore", [])
    print(f"Ignoring the following patterns: {ignored_patterns}")

    pathspec = PathSpec.from_lines(GitWildMatchPattern, ignored_patterns)
    return collect_text_from_files(Path("."), pathspec)


def convert_dict_to_string(file_dict: dict):
    text = ""
    for path, content in file_dict.items():
        text += f"{path}:\n\n{content}\n\n"
    return text
