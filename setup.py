from setuptools import setup, find_packages

setup(
    name="spoofy",
    version="0.1.0",
    packages=find_packages(),  # will now include 'spoofy' and 'modules'
    install_requires=[
        "colorama",
        "dnspython>=2.2.1",
        "tldextract",
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "spoofy=spoofy.main:main",  # now correctly points to main() inside spoofy/main.py
        ],
    },
)
