from csv import DictReader, DictWriter
from .crypto import CryptoKey, Encrypted, Encryption
from typing import List, Dict, Union

def encryptCsv(
    crypto_key: CryptoKey,
    original_path: str,
    new_path: str,
    encrypt_headers: List,
    separator: Union[str, bytes] = b'|'
    ):
  if type(separator) == str:
    separator = separator.encode('utf-8')
  encryptor = Encryption(crypto_key)
  
  with open(original_path, newline='') as r:
    reader = DictReader(r)
    headers = reader.fieldnames
    encrypt_headers_real: List[str] = list()
    for h in encrypt_headers:
      if h not in headers:
        print(f'Warning: Header "{h}" does not exist in the CSV data file, so that will be skipped.')
      else:
        encrypt_headers_real.append(h)
    
    new_data: List[Dict[str, str]] = list()
    for row in reader:
      for h in encrypt_headers_real:
        data = row[h]
        enc: Encrypted = encryptor.encrypt(data.encode('utf-8'))
        row[h] = (enc.ciphertext + separator + enc.iv).decode('utf-8')
      new_data.append(row)
  with open(new_path, 'w', newline='') as w:
    writer = DictWriter(w, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_data)