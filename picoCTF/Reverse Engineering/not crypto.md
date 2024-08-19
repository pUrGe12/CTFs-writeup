This challenge led me astray for a while, so, I shall put my attempt first (I am sure it can be done this way, I am just not competent enough), and then explain the actual solution.

# My Idea
---
I opened this first with `IDA` and checked the assembly. I was thinking in terms of patching this binary to directly reveal the flag.

    .text:0000000000001385 loc_1385:                               ; CODE XREF: main+A2A↓j
    .text:0000000000001385                                         ; main+BF4↓j
    .text:0000000000001385                 mov     rbx, [rsp+208h+var_1E8]
    .text:000000000000138A                 movsxd  rdx, eax
    .text:000000000000138D                 add     eax, 1
    .text:0000000000001390                 movzx   edx, byte ptr [rsp+rdx+208h+var_98]
    .text:0000000000001398                 xor     [rbx], dl
    .text:000000000000139A                 add     rbx, 1
    .text:000000000000139E                 mov     [rsp+208h+var_1E8], rbx
    .text:00000000000013A3                 cmp     [rsp+208h+var_1D8], rbx
    .text:00000000000013A8                 jnz     short loc_1380
    .text:00000000000013AA                 mov     rsi, [rsp+208h+s2] ; s2
    .text:00000000000013AF                 mov     edx, 40h ; '@'  ; n
    .text:00000000000013B4                 mov     rdi, [rsp+208h+s1] ; s1
    .text:00000000000013B9                 call    _memcmp
    .text:00000000000013BE                 mov     r12d, eax
    .text:00000000000013C1                 test    eax, eax
    .text:00000000000013C3                 jnz     loc_1A9F
    .text:00000000000013C9                 lea     rdi, aYepThatSIt ; "Yep, that's it!"
    .text:00000000000013D0                 call    _puts

This caught my eye first. Even though it's not directly printing the flag, I figured reaching where would be step 1. To do that, we need to first check this part,
    
    .text:0000000000001A8A                 cmp     al, 0FFh
    .text:0000000000001A8C                 jz      short loc_1AB6
The reason was evident from the last few lines of ghidra,

    lVar23 = (long)iVar15;
    iVar15 = iVar15 + 1;
    *(byte *)local_1e8 = *(byte *)local_1e8 ^ local_98[lVar23];
    local_1e8 = (undefined4 *)((long)local_1e8 + 1);
    if (local_48 == local_1e8) {
      iVar15 = memcmp(&local_88,local_198,0x40);
      if (iVar15 != 0) {
        puts("Nope, come back later");
      }
      else {
        puts("Yep, that\'s it!");
      }
      if (local_40 == *(long *)(in_FS_OFFSET + 0x28)) {
        return iVar15 != 0;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
      }
    } while( true );

The `if (local_48 == local_1e8)` condition needed to be satisfied in order to get inside the `memcmp` command. In order to make sure that we jump inside, I changed the `jz` instruction (which basically means jump only if true) to a normal jump (with no conditions)

This can be done by changing the bytes of the `jz` instruction from "74 28 83 C0 01 88 84 14 60 01 00 00 31 C0 E9 E6" to "EB 28 83 C0 01 88 84 14 60 01 00 00 31 C0 E9 E6". This is because, the `jmp` and `jz` instructions have their `opcodes` as "EB" and "74" respectively. 
The next byte corresponds to the jump offset, which determines which code segment you want to jump to. We'll keep this the same since I want to jump to the same segment it would have, had the condition been satisfied.
    
    .text:0000000000001A8A                 cmp     al, 0FFh
    .text:0000000000001A8C                 jmp     short loc_1AB6

Then we eventually end up in the `loc_1385` as mentioned in the start. Here we can see that there is a `test` being performed. The `test` command is basically a baby version of the `cmp` command. They perform the same tasks. The result of this test determines the next instruction. If the test gives `False`, then the program jumps to `loc_1A9F` which prints the "Nope, come back later" message. 

Thus, my goal was to see if I can firstly bypass this check. In order to do that, I changed the `test` instruction to a `nop` by replacing the first 2 bytes of it by 90 and 90. Then, I changed the `jnz` instruction also to `nop` by replacing the first 6 bytes of it with 90s. 

