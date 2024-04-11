from scto_encryption.functions import generateKey

import qrcode
from os.path import dirname, join, exists
from os import mkdir

def main():
  repo_path = dirname(dirname(__file__))
  data_path = join(repo_path, 'sample_data')

  if not exists(data_path):
    mkdir(data_path)

  key_path = join(data_path, 'sample_key_for_qr.pem')
  encryption_key = generateKey(key_path)
  print('Encryption key:')
  print(encryption_key)
  
  img = qrcode.make(encryption_key)
  img.save(join(data_path, 'qr_key.png'))

if __name__ == '__main__':
  main()
