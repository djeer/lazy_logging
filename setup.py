import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="lazy_logging",
    version="0.0.2",
    install_requires=requirements,
    author="djer",
    author_email="djer@github.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djeer/lazy_logging",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
