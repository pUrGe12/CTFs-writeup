# challenge

We've been given a binary and a scrambled flag, our goal is to reverse engineer this cipher. This was a pretty easy cipher. Let's open this file in Ghidra,

    void main(void)
    
    {
      size_t either1or0;
      char buffer [23];
      char wheredyoucomefrom;
      int local_2c;
      FILE *revThisfile;
      FILE *flagFile;
      uint j;
      int i;
      char flagval;
      
      flagFile = fopen("flag.txt","r");
      revThisfile = fopen("rev_this","a");
      if (flagFile == (FILE *)0x0) {
        puts("No flag found, please make sure this is run on the server");
      }
      if (revThisfile == (FILE *)0x0) {
        puts("please run this on the server");
      }
      either1or0 = fread(buffer,0x18,1,flagFile);
      local_2c = (int)either1or0;
      if ((int)either1or0 < 1) {
                        /* WARNING: Subroutine does not return */
        exit(0);
      }
      for (i = 0; i < 8; i = i + 1) {
        flagval = buffer[i];
        fputc((int)flagval,revThisfile);
      }
      for (j = 8; (int)j < 23; j = j + 1) {
        if ((j & 1) == 0) {
          flagval = buffer[(int)j] + '\x05';
        }
        else {
          flagval = buffer[(int)j] + -2;
        }
        fputc((int)flagval,revThisfile);
      }
      flagval = wheredyoucomefrom;
      fputc((int)wheredyoucomefrom,revThisfile);
      fclose(revThisfile);
      fclose(flagFile);
      return;
    }

This is the main function as analysed by Ghidra. I have already formatted the variable names as I deemed fit. So, what's happening here is,

1. Make a flag.txt file which contains a string of more than 24 bytes. (if you want to run the binary and see)

`fread` is called like `fread(buffer,0x18,1,flagFile)`. A quick look at the documentation will explain this syntax,

2. This basically, at least 1 element of 24 bytes is being read by fread.

3. This number `either1or0` can either be 1 or 0, cause it wants to read only 1 element of 24 bytes through `fread`.

Then we go over the elements of the buffer (which now contains 24 characters), one by one.

The first 8 bytes are added to the rev_this file as it is, without any processing using fputc(). `(this is "picoCTF{" part).`

5. Then we go over the 9th byte onwards and if the iterator is even

--> Its LSB will be 0, --> j & 1 == 0 is True:
--> else false

6. The last byte is directly added to the scrambled_flag, and a quick look (in `rev_this`) tells us that this is the character "}"

This allows a very simple construction of a decrypt script using python, as shown below,

    buffer = "picoCTF{w1{1wq8/7376j.:}"
    
    actual_flag = []
    
    for i in range(0, 8):
    	actual_flag += buffer[i]
    
    # Loop from the 9th character onwards (index 8 in Python)
    for j in range(8, len(buffer)):
        if j % 2 == 0:  # If the iterator is even
            flagval = ord(buffer[j]) - 0x05
        else:  # If the iterator is odd
            flagval = ord(buffer[j]) + 2
    
        # Convert flagval back to a character and add to the list
        actual_flag.append(chr(flagval))
    
    # Join the list into a final string
    reversed_output = ''.join(actual_flag)
    
    print(reversed_output + "}")


