# Turbo Docs 🚀

Welcome to Turbo Docs, the cutting-edge documentation generator that empowers developers to create beautiful README files and manage their documentation with ease. Whether you're a user looking to generate your project's documentation, or a contributor aiming to enhance this tool, Turbo Docs is crafted to elevate your project's visibility and collaboration to the next level.

## Table of Contents 📑

- [Installation](#installation)
- [Usage](#usage)
  - [Commands](#commands)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation 🛠️

Before you can start using Turbo Docs, ensure you have Python installed on your system. Turbo Docs is compatible with Python 3.6 and above.

To install Turbo Docs, simply clone the repo and install the required packages listed in `requirements.txt` by running the following commands:

```bash
git clone https://github.com/voynow/turbo-docs.git
cd turbo_docs
pip install -r requirements.txt
```

Alternatively, you can install Turbo Docs directly via `pip` with:

```bash
pip install turbo-docs
```

## Usage ⚙️

Turbo Docs is designed with a simple command-line interface, making it a breeze to generate your README or copy documentation to your clipboard.

### Commands

- **Generate README:**
  To generate a `README.md` file, navigate to your project directory and run:
  ```bash
  turbo_docs --readme
  ```
  This command will generate a `README.md` file based on the contents of your current directory, excluding files specified in the `.gitignore`.

- **Copy to Clipboard:**
  If you want to copy the contents of your current directory's documentation to the clipboard, use:
  ```bash
  turbo_docs --copy
  ```
  The text will be copied to the clipboard, and the number of tokens in the text will be displayed.

## Features ✨

- Markdown generation for `README.md` powered by OpenAI's language models
- Clipboard support for easy text manipulation
- Exclusion patterns to prevent certain files from being included in the documentation (supports `.gitignore` patterns)
- Command-line interface for straightforward usage

## Contributing 🤝

Contributions are what make the open-source community such a fantastic place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute to Turbo Docs:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements 🎉

- OpenAI for the language models that power the documentation generation
- The Python community for the invaluable libraries used in this project

---

Give your projects a boost with Turbo Docs and take your documentation to the next level! 🌟

