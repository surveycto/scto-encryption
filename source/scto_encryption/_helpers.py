from base64 import b64decode

def loadStringFromFile(path: str) -> str:
  with open(path, newline='') as f:
    return f.read()

def verifyEncryptionKeyString(key_str: str) -> str:
  decoded = b64decode(key_str)
  if len(decoded) != 16:
    raise Exception(f'Invalid encryption key "{key_str}": Key must be 128-bit, but this key is {len(decoded)*8}-bit.')
  else:
    return key_str