If we view the eml file using cat 

    cat email-export.eml
we can see that it is an email sent via SMTP. We can find the client-ip using 

    cat email-export.eml | grep client-ip

the client_ip is `173.249.33.206`

running a whois command on this ip:

    whois 173.249.33.206

we can get the person name using

    whois 173.249.33.206 | grep person

flag: picoCTF{WilhelmZwalina}
