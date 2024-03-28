from scto_encryption.crypto import CryptoKey
from scto_encryption.csv_encrypt import decryptCsv

from os.path import dirname, join

def main():
  # key = CryptoKey.generate()
  repo_path = dirname(dirname(__file__))
  key = CryptoKey.fromKey(b'haGwM/krSlYJ7UZG2FGPfkUJh2Pr0OVEDnrn2WUB2YY=')
  data_path = join(repo_path, 'sample_data')
  encrypted_path = join(data_path, 'encrypted_data.csv')
  decrypted_path = join(data_path, 'data_new.csv')
  decryptCsv(key, encrypted_path, decrypted_path)

if __name__ == '__main__':
  main()