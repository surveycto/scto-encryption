from scto_encryption.crypto import Encryption

import qrcode
from os.path import dirname, join

def main():
  encryption1 = Encryption.initWithKey()
  key = encryption1.key
  string_enc_key = key.encryption_key.decode('utf-8')
  print('Encryption key:')
  print(string_enc_key)
  
  img = qrcode.make(string_enc_key)
  repo_path = dirname(dirname(__file__))
  data_path = join(repo_path, 'sample_data')
  img.save(join(data_path, 'qr_key.png'))

if __name__ == '__main__':
  main()
