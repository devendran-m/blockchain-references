import os
from chacha20poly1305 import ChaCha20Poly1305

key = os.urandom(32)
print(key)
cip = ChaCha20Poly1305(key)
print(cip)

nonce = os.urandom(12)
print(nonce)

ciphertext = cip.encrypt(nonce, b'test')
print(ciphertext)

plaintext = cip.decrypt(nonce, ciphertext)
print(plaintext)