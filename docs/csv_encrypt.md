# Module: csv_encrypt

Use this module to encrypt the data in a CSV file using AES.

**Table of contents**

* [Features](#features)
* [Function](#function)

## Features

* Encrypt each individual piece of data in each column of data.
* Exclude specided columns from encryption data, so those columns remain unencrypted.
* Include both the ciphertext and IV in the CSV file.
* Create a new CSV file at the specified location with the encrypted data. The original CSV file will remain unencrypted.

## Functions

This module has two functions.

**encryptCsvCryptoKey(crypto_key: `CryptoKey`, source_path: `str`, new_path: `str`, exclude_headers: `List[str]`, separator: `Union[str, bytes]` = `b'|'`)**

### Parameters

* **crypto_key** (`CryptoKey`): The [`Cryptokey`](crypto.md#cryptokey) object that will be used to encrypt the data.
* **source_path** (`str`): Full filepath to the CSV file that will be encrypted.
* **encrypted_path** (`str`): Full filepath to the CSV file that will be **created** and contain the encrypted data.
* **exclude_headers** (`List[str]`): Headers of the columns that should not be encrypted. We strongly recommend exluding the unique identifier column from encryption.
* **separator** (`Union[str, bytes]`): Character used to separate the ciphertext and IV. You can provide a string, which the function will convert to a `bytes` variable for you. Default: `b'|'`

**Important when specifying the separator**: Make sure you do not use a letter, number, plus `+`, nor slash `/` as the separator, since these are all used in Base64 encoding.

**When using with SurveyCTO**: Leave the separator as a pipe `|`, since that is used by the [decrypt](https://github.com/surveycto/decrypt/blob/main/README.md) field plug-in

### Result

When you run this function, it will generate a new CSV file at the path specified in **encrypted_path**. Other than the data in the columns specified in **exclude_headers**, the data in each cell will be encrypted.

Each encrypted cell will be a combination of the ciphertext and initialization vector (IV), separated by a pipe `|`, or whatever character you specified for the **separator**. Here is an example:

    f5l2KcvRKodlSf6n06tqgQ==|XSFHs2RWb/w2bo5VC2+ipg==

Here, the ciphertext is `f5l2KcvRKodlSf6n06tqgQ==`, and the IV is `XSFHs2RWb/w2bo5VC2+ipg==`. You will need both of these with the encryption key to decrypt your data later.

**decryptCsvCryptoKey(crypto_key: `CryptoKey`, source_path: `str`, decrypted_path: `str`, exclude_headers: `List[str]`, separator: `Union[str, bytes]` = `b'|'`)**

### Parameters

* **crypto_key** (`CryptoKey`): The [`Cryptokey`](crypto.md#cryptokey) object that will be used to decrypt the data.
* **source_path** (`str`): Full filepath to the CSV file that will be decrypted.
* **decrypted_path** (`str`): Full filepath to the CSV file that will be **created** and contain the decrypted data.
* **exclude_headers** (`List[str]`): Headers of the columns that were not encrypted, and do not need to be decrypted.
* **separator** (`Union[str, bytes]`): Character used to separate the ciphertext and IV. You can provide a string, which the function will convert to a `bytes` variable for you. Default: `b'|'`
