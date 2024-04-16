# Quick start guide

This quick start guide is aimed at helping basic users access the core functions of this package as quickly as possible. You'll be able to generate encryption keys, encrypt CSV data, and decrypt it by following these steps. Advanced users should skip this guide and stick to the main the documentation.

## Prerequisites

This quick start guide has some prerequisites and assumptions:

1. You need to know what the terminal application on your computer is and have basic knowledge of typing in commands and running them. If you have never used the terminal or run any computer code ever, you might need to look for additional resources to help you.
2. Python must be installed on your computer. You can download a user-friendly installer from [the Python website](https://www.python.org/). Confirm that Python is installed by running `python3 --version` or `python --version` in the terminal. It should report the installed version number. Make sure you are using at least Python 3.8 (but a later version will also work well).
3. You must install the scto-encryption package by running `pip install git+https://github.com/surveycto/scto-encryption.git`. You can confirm that it is installed by running `pip list | findstr scto-encryption` on Windows or `pip list | grep scto-encryption` on MacOS or Linux. It will list the package name, followed by the latest version number (`1.0.0`).

**Important**: If in step 2, if `python3 --version` works but not  `python --version`, in all command in this document, use `python3` instead of `python`, and use `pip3` instead of `pip`.

## How to run a Python command

### Run commands

To start Python, open a terminal (called "Command prompt" on Windows), and run the `python` command. You can then enter and run Python commands. For example, you can run this command:

    from scto_encryption.functions import generateKey

Followed by this command:

    generateKey('C:\\Users\\surveycto.user\\Documents\\Keys\\my_key.pem')

We will discuss these commands [later](#generating-an-encryption-key).

### Run a Python file

To run a Python file, in your terminal, enter the `python` command, followed by a space, followed by the path to the Python file you would like to run in quotes. Here is an example:

    python "C:\\Users\\surveycto.user\\Documents\\Python scripts\\quick_key.py"

All of the top-level files in [this folder](../source/) can be run this way once they are downloaded to your computer.

## Generating an encryption key

The `scto-encryption` package can generate an encryption key similar to the one used by the SurveyCTO platform to [encrypt data](https://docs.surveycto.com/02-designing-forms/02-additional-topics/06.encrypting.html) but with an important difference: only one key file is is used for both encryption and decryption. That key needs to be safeguarded.

To generate your key, first customize the file path in the [`quick_key.py`](../source/quick_key.py) template file. Specify the path where you would like the key to be created, including the file name. Your file named should end in ".pem". Here are the contents of `quick_key.py`:

```
from scto_encryption.functions import generateKey
generateKey('C:\\Users\\surveycto.user\\Documents\\Keys\\my_key.pem')
```

Once you have customized the file, you can run it using the terminal application on your computer. When it is complete, check the specified folder, and make sure the key has been created.

**Important notes**:

* Make sure the folder path already exists. In the above example, make sure the `C:\\Users\\surveycto.user\\Documents\\Keys\\` folder already exists.
* This example path is for MacOS and Linux. On Windows, use two backslashes `\\` instead of a single forward slash (Windows uses backslashes in folder paths, but backslashes are also used by Python, so the double-backslash means to use an actual backslash). Here is an example file path in Windows:<br>
`C:\\Users\\surveycto.user\\Documents\\my_key.pem`<br>
And here is an example file path in MacOS:<br>
`/Users/surveycto.user/Documents/my_key.pem`<br>
Consult your operating system's operating manual as required.
* When specifying the path, for consistent results, use the absolute path (i.e. the path from the root of your system, e.g. `C:\\` on Windows), as opposed to the relative path (the path relative to the Python file).
* Keep this file secure, since it will be used to both encrypt and decrypt your data. We recommend you don't back it up to the cloud. Safeguard this key; for example, consider storing it as a secure note in a password manager.

## Encrypting a CSV file

You should have a CSV file prepared and know the column header names of any columns you wish to exempt from the encryption process. At a minimum, you will at least want to leave the unique ID column unencrypted, so that you can pre-load encrypted data into a form.

This is demonstrated in the [encrypt_csv.py](../source/encrypt_csv.py) file. You will have to customize the contents of the template file. The following parameters need to be specified in the code:

* **key_path**: The file path to the encryption key that you generated (the file ending in ".pem").
* **source_path**: The file path to the CSV file with data you would like encrypted.
* **encrypted_path**: The file path to the new CSV file you would like to be created with the encrypted data. Make sure the folder path exists, you specify the new file name, and the file name ends in `.csv`.
* **exclude_headers**: The list of columns to not be encrypted. Include column header names in the list following "exclude_headers" inside the square brackets. Be sure to specify them in quotes, separated by commas (e.g. `['column_a', 'column_b', 'column_c']`)

Once you run the script, use the file path location specified for **encrypted_path** to locate your encrypted CSV file. View the contents of the CSV file to confirm that you've encrypted all sensitive data; you may need to import the CSV file into Excel. Alternatively, [CSView](https://kothar.net/csview) is a free, cross-platform utility for opening and viewing CSV files. Do not use Google Sheets or any other cloud-based app just in case you missed some columns that should be encrypted, so your data remains safe and not saved to the cloud.

Once you have confirmed that the CSV file is prepared correctly, you can upload it to a server dataset on your SurveyCTO server for use with the [`decrypt`](https://github.com/surveycto/decrypt/blob/main/README.md) field plug-in, which will be able to decrypt the data!

## Decrypting a CSV file

It is a good idea to test that you can decrypt the data that you've encrypted. You may also need to export and view the true values at some point. To decrypt CSV data using `scto-encryption`, you can customize the [decrypt_csv.py](../source/decrypt_csv.py) template file. 

Customize the following parameters in the code:

* **key_path**: The file path to the encryption key that you generated (the file ending in ".pem").
* **encrypted_path**: The file path to the CSV file with the encrypted data you would like encrypted.
* **decrypted_path**: The file path to the new CSV file you would like to be created with the decrypted data. Make sure the folder path exists, you specify the new file name, and the file name ends in `.csv`.

Visit the file path location specified for **decrypted_path** to locate your decrypted CSV file. As discusssed above, view the contents of the CSV file to ensure that the decryption worked. Do not use Google Sheets or any other cloud-based app, as this can expose sensitive data.

## Using your form to decrypt pre-loaded data

Once you have prepared a server dataset with encrypted data, you can design forms to [pre-load](https://docs.surveycto.com/02-designing-forms/03-advanced-topics/03.preloading.html) that data and decrypt it using the [`decrypt`](https://github.com/surveycto/decrypt/blob/main/README.md) field plug-in for display. That data can then be updated in the form and encrypted using the same key with the [`encrypt`](https://github.com/surveycto/encrypt/blob/main/README.md) field plug-in before publishing it back to the server dataset. Server console users will not be able to view the true values stored in the server dataset unless they have the encryption key.

Have a look at [this use case]() (LINK TBC) for a full working example of managing and updating encrypted data using a form.
