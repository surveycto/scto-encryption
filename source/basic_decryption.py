from scto_encryption.crypto import Encryption, CryptoKey, Encrypted

def main():
  encryption_key = b'RQmHY+vQ5UQOeufZZQHZhg=='
  ciphertext = b'4YxSB2Ku9xThjYnkAhjz/A=='
  iv = b'sAkgqKFdhPgOmb3P5INIEg=='

  key = CryptoKey.fromEncryptionKey(encryption_key)
  encrypted = Encrypted.tokenless(iv, ciphertext, key)
  encryption = Encryption(key)
  print(encryption.decrypt(encrypted))
  
if __name__ == '__main__':
  main()