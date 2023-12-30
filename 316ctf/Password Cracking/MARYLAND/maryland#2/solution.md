The dictionary-list.txt file contains the possible passwords. We need to hash each password using some hashing algorithm and check if it maches with the given one.

We will use hashcat for this!

save the given hash in a file called hash.txt using the command: `$ echo 'given_hash' > hash.txt`

commands:

Run `$ hashcat --help` to get an idea of how to use hashcat.
The parameters of our need are `-m` and `-a`.
`-m` --> specifies the type of hash to use. We will start with MD5 whos number is 0.

`-a`--> specifies the attack type. Since we are trying to hash all keywords in the dictionary-list.txt and match it with our hash, it corresponds to an attack type of 0.

`--show` --> used to show only the correct matches.

Run `$ hashcat -m 0 -a 0 hash.txt dictionary-list.txt --show` to get the flag
