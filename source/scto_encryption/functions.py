from .crypto import CryptoKey
from .csv_encrypt import encryptCsvCryptoKey, decryptCsvCryptoKey
from ._helpers import loadStringFromFile, verifyEncryptionKeyString
from typing import List, Union
from os import urandom
from base64 import b64encode

def generateKey(path: str) -> str:
  decoded_encryption_key = urandom(16)
  encryption_key = b64encode(decoded_encryption_key).decode('utf-8')
  with open(path, 'w', newline='') as f:
    f.write(encryption_key)
  return encryption_key

def loadKeyFromFile(path: str) -> str:
  encryption_key = loadStringFromFile(path)
  verifyEncryptionKeyString(encryption_key)
  return encryption_key

def encryptCsv(
    key_path: str,
    source_path: str,
    encrypted_path: str,
    exclude_headers: List[str] = list(),
    separator: Union[str, bytes] = b'|'
    ):
  key = CryptoKey.fromFile(key_path)
  encryptCsvCryptoKey(key, source_path, encrypted_path, exclude_headers, separator)

def decryptCsv(
    key_path: str,
    source_path: str,
    decrypted_path: str,
    exclude_headers: List[str] = list(),
    separator: Union[str, bytes] = b'|'
    ):
  key = CryptoKey.fromFile(key_path)
  decryptCsvCryptoKey(key, source_path, decrypted_path, exclude_headers, separator)