So, `jnz` went from "0F 85 D6 06 00 00 48 8D 3D 87 0C 00 00 E8 5B FC" t "90 90 90 90 90 90 48 8D 3D 87 0C 00 00 E8 5B FC". It finally looked something like this, 
    
    .text:0000000000001385 loc_1385:                               ; CODE XREF: main+A2A↓j
    .text:0000000000001385                                         ; main+BF4↓j
    .text:0000000000001385                 mov     rbx, [rsp+208h+var_1E8]
    .text:000000000000138A                 movsxd  rdx, eax
    .text:000000000000138D                 add     eax, 1
    .text:0000000000001390                 movzx   edx, byte ptr [rsp+rdx+208h+var_98]
    .text:0000000000001398                 xor     [rbx], dl
    .text:000000000000139A                 add     rbx, 1
    .text:000000000000139E                 mov     [rsp+208h+var_1E8], rbx
    .text:00000000000013A3                 cmp     [rsp+208h+var_1D8], rbx
    .text:00000000000013A8                 jnz     short loc_1380
    .text:00000000000013AA                 mov     rsi, [rsp+208h+s2] ; s2
    .text:00000000000013AF                 mov     edx, 40h ; '@'  ; n
    .text:00000000000013B4                 mov     rdi, [rsp+208h+s1] ; s1
    .text:00000000000013B9                 call    _memcmp
    .text:00000000000013BE                 mov     r12d, eax
    .text:00000000000013C1                 nop
    .text:00000000000013C2                 nop
    .text:00000000000013C3                 nop
    .text:00000000000013C4                 nop
    .text:00000000000013C5                 nop
    .text:00000000000013C6                 nop
    .text:00000000000013C7                 nop
    .text:00000000000013C8                 nop
    .text:00000000000013C9                 lea     rdi, aYepThatSIt ; "Yep, that's it!"
    .text:00000000000013D0                 call    _puts

When I apply changes and run the binary, I get the message "Yep, that's it!". BUT, I don't get the flag.

My first though was to load the `rsi` and `rdi` registers and print their values (cause one of them must be the flag since, they're the ones being compared). I did this first with the `rsi` reigster and I hit jackpot! Until I didn't.

This is what my assembly looked like,
    
    .text:0000000000001385 loc_1385:                               ; CODE XREF: main+A2A↓j
    .text:0000000000001385                                         ; main+BF4↓j
    .text:0000000000001385                 mov     rbx, [rsp+208h+var_1E8]
    .text:000000000000138A                 movsxd  rdx, eax
    .text:000000000000138D                 add     eax, 1
    .text:0000000000001390                 movzx   edx, byte ptr [rsp+rdx+208h+var_98]
    .text:0000000000001398                 xor     [rbx], dl
    .text:000000000000139A                 add     rbx, 1
    .text:000000000000139E                 mov     [rsp+208h+var_1E8], rbx
    .text:00000000000013A3                 cmp     [rsp+208h+var_1D8], rbx
    .text:00000000000013A8                 jnz     short loc_1380
    .text:00000000000013AA                 mov     rsi, [rsp+208h+s2] ; s2
    .text:00000000000013AF                 mov     edx, 40h ; '@'  ; n
    .text:00000000000013B4                 mov     rdi, [rsp+208h+s1] ; s1
    .text:00000000000013B9                 call    _memcmp
    .text:00000000000013BE                 mov     r12d, eax
    .text:00000000000013C1                 mov     rsi, rdi
    .text:00000000000013C4                 nop
    .text:00000000000013C5                 nop
    .text:00000000000013C6                 nop
    .text:00000000000013C7                 nop
    .text:00000000000013C8                 nop
    .text:00000000000013C9                 nop
    .text:00000000000013CA                 nop
    .text:00000000000013CB                 nop
    .text:00000000000013CC                 nop
    .text:00000000000013CD                 nop
    .text:00000000000013CE                 nop
    .text:00000000000013CF                 nop
    .text:00000000000013D0                 call    _puts

I used the last `_puts` command to print the `rsi` register's value (turns out that puts works on the `rdi` register, so you need to first move the `rsi` value into the `rdi` register). I then ran the code and viola!

[image of binary data](./screenshot.png)

# The actual method 
