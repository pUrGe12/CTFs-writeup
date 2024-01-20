The problem gives us a source code and we can see it has several functions but the big ones are all commented out.

Connecting with the program, we are asked to input the function name `getRandomNumber` and look at the source code, we can see that it takes the input as `eval`

This is dangerous because it allows `code injection`. Thus typing in 'win' will print out the flag in hex.

flag: `picoCTF{4_d14m0nd_1n_7h3_r0ugh_b523b2a1}`
