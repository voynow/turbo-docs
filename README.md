# Turbo Docs 🚀

Turbo Docs is a powerful Python tool that helps developers generate high-quality README.md files for their repositories. It uses OpenAI's GPT-3.5 Turbo and GPT-4 models to create well-structured and informative documentation.

## Why Turbo Docs? 🤔

Writing a good README.md file is essential for any software project, as it provides an overview of the project, its purpose, and how to use it. However, creating a comprehensive and well-structured README.md can be time-consuming. Turbo Docs automates this process, allowing developers to focus on writing code while ensuring their documentation is up-to-date and professional.

## Table of Contents 📚

- [Installation](#installation)
- [Usage](#usage)
  - [Generate README.md](#generate-readmemd)
  - [Copy Directory Text](#copy-directory-text)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Installation 💻

To install Turbo Docs, simply run the following command:

```bash
pip install turbo_docs
```

## Usage 🛠️

### Generate README.md 📝

To generate a README.md file for your repository, navigate to the root directory of your project and run the following command:

```bash
turbo_docs --readme
```

By default, Turbo Docs uses the GPT-4 model. To use the GPT-3.5 Turbo model instead, add the `--gpt3` flag:

```bash
turbo_docs --readme --gpt3
```

### Copy Directory Text 📋

To copy the text from all files in the current directory to your clipboard, run the following command:

```bash
turbo_docs --copy
```

This can be useful when working with ChatGPT.

## Requirements 📦

Turbo Docs requires the following packages:

- requests
- openai
- llm-blocks
- click
- pyperclip
- redbaron
- gitpython
- toml
- pathspec

These dependencies are automatically installed when you install Turbo Docs using pip.

## Contributing 🤝

Contributions are welcome! If you'd like to improve Turbo Docs, please feel free to submit a pull request or open an issue on GitHub.

## License 📄

Turbo Docs is released under the MIT License. See [LICENSE](LICENSE) for more information.