import hashlib
def gethash(filename):
 sha256_hash=hashlib.sha256()
 with open(filename,"rb")as file_contents:
  for byte_block in iter(lambda:file_contents.read(4096),b""):
   sha256_hash.update(byte_block)
   return sha256_hash.hexdigest()
# Created by pyminifier (https://github.com/liftoff/pyminifier)
