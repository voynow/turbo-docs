from setuptools import setup, find_packages

setup(
    name="my-package",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "openai",
        "click",
        "pyperclip",
    ],
    entry_points={
        "console_scripts": [
            "my-package=my_package.generate:driver"
        ],
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
)
