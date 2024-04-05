from scto_encryption.functions import decryptCsv

from os.path import dirname, join

def main():
  repo_path = dirname(dirname(__file__))
  data_path = join(repo_path, 'sample_data')
  key_path = join(data_path, 'sample_key.pem')
  encrypted_path = join(data_path, 'encrypted_data.csv')
  decrypted_path = join(data_path, 'data_decrypted.csv')
  decryptCsv(key_path, encrypted_path, decrypted_path)

if __name__ == '__main__':
  main()