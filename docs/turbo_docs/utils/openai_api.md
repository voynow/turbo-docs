## function: gpt_completion
#### args: template, inputs, model='gpt-4'
Genneric chat wrapper over the OpenAI API. This function takes in a template, inputs, and an optional model name. It prints the model being used and displays warnings if the model is 'gpt-4'. It then tries to generate a response using the OpenAI API and returns the generated text. If there is an error with the API request, it catches the error and prints the error message.

