from scto_encryption.crypto import CryptoKey
from scto_encryption.csv_encrypt import encryptCsv

from os.path import dirname, join

def main():
  # key = CryptoKey.generate()
  repo_path = dirname(dirname(__file__))
  key = CryptoKey.fromKey(b'haGwM/krSlYJ7UZG2FGPfkUJh2Pr0OVEDnrn2WUB2YY=')
  data_path = join(repo_path, 'sample_data')
  original_path = join(data_path, 'data.csv')
  new_path = join(data_path, 'encrypted_data.csv')
  encryptCsv(key, original_path, new_path, exclude_headers = ['id_key'])
  encryption_key = key.encryption_key.decode('utf-8')
  print(f'Your decryption key:\n{encryption_key}')
  print(key.whole_key)

if __name__ == '__main__':
  main()