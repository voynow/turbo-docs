## function: readme
#### args: repo, model, template, narrative
The `readme` function is designed to generate a README.md file for the current repository. It allows the user to choose between GPT-3.5 Turbo and GPT-4 models and provides an option to override the default template. If a narrative is provided, it is appended to the template with a specific instruction to follow it at all costs. The function then calls the OpenAI API to generate the content of the README file based on the template and the chosen model. The generated content is then written to the README.md file in the current repository.

