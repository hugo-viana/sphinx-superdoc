#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""setup module."""

import os

from setuptools import find_packages, setup


# Extract the requirements from the requirements.txt file.
base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_dir, "README.md")) as f:
    readme = f.read()


setup(
    name="sphinx-superdoc",
    version="0.1.0",
    author="Hugo Viana",
    author_email="hugosemianoviana@gmail.com",
    description=(
        "Sphinx multiversion extension with html select version template"
    ),
    install_requires=[
        "Sphinx==3.3.0",
        "semantic_version==2.8.5",
    ],
    test_suite="tests",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/hugo-viana/sphinx-superdoc/",
    project_urls={
        "Bug Tracker": "https://github.com/hugo-viana/sphinx-superdoc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "sphinx_superdoc"},
    packages=find_packages(where="sphinx_superdoc"),
    python_requires=">=3.8",
)
