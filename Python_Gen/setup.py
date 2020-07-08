import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number_generator", # Replace with your own username
    version="0.0.1",
    author="Anuj Kumar",
    author_email="anujkr2210@gmail.com",
    description="Package to generate fibonnacci, factorial and ackermann no",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" ",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)