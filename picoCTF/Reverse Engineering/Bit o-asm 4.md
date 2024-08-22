This is the diassembly given to us,
    
    <+0>:     endbr64 
    <+4>:     push   rbp
    <+5>:     mov    rbp,rsp
    <+8>:     mov    DWORD PTR [rbp-0x14],edi
    <+11>:    mov    QWORD PTR [rbp-0x20],rsi
    <+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
    <+22>:    cmp    DWORD PTR [rbp-0x4],0x2710
    <+29>:    jle    0x55555555514e <main+37>
    <+31>:    sub    DWORD PTR [rbp-0x4],0x65
    <+35>:    jmp    0x555555555152 <main+41>
    <+37>:    add    DWORD PTR [rbp-0x4],0x65
    <+41>:    mov    eax,DWORD PTR [rbp-0x4]
    <+44>:    pop    rbp
    <+45>:    ret

Whats happening here is:

1. In instruction `<main+15>` we are defining a DWORD PTR at `rbp-0x4`. See, `rbp` from what I see it as, is like a stack, and when we define `PTRs` like this, it references the value stored in this specfic memory location of the stack

   So, in this case, it has allocated 4 bytes from the top of the stack to a specific value which is `0x9fe1a`.

2. Now, it uses `cmp` (which is used for checking less than or greater than, unlike `test` which is used to check equality) on the same memory location in the stack it just defined, and a new value. This means, it's comparing `0x9fe1a` with `0x2710`.

3. The `jle` instruction stands for **"jump if less than"**. This checks if `0x9fe1a` is less than `0x2710`, and if it is, then it jumps to `main+37`. In our case, it isn't, and hence this jump doesn't take place.

4. Now, it uses `sub` instruction, which is simple **subtraction** and subtracts `0x65` from `0x9fe1a`. This gives us a decimal value of **"654773"**.

5. Then it directly jumps to `<main+41>` and from there, it pushes the new value to `eax`.

Thus, `eax` contains the value "654773".
