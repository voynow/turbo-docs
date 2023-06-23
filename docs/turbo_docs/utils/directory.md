## function: read_text
#### args: path
Reads the contents of a file located at the given path. If the file contains non-textual content, it prints a warning message and attempts to read the file with the 'utf-8' encoding, replacing any decoding errors.

## function: collect_text_from_files
#### args: dir_path, pathspec
Recursively collects text from all files in a directory.

## function: get_repo_text_dict
#### args: None
Return a dictionary of all text in the current repository. If the file 'turbo_docs.toml' does not exist, all files will be included. If the file does exist, it will be loaded and any patterns specified in the 'ignore' key will be ignored. The function will print the patterns that are being ignored and then collect the text from all files in the repository that do not match the ignored patterns.

## function: remove_readme
#### args: file_dict
Removes any key-value pairs from the input dictionary `file_dict` where the key ends with 'README.md'. Returns a new dictionary with the remaining key-value pairs.

## function: convert_dict_to_string
#### args: file_dict
Converts a dictionary of file paths and contents into a single string. Each file path is followed by a colon and two newlines, and then the content of the file. The resulting string is returned.

