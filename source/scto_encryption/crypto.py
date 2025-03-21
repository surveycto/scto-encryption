from ._helpers import loadStringFromFile, verifyEncryptionKeyString

from base64 import urlsafe_b64decode, b64encode, b64decode
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.hmac import HMAC
from time import time
from os import urandom

from typing import Union

def base64urlToStandard(data: bytes) -> bytes:
  return data.replace(b'-', b'+').replace(b'_', b'/')

def base64standardToUrl(data: bytes) -> bytes:
  return data.replace(b'+', b'-').replace(b'/', b'_')

def strToBytes(data: Union[str, bytes]) -> bytes:
  if type(data) == str:
    return data.encode('utf-8')
  else:
    return data

def bytesToStr(data: Union[str, bytes]) -> str:
  if type(data) == bytes:
    return data.decode('utf-8')
  else:
    return data

class CryptoKey:
  def __init__(
      self,
      whole_key: bytes,
      signing_key: bytes,
      encryption_key: bytes,
      ):
    self.whole_key = whole_key
    self.signing_key = signing_key
    self.encryption_key = encryption_key
  
  @staticmethod
  def fromKey(key: Union[bytes, str]) -> 'CryptoKey':
    key = strToBytes(key)
    decoded_key = urlsafe_b64decode(key)
    signing_key = b64encode(decoded_key[0:16])
    encryption_key = b64encode(decoded_key[16:])
    return CryptoKey(base64urlToStandard(key), signing_key, encryption_key)
  
  @staticmethod
  def fromEncryptionKey(encryption_key: Union[bytes, str]) -> 'CryptoKey':
    encryption_key = strToBytes(encryption_key)
    decoded_signing_key = urandom(16)
    whole_key = b64encode(decoded_signing_key + b64decode(encryption_key))
    return CryptoKey(whole_key, b64encode(decoded_signing_key), encryption_key)

  @staticmethod
  def generate() -> 'CryptoKey':
    key = Fernet.generate_key()
    return CryptoKey.fromKey(key)

  @staticmethod
  def fromFile(path: str) -> 'CryptoKey':
    encryption_key = loadStringFromFile(path)
    verifyEncryptionKeyString(encryption_key)
    return CryptoKey.fromEncryptionKey(encryption_key)

class Encrypted:
  def __init__(
      self,
      token: bytes,
      version: int,
      timestamp: bytes,
      iv: bytes,
      ciphertext: bytes,
      hmac: bytes,
      ) -> None:
    self.token = token
    self.version = version
    self.timestamp = timestamp
    self.iv = iv
    self.ciphertext = ciphertext
    self.hmac = hmac
  
  # Should be decoded byte data, NOT Base64.
  @staticmethod
  def _genHmac(data: bytes, signing_key: bytes) -> bytes:
    h = HMAC(signing_key, SHA256())
    h.update(data)
    return h.finalize()

  @staticmethod
  def fromToken(token: bytes) -> 'Encrypted':
    decoded_token = urlsafe_b64decode(token)
    version = decoded_token[0]
    timestamp = b64encode(decoded_token[1:9])
    iv = b64encode(decoded_token[9:25])
    ciphertext = b64encode(decoded_token[25:len(decoded_token) - 32])
    hmac = b64encode(decoded_token[-32:])
    return Encrypted(base64urlToStandard(token), version, timestamp, iv, ciphertext, hmac)
  
  @staticmethod
  def tokenless(
    ciphertext: Union[bytes, str],
    iv: Union[bytes, str],
    key: CryptoKey) -> 'Encrypted':
    ciphertext = strToBytes(ciphertext)
    iv = strToBytes(iv)
    signing_key = key.signing_key

    timestamp = int(time()).to_bytes(8, 'big')
    hmac_data = b'\x80' + timestamp + b64decode(iv) + b64decode(ciphertext)
    hmac = Encrypted._genHmac(hmac_data, b64decode(signing_key))
    constructed_token = b64encode(hmac_data + hmac)
    return Encrypted.fromToken(constructed_token)


class Encryption:
  def __init__(self, key: CryptoKey):
    self.key = key
    self._f = Fernet(key.whole_key)
  
  @staticmethod
  def initWithKey() -> 'Encryption':
    return Encryption(CryptoKey.generate())

  def encrypt(self, data: bytes) -> Encrypted:
    token = self._f.encrypt(data)
    return Encrypted.fromToken(token)
  
  def decrypt(self, encrypted: Encrypted) -> bytes:
    return self._f.decrypt(encrypted.token)
