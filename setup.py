import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scto-encryption", # This is the name of the package
    version="0.0.0", # The initial release version
    author="Dobility, Inc", # Full name of the author
    license="Apache Software License",
    description="Encrypt data for use in AES.",
    long_description=long_description, # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=["scto_encryption"], # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ], # Information to filter the project on PyPi website
    python_requires='>=3.6', # Minimum version requirement of the package
    py_modules=[], # Name of the python package
    package_dir={'':'source'}, # Directory of the source code of the package
    install_requires=['cryptography'] # Install other dependencies if any
)
