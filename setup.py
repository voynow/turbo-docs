from setuptools import find_packages, setup

setup(
    name="turbo_docs",
    version="1.1.2",
    packages=find_packages(),
    install_requires=[
        "openai>=1.3.6",
        "click",
        "pyperclip",
        "toml",
        "pathspec",
        "tiktoken",
    ],
    entry_points={
        "console_scripts": ["turbo_docs=turbo_docs.generate:driver"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
)

# python setup.py sdist bdist_wheel
# twine upload dist/*
