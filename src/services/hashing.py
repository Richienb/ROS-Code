# Import module to generate hashes
import hashlib

# Function to get the hash


def gethash(filename):
    new_hash = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as file_name:
        for hash_array in iter(lambda: file_name.read(128*1024), b''):
            new_hash.update(hash_array)
    return new_hash.hexdigest()
