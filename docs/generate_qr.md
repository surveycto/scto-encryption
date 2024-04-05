# How to generate a QR code with your encryption key

*This is demonstrated in the file [create_qr.py](../source/create_qr.py).*

It will be much easier for your enumerators to scan a QR code with the encryption key instead of entering it manually every time (and possibly more secure). You can easily turn your encryption key into a QR code using the [`qrcode`](https://pypi.org/project/qrcode/) library.

Note: The `qrcode` library is a third-party library, and it is not maintained by SurveyCTO/Dobility.

## Generate QR code

### Step 1: Generate encryption key

First, you will need an encryption key. You can quickly generate an encryption key using the `generateKey()` function in the [functions](functions.md) module to generate a key and save it to a file:

```
from scto_encryption.functions import generateKey
  encryption_key = generateKey(key_path)
```

If you already have an encryption key you would like to use, you can use the `loadKey()` function instead.

### Step 2: Generate QR code

Use the `qrcode` library to generate a QR code from the encryption key. Import the package:

    import qrcode

Then, generate the QR code:

    img = qrcode.make(encryption_key)

Here, the variable "img" stores an object with the QR code image. You can then save that image to your preferred destination:

    img.save(img_path)

Your QR code image will be saved! You can share that with your enumerators, so they can decrypt your data.

Check out the [`qrcode` documentation](https://pypi.org/project/qrcode/) for more advanced usage of the library to further customize your QR codes.

**Important**: Be very careful with your QR code, since anyone with access to that QR code can decrypt your data.
