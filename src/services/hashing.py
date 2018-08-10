# Import module to generate hashes
import hashlib

# Function to get the hash


def gethash(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as file_contents:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file_contents.read(4096), b""):
            sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
