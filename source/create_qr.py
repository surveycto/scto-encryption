from scto_encryption.functions import generateKey

import qrcode
from os.path import join

def main():
  data_path = 'C:\\Users\\surveycto.user\\Documents\\Encrypt data\\'

  key_path = join(data_path, 'sample_key_for_qr.pem')
  encryption_key = generateKey(key_path)
  print('Encryption key:')
  print(encryption_key)
  
  img = qrcode.make(encryption_key)
  img.save(join(data_path, 'qr_key.png'))

if __name__ == '__main__':
  main()
