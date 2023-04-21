
import click
from git import Repo
from turbo_docs.utils import openai_api


def get_commit_prompt(repo, files):
    """
    Generate a prompt for the user to generate a commit message.
    """
    diff = repo.git.diff("--cached", "HEAD")

    # Check if there are any changes
    if not diff.strip():
        print("(--generate_commit) No changes detected, commit aborted.")
        return None

    diff_files_string = repo.git.diff("--name-status",  "--cached", "HEAD")
    diff_files = [file.split("\t")[1].replace("/", "\\")
                  for file in diff_files_string.split("\n")]

    diff_files = {file: files[file] for file in diff_files}
    context = "\n\n".join(
        [f"{name}:\n\n{content}" for name, content in diff_files.items()])

    prompt = f"Here is some relevant code:\n\n{context}\n\n"
    prompt += f"Generate a useful, concise, commit message for the following changes:\n\n{diff}\n\n"
    return prompt


def commit(files):
    """
    Generate a commit message and execute the commit based on the changed files.
    """
    repo = Repo()
    repo.git.add(".")

    # Generate prompt for commit message
    prompt = get_commit_prompt(repo, files)
    if prompt is None:
        return

    # Generate commit message with user confirmation
    resp = "n"
    while resp == "n" or resp == "N":
        commit_message = openai_api.gpt_completion_wrapper(prompt)
        if ":" in commit_message:
            commit_message = commit_message.split(":")[1]
        if "\n" in commit_message:
            commit_message = commit_message.replace("\n", "")
        resp = input(
            f"Here is your commit message: {commit_message}\nWould you like to commit? (Y/n)")

    # Commit changes
    try:
        repo.git.commit("-m", commit_message)
        print(
            f"(--generate_commit) Commit executed with message: {commit_message}")
    except Exception as e:
        print(f"(--generate_commit) Failed to execute the commit. Error: {e}")
