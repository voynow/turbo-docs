## function: gpt_completion
#### args: template, model, chain, **inputs
The `gpt_completion` function is a generic chat wrapper over the OpenAI API. It uses a given template and model to generate a response based on the provided inputs. If no chain is provided, it creates a new one using the template and model. It handles OpenAI API errors gracefully by catching them and raising a more descriptive ValueError. The function returns the generated response and the chain used.

