#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap_freshsales",
    version="0.1.0",
    description="Singer.io tap for extracting FreshSales Data",
    author="Tisham Dhar (Lori)",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_freshsales"],
    install_requires=[
        "singer-python==5.1.1",
        "requests==2.20.0",
    ],
    entry_points="""
    [console_scripts]
    tap_freshsales=tap_freshsales:main
    """,
    packages=["tap_freshsales"],
    package_data = {
        "schemas": ["tap_freshsales/schemas/*.json"]
    },
    include_package_data=True,
)
