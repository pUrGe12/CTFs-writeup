Looking at the source code we can see that it called a function `filter` before passing our input to eval, which makes sure that 'win' is not in the input.

Thus, there is no way to call the function win itself. We need to do what win dooes in one line.

The eval function also adds '()' after each string making sure that its a callable function. Thus, we can use an injection like the one below:

    print(open('flag.txt','r').read().strip())#

the '#' makes sure that the '()' do not affect our injection. 

flag: `picoCTF{f1l73r5_f41l_c0d3_r3f4c70r_m1gh7_5ucc33d_b924e8e5}`
