from hashlib import blake2b
h = blake2b(digest_size=32)
h.update(b'Hello world')
hash = h.hexdigest()
print(hash)