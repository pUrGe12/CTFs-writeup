# Simple Keygen me

When we open the provided binary, its evident that it's packed using UPX. If you run strings, you'll see hints of that. First, we'll unpack it,

    .\upx.exe -d <binary_name>.exe

Now, we'll open this with IDA. Clearly, this binary isn't hard to patch, but that's not the challenge here. The challenge is to `keygen` this bad boy. So, let's look at the code the validates the `username`,

    .text:00000000004016F4                 lea     rdx, aPleaseEnterAUs ; "Please enter a username: "
    .text:00000000004016FB                 mov     rcx, cs:off_405420
    .text:0000000000401702 ;   try {
    .text:0000000000401702                 call    _ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc ; std::operator<<<std::char_traits<char>>(std::basic_ostream<char,std::char_traits<char>> &,char const*)
    .text:0000000000401707                 mov     rdx, cs:off_405430
    .text:000000000040170E                 mov     rcx, rax
    .text:0000000000401711                 call    _ZNSolsEPFRSoS_E ; std::ostream::operator<<(std::ostream & (*)(std::ostream &))
    .text:0000000000401716                 lea     rax, [rbp-10h+var_40]
    .text:000000000040171A                 mov     rdx, rax
    .text:000000000040171D                 mov     rcx, cs:off_405410
    .text:0000000000401724                 call    _ZStrsIcSt11char_traitsIcESaIcEERSt13basic_istreamIT_T0_ES7_RNSt7__cxx1112basic_stringIS4_S5_T1_EE ; std::operator>><char,std::char_traits<char>,std::allocator<char>>(std::basic_istream<char,std::char_traits<char>> &,std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>> &)
    .text:0000000000401729                 lea     rax, [rbp-10h+var_40]
    .text:000000000040172D                 mov     rcx, rax
    .text:0000000000401730                 call    _ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE6lengthEv ; std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(void)
    .text:0000000000401735                 cmp     rax, 3
    .text:0000000000401739                 jbe     short loc_40174D
    .text:000000000040173B                 lea     rax, [rbp-10h+var_40]
    .text:000000000040173F                 mov     rcx, rax
    .text:0000000000401742                 call    _ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE6lengthEv ; std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(void)
    .text:0000000000401747                 cmp     rax, 8
    .text:000000000040174B                 jbe     short loc_401754
    .text:000000000040174D
    .text:000000000040174D loc_40174D:                             ; CODE XREF: main+8A↑j
    .text:000000000040174D                 mov     eax, 1
    .text:0000000000401752                 jmp     short loc_401759
    .text:0000000000401754 ; ---------------------------------------------------------------------------
    .text:0000000000401754
    .text:0000000000401754 loc_401754:                             ; CODE XREF: main+9C↑j
    .text:0000000000401754                 mov     eax, 0
    .text:0000000000401759
    .text:0000000000401759 loc_401759:                             ; CODE XREF: main+A3↑j
    .text:0000000000401759                 test    al, al
    .text:000000000040175B                 jz      short loc_401795
    .text:000000000040175D                 lea     rdx, aStringCC

In the initial lines of code, it essentially defines **libc** functions like `std::cin` and `std::cout` and take in user input. It also defines the `length()` function which is what is being used to check the length of the username.

    Keep in mind that 
        test eax, eax 
    is equivalent to
        cmp eax, 0
        
Now the main logic to check username comes here,

    .text:0000000000401735                 cmp     rax, 3
    .text:0000000000401739                 jbe     short loc_40174D
    .text:000000000040173B                 lea     rax, [rbp-10h+var_40]
    .text:000000000040173F                 mov     rcx, rax
    .text:0000000000401742                 call    _ZNKSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE6lengthEv ; std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(void)
    .text:0000000000401747                 cmp     rax, 8
    .text:000000000040174B                 jbe     short loc_401754
    .text:000000000040174D
    .text:000000000040174D loc_40174D:                             ; CODE XREF: main+8A↑j
    .text:000000000040174D                 mov     eax, 1
    .text:0000000000401752                 jmp     short loc_401759
    .text:0000000000401754 ; ---------------------------------------------------------------------------
    .text:0000000000401754
    .text:0000000000401754 loc_401754:                             ; CODE XREF: main+9C↑j
    .text:0000000000401754                 mov     eax, 0
    .text:0000000000401759
    .text:0000000000401759 loc_401759:                             ; CODE XREF: main+A3↑j
    .text:0000000000401759                 test    al, al
    .text:000000000040175B                 jz      short loc_401795
    .text:000000000040175D                 lea     rdx, aStringCC

---

We compare the length of the input string to 3, and if its less that or equal to 3 (this is the `jbe` instruction) it jumps to `loc_40174D` which pushes the value '1' into the `eax` register.

But if it's greater than 3, then the execution continues and we again call the length function, store that in `rax` and compare it to 8. 
If its less than or equal to 8 as well, then we set the **eax value as 0**, and jump directly to `loc_401759` (this is because jmp is an unconditional jump statement)

Now, the `first byte of eax is being compared to 0 using test` (check out the note from above).

    test al, al

`al` represents the first 8 bits of the eax register. Similar to this are `ah`, the next 8 bits after `al`, `ax` which has the first 16 bits of `eax` and more. 

This implies we want `eax` to have 0 and not 1, and hence, the length of the username must be **strictly more than 3 and less than or equal to 8**. This is because, if it isn't then it `doesn't` take the jump and asks you enter the right username.

Password 
---

Now that it has taken the jump, we've got to crack the password.
