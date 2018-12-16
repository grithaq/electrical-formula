import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ohmlaws",
    version="0.0.1",
    author="M afif Nur Azizi",
    author_email="afifnurazizi@gmail.com",
    description="The formula of electrical enginering",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zizonk/electrical-formula.git",
    packages=['electrical_formula'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)