from csv import DictReader, DictWriter
from .crypto import CryptoKey, Encrypted, Encryption
from typing import List, Dict, Union

def encryptCsv(
    crypto_key: CryptoKey,
    original_path: str,
    new_path: str,
    exclude_headers: List[str],
    separator: Union[str, bytes] = b'|'
    ):
  if type(separator) == str:
    separator = separator.encode('utf-8')
  encryptor = Encryption(crypto_key)
  
  with open(original_path, newline='', encoding='utf-8-sig') as r:
    reader = DictReader(r)
    headers = reader.fieldnames
    
    new_data: List[Dict[str, str]] = list()
    for row in reader:
      for h in headers:
        if h not in exclude_headers:
          data = row[h]
          enc: Encrypted = encryptor.encrypt(data.encode('utf-8'))
          row[h] = (enc.ciphertext + separator + enc.iv).decode('utf-8')
      new_data.append(row)
  with open(new_path, 'w', newline='', encoding='utf-8-sig') as w:
    writer = DictWriter(w, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_data)