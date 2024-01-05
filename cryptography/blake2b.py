# Import the blake2b function from the hashlib module.
# Blake2b is a cryptographic hash function.
from hashlib import blake2b

# Create a new blake2b hash object.
# Set the digest size to 32 bytes (256 bits).
# You can also create a new blake2b hash object without a digest size.
# The digest size determines the length of the output hash. 
h = blake2b(digest_size=32)

# Update the hash object with the byte string 'Hello world'.
# The b before the string creates a byte literal.
# Hash functions like blake2b work on bytes, not on strings.
h.update(b'Hello world')

# Compute the final hash (digest) of the data passed to the update method.
# The hexdigest method returns the hash as a string of hexadecimal digits.
# This is useful for human-readable representations.
hash = h.hexdigest()

# Print the computed hash.
# TODO: Consider handling this hash in a secure manner if used in a sensitive context.
print(hash)
