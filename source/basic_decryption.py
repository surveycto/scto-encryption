from scto_encryption.crypto import Encryption, CryptoKey, Encrypted
from base64 import urlsafe_b64decode, b64encode, urlsafe_b64encode, b64decode
from time import time

import hmac
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC

def genHmac1(string, signing_key):
  return hmac.new(signing_key, msg=string.decode('utf-8'), digestmod=hashlib.sha256).digest()

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

  encryption1 = Encryption(key)
  encrypted1 = encryption1.encrypt(b'You found me!')

  # ciphertext = b'4YxSB2Ku9xThjYnkAhjz/A=='
  # iv = b'sAkgqKFdhPgOmb3P5INIEg=='
  ciphertext = encrypted1.ciphertext
  iv = encrypted1.iv

  decoded_ct = b64decode(ciphertext)
  decoded_iv = b64decode(iv)

  version = b'\x80'
  # timestamp = int(time()).to_bytes(8, 'big')
  timestamp = b64decode(encrypted1.timestamp)
  hmac_raw = version + timestamp + decoded_iv + decoded_ct



  print('HMAC parts 2')
  print(timestamp)
  print(decoded_iv)
  print(decoded_ct)
  print(hmac_raw)
  print(key.signing_key)

  hmac = genHmac(hmac_raw, key.signing_key)
  print(len(hmac))
  print(hmac)
  constructed_token_bytes = hmac_raw + hmac
  constructed_token = urlsafe_b64encode(constructed_token_bytes)
  print(constructed_token)

  encrypted2 = Encrypted.fromToken(constructed_token)
  
  # encrypted2 = 

  encryption = Encryption(key)
  print(encrypted1.token)
  print(encrypted2.token)
  decrypted1 = encryption.decrypt(encrypted1)
  decrypted2 = encryption.decrypt(encrypted2)
  print(decrypted2)

  # constructed token - 
  pass


if __name__ == '__main__':
  main()