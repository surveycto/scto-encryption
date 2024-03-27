from scto_encryption.crypto import Encryption, CryptoKey, Encrypted
from base64 import b64encode, b64decode
from time import time

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC

def genHmac(data, signing_key):
  h = HMAC(b64decode(signing_key), hashes.SHA256())
  h.update(data)
  hmac = h.finalize()
  return hmac

def basic():
  key = CryptoKey.fromKey(b'haGwM/krSlYJ7UZG2FGPfkUJh2Pr0OVEDnrn2WUB2YY=')
  encryption = Encryption(key)

  encryption_token = b'gAAAAABmBIANsAkgqKFdhPgOmb3P5INIEuGMUgdirvcU4Y2J5AIY8/zfuL+nXHxtJxC+GsqOlctR0HDrXOcRv4PViqbvBOfOIQ=='

  encrypted = Encrypted.fromToken(encryption_token)
  decrypted = encryption.decrypt(encrypted)

  print(encrypted.ciphertext)
  print(encrypted.iv)

  print(f'Decrypted:\n{decrypted}')

def main():
  key = CryptoKey.fromKey(b'haGwM/krSlYJ7UZG2FGPfkUJh2Pr0OVEDnrn2WUB2YY=')

  ciphertext = b'4YxSB2Ku9xThjYnkAhjz/A=='
  iv = b'sAkgqKFdhPgOmb3P5INIEg=='

  decoded_ct = b64decode(ciphertext)
  decoded_iv = b64decode(iv)

  timestamp = int(time()).to_bytes(8, 'big')
  hmac_data = b'\x80' + timestamp + decoded_iv + decoded_ct

  hmac = genHmac(hmac_data, key.signing_key)
  constructed_token_bytes = hmac_data + hmac
  constructed_token = b64encode(constructed_token_bytes)

  encrypted = Encrypted.fromToken(constructed_token)
  
  encryption = Encryption(key)
  print('Full encryption token:')
  print(encrypted.token)
  decrypted = encryption.decrypt(encrypted)
  print('Decrypted message:')
  print(decrypted)


if __name__ == '__main__':
  main()