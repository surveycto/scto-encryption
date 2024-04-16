from scto_encryption.functions import decryptCsv

from os.path import join

def main():
  data_path = 'C:\\Users\\surveycto.user\\Documents\\Encrypt data\\'
  key_path = join(data_path, 'sample_key.pem')
  encrypted_path = join(data_path, 'encrypted_data.csv')
  decrypted_path = join(data_path, 'data_decrypted.csv')
  decryptCsv(key_path, encrypted_path, decrypted_path)

if __name__ == '__main__':
  main()