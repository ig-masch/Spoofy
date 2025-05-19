from setuptools import setup

setup(
    name="spoofy",
    version="0.1.0",
    py_modules=["spoofy"],  # this assumes there's a spoofy.py at the root
    install_requires=[
        "colorama",
        "dnspython>=2.2.1",
        "tldextract",
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "spoofy=spoofy:main",  # 'main' should be the function that runs the app
        ],
    },
)
