from scto_encryption.functions import encryptCsv

from os.path import join

def main():
  data_path = 'C:\\Users\\surveycto.user\\Documents\\Encrypt data\\'
  key_path = join(data_path, 'sample_key.pem')
  source_path = join(data_path, 'data.csv')
  encrypted_path = join(data_path, 'encrypted_data.csv')
  encryptCsv(key_path, source_path, encrypted_path, exclude_headers = ['id_key'])

if __name__ == '__main__':
  main()