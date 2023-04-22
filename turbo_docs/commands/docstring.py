from redbaron import RedBaron
import textwrap
from turbo_docs.utils import openai_api


def wrap_text(text):
    """
    Wrap a given string of text to 80 characters
    """
    line_length = 80

    # wrap text to 80 chars
    text = " ".join(text.split("\n"))
    wrapped_text = '\n'.join(textwrap.wrap(
        text, line_length, break_long_words=False))

    return wrapped_text


def format_docstring(s):
    """
    Apply specific formatting to docstring
    """
    if s.startswith('"') or s.startswith('\n'):
        return format_docstring(s[1:])

    if s.endswith('"') or s.endswith('\n'):
        return format_docstring(s[:-1])

    if "\n\n" in s:
        return format_docstring(s.replace("\n\n", "\n"))

    if '"""' in s:
        return format_docstring(s.replace('"""', '\\"\\"\\"'))

    wrapped_text = wrap_text(s.strip())
    return f'"""\n{wrapped_text}\n"""'


def docstring(files):
    """
    Generate docstrings for Python functions in specified files using OpenAI API.
    """
    for file_path, content in files.items():
        if file_path.split(".")[1]:

            red = RedBaron(content)
            functions = red.find_all("def")
            if functions:
                for func in functions:
                    func_name = func.name
                    print(
                        f"(--docstring) Generating docstring for {file_path}.{func_name}")

                    # Remove existing docstring before creating the prompt
                    if func.value[0].type == "string":
                        func.value.pop(0)

                    prompt = f'Generate a concise docstring for the following Python function. Do not include argurments and returns.\n\n{func.dumps()}'
                    docstring = openai_api.gpt_completion_wrapper(prompt)
                    docstring_formatted = format_docstring(docstring)
                    func.value.insert(0, docstring_formatted)

                # Write the modified code back to the file
                with open(file_path, "w") as f:
                    f.write(red.dumps().replace("\t", " " * 4))
