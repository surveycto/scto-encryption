from scto_encryption.functions import encryptCsv

from os.path import dirname, join

def main():
  repo_path = dirname(dirname(__file__))
  data_path = join(repo_path, 'sample_data')
  key_path = join(data_path, 'sample_key.pem')
  source_path = join(data_path, 'data.csv')
  encrypted_path = join(data_path, 'encrypted_data.csv')
  encryptCsv(key_path, source_path, encrypted_path, exclude_headers = ['id_key'])

if __name__ == '__main__':
  main()