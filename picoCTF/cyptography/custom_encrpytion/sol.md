We've been given a custom encryption file,

    def test(plain_text, text_key):
        p = 97
        g = 31
        if not is_prime(p) and not is_prime(g):
            print("Enter prime numbers")
            return
        a = randint(p-10, p)
        b = randint(g-10, g)
        print(f"a = {a}")
        print(f"b = {b}")
        u = generator(g, a, p)
        v = generator(g, b, p)
        key = generator(v, a, p)
        b_key = generator(u, b, p)
        shared_key = None
        if key == b_key:
            shared_key = key
        else:
            print("Invalid key")
            return
        semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
        cipher = encrypt(semi_cipher, shared_key)
        print(f'cipher is: {cipher}')
    
    if __name__ == "__main__":
        message = sys.argv[1]
        test(message, "trudeau")

This has many flaws, and its a decently easy encryption process. The main thing to notice here is that there is a 2 stage encryption, which looks something like this,

    encrypt(dynamic_xor_encrypt(plain_text, text_key), shared_key)

So, while decrypting we'll need to do something like this,

    dynamic_xor_decrypt(decrypt(encrypted_text, text_key), shared_key)

We can make use of the same keys which is why the encryptions are bad! The script that does this is provided [here](./custom_encryption/custom_encryption.py).

The basic explanation is
1. `encrypt` simply multiplies each value of `ord(i)` for i in `semi_cipher` with shared_key and 311. So, to decrypt we must divide it by `shared_key * 311`.
2. `dynamic_xor_encrypt` is a simple xor (with additional reversing of the text), so to get the plaintext back, we only need to `xor` it with the same key and reverse it.

Putting these together, we get the solution script.
