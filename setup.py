#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hi_basic_ext",
    version="1.0.0",
    author="Cosmade",
    author_email="deepskystar@outlook.com",
    description="hi_basic_ext",
    long_description=long_description,
    url="git@github.com:DeepSkyStar/hi_basic_ext.git",
    packages=setuptools.find_packages(),
    test_suite="hi_basic_ext.tests.test_all",
    install_requires=[],
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)