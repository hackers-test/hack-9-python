#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="darwinday",
    version="0.0.1",
    author="Deren Eaton",
    author_email="de2356@columbia.edu",
    license="GPLv3",
    description="A package for celebratin Darwin",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["darwinday = darwinday.__main__:main"]
    },
)
