from crypto import csv_encrypt
from crypto.crypto import CryptoKey, Encrypted, Encryption

def main():
  # key = CryptoKey.generate()
  key = CryptoKey.fromKey(b'haGwM/krSlYJ7UZG2FGPfkUJh2Pr0OVEDnrn2WUB2YY=')
  original_path = '/Users/max.s.haberman/Documents/SurveyCTO code/Field plug-ins by Max/In progress/decrypt/extras/sample-form/data.csv'
  new_path = '/Users/max.s.haberman/Documents/SurveyCTO code/Field plug-ins by Max/In progress/decrypt/extras/sample-form/encrypted_data.csv'
  csv_encrypt.encryptCsv(key, original_path, new_path, encrypt_headers = ['name', 'age', 'marital'])
  encryption_key = key.encryption_key.decode('utf-8')
  print(f'Your decryption key:\n{encryption_key}')
  print(key.whole_key)

if __name__ == '__main__':
  main()