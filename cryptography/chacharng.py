from bitstring import Bits

def roll(x, n):
        bits = Bits(uint=x, length=32)
        return (bits[n:] + bits[:n]).uint

def quarter_round(a, b, c, d):
        a = (a+b) % 2**32; d = roll(d^a, 16)
        c = (c+d) % 2**32; b = roll(b^c, 12)
        a = (a+b) % 2**32; d = roll(d^a,  8)
        c = (c+d) % 2**32; b = roll(b^c,  7)
        return a, b, c, d

print('Roll is', roll(2,4))

print('Quarter round is', quarter_round(2,4,6,8))
