We have been given a `upx` compressed file. This we can evidently see using `strings` on the given binary.

    strings unpackme

gives, 

    $Info: This file is packed with the UPX executable packer http://upx.sf.net $
    $Id: UPX 3.95 Copyright (C) 1996-2018 the UPX Team. All Rights Reserved. $

We can download the `upx` binary to decompress it from this [link](https://github.com/upx/upx/releases/tag/v4.2.4). Running the following command will decompress it

    ./upx -d unpackme

Then we can open this file on `IDA` and observe the following instructions

    .text:0000000000401E9C                 lea     rdi, aWhatSMyFavorit ; "What's my favorite number? "
    .text:0000000000401EA3                 mov     eax, 0
    .text:0000000000401EA8                 call    printf
    .text:0000000000401EAD                 lea     rax, [rbp+var_3C]
    .text:0000000000401EB1                 mov     rsi, rax
    .text:0000000000401EB4                 lea     rdi, aD         ; "%d"
    .text:0000000000401EBB                 mov     eax, 0
    .text:0000000000401EC0                 call    __isoc99_scanf
    .text:0000000000401EC5                 mov     eax, [rbp+var_3C]
    .text:0000000000401EC8                 cmp     eax, 0B83CBh
    .text:0000000000401ECD                 jnz     short loc_401F12

These instructions basically mean, the value we enter (after the `call __isoc99_scanf` instruction), is being copared to a certian hex value.

If the comparision fails, then we jump to `loc_401F12`
    
    .text:0000000000401F12 loc_401F12:                             ; CODE XREF: main+8A↑j
    .text:0000000000401F12                 lea     rdi, aSorryThatSNotI ; "Sorry, that's not it!"
    .text:0000000000401F19                 call    puts

This means, the check must pass!

Since, we know the hex value, we can convert that to decimal (since the program expects a `long`). We pass that to the program and get our flag.
