# Module: csv_encrypt

Use this module to encrypt the data in a CSV file using AES.

**Table of contents**

* [Features](#features)
* [Quick start](#quick-start)
* [Function](#function)

## Features

* Encrypt each individual piece of data in each column of data.
* Exclude specided columns from encryption data, so those columns remain unencrypted.
* Include both the ciphertext and IV in the CSV file.
* Create a new CSV file at the specified location with the encrypted data. The original CSV file will remain unencrypted.

## Quick start

*This is demonstrated in the [**encrypt_csv.py**](../source/encrypt_csv.py) file.*

### Part 1: Import

First, import the relevant modules:

    from scto_encryption.crypto import CryptoKey
    from scto_encryption import csv_encrypt

### Part 2: Generate key

Next, generate a `CryptoKey` object, and store it in a variable. It is usually easiest to use the `Cryptojey.generate()` static method:

    key = CryptoKey.generate()

However, if you already have your own key, you can also use the `CryptoKey.fromKey()` static method.

**Important**: If you use the `CryptoKey.fromKey()` static method, keep in mind that the key used for the argument needs to be a key that combines BOTH the signing key and the encryption key. However, only the encryption key is used for actual encryption and decryption, and you will need that later if you decrypt your data using a different library.

### Part 3: Generate CSV file

Run the `csv_encrypt.encryptCsv()` function, providing it with the needed [parameters](#parameters). This will generate a new CSV file at the specified location with encrypted data.

### Part 4: Generate CSV file

From the `CryptoKey` object created earlier. retrieve the **encryption_key** variable value:

    encryption_key = key.encryption_key.decode('utf-8')

(In this example, the encryption key is being saved as a `string`.)

Put that value somewhere safe. You can write it to a `.pem` file, print it to the console and copy it, etc. Just make sure you keep that encryption key safe, since it is required to decrypt the data later.

## Function

This module has one function, `encryptCsv()`.

**encryptCsv(crypto_key: `CryptoKey`, original_path: `str`, new_path: `str`, exclude_headers: `List[str]`, separator: `Union[str, bytes]` = `b'|'`)**

### Parameters

* **crypto_key** (`CryptoKey`): The [`Cryptokey`](crypto.md#cryptokey) object that will be used to encrypt the data.
* **original_path** (`str`): Full filepath to the CSV file that will be encrypted.
* **new_path** (`str`): Full filepath to the CSV file that will be **created** and contain the encrypted data.
* **exclude_headers** (`List[str]`): Headers of the columns that should not be encrypted. We strongly recommend exluding the unique identifier column from encryption.
* **separator** (`Union[str, bytes]`): Character used to separate the ciphertext and IV. You can provide a string, which the function will convert to a `bytes` variable for you. Default: `b'|'`

**Important when specifying the separator**: Make sure you do not use a letter, number, plus `+`, nor slash `/` as the separator, since these are all used in Base64 encoding.

**When using with SurveyCTO**: Leave the separator as a pipe `|`, since that is used by the [decrypt](https://github.com/surveycto/decrypt/blob/main/README.md) field plug-in

### Result

When you run this function, it will generate a new CSV file at the path specified in **new_path**. Other than the data in the columns specified in **exclude_headers**, the data in each cell will be encrypted.

Each encrypted cell will be a combination of the ciphertext and initialization vector (IV), separated by a pipe `|`, or whatever character you specified for the **separator**. Here is an example:

    f5l2KcvRKodlSf6n06tqgQ==|XSFHs2RWb/w2bo5VC2+ipg==

Here, the ciphertext is `f5l2KcvRKodlSf6n06tqgQ==`, and the IV is `XSFHs2RWb/w2bo5VC2+ipg==`. You will need both of these with the encryption key to decrypt your data later.
