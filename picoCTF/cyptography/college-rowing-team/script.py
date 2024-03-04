#!/usr/bin/env python3

from gmpy2 import iroot
from Crypto.Util.number import long_to_bytes

c = int(input('enter the cipher text: '))
e = int(input('enter the exponent: '))

msg, is_correct = iroot(c, e)
print(long_to_bytes(msg))
