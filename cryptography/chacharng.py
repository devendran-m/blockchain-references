# Import the Bits class from the bitstring module.
# This module provides tools for manipulating binary data.
from bitstring import Bits

def roll(x, n):
    # This function performs a bitwise rotation (circular shift) of 32-bit integers.
    # x: The integer to be rotated.
    # n: The number of bits to rotate by.

    # Convert the integer x into a 32-bit binary representation.
    bits = Bits(uint=x, length=32)

    # Perform the rotation: bits[n:] gets the bits from position n to the end,
    # and bits[:n] gets the first n bits. Concatenating these two slices
    # results in a rotated bitstring.
    # The .uint converts the bitstring back to an unsigned integer.
    return (bits[n:] + bits[:n]).uint

def quarter_round(a, b, c, d):
    # This function performs one quarter round of the ChaCha20 block cipher.
    # It takes four 32-bit unsigned integers as input and returns four transformed integers.
    # a, b, c, d: 32-bit unsigned integers.

    # The quarter round transformations are performed as per the ChaCha20 algorithm.
    # Each line consists of an addition modulo 2^32 and a bitwise rotation.
    a = (a+b) % 2**32; d = roll(d^a, 16)
    c = (c+d) % 2**32; b = roll(b^c, 12)
    a = (a+b) % 2**32; d = roll(d^a,  8)
    c = (c+d) % 2**32; b = roll(b^c,  7)

    # Return the transformed values.
    return a, b, c, d

# Test the roll function with a simple example.
# TODO: Add more comprehensive tests to validate the roll function.
print('Roll is', roll(2,4))

# Test the quarter_round function with example values.
# TODO: Add more tests and validate against known ChaCha20 test vectors.
print('Quarter round is', quarter_round(2,4,6,8))

