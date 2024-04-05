# Module: functions

Basic functions for generating keys, saving them to a file, encrypting CSV files, and decrypting CSV files

## Functions

This module has four functions.

**generateKey(path: `str`) -> `str`**

Generate a new, 128-bit encryption key, and save it at the path specified. This key will be used to both encrypt and decrypt your data.

Here is an example:

    generateKey('/Users/surveycto.user/Documents/Keys/my_key.pem')

That will generate a new encryption key, and save it at the location `/Users/surveycto.user/Documents/Keys/my_key.pem`.

This function will also return that key as a string, but you usually don't need to save it to a variable, since it will be saved at the specified path.

**loadKeyFromFile(path: `str`) -> `str`**

Load the 128-bit encryption key at the specifed location, and return it as a string.

If the key is not a Base64-encoded, 128-bit key, there will be an error. As long as they key was generated using `generateKey()`, it will load well.

Note: You will probably not need to use this function, since the CSV functions mentioned below will load the key for you. However, this function is available to you if you need it.

**encryptCsv(key_path: `str`, original_path: `str`, new_path: `str`, exclude_headers: `List[str]`, separator: `Union[str, bytes]` = `b'|'`)**

Use this function to encrypt the data in the specified CSV file, and save the encrypted file in the specified location.

*This is demonstrated in [encrypt_csv.py](../source/encrypt_csv.py).*

### Parameters

* **key_path** (`str`): The file path to the 128-bit key that will be used to encrypt your data.
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

**decryptCsv(key_path: `str`, original_path: `str`, new_path: `str`, exclude_headers: `List[str]`, separator: `Union[str, bytes]` = `b'|'`)**

Use this function to decrypt data in a CSV file, and save the decrypted file in the specified location.

Each piece of data must be the ciphertext followed by the IV, separated by a pipe `|`. This is the same format used by the `decryptCsv()` function above, as well as the [encrypt field plug-in](https://github.com/surveycto/encrypt/blob/main/README.md).

*This is demonstrated in [decrypt_csv.py](../source/decrypt_csv.py).*

### Parameters

* **key_path** (`str`): The file path to the 128-bit key that will be used to decrypt your data.
* **source_path** (`str`): Full filepath to the CSV file that will be decrypted.
* **decrypted_path** (`str`): Full filepath to the CSV file that will be **created** and contain the decrypted data.
* **exclude_headers** (`List[str]`): Headers of the columns that were not encrypted, and do not need to be decrypted. You can also leave this alone, and as long as a piece of data does not contain the **separator**, it will be skipped, and the function will not even attempt to decrypt it.
* **separator** (`Union[str, bytes]`): Character used to separate the ciphertext and IV. You can provide a string, which the function will convert to a `bytes` variable for you. Default: `b'|'`
