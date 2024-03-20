from crypto.crypto import Encryption


def main():
  # ENCRYPTION
  secret_message = input('Enter your secret message: ').encode('utf-8')

  print(f'Secret message:\n{secret_message}')

  encryption1 = Encryption.initWithKey()
  key = encryption1.key
  print(f'Key:\n{key.whole_key}')

  encrypted = encryption1.encrypt(secret_message)

  print(f'Encryption token:\n{encrypted.token}')

  # DECRYPTION
  encryption2 = Encryption(key)
  decrypted = encryption2.decrypt(encrypted)

  print(f'Decrypted:\n{decrypted}')

def main_detailed():
  secret_message = input('Enter your secret message: ').encode('utf-8')

  print(f'Secret message:\n{secret_message}')

  encryption1 = Encryption.initWithKey()
  key = encryption1.key
  print(f'Key:\n{key.whole_key}')
  print(f'Signing key:\n{key.signing_key}')
  print(f'Encryption key:\n{key.encryption_key}')

  encrypted = encryption1.encrypt(secret_message)

  print(f'Encryption token:\n{encrypted.token}')

  print(f'Version:\n{encrypted.version}')
  print(f'Timestamp:\n{encrypted.timestamp}')
  print(f'IV:\n{encrypted.iv}')
  print(f'Ciphertext:\n{encrypted.ciphertext}')
  print(f'HMAC:\n{encrypted.hmac}')

  encryption2 = Encryption(key)
  decrypted = encryption2.decrypt(encrypted)

  print(f'Decrypted:\n{decrypted}')

if __name__ == '__main__':
  main()