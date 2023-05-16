import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="parse_pip_search",
    version="0.0.1",
    author="Martí Climent",
    author_email="marticlilop@gmail.com",
    url="https://github.com/marticliment/parseable_pip_search",
    description="A parseable command-line package to search like pip used to, via PyPi",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    install_requires=["bs4", "requests", "rich"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.2",
    entry_points={
        "console_scripts": [
            "parse_pip_search=parse_pip_search.__main__:main",
        ],
    },
)
