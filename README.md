# Python package: scto-encryption

Use this Python package to encrypt your data for use with the [decrypt field plug-in](https://github.com/surveycto/decrypt/blob/main/README.md). It can even encrypt data in a CSV file for you.

*New to SurveyCTO? Check out [this video](https://www.surveycto.com/videos/surveycto-overview/)!*

## Features

* Encrypt data using AES-CBC encryption.
* Provide tools and information to easily decrypt data using a different platform.
* Encrypt a CSV file for use with SurveyCTO, including the [decrypt field plug-in](https://github.com/surveycto/decrypt/blob/main/README.md).

## Installation

(To be added...)

## Documentation

Check out these resources to learn how to use the package:

* [**Module: crypto**](docs/crypto.md): Classes used for easy encryption and decryption, including tools to later decrypt your data using other packages on other platforms.
* [**Module: csv_encrypt**](docs/csv_encrypt.md): Includes function to encrypt the data in a CSV file that can be used for pre-loading in SurveyCTO.
* [**Use with SurveyCTO**](docs/use_with_surveycto.md): Tips on using this package to assist you with SurveyCTO.
 
## Further information

This package uses the [cryptography](https://cryptography.io/) Python package to encrypt your data, specifically the [Fernet](https://cryptography.io/en/latest/fernet/) class.