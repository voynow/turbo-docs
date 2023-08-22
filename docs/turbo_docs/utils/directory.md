## function: read_text
#### args: path
The `read_text` function reads a text file from a given path and returns its content as a string. It assumes that all non-textual files are in the turbo_docs.toml ignore list. If the file cannot be read due to a UnicodeDecodeError, it tries to read the file again with UTF-8 encoding, replacing any errors. If any other exception occurs, it raises the exception.

## function: collect_text_from_files
#### args: dir_path, pathspec
The function `collect_text_from_files` is designed to recursively collect text from all files in a specified directory. It uses a path specification to filter out files that do not match the given pattern. The function returns a dictionary where the keys are the paths of the files and the values are the text content of the files. This function is particularly useful when you need to extract text from a large number of files in a directory structure.

## function: create_default_config
#### args: toml_path
The function `create_default_config` is used to create a default configuration file named 'turbo_docs.toml' with predefined ignore patterns. If the configuration file is not found, it prints a message and creates a new one at the specified path. The function is particularly useful in setting up a new project or resetting the configuration to its default state.

## function: get_repo_text_dict
#### args: None
This function returns a dictionary containing all the text in the current repository. It checks for a configuration file and creates a default one if it doesn't exist. The function also handles ignored patterns specified in the configuration, ensuring that certain files or directories are excluded from the text collection process.

## function: convert_dict_to_string
#### args: file_dict
This function takes a dictionary where the keys are file paths and the values are file contents, and converts it into a single string. Each key-value pair is separated by a newline character, with the key (file path) followed by its corresponding value (file content). This is particularly useful for creating a readable and organized string representation of multiple files and their contents.

