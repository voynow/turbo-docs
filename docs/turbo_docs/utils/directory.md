## function: read_text
#### args: path
This function reads the content of a text file given its path, while handling non-textual content by printing a message suggesting to add the file to the 'turbo_docs.toml' ignore list. It returns the file content as a string, replacing any non-textual content with Unicode replacement characters if necessary.

## function: collect_text_from_files
#### args: dir_path, pathspec
This function recursively collects text from all files in a given directory, excluding files that match a specified path pattern, and returns the text as a dictionary with file paths as keys.

## function: get_repo_text_dict
#### args: None
This function returns a dictionary containing all text in the current repository, while considering the 'turbo_docs.toml' configuration file for any ignored patterns. If the configuration file is not found, a warning is displayed and all files are included in the dictionary.

## function: convert_dict_to_string
#### args: file_dict
This function takes a dictionary containing file paths and their corresponding content and converts it into a single formatted string. Each file path is followed by a newline, its content, and two newlines, making the output easy to read and understand.

