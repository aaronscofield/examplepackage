import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="hello",
    version="0.0.1",
    author="Aaron Scofield",
    author_email="aaron.scofield@icloud.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aaronscofield",
    packages=setuptools.find_packages(),
    install_requires=[
        "awscliv2",
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)