import io
from setuptools import (
    setup,
    find_packages,
)  # pylint: disable=no-name-in-module,import-error


def dependencies(file):
    with open(file) as f:
        return f.read().splitlines()


with io.open("README.md", encoding="utf-8") as infile:
    long_description = infile.read()

setup(
    name="halo",
    packages=find_packages(exclude=("tests", "examples", "art")),
    version="0.0.32",
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
    ],
    python_requires=">=3.11",
    description="Beautiful terminal spinners in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Manraj Singh",
    author_email="manrajsinghgrover@gmail.com",
    url="https://github.com/manrajgrover/halo",
    keywords=[
        "console",
        "loading",
        "indicator",
        "progress",
        "cli",
        "spinner",
        "spinners",
        "terminal",
        "term",
        "busy",
        "wait",
        "idle",
    ],
    install_requires=dependencies("requirements.txt"),
    tests_require=dependencies("requirements-dev.txt"),
    include_package_data=True,
    extras_require={
        "ipython": [
            "IPython>=8.12.3",
            "ipywidgets>=8.1.3",
        ]
    },
)
