Analysing this file using IDA, 

    sub     rsp, 88h
    mov     rax, cs:__security_cookie
    xor     rax, rsp
    mov     [rsp+88h+var_18], rax
    movups  xmm0, cs:xmmword_1400032E0
    lea     rcx, aSecretVault ; "!!!SECRET VAULT!!!\n"
    movups  xmmword ptr [rsp+88h+Str2], xmm0
    call    sub_140001010
    lea     rcx, aPleaseEnterAPa ; "Please enter a password:\n"
    call    sub_140001010
    xor     ecx, ecx        ; Ix
    call    cs:__acrt_iob_func
    mov     edx, 40h ; '@'  ; MaxCount
    lea     rcx, [rsp+88h+Buffer] ; Buffer
    mov     r8, rax         ; Stream
    call    cs:fgets
    lea     rcx, asc_140003324 ; "\n"
    call    sub_140001010
    lea     rdx, [rsp+88h+Str2] ; Str2
    lea     rcx, [rsp+88h+Buffer] ; Str1
    call    sub_140001070
    xor     eax, eax
    mov     rcx, [rsp+88h+var_18]
    xor     rcx, rsp        ; StackCookie
    call    __security_check_cookie
    add     rsp, 88h
    retn

This is the `main` function. Its putting the message "!!!SECRET VALUE!!!" and then asking us to enter a password. 

- The `__acrt_iob_func` apparently initialises the input/output stream, according to [this](https://stackoverflow.com/questions/47948234/assembly-code-of-a-hello-world-program-in-c) stack exchange answer.

- The function `sub_140001010` is called on out input and its formats the string entered in a specfic way, but thats not really important. 

- We have 2 strings here `str1` and `str2`, where `str2` is something we already know and str1 is the buffer that our input is stored into.

- The function `sub_140001070` is the one that does some stuff to our input and then compares it to `str2`.

We can check the pseudocode for `sub_140001070`. Note that I have patched it to ignore the check for the length being equal to 16. (changed those instructions to `nop` cause I thought it might be helpful, but it doesn't really matter). 

In your pseudocode you may see an additional if statement after `while (Str1[v3]);`, and its alright.
    
    int __fastcall sub_140001070(char *Str1, char *Str2)
    {
      __int64 v3; // rax
      __int64 v4; // r10
      int v5; // r9d
      int v6; // ecx
      char v7; // al
      int v8; // ecx
      char v9; // al
      int v10; // ecx
      char v11; // al
      int v12; // ecx
      char v13; // al
      int v14; // ecx
      char v15; // al
      char v17[80]; // [rsp+20h] [rbp-68h] BYREF
    
      v3 = -1LL;
      do
        ++v3;
      while ( Str1[v3] );
      v4 = 0LL;
      v5 = 2;
      do
      {
        v6 = (v5 - 1) % 5;
        if ( v5 - 1 == 5 * ((v5 - 1) / 5) )
        {
          v7 = 14;
        }
        else if ( v6 == 4 )
        {
          v7 = 13;
        }
        else if ( v6 == 3 )
        {
          v7 = 12;
        }
        else
        {
          v7 = (v6 == 2) + 10;
        }
        Str1[v4] += v7;
        v8 = v5 % 5;
        if ( v5 == 5 * (v5 / 5) )
        {
          v9 = 14;
        }
        else if ( v8 == 4 )
        {
          v9 = 13;
        }
        else if ( v8 == 3 )
        {
          v9 = 12;
        }
        else
        {
          v9 = (v8 == 2) + 10;
        }
        Str1[v4 + 1] += v9;
        v10 = (v5 + 1) % 5;
        if ( v5 + 1 == 5 * ((v5 + 1) / 5) )
        {
          v11 = 14;
        }
        else if ( v10 == 4 )
        {
          v11 = 13;
        }
        else if ( v10 == 3 )
        {
          v11 = 12;
        }
        else
        {
          v11 = (v10 == 2) + 10;
        }
        Str1[v4 + 2] += v11;
        v12 = (v5 + 2) % 5;
        if ( v5 + 2 == 5 * ((v5 + 2) / 5) )
        {
          v13 = 14;
        }
        else if ( v12 == 4 )
        {
          v13 = 13;
        }
        else if ( v12 == 3 )
        {
          v13 = 12;
        }
        else
        {
          v13 = (v12 == 2) + 10;
        }
        Str1[v4 + 3] += v13;
        v14 = (v5 + 3) % 5;
        if ( v5 + 3 == 5 * ((v5 + 3) / 5) )
        {
          v15 = 14;
        }
        else if ( v14 == 4 )
        {
          v15 = 13;
        }
        else if ( v14 == 3 )
        {
          v15 = 12;
        }
        else
        {
          v15 = (v14 == 2) + 10;
        }
        Str1[v4 + 4] += v15;
        v5 += 5;
        v4 += 5LL;
      }
      while ( v4 < 15 );
      if ( strncmp(Str1, Str2, 15uLL) )
        return sub_140001010("VERIFICATION FAILED!\n");
      strcpy(v17, "CONGRATULATIONS!!!\nYOU UNLOCKED THE SECRET VAULT!\nYOUR TREASURE -> $1.000.000");
      return sub_140001010("%s\n", v17);
    }

There is some string manipulation going on. Its easy to see that just one patch (where it calls `strcmp` and tests the two values) can solve the problem. But, the real challenge is reversing this.

The algorithm is pretty simple, hence I have written a python script that reverses this for me [here](./noOFF's_VaultCrackme/script.py)
