# Use with SurveyCTO

You can use the `csv_encrypt` module to create a CSV file with encrypted data. Check out the [documentation](csv_encrypt.md) to learn how to set that up.

When you encrypt your data, **make sure you have the encryption key**. Remember: the key normally returned by the `cryptography` library combines the signing key and the encryption key, but you will need the encryption key to decrypt the data.

With that CSV file, you can either attach it directly to your form definition, or create a [server dataset](https://support.surveycto.com/hc/en-us/articles/11854064982675) with that data, and attach the server dataset to your form. You can then [pre-load its data](https://docs.surveycto.com/02-designing-forms/03-advanced-topics/03.preloading.html).

Feed the pre-loaded, encrypted data into the [decrypt](https://github.com/surveycto/decrypt/blob/main/README.md) field plug-in, which will decrypt your data for you.

If you publish data to a server dataset using the [encrypt field plug-in](https://github.com/surveycto/encrypt/blob/main/README.md), you can download the server dataset's CSV file, and then use the [`decryptCsv()` function](csv_encrypt.md#functions) in this package to decrypt the data.
