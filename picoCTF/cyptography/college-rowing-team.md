We've been given an encryption code and the message. Looking through the code,

    msgs = [
    b'I just cannot wait for rowing practice today!',
    b'I hope we win that big rowing match next week!',
    b'Rowing is such a fun sport!'
        ]

    msgs.append(flag)
    msgs *= 3
    random.shuffle(msgs)
the flag is being added to the message list and the entire list is duplicated in itself 3 times, and then randomly shuffled. Then,

    for msg in msgs:
    p = getPrime(1024)
    q = getPrime(1024)
    n = p * q
    e = 3
    m = bytes_to_long(msg)
    c = pow(m, e, n)
    with open('encrypted-messages.txt', 'a') as f:
        f.write(f'n: {n}\n')
        f.write(f'e: {e}\n')
        f.write(f'c: {c}\n\n')
Each message in the list is RSA encrypted and the cipher text is written in the `encrypted-message.txt` file. Since the exponent is small, we can assume that the modulo operation does not take place (it is usually valid in challenges like these)

Using the script provided we can try each cipher text manually (automation is possible by not needed here as worst case is small) and decipher it.
