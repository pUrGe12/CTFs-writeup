from random import randint
import sys

def generator(g, x, p):
    return pow(g, x) % p

def decrypt(cipher: list, shared_key):
    semi_cipher = []
    for i in cipher:
        semi_cipher.append(chr(i//(shared_key*311)))
    return semi_cipher

def dynamic_xor_decrypt(semi_cipher, text_key):
    plaintext = ""
    key_length = len(text_key)
    for i, char in enumerate(semi_cipher):
        key_char = text_key[i % key_length]
        plaintext_char = chr(ord(char) ^ ord(key_char))
        plaintext += plaintext_char
    return plaintext[::-1]

a = 95
b = 21

p = 97 # this was hard coded
g = 31 # this was hard coded

# these values will be generated as it is
u = generator(g,a,p)
v = generator(g,b,p)
key = generator(v,a,p)
shared_key = generator(u,b,p)

# this is the given ciphertext
cipher = [237915, 1850450, 1850450, 158610, 2458455, 2273410, 1744710, 1744710, 1797580, 1110270, 0, 2194105, 555135, 132175, 1797580, 0, 581570, 2273410, 26435, 1638970, 634440, 713745, 158610, 158610, 449395, 158610, 687310, 1348185, 845920, 1295315, 687310, 185045, 317220, 449395]
text_key = "trudeau"

print(dynamic_xor_decrypt(decrypt(cipher, shared_key), text_key))
