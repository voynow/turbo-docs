import os
from turbo_docs.utils import openai_api


def readme(text):
    """
    Generate a formatted and user-friendly README.md using openAI API, or use an
    alternative command if unable to generate.
    """
    readme = "README.md"
    prompt = f"Create a formatted & user-friendly readme.md from the following:\n\n{text}"
    response = openai_api.gpt_completion_error_handler(prompt)
    if response is None:
        print("Unable to generate README.md, try the folling command instead: turbo_docs --readme_large_repo")
    else:
        with open(readme, "w") as readme_file:
            readme_file.write(response)
        print(f"(--readme) Generated README.md")


def readme_large_repo(files):
    """
    return flatmap Create a summarization for files, soliciting user input if the
    summary is satisfactory.
    """
    responses = {}
    for file_path, file_content in files.items():
        if os.stat(file_path).st_size and file_path.split(".")[1]:
            print(f"(--readme_large_repo) Summarizing {file_path}")
            prompt = f"Condense the following information, minimize the amount of tokens used and maximize the preservation of information:\n{file_content}"
            responses[file_path] = openai_api.gpt_completion_wrapper(prompt)
    flatmap = "\n\n\n".join([f"{file_path}:\n{summary}" for file_path, summary in responses.items()])

    user_acceptance = False
    while not user_acceptance:
        readme(flatmap)
        resp = input("(--readme_plus) Check your README.md, want to generate a new one? (Y/n):")
        if resp != "y" and resp != "Y":
            user_acceptance = True
