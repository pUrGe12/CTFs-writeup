Here, we can run checksec and figure out that all the security measures have been disabled. (including NX). If we decompile the binary using ghidra, we can see that there aren't any interesting functions we can return too. 

This challenge is therefore a `ret2shellcode` challenge. We figure out the offset for the return pointer, and then inject our shell-code into that. 

This shellcode is to spawn a bash shell in the server where the program is running. There might be something interesting. 
