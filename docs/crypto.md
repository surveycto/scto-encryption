# Module: crypto

Use this Python module to encrypt data.

If you want to encrypt the data in a CSV file, we recommend using the [csv_encrypt](csv_encrypt.md) module as well.

**Table of contents**

1. [Quick start: Encryption](#quick-start-encryption)
1. [Quick start: Decryption](#quick-start-decryption)
1. [Classes](#classes)
  1. [CryptoKey](#cryptokey): Stores information about the key used to encrypt and decrypt data.
  1. [Encrypted](#encrypted): Stores information about encrypted data, including the ciphertext and IV.
  1. [Encryption](#encryption): Tool used to encrypt and decrypt data.
1. [Functions](#functions)

## Quick start: Encryption

*This is demonstrated in the [**basic_encryption.py**](../source/basic_encryption.py) file.*

Here, we demonstrate how to encrypt data using this library, and then decrypt it to confirm the encryption was successful.

### Part 1: Import class

For basic encryption, you just need to import the "Encryption" class:

    from scto_encryption.crypto import Encryption

### Part 2: Encryption

You then need a message to encrypt. It should be encoded to a `bytes` variable using UTF-8. In this example, the message is entered using the `input()` function:

    secret_message = input('Enter your secret message: ').encode('utf-8')

You then need to create an [`Encryption`](#encryption) object. The easiest way to do this is using the `Encryption.initWithKey()` static method:

    encryption1 = Encryption.initWithKey()

This not only initializes an object you can use for encryption, but it also generates an encryption key for you, which will be used to encrypt your data. Retrieve the key from this `Encryption` object:

    key = encryption1.key

This "key" is a [`CryptoKey`](#cryptokey) object that stores the encryption key, which will be used to both encrypt and decrypt your data.

To encrypt your data, use the `Encryption.encrypt()` method, which takes the encoded message as an argument:

    encrypted = encryption1.encrypt(secret_message)

This will create an [`Encrypted`](#encrypted) object, which stores encryption information. It has various variables that are later used to decrypt your data, including the ciphertext (the encrypted data) and the IV (which was used to help encrypt your data). However, it does NOT include the encryption key.

### Part 3: Decryption

Now that you have your encrypted data, you can try decrypting it. To decrypt your data, you need both the `CryptoKey` object and `Encrypted` objects you created earlier.

First, you need an `Encryption` object to decrypt your data. You could use the same one you created earlier, but since you are not normally going to be encrypting and decrypting in the same run of a Python script, for this demonstration, we are going to create a new `Encryption` object:

    encryption2 = Encryption(key)

Notice how it takes the `CryptoKey` object from earlier as an argument, as opposed to creating an object with a brand new, different key.

All that's left is to decrypt your data! You can do this using the `Encryption.decrypt()` method:

    decrypted = encryption2.decrypt(encrypted)

This method takes the `Encrypted` object from earlier as an argument, and it returns the decrypted data.

And that's all! Here it is all put together:

```
# IMPORT
from crypto.crypto import Encryption

# ENCRYPTION
secret_message = input('Enter your secret message: ').encode('utf-8')
encryption1 = Encryption.initWithKey()
key = encryption1.key
encrypted = encryption1.encrypt(secret_message)

# DECRYPTION
encryption2 = Encryption(key)
decrypted = encryption2.decrypt(encrypted)
```

## Quick start: Decryption

*This is demonstrated in the [**basic_decryption.py**](../source/basic_decryption.py) file.*

You can use this module to not only encrypt your plaintext data, but decrypt ciphertext data encrypted using a different library.

### Step 1: Import classes

For decryption, you need all three classes:

    from scto_encryption.crypto import CryptoKey, Encrypted, Encryption

### Step 2: Retrieve data

Retrieve your ciphertext, IV, and encryption key, and store them in variables. They can be either `str` or `bytes` variables, but make sure they are all Base64-encoded.

### Step 3: Generate key

This module requires the key to be in a specific format. Use the encryption key to generate a `CryptoKey` object:

    key = CryptoKey.fromEncryptionKey(encryption_key)

## Step 4: Collect encryption data

Use the ciphertext, IV, and `CryptoKey` key to generate an `Encrypted` object:

    encrypted = Encrypted.tokenless(iv, ciphertext, key)

This will store information that will be used for decryption.

### Step 5: Generate encryption tool

Use the `CryptoKey` key to generate an `Encryption` object, which is a tool that will be used to decrypt your data:

    encryption = Encryption(key)

### Step 6: Decrypt data

Use the `Encryption` and `Encrypted` objects to decrypt your data:

    decrypted = encryption.decrypt(encrypted)

And "decrypted" will store your decrypted, plaintext data!

## Classes

This module contains three classes

### CryptoKey

Objects with this class store information about the encryption key.

#### Class variables

This class has three variables:

 * **whole_key** (`bytes`): The whole, 256-bit encryption key encoded using Base64. This is a combination of the signing key and the encryption key. This is the key that is used by the [`cryptopraphy`](https://cryptography.io/) library. 
 * **signing_key** (`bytes`): The 128-bit signing key encoded using Base64.
 * **encryption_key** (`bytes`): The 128-bit encryption key encoded using Base64. This is the key that is actually used to encrypt your data.

 Importantly, the `cryptography` library requires the **whole_key** when encrypting data, but other services, such as the [decrypt field plug-in](https://github.com/surveycto/decrypt/blob/main/README.md), will only use the **encryption_key**.
 
 You can learn more about the `cryptography` key format in their [specification](https://github.com/fernet/spec/blob/master/Spec.md#key-format).

#### Initiation

**CryptoKey(whole_key: `byte`, signing_key: `bytes`, encryption_key: `bytes`) -> CryptoKey**

While this is available, we strongly recommend creating objects with this class using the [static methods below](#static-methods), so it properly generates the **signing_key** and **encryption_key** from the **whole_key**.

#### Static methods

**fromKey(key: `bytes`) -> `CryptoKey`**

Takes a 256-bit, Base64-encoded key, and returns a `CryptoKey` object.

**Important**: That 256-bit key will be divided up and turned into a 128-bit signing key and a 128-bit encryption key. So, with the argument you pass into this method, only the second-half of that key will be used to actually encrypt your data. If you only have the encryption key (and no signing key), use `CryptoKey.fromEncryptionKey()` instead.

**fromEncryptionKey(encryption_key: `bytes`) -> `CryptoKey`**

Takes a 128-bit, Base64-encoded encryption key, and returns a `CryptoKey` object. This method will generate a signing key for you.

**generate() -> `CryptoKey`**

Generates a 256-bit, Base64-encoded key for you, and returns a `CryptoKey` object.

### Encrypted

This class stores the data regarding an encrypted piece of data.

This class has six variables. The second through sixth variables are all directly derived from the **token**, as described in the `cryptography` [spec](https://github.com/fernet/spec/blob/master/Spec.md#token-format).

 * **token** (`bytes`): The full, Base64-encoded encryption token that the `cryptography` library generates.
 * **version** (`int`): The version format used by the token. This will always be 128.
 * **timestamp** (`bytes`): Base64-encoded Unix epoch time the token was created.
 * **iv** (`bytes`): The Base64-encoded initialization vector (IV) used when encrypting the data.
 * **ciphertext** (`bytes`): The actual encrypted data, encoded using Base64.
 * **hmac** (`bytes`): The [HMAC](https://github.com/fernet/spec/blob/master/Spec.md#hmac).

 When decrypting your data using a different library, you will typically only need the **iv** and **ciphertext**. This class makes it easy to retrieve those two from the full token returned by the `cryptography` library.

**Important**: The `cryptopgraphy` library typically uses Base64URL encoding, but these variables all use Base64 encoding, which is more common. The only difference is that Base64 uses `+` instead of `-` and `/` instead of `_`.

#### Initiation

**Encrypted(token: `byte`, version: `int`, timestamp: `bytes`, iv: `bytes`, ciphertext: `bytes`, hmac: `bytes`) -> Encrypted**

While this is available, we strongly recommend creating objects with this class using one of the static methods below, so it properly retrieves all of the needed data from the **token**.

#### Static methods

**fromToken(token: `bytes`) -> `Encrypted`**

Takes an encryption token generated by the `cryptography` library, and returns an `Encrypted` object where it is much easier to get the data you need to decrypt using a different library.

Note: The [`Encryption`](#encryption) class will generate `Encrypted` objects for you, so it is unlikely you will actually need to directly use this method.

**tokenless(ciphertext: `Union[bytes, str]`, iv: `Union[bytes, str]`, key: `CryptoKey`) -> `Encrypted`**

Takes an ciphertext, IV, and key, and generates an `Encrypted` object.

Use this method when decrypting data from outside of this library or the `cryptography` library. 

The "iv" and "ciphertext" can be either `bytes` or `str`. The method will convert them for you.

**Important**: The "key" must be a `CryptoKey` object. Make sure you generate it before running this method. You can create a `CryptoKey` object using just the encryption key using the `CryptoKey.fromEncryptionKey()` method. You can see this demonstrated in [basic_decryption.py](../source/basic_decryption.py).

### Encryption

This class is used to encrypt and decrypt your data.

#### Class variable

* **key** (`CryptoKey`): The encryption key used to encrypt data.

#### Initialization

**Encryption(key: `CryptoKey`)**

This class takes a [`CryptoKey`](#cryptokey) object as an argument. That key will be used to encrypt and decrypt your data.

#### Static method

**initWithKey() -> `Encryption`**

Generates a `CryptoKey` object for you (so you don't have to), and returns an `Encryption` object using that key.

#### Other methods

**encrypt(data: `bytes`) -> `Encrypted`**

Encrypts the data using AES, returning an `Encrypted` object with the encryption information.

**decrypt(encrypted: `Encrypted`) -> `bytes`**

Decrypts the data in the `Encrypted` object, and returns the decrypted data.

## Functions

**base64urlToStandard(data: `bytes`) -> `bytes`**

Takes Base64URL-encoded data, and converts it to Base64-encoded data.

**base64standardToUrl(data: `bytes`) -> `bytes`**

Takes Base64-encoded data, and converts it to Base64URL-encoded data.

**Note**: The only difference between Base64 and Base64URL is that Base64 uses `+` instead of `-` and `/` instead of `_`.

**strToBytes(data: `Union[str, bytes]`) -> `bytes`**

If the argument is `str` data, it will encode it as UTF-8 `bytes` data and return it. If the argument is `bytes` data, it will return that same data, unchanged.

**bytesToStr(data: `Union[str, bytes]`) -> `str`**

If the argument is `bytes` data, it will decode it to `str` data using UTF-8 and return it. If the argument is `str` data, it will return that same data, unchanged.
