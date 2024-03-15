from base64 import urlsafe_b64decode, b64encode
from cryptography.fernet import Fernet

def base64urlToStandard(string: bytes) -> bytes:
  return string.replace(b'-', b'+').replace(b'_', b'/')

def base64standardToUrl(string: bytes) -> bytes:
  return string.replace(b'+', b'-').replace(b'/', b'_')

class CryptoKey:
  def __init__(
      self,
      whole_key: bytes,
      signing_key: bytes,
      encryption_key: bytes,
      ) -> None:
    self.whole_key = whole_key
    self.signing_key = signing_key
    self.encryption_key = encryption_key
  
  @staticmethod
  def fromKey(key: bytes) -> "CryptoKey":
    decoded_key = urlsafe_b64decode(key)
    signing_key_raw = decoded_key[0:16]
    encryption_key_raw = decoded_key[16:]
    signing_key = b64encode(signing_key_raw)
    encryption_key = b64encode(encryption_key_raw)
    return CryptoKey(base64urlToStandard(key), signing_key, encryption_key)
  
  @staticmethod
  def generate() -> "CryptoKey":
    key = Fernet.generate_key()
    return CryptoKey.fromKey(key)

class Encrypted:
  def __init__(
      self,
      token: bytes,
      version: bytes,
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

  @staticmethod
  def fromToken(token: bytes) -> "Encrypted":
    decoded_token = urlsafe_b64decode(token)
    version = decoded_token[0]
    timestamp = b64encode(decoded_token[1:9])
    iv = b64encode(decoded_token[9:25])
    ciphertext = b64encode(decoded_token[25:len(decoded_token) - 32])
    hmac = b64encode(decoded_token[-32:])
    return Encrypted(base64urlToStandard(token), version, timestamp, iv, ciphertext, hmac)

class Encryption:
  def __init__(self, key: CryptoKey) -> None:
    self.key = key
    self._f = Fernet(key.whole_key)
  
  @staticmethod
  def initWithKey() -> "Encryption":
    return Encryption(CryptoKey.generate())

  def encrypt(self, data: bytes) -> Encrypted:
    token = self._f.encrypt(data)
    return Encrypted.fromToken(token)
  
  def decrypt(self, encrypted: Encrypted) -> bytes:
    print(base64urlToStandard(encrypted.token))
    return self._f.decrypt(encrypted.token)

