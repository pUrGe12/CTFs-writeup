So, we start with running nmap on the provided IP address:

    nmap -sV $IP

report:

    # Nmap 7.60 scan initiated Sun Jan 14 09:44:26 2024 as: nmap -sV -oN initial 10.10.146.146
    Nmap scan report for ip-10-10-146-146.eu-west-1.compute.internal (10.10.146.146)
    Host is up (0.00038s latency).
    Not shown: 998 closed ports
    PORT   STATE SERVICE VERSION
    22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
    80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
    MAC Address: 02:72:CE:1E:FD:8D (Unknown)
    Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
    
    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    # Nmap done at Sun Jan 14 09:44:34 2024 -- 1 IP address (1 host up) scanned in 8.07 seconds

We can see that `SSH` is open on the website at the default port.

opening the website on firefox and reading the source code we get the following information:
    
    Username: R1ckRul3s
if there is a username there must also be a password somewhere along with a login page (we can't use SSH because the port is not mentioned).

using gobuster we can do a directories search on the website along with trying to find php,html,xml,txt pages in the website.

    gobuster dir -u 10.10.146.146 -w /usr/share/wordlists/dirb/big.txt -x php,xml,txt,html

The output gives the following relevant directories:

    /assets (Status: 301)
    /denied.php (Status: 302)
    /index.html (Status: 200)
    /login.php (Status: 200)
    /portal.php (Status: 302)
    /robots.txt (Status: 200)
    /robots.txt (Status: 200)

we can check the assets page but it contains only pictures so they aren't of any use. `login.php` looks like where we will enter the username and password, but we still don't have a password.

Checking the `robots.txt` page gives:

    Wubbalubbadubdub
This might be the **password!**

Go over to the `login.php` page and enter the username and password to gain access as Rick. Next up we see a command line.

Run `whoami` to see that we are `www-data` and run `pwd` to get that we are in the `var/www/html` directory. From here we can use `ls` to view all the files in the current directory

    Sup3rS3cretPickl3Ingred.txt
    assets
    clue.txt
    denied.php
    index.html
    login.php
    portal.php
    robots.txt

since the `cat` command does't work we can use:

    less Sup3rS3cretPickl3Ingred.txt
to get the first flag
