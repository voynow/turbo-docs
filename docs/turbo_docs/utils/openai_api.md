## function: gpt_completion
#### args: template, model, chain, **inputs
This function serves as a generic chat wrapper for the OpenAI API, utilizing a specified template and model to generate a response based on the provided inputs. It returns the generated response and the chain object, while handling any InvalidRequestError exceptions that may occur.

