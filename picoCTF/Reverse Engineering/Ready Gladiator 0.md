Core Wars is a programming game, more information can be found here:

    https://vyznev.net/corewar/guide.html

The given instructions to us are in `RedCode` which is a special low level language developed for this game.

    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 1
    end

'Imp' is the first character developed by the game creators. Imp is the simplest hero in the game, and he overwrites the stack with the instruction `mov 0, 1`

pushing `mov 0, 1` means the next character that reads this code will also do the same (note that memory addresses are relative to current position, refer to the above guide).
And thus the two bots will end up tying. To avoid that we can change the source code for Imp:
    
    ;redcode
    ;name Imp Ex
    ;assert 1
    mov 0, 0
    end

`mov 0, 0` is a null move, and this allows the other hero to use the `dat` and push that in the stack, which when read by our null-moving hero, kills us. Thus, we are going to lose everygame.

flag: `picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57}`
