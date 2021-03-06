import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mongoengine-user",
    version="0.0.3",
    description="Basic user models for mongoengine",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/The-Nicholas-R-Barrow-Company-LLC/mongoengine-user",
    author="The Nicholas R. Barrow Company, LLC",
    author_email="me@nicholasrbarrow.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["mongoengineuser"],
    include_package_data=True,
    install_requires=["mongoengine"],
)