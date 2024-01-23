Here, we have been asked to win atleast once against Imp. 

Recall that Imp only multiplies itself across the stack, and has no kill (dat) in it, which means that our warrior will never lose against Imp. It can win or tie.

In order to win, we can employ the `Dwarf` warrior. His source code: (the lines followed by ';' are comments)

    ;redcode
    ;name Imp Ex
    ;assert 1
    ADD #4, 3
    MOV 2, @2
    JMP -2
    DAT #0, #0
    end

this code was taken from:

    https://vyznev.net/corewar/guide.html

Using this warrior we can able to win 22 times.

flag: `picoCTF{1mp_1n_7h3_cr055h41r5_dba6f40d}`
