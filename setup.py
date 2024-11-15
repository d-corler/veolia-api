from setuptools import find_packages, setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="veolia_api",
    version="1.0.0",
    author="Jezza34000",
    author_email="",
    description="Python wrapper for Veolia API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jezza34000/veolia-api",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "aiohttp",
    ],
    python_requires=">=3.9",
)
