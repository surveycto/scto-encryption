# Python package: scto-encryption

Use this Python package to encrypt your data for use with the [decrypt field plug-in](https://github.com/surveycto/decrypt/blob/main/README.md). It can even encrypt data in a CSV file for you.

This package can also decrypt data, such as data encrypted using the [encrypt field plug-in](https://github.com/surveycto/encrypt/blob/main/README.md).

For a full account of the above plug-ins working with this package, see this [installable SurveyCTO workflow](https://support.surveycto.com/hc/en-us/articles/33842170036499). It demonstrates how sensitive data like personally identifying information (PII) belonging to refugees can be securely managed in [server datasets](https://support.surveycto.com/hc/en-us/articles/11854783867539) while still being available inside forms to help program staff positively identify beneficiaries.

*New to SurveyCTO? Check out [this video](https://www.surveycto.com/videos/surveycto-overview/)!*

## Features

* Encrypt data using AES-CBC encryption.
* Provide tools and information to easily decrypt data using a different platform.
* Encrypt a CSV file for use as [pre-load](https://docs.surveycto.com/02-designing-forms/03-advanced-topics/03.preloading.html) data with SurveyCTO, including the [decrypt field plug-in](https://github.com/surveycto/decrypt/blob/main/README.md).

## Installation

To install the Python package, run this command:

```
pip install git+https://github.com/surveycto/scto-encryption.git
```

**Important**: You may have to replace `pip` with `pip3`, depending on how Python is installed on your system.

## Documentation

Check out these resources to learn how to use the package:

* [**Quick start guide**](docs/quick_start.md): For Python beginners.
* [**Module: functions**](docs/functions.md): Basic functions for Python novices, including generate encryption keys, encrypt CSV files, and decrypt CSV files.
* [**Module: crypto**](docs/crypto.md): Classes used for easy encryption and decryption, including tools to later decrypt your data using other packages on other platforms.
* [**Module: csv_encrypt**](docs/csv_encrypt.md): Functions to encrypt data in a CSV file that can be used for pre-loading in SurveyCTO.
* [**How to generate a QR code with your encryption key**](docs/generate_qr.md): Generate a QR code to make it easier to distribute your encryption key.
* [**Use with SurveyCTO**](docs/use_with_surveycto.md): Tips on using this package to assist you with SurveyCTO.
 
## Further information

This package uses the [cryptography](https://cryptography.io/) Python package to encrypt your data, specifically the [Fernet](https://cryptography.io/en/latest/fernet/) class.