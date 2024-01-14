we can do

    less clue.txt
to get a hint for the next flag: `Look around the file system for the other ingredient`

Thus, we need to explore the file system. We can do this using `directory/path transversal`. We can go back a few directories and list its contents using:

    cd ../../../../../; ls -la
to get the following directories in the system of which 2 are of significance.

    total 88
    .
    .
    drwxr-xr-x   4 root root  4096 Feb 10  2019 home
    .
    .
    drwx------   4 root root  4096 Feb 10  2019 root
    .
    .

navigating to home directory and listing its contents:

    cd /home; ls -la
we see that there is a directory named rick. Entering that and listing contents:

    cd /home/rick; ls -la
we find `second ingredients` there. To view that we need to use the less command:

    cd /home/rick; less 'second ingredients'
and we get the next flag.
