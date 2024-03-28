from scto_encryption.crypto import CryptoKey, Encrypted, Encryption, bytesToStr

def main():
  ciphertext = b'4YxSB2Ku9xThjYnkAhjz/A=='
  iv = b'sAkgqKFdhPgOmb3P5INIEg=='
  encryption_key = b'RQmHY+vQ5UQOeufZZQHZhg=='

  key = CryptoKey.fromEncryptionKey(encryption_key)
  encrypted = Encrypted.tokenless(ciphertext, iv, key)
  encryption = Encryption(key)
  decrypted = encryption.decrypt(encrypted)
  print(bytesToStr(decrypted))
  
if __name__ == '__main__':
  main()