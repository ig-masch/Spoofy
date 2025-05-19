from setuptools import setup, find_packages

setup(
    name="spoofy",
    version="0.1.0",
    packages=find_packages(),  # this finds all folders with __init__.py
    install_requires=[
        "colorama",
        "dnspython>=2.2.1",
        "tldextract",
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "spoofy=spoofy:main",  # assumes main() is in spoofy.py
        ],
    },
)
